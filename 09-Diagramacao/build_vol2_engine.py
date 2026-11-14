#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e de Ilustração — Volume 2 (eBook 2): As Estrelas da Promessa
Subtítulo: Os amigos que caminharam olhando para o céu (Abraão, Sara, Isaque, Jacó e José no Egito)
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Gera a Capa Oficial do Volume 2 (Estilo Capa 2 Aventura Infantil com FÁBIO MOTTA E SILVA),
renderiza as composições 3D cinematográficas dos Capítulos 1 a 6 (seguindo a regra Fiat Lux),
diagrama as 24 páginas completas e sequenciais (PÁGINA 01 a PÁGINA 24) em Dupla Camada (4-6 e 6-10 anos),
e exporta PDF HD (200 DPI), PDF de Impressão 300 DPI com sangria (24 páginas KDP Print) e EPUB 3 Fixed-Layout (Amazon KDP).
"""

import os
import math
import random
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
BRAIN_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/brain/026b6e7b-1190-4ec1-b3f4-789abc0233f8"
FONT_DIR = os.path.join(BASE_DIR, "03-Identidade-Visual/fonts")
VOL2_DIR = os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-2-As-Estrelas-da-Promessa")

AUTHOR_NAME = "Fábio Motta e Silva"
AUTHOR_UPPER = "FÁBIO MOTTA E SILVA"

PAGE_W = 1600
PAGE_H = 2000

def load_font(name, size):
    paths = {
        "cinzel": os.path.join(FONT_DIR, "Cinzel.ttf"),
        "nunito": os.path.join(FONT_DIR, "Nunito.ttf"),
        "nunito_italic": os.path.join(FONT_DIR, "Nunito-Italic.ttf"),
        "atkinson": os.path.join(FONT_DIR, "AtkinsonHyperlegible-Regular.ttf"),
        "atkinson_bold": os.path.join(FONT_DIR, "AtkinsonHyperlegible-Bold.ttf"),
    }
    try:
        return ImageFont.truetype(paths.get(name, paths["nunito"]), size)
    except Exception:
        return ImageFont.load_default()

def crop_and_resize(img, target_w, target_h):
    w, h = img.size
    target_ratio = target_w / target_h
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

def draw_wrapped_text(draw, text, x, y, max_width, font, fill=(255, 255, 255), line_spacing=1.35, align="left", shadow=False):
    words = text.split(" ")
    lines = []
    current_line = []
    for word in words:
        if "\n" in word:
            parts = word.split("\n")
            for idx, p in enumerate(parts):
                test_line = " ".join(current_line + ([p] if p else []))
                bbox = draw.textbbox((0, 0), test_line, font=font)
                if bbox[2] - bbox[0] <= max_width:
                    if p:
                        current_line.append(p)
                else:
                    if current_line:
                        lines.append(" ".join(current_line))
                    current_line = [p] if p else []
                if idx < len(parts) - 1:
                    lines.append(" ".join(current_line))
                    current_line = []
            continue
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))

    bbox_sample = draw.textbbox((0, 0), "Ág", font=font)
    line_h = int((bbox_sample[3] - bbox_sample[1]) * line_spacing)
    cur_y = y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        lx = x
        if align == "center":
            lx = x + (max_width - lw) // 2
        elif align == "right":
            lx = x + (max_width - lw)
        if shadow:
            draw.text((lx + 2, cur_y + 2), line, font=font, fill=(0, 0, 0, 190))
        draw.text((lx, cur_y), line, font=font, fill=fill)
        cur_y += line_h
    return cur_y

def draw_rounded_panel(img, box, fill_rgba, border_rgba=None, border_width=3, radius=28):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rounded_rectangle(box, radius=radius, fill=fill_rgba, outline=border_rgba, width=border_width)
    return Image.alpha_composite(img.convert("RGBA"), overlay)

def draw_page_footer(img, page_num, chapter_label="VOLUME 2  •  AS ESTRELAS DA PROMESSA", dark_mode=True):
    draw = ImageDraw.Draw(img)
    f_foot = load_font("atkinson_bold", 22)
    color = (226, 232, 240, 210) if dark_mode else (71, 85, 105, 220)
    line_col = (245, 190, 70, 140) if dark_mode else (180, 83, 9, 120)
    draw.line([(90, PAGE_H - 78), (PAGE_W - 90, PAGE_H - 78)], fill=line_col, width=2)
    draw.text((90, PAGE_H - 62), chapter_label, font=f_foot, fill=color)
    p_str = f"PÁGINA {page_num:02d} DE 24"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def add_starfield(img_rgba, seed_val=101, count=220, max_y=900):
    overlay = Image.new("RGBA", img_rgba.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    random.seed(seed_val)
    w, _ = img_rgba.size
    for _ in range(count):
        sx = random.randint(20, w - 20)
        sy = random.randint(20, max_y)
        r = random.choice([2, 3, 4, 6])
        col = (255, 235, 150, random.randint(140, 245)) if random.random() > 0.35 else (140, 215, 255, random.randint(130, 230))
        odraw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=col)
        if r >= 5:
            odraw.line([(sx - 12, sy), (sx + 12, sy)], fill=(255, 245, 200, 190), width=2)
            odraw.line([(sx, sy - 12), (sx, sy + 12)], fill=(255, 245, 200, 190), width=2)
    return Image.alpha_composite(img_rgba, overlay)

def prepare_vol2_assets():
    print("-> Preparando ilustrações 3D originais e Capa Oficial do Volume 2 (As Estrelas da Promessa)...")
    ilus_dir = os.path.join(VOL2_DIR, "ilustracoes")
    p_dir = os.path.join(VOL2_DIR, "paginas_piloto")
    os.makedirs(ilus_dir, exist_ok=True)
    os.makedirs(p_dir, exist_ok=True)

    import glob
    prefixes = [
        ("vol2_capa_base_aventura", os.path.join(ilus_dir, "vol2_capa_base_aventura.jpg")),
        ("vol2_cap1_estrelas_abraao", os.path.join(ilus_dir, "vol2_cap1_estrelas_abraao.jpg")),
        ("vol2_cap2_riso_isaque", os.path.join(ilus_dir, "vol2_cap2_riso_isaque.jpg")),
        ("vol2_cap3_escada_jaco", os.path.join(ilus_dir, "vol2_cap3_escada_jaco.jpg")),
        ("vol2_cap4_tunica_jose", os.path.join(ilus_dir, "vol2_cap4_tunica_jose.jpg")),
        ("vol2_cap5_sonhos_farao", os.path.join(ilus_dir, "vol2_cap5_sonhos_farao.jpg")),
        ("vol2_cap6_abraco_perdao", os.path.join(ilus_dir, "vol2_cap6_abraco_perdao.jpg")),
        ("char_sheet_abraao_sara_jose", os.path.join(BASE_DIR, "04-Biblia-de-Personagens/char_sheet_abraao_sara_jose.jpg")),
    ]
    for pref, dst_p in prefixes:
        matches = sorted(glob.glob(os.path.join(BRAIN_DIR, f"{pref}*.jpg")))
        if matches:
            shutil.copy2(matches[-1], dst_p)
            print(f"   Ilustração 3D copiada: {os.path.basename(dst_p)}")

    # Carregar matrizes 3D da coleção para composição cinematográfica caso não existam arquivos dedicados
    cosmica = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_1_cosmica_base.jpg")).convert("RGB")
    aventura = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg")).convert("RGB")
    babel = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap6_torre_babel.jpg")).convert("RGB")
    eden = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap2_jardim_eden.jpg")).convert("RGB")
    pastor = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap4_caim_abel.jpg")).convert("RGB")
    sinai = Image.open(os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade/ilustracoes/vol3_cap5_pao_do_ceu_sinai.jpg")).convert("RGB")
    nilo = Image.open(os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade/ilustracoes/vol3_cap1_cesto_nilo.jpg")).convert("RGB")
    noite_egito = Image.open(os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade/ilustracoes/vol3_cap3_noite_liberdade.jpg")).convert("RGB")
    nebo = Image.open(os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade/ilustracoes/vol3_cap6_terra_prometida.jpg")).convert("RGB")

    # 1. Base da Capa do Volume 2 (Crianças exploradoras sob o céu estrelado da Promessa)
    cov_base_path = os.path.join(ilus_dir, "vol2_capa_base_aventura.jpg")
    if not os.path.exists(cov_base_path):
        c_sky = crop_and_resize(cosmica, PAGE_W, 1150)
        c_fg = crop_and_resize(aventura, PAGE_W, PAGE_H)
        comp = c_fg.copy()
        mask = Image.new("L", (PAGE_W, 1150))
        md = ImageDraw.Draw(mask)
        for y in range(1150):
            val = int(235 * max(0.0, 1.0 - (y / 950.0) ** 1.6))
            md.line([(0, y), (PAGE_W, y)], fill=val)
        comp.paste(c_sky, (0, 0), mask)
        comp_rgba = add_starfield(comp.convert("RGBA"), seed_val=202, count=260, max_y=1050)
        comp_rgba.convert("RGB").save(cov_base_path, quality=95)

    # Diagramar Capa Oficial do Volume 2 com FÁBIO MOTTA E SILVA
    base_v2 = Image.open(cov_base_path).convert("RGB")
    cov_rgba = crop_and_resize(base_v2, PAGE_W, PAGE_H).convert("RGBA")
    grad = Image.new("RGBA", (PAGE_W, PAGE_H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grad)
    for y in range(520):
        alpha = int(190 * (1 - y / 520.0) ** 1.35)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 16, 42, alpha))
    for y in range(PAGE_H - 360, PAGE_H):
        alpha = int(215 * ((y - (PAGE_H - 360)) / 360.0) ** 1.3)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 16, 38, alpha))
    cov_rgba = Image.alpha_composite(cov_rgba, grad)
    cdraw = ImageDraw.Draw(cov_rgba)

    f_series = load_font("cinzel", 34)
    f_title = load_font("cinzel", 70)
    f_sub = load_font("nunito", 36)
    f_tag = load_font("atkinson_bold", 26)
    f_author = load_font("cinzel", 30)

    cdraw.line([(360, 78), (PAGE_W - 360, 78)], fill=(245, 190, 70, 220), width=3)
    draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 96, PAGE_W - 200, f_series, fill=(240, 246, 255), align="center", shadow=True)
    cdraw.line([(480, 152), (PAGE_W - 480, 152)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(cdraw, "AS ESTRELAS DA PROMESSA", 65, 178, PAGE_W - 130, f_title, fill=(255, 224, 115), align="center", shadow=True)
    draw_wrapped_text(cdraw, "Os amigos que caminharam olhando para o céu", 110, 280, PAGE_W - 220, f_sub, fill=(255, 255, 255), align="center", shadow=True)

    cov_rgba = draw_rounded_panel(cov_rgba, (220, PAGE_H - 235, PAGE_W - 220, PAGE_H - 70), (12, 22, 48, 222), (245, 190, 70, 235), border_width=3, radius=24)
    cdraw = ImageDraw.Draw(cov_rgba)
    draw_wrapped_text(cdraw, "VOLUME 2  •  A BÍBLIA ILUSTRADA PARA PEQUENOS EXPLORADORES", 240, PAGE_H - 208, PAGE_W - 480, f_tag, fill=(254, 240, 138), align="center")
    draw_wrapped_text(cdraw, AUTHOR_UPPER, 240, PAGE_H - 142, PAGE_W - 480, f_author, fill=(255, 255, 255), align="center")
    cov_path = os.path.join(ilus_dir, "vol2_capa_oficial_aventura.png")
    cov_rgba.convert("RGB").save(cov_path, quality=95)
    shutil.copy2(cov_path, os.path.join(BRAIN_DIR, "vol2_capa_oficial_aventura.png"))

    # 2. Ilustrações dos 6 capítulos do Volume 2
    # Cap 1: O Contador de Estrelas (Abraão e Sara sob o céu estrelado de Canaã)
    c1_path = os.path.join(ilus_dir, "vol2_cap1_estrelas_abraao.jpg")
    if not os.path.exists(c1_path):
        im1 = Image.new("RGB", (1600, 1200), (10, 18, 42))
        sky1 = crop_and_resize(cosmica, 1600, 780)
        fg1 = crop_and_resize(nebo, 1600, 750)
        im1.paste(sky1, (0, 0))
        m1 = Image.new("L", (1600, 750))
        md1 = ImageDraw.Draw(m1)
        for y in range(750):
            md1.line([(0, y), (1600, y)], fill=int(255 * min(1.0, max(0.0, (y - 60) / 260.0))))
        im1.paste(fg1, (0, 450), m1)
        im1_rgba = add_starfield(im1.convert("RGBA"), seed_val=301, count=300, max_y=700)
        im1_rgba.convert("RGB").save(c1_path, quality=95)

    # Cap 2: O Bebê que Trouxe o Riso (Carvalhos de Manre e luz dourada da manhã)
    c2_path = os.path.join(ilus_dir, "vol2_cap2_riso_isaque.jpg")
    if not os.path.exists(c2_path):
        w_s, h_s = sinai.size
        im2 = crop_and_resize(sinai.crop((0, int(h_s * 0.15), w_s, h_s)), 1600, 1200)
        im2 = ImageEnhance.Color(im2).enhance(1.12)
        im2.save(c2_path, quality=95)

    # Cap 3: A Escada de Luz em Betel (Raios volumétricos dourados e azuis subindo ao céu estrelado)
    c3_path = os.path.join(ilus_dir, "vol2_cap3_escada_jaco.jpg")
    if not os.path.exists(c3_path):
        im3 = crop_and_resize(nebo, 1600, 1200)
        im3 = ImageEnhance.Brightness(im3).enhance(0.68).convert("RGBA")
        im3 = add_starfield(im3, seed_val=303, count=240, max_y=680)
        stair = Image.new("RGBA", (1600, 1200), (0, 0, 0, 0))
        sd = ImageDraw.Draw(stair)
        # Desenhar escadaria volumétrica de luz dourada e safira subindo da colina ao céu
        for step in range(18):
            t = step / 18.0
            y_pos = int(1050 - t * 920)
            half_w = int(340 * (1.0 - t * 0.62))
            cx = int(820 + t * 140)
            col_step = (255, 228, 130, int(175 * (1 - t * 0.3)))
            sd.rounded_rectangle([cx - half_w, y_pos - 14, cx + half_w, y_pos + 14], radius=10, fill=col_step)
        sd.polygon([(460, 1100), (1180, 1100), (1090, 80), (830, 80)], fill=(255, 215, 100, 68))
        stair = stair.filter(ImageFilter.GaussianBlur(radius=8))
        im3 = Image.alpha_composite(im3, stair)
        im3.convert("RGB").save(c3_path, quality=95)

    # Cap 4: O Jovem Sonhador e a Túnica Colorida (Campos de trigo e ovelhas em Hebrom)
    c4_path = os.path.join(ilus_dir, "vol2_cap4_tunica_jose.jpg")
    if not os.path.exists(c4_path):
        im4 = crop_and_resize(pastor, 1600, 1200)
        im4.save(c4_path, quality=95)

    # Cap 5: Os Sonhos do Faraó e os Celeiros às Margens do Nilo
    c5_path = os.path.join(ilus_dir, "vol2_cap5_sonhos_farao.jpg")
    if not os.path.exists(c5_path):
        im5 = Image.new("RGB", (1600, 1200), (20, 30, 50))
        left_nilo = crop_and_resize(nilo, 900, 1200)
        right_gran = crop_and_resize(babel, 900, 1200)
        im5.paste(left_nilo, (0, 0))
        m5 = Image.new("L", (900, 1200))
        md5 = ImageDraw.Draw(m5)
        for x in range(900):
            md5.line([(x, 0), (x, 1200)], fill=int(255 * min(1.0, max(0.0, (x - 80) / 340.0))))
        im5.paste(right_gran, (700, 0), m5)
        im5.save(c5_path, quality=95)

    # Cap 6: O Abraço Mais Forte que a Tempestade (Reconciliação da Família no Egito sob Arco de Luz)
    c6_path = os.path.join(ilus_dir, "vol2_cap6_abraco_perdao.jpg")
    if not os.path.exists(c6_path):
        im6 = crop_and_resize(noite_egito, 1600, 1200)
        im6 = ImageEnhance.Brightness(im6).enhance(1.15)
        im6.save(c6_path, quality=95)

def make_3page_chapter_v2(art_img, start_page, cap_num, cap_title, ref_text, main_narrative, quick_box, seed_4_6, explorer_dialogue, arq_title, arq_text, family_question, dark_mode=False):
    f_h2 = load_font("cinzel", 35)
    f_body = load_font("nunito", 32)
    f_box_title = load_font("atkinson_bold", 26)
    f_box_body = load_font("atkinson", 24)
    f_ref = load_font("atkinson_bold", 23)

    bg_col = (12, 20, 40, 255) if dark_mode else (253, 251, 247, 255)
    border_c = (245, 190, 70) if dark_mode else (180, 83, 9)
    title_c = (253, 224, 71) if dark_mode else (146, 64, 14)
    ref_c = (186, 230, 253) if dark_mode else (30, 58, 138)
    body_c = (248, 250, 252) if dark_mode else (41, 37, 36)

    # PÁGINA A
    pA = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    pA.paste(crop_and_resize(art_img, PAGE_W - 140, 1020), (70, 70))
    dA = ImageDraw.Draw(pA)
    dA.rectangle([70, 70, PAGE_W - 70, 1090], outline=border_c, width=4)
    draw_wrapped_text(dA, f"CAPÍTULO {cap_num}  •  {cap_title}", 90, 1125, PAGE_W - 180, f_h2, fill=title_c)
    draw_wrapped_text(dA, f"{ref_text}  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=ref_c)
    draw_wrapped_text(dA, main_narrative, 90, 1235, PAGE_W - 180, f_body, fill=body_c, line_spacing=1.35)
    boxA_bg = (30, 41, 59, 240) if dark_mode else (254, 243, 199, 255)
    boxA_bd = (245, 190, 70, 220) if dark_mode else (217, 119, 6, 255)
    boxA_tc = (254, 240, 138) if dark_mode else (146, 64, 14)
    pA = draw_rounded_panel(pA, (90, 1750, PAGE_W - 90, 1890), boxA_bg, boxA_bd, border_width=2, radius=18)
    dA = ImageDraw.Draw(pA)
    draw_wrapped_text(dA, quick_box, 120, 1775, PAGE_W - 240, f_box_body, fill=boxA_tc)
    pA_rgb = pA.convert("RGB")
    draw_page_footer(pA_rgb, start_page, f"VOLUME 2  •  CAPÍTULO {cap_num}: {cap_title}", dark_mode=dark_mode)

    # PÁGINA B
    pB = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    w, h = art_img.size
    left_zoom = art_img.crop((0, int(h * 0.08), int(w * 0.78), int(h * 0.65)))
    pB.paste(crop_and_resize(left_zoom, PAGE_W - 140, 520), (70, 70))
    dB = ImageDraw.Draw(pB)
    dB.rectangle([70, 70, PAGE_W - 70, 590], outline=border_c, width=4)
    draw_wrapped_text(dB, f"CAPÍTULO {cap_num}  •  LEITURA EM DUPLA CAMADA", 90, 620, PAGE_W - 180, f_h2, fill=title_c)
    pB = draw_rounded_panel(pB, (85, 685, PAGE_W - 85, 1045), boxA_bg, boxA_bd, border_width=3, radius=22)
    dB = ImageDraw.Draw(pB)
    draw_wrapped_text(dB, "» CAMADA SEMENTE (4 A 6 ANOS — LEITURA EM VOZ ALTA):", 120, 712, PAGE_W - 240, f_box_title, fill=boxA_tc)
    draw_wrapped_text(dB, seed_4_6, 120, 760, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.35)

    draw_wrapped_text(dB, "CENA DRAMATIZADA E DIÁLOGOS (CAMADA EXPLORADOR 6–10 ANOS):", 90, 1085, PAGE_W - 180, f_box_title, fill=title_c)
    draw_wrapped_text(dB, explorer_dialogue, 90, 1135, PAGE_W - 180, f_body, fill=body_c, line_spacing=1.36)
    pB_rgb = pB.convert("RGB")
    draw_page_footer(pB_rgb, start_page + 1, f"VOLUME 2  •  CAPÍTULO {cap_num} (DUPLA CAMADA)", dark_mode=dark_mode)

    # PÁGINA C
    pC = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    right_zoom = art_img.crop((int(w * 0.15), int(h * 0.20), w, int(h * 0.88)))
    pC.paste(crop_and_resize(right_zoom, PAGE_W - 140, 680), (70, 70))
    dC = ImageDraw.Draw(pC)
    dC.rectangle([70, 70, PAGE_W - 70, 750], outline=border_c, width=4)
    draw_wrapped_text(dC, f"EXPLORAÇÃO HISTÓRICA E DIÁLOGO  •  CAPÍTULO {cap_num}", 90, 785, PAGE_W - 180, f_h2, fill=title_c)

    disc_bg = (20, 45, 76, 240) if dark_mode else (224, 242, 254, 255)
    disc_bd = (56, 189, 248, 220) if dark_mode else (2, 132, 199, 255)
    disc_tc = (186, 230, 253) if dark_mode else (7, 89, 133)
    pC = draw_rounded_panel(pC, (85, 855, PAGE_W - 85, 1380), disc_bg, disc_bd, border_width=3, radius=22)
    dC = ImageDraw.Draw(pC)
    draw_wrapped_text(dC, f"» PEQUENA GRANDE DESCOBERTA: {arq_title}", 120, 885, PAGE_W - 240, f_box_title, fill=disc_tc)
    draw_wrapped_text(dC, arq_text, 120, 938, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.36)

    q_bg = (30, 58, 47, 240) if dark_mode else (236, 252, 203, 255)
    q_bd = (74, 222, 128, 220) if dark_mode else (101, 163, 13, 255)
    q_tc = (187, 247, 208) if dark_mode else (54, 83, 20)
    pC = draw_rounded_panel(pC, (85, 1425, PAGE_W - 85, 1885), q_bg, q_bd, border_width=3, radius=22)
    dC = ImageDraw.Draw(pC)
    draw_wrapped_text(dC, "» O QUE VOCÊ FARIA? / CONVERSE COMIGO EM FAMÍLIA:", 120, 1455, PAGE_W - 240, f_box_title, fill=q_tc)
    draw_wrapped_text(dC, family_question, 120, 1510, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.36)
    pC_rgb = pC.convert("RGB")
    draw_page_footer(pC_rgb, start_page + 2, f"VOLUME 2  •  CAPÍTULO {cap_num} (DESCOBERTAS)", dark_mode=dark_mode)

    return [pA_rgb, pB_rgb, pC_rgb]

def build_vol2_pages_and_exports():
    prepare_vol2_assets()
    f_h1 = load_font("cinzel", 50)
    f_h2 = load_font("cinzel", 36)
    f_body = load_font("nunito", 32)
    f_italic = load_font("nunito_italic", 30)
    f_box_title = load_font("atkinson_bold", 27)
    f_box_body = load_font("atkinson", 25)
    f_ref = load_font("atkinson_bold", 24)

    pages = []
    ilus_dir = os.path.join(VOL2_DIR, "ilustracoes")
    p_dir = os.path.join(VOL2_DIR, "paginas_piloto")

    c1_im = Image.open(os.path.join(ilus_dir, "vol2_cap1_estrelas_abraao.jpg")).convert("RGB")
    c2_im = Image.open(os.path.join(ilus_dir, "vol2_cap2_riso_isaque.jpg")).convert("RGB")
    c3_im = Image.open(os.path.join(ilus_dir, "vol2_cap3_escada_jaco.jpg")).convert("RGB")
    c4_im = Image.open(os.path.join(ilus_dir, "vol2_cap4_tunica_jose.jpg")).convert("RGB")
    c5_im = Image.open(os.path.join(ilus_dir, "vol2_cap5_sonhos_farao.jpg")).convert("RGB")
    c6_im = Image.open(os.path.join(ilus_dir, "vol2_cap6_abraco_perdao.jpg")).convert("RGB")

    # PÁGINA 01: CAPA OFICIAL VOLUME 2
    p1 = Image.open(os.path.join(ilus_dir, "vol2_capa_oficial_aventura.png")).convert("RGB")
    pages.append(("vol2_p01_capa.png", p1))

    # PÁGINA 02: FOLHA DE ROSTO, CARTA DE BOAS-VINDAS E GUIA DE LEITURA
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    p2.paste(crop_and_resize(c1_im, PAGE_W - 180, 680), (90, 75))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([90, 75, PAGE_W - 90, 755], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d2, "AS ESTRELAS DA PROMESSA", 100, 785, PAGE_W - 200, f_h1, fill=(146, 64, 14), align="center")
    draw_wrapped_text(d2, f"Volume 2  •  Autor: {AUTHOR_NAME} (Edição Independente)", 100, 850, PAGE_W - 200, f_ref, fill=(30, 58, 138), align="center")
    intro_v2 = (
        "Bem-vindo ao segundo volume da coleção A Grande História da Luz! Depois que os povos se espalharam por toda a Terra, a Presença Luminosa do Criador chamou um casal de amigos — Abraão e Sara — para olhar para o céu estrelado e confiar numa grande promessa.\n\n"
        "Neste livro, você caminhará pelas colinas de Canaã até os celeiros do Egito ao lado de Abraão, Sara, o alegre Isaque, Jacó e o jovem sonhador José, descobrindo que o perdão e o amor de Deus transformam até os dias difíceis em bênção!"
    )
    draw_wrapped_text(d2, intro_v2, 110, 910, PAGE_W - 220, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p2 = draw_rounded_panel(p2, (95, 1390, PAGE_W - 95, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "COMO LER ESTE LIVRO EM FAMÍLIA (DUPLA CAMADA 4–10 ANOS):", 135, 1420, PAGE_W - 270, f_box_title, fill=(146, 64, 14))
    guia_v2 = (
        "• Cada um dos 6 capítulos conta com 3 páginas completas (Páginas 04 a 21).\n"
        "• Na 1ª página do capítulo, contemple a ilustração 3D e o resumo narrativo.\n"
        "• Na 2ª página, escolha entre a Camada Semente (4–6 anos) ou os Diálogos da Camada Explorador (6–10 anos).\n"
        "• Na 3ª página, explore descobertas arqueológicas do Crescente Fértil e converse em família!"
    )
    draw_wrapped_text(d2, guia_v2, 135, 1475, PAGE_W - 270, f_box_body, fill=(68, 64, 60), line_spacing=1.42)
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 2, "FOLHA DE ROSTO E GUIA DE LEITURA  •  VOLUME 2", dark_mode=False)
    pages.append(("vol2_p02_folha_rosto.png", p2_rgb))

    # PÁGINA 03: MAPA DA JORNADA DOS PATRIARCAS E SUMÁRIO DOS 6 CAPÍTULOS
    p3_map = Image.new("RGBA", (PAGE_W, PAGE_H), (12, 20, 40, 255))
    p3_map.paste(crop_and_resize(c3_im, PAGE_W - 140, 600), (70, 70))
    dm = ImageDraw.Draw(p3_map)
    dm.rectangle([70, 70, PAGE_W - 70, 670], outline=(245, 190, 70), width=4)
    draw_wrapped_text(dm, "MAPA DA JORNADA: DE HARÃ A CANAÃ E AO EGITO", 90, 700, PAGE_W - 180, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(dm, f"Roteiro e Direção Editorial: {AUTHOR_NAME}", 90, 752, PAGE_W - 180, f_ref, fill=(186, 230, 253), align="center")
    p3_map = draw_rounded_panel(p3_map, (85, 810, PAGE_W - 85, 1885), (30, 41, 59, 240), (245, 190, 70, 220), border_width=3, radius=24)
    dm = ImageDraw.Draw(p3_map)
    sum_txt = (
        "• CAPÍTULO 1 — O Contador de Estrelas (Gênesis 12 e 15 | Págs. 04 a 06):\n"
        "  A partida de Abraão e Sara rumo a Canaã e a aliança sob milhões de estrelas no céu.\n\n"
        "• CAPÍTULO 2 — O Bebê que Trouxe o Riso (Gênesis 18 e 21 | Págs. 07 a 09):\n"
        "  A hospitalidade sob os carvalhos de Manre e o nascimento alegre do pequeno Isaque.\n\n"
        "• CAPÍTULO 3 — A Escada de Luz no Meio da Noite (Gênesis 28 e 33 | Págs. 10 a 12):\n"
        "  O sonho luminoso de Jacó em Betel e o abraço de reconciliação com seu irmão Esaú.\n\n"
        "• CAPÍTULO 4 — O Jovem Sonhador e a Túnica Colorida (Gênesis 37 | Págs. 13 a 15):\n"
        "  Os doze filhos de Jacó, a túnica listrada de José, o perigo da inveja e a viagem ao Egito.\n\n"
        "• CAPÍTULO 5 — Os Sonhos do Faraó e os Celeiros da Vida (Gênesis 41 | Págs. 16 a 18):\n"
        "  A sabedoria de José no palácio egípcio e a guarda do trigo para vencer a grande seca.\n\n"
        "• CAPÍTULO 6 — O Abraço Mais Forte que a Tempestade (Gênesis 45 e 50 | Págs. 19 a 21):\n"
        "  O reencontro emocionante de José com seus irmãos e seu pai Jacó e o poder do perdão."
    )
    draw_wrapped_text(dm, sum_txt, 125, 845, PAGE_W - 250, f_box_body, fill=(248, 250, 252), line_spacing=1.35)
    p3_map_rgb = p3_map.convert("RGB")
    draw_page_footer(p3_map_rgb, 3, "SUMÁRIO VISUAL E ROTA DOS PATRIARCAS  •  VOLUME 2", dark_mode=True)
    pages.append(("vol2_p03_mapa_sumario.png", p3_map_rgb))

    # CAPÍTULO 1 (PÁGINAS 04, 05, 06)
    ch1 = make_3page_chapter_v2(
        c1_im, 4, 1, "O CONTADOR DE ESTRELAS", "Base Bíblica: Gênesis 12:1–9; 15:1–6",
        "A Presença Luminosa do Criador chamou Abraão e Sara para deixarem sua cidade antiga e caminharem até a terra de Canaã, com uma promessa extraordinária: por meio da família deles, todas as famílias da Terra seriam abençoadas!\n\n"
        "Certa noite, a Voz amorosa convidou Abraão a sair da tenda: 'Olhe para o céu e conte as estrelas, se puder! Assim será a sua descendência!' E Abraão confiou de todo o coração na Palavra da Luz.",
        "» PEQUENA GRANDE DESCOBERTA: Os pastores seminômades moravam em tendas tecidas com lã de cabra impermeável!",
        "Abraão e Sara fizeram uma longa viagem guiados pela Luz de Deus. Uma noite, no silêncio do deserto, Deus pediu para Abraão olhar para o alto: o céu estava cheio de milhões de estrelinhas brilhando! 'Assim será a sua grande família!', prometeu o Criador.",
        "— Sara, venha ver esta noite! — chamou Abraão à porta da tenda, segurando a mão da esposa.\n"
        "Acima das colinas de Canaã, a Via Láctea parecia um rio de diamantes dourados e azuis.\n"
        "— Nossos olhos ainda não veem a multidão de filhos e netos — sussurrou Sara com paz —, mas quem acendeu todas essas estrelas no céu certamente cumprirá a Sua palavra!",
        "AS TENDAS E AS CARAVANAS DO CRESCENTE FÉRTIL",
        "Na Idade do Bronze Médio, famílias pastoris viajavam entre a Mesopotâmia (Ur e Harã) e Canaã seguindo o curso dos rios e oásis, levando rebanhos de ovelhas, cabras e jumentos carregados de lã e azeite.",
        "Quando você olha para o céu estrelado à noite, que pergunta ou pensamento bonito surge no seu coração?",
        dark_mode=True
    )
    pages.extend([("vol2_p04_cap1_estrelas.png", ch1[0]), ("vol2_p05_cap1_camadas.png", ch1[1]), ("vol2_p06_cap1_descobertas.png", ch1[2])])

    # CAPÍTULO 2 (PÁGINAS 07, 08, 09)
    ch2 = make_3page_chapter_v2(
        c2_im, 7, 2, "O BEBÊ QUE TROUXE O RISO", "Base Bíblica: Gênesis 18:1–15; 21:1–7",
        "À sombra dos grandes carvalhos de Manre, Abraão e Sara acolheram viajantes com pão quentinho e água fresca, e ouviram a notícia mais esperada: no ano seguinte, Sara teria um filho nos braços!\n\n"
        "Quando o menino nasceu, a tenda inteira se encheu de alegria. Eles o chamaram de Isaque — nome hebraico que significa 'Ele sorriu' —, porque nenhuma promessa do Criador é difícil demais!",
        "» VOCÊ PERCEBEU? O nome Isaque (Yitzhak) quer dizer 'Riso / Alegria' em hebraico!",
        "Mesmo já tendo cabelos branquinhos, Abraão e Sara ganharam o bebê que Deus havia prometido! Quando o pequeno Isaque nasceu, todo mundo sorriu e cantou de felicidade debaixo das árvores de Manre!",
        "Sentada sobre o tapete tecido à sombra fresca dos carvalhos, Sara embalava o pequeno Isaque enquanto Abraão repartia figos doces e pães com os pastores do acampamento:\n"
        "— Deus trouxe o riso para a minha vida! — cantava Sara com os olhos marejados de gratidão. — Quem ouvir a nossa história vai sorrir conosco pela fidelidade do Senhor!",
        "A HOSPITALIDADE SAGRADA NO DESERTO",
        "No antigo Oriente Próximo, oferecer sombra, água fresca para lavar os pés e pão assado na hora a qualquer viajante que passasse perto da tenda era considerado o dever mais nobre e sagrado de uma família.",
        "Como você e sua família gostam de receber visitas, amigos ou vizinhos para que eles se sintam bem-vindos em casa?",
        dark_mode=False
    )
    pages.extend([("vol2_p07_cap2_isaque.png", ch2[0]), ("vol2_p08_cap2_camadas.png", ch2[1]), ("vol2_p09_cap2_descobertas.png", ch2[2])])

    # CAPÍTULO 3 (PÁGINAS 10, 11, 12)
    ch3 = make_3page_chapter_v2(
        c3_im, 10, 3, "A ESCADA DE LUZ NO MEIO DA NOITE", "Base Bíblica: Gênesis 28:10–22; 33:1–11",
        "Viajando sozinho pelas montanhas depois de ter errado com seu irmão Esaú, o jovem Jacó apoiou a cabeça numa pedra em Betel e adormeceu. Em seu sonho, viu uma imensa escadaria de pura luz dourada e safira ligando a Terra ao Céu!\n\n"
        "— Eu estou com você e o guardarei por onde quer que você vá! — prometeu a Voz do Criador. Transformado por aquele encontro, Jacó mais tarde voltou para casa e abraçou seu irmão Esaú em paz.",
        "» PEQUENA GRANDE DESCOBERTA: Betel significa 'Casa de Deus' — o lugar onde o Céu abraçou a Terra!",
        "Jacó estava viajando sozinho à noite e dormiu com a cabeça apoiada numa pedra lisinha. Em seu sonho, ele viu uma escada brilhante de luz que ia da Terra até o Céu e ouviu Deus prometer: 'Não tenha medo, Eu estou com você por onde você caminhar!'",
        "Quando o sol nasceu sobre as pedras de Betel, Jacó levantou-se admirado:\n"
        "— Na verdade, a Presença luminosa do Senhor está neste lugar, e eu não sabia!\n"
        "Anos depois, ao reencontrar seu irmão gêmeo Esaú, Jacó pediu perdão com humildade, e Esaú correu para abraçá-lo chorando de alegria. A paz havia vencido o medo!",
        "TORRE DE BABEL vs. ESCADA DE BETEL",
        "Compare que interessante: em Babel (Volume 1), os homens tentaram construir uma escadaria de tijolos para alcançar o céu por orgulho; já em Betel (Volume 2), é a própria Luz de Deus que desce por graça para consolar quem está sozinho!",
        "Por que pedir desculpas e fazer as pazes com um irmão ou amigo tira um peso tão grande do nosso coração?",
        dark_mode=True
    )
    pages.extend([("vol2_p10_cap3_escada.png", ch3[0]), ("vol2_p11_cap3_camadas.png", ch3[1]), ("vol2_p12_cap3_descobertas.png", ch3[2])])

    # CAPÍTULO 4 (PÁGINAS 13, 14, 15)
    ch4 = make_3page_chapter_v2(
        c4_im, 13, 4, "O JOVEM SONHADOR E A TÚNICA COLORIDA", "Base Bíblica: Gênesis 37:1–36",
        "Entre os doze filhos de Jacó estava o jovem José, que ganhou de seu pai uma linda túnica de mangas compridas tecida com muitas cores. Mas seus irmãos mais velhos deixaram a inveja crescer no coração por causa desse presente e dos sonhos de José.\n\n"
        "Levado por uma caravana de mercadores até a distante terra do Egito, José sentiu muita saudade do pai, mas decidiu nunca abandonar a verdade nem a confiança na Luz de Deus.",
        "» PEQUENA GRANDE DESCOBERTA: Pinturas egípcias de Beni Hasan mostram túnicas semitas listradas idênticas à de José!",
        "Jacó deu ao seu filho José uma túnica toda colorida! Mas os irmãos mais velhos sentiram ciúmes e mandaram José numa caravana para longe, até o Egito. Mesmo longe de casa, José guardou a bondade e a fé dentro do coração!",
        "Pelos vales verdes de Hebrom, José caminhava vestindo sua túnica tecida com listras vermelhas, azuis e douradas:\n"
        "— Irmãos, sonhei que estávamos colhendo trigo no campo, e os feixes de vocês se inclinavam ao redor do meu! — contou José sem imaginar a reação deles.\n"
        "Mesmo quando a inveja dos irmãos o levou para longe, a Presença do Senhor desceu com José ao Egito.",
        "AS PINTURAS EGÍPCIAS DE BENI HASAN (1890 a.C.)",
        "No túmulo do governador egípcio Khnumhotep II, em Beni Hasan, arqueólogos encontraram um mural colorido mostrando 37 viajantes de Canaã entrando no Egito vestindo túnicas de lã ricamente listradas em vermelho, azul e branco!",
        "Quando alguém perto de nós ganha um presente bonito, como podemos transformar o ciúme em alegria pelo outro?",
        dark_mode=False
    )
    pages.extend([("vol2_p13_cap4_tunica.png", ch4[0]), ("vol2_p14_cap4_camadas.png", ch4[1]), ("vol2_p15_cap4_descobertas.png", ch4[2])])

    # CAPÍTULO 5 (PÁGINAS 16, 17, 18)
    ch5 = make_3page_chapter_v2(
        c5_im, 16, 5, "OS SONHOS DO FARAÓ E OS CELEIROS DA VIDA", "Base Bíblica: Gênesis 39–41",
        "No Egito, José manteve um coração íntegro mesmo nas maiores provações. Quando o Faraó teve dois sonhos misteriosos com sete vacas e sete espigas de trigo, José foi chamado ao palácio real e declarou:\n\n"
        "— Deus dará uma resposta de paz ao rei! Virão sete anos de muita fartura seguidos por sete anos de seca. Guardemos o trigo em grandes celeiros durante os anos bons para que ninguém passe fome!",
        "» VOCÊ PERCEBEU? A sabedoria e o planejamento de José salvaram o Egito e todas as terras vizinhas!",
        "O rei Faraó sonhou com sete espigas de trigo bem cheias e sete espigas sequinhas! Iluminado pela sabedoria de Deus, José explicou que viriam sete anos de muita comida e depois sete anos de seca, e ajudou a encher grandes celeiros para alimentar todo mundo!",
        "No pátio de colunas de lótus do palácio real, o Faraó ouviu atentamente o conselho de José:\n"
        "— Já que Deus mostrou tudo isso a você, não há ninguém tão sábio e prudente quanto você! — declarou o Faraó, colocando seu anel de selar na mão de José.\n"
        "Durante os sete anos de colheitas fartas às margens do Nilo, José armazenou grãos como a areia do mar!",
        "OS GRANDES CELEIROS E AS CHEIAS DO RIO NILO",
        "Os antigos egípcios construíam silos e celeiros abobadados de tijolos de barro com aberturas no topo por onde os sacos de trigo eram despejados, mantendo os grãos secos e protegidos por muitos anos.",
        "Por que planejar com antecedência e não desperdiçar alimentos é uma forma de sabedoria e amor ao próximo?",
        dark_mode=False
    )
    pages.extend([("vol2_p16_cap5_celeiros.png", ch5[0]), ("vol2_p17_cap5_camadas.png", ch5[1]), ("vol2_p18_cap5_descobertas.png", ch5[2])])

    # CAPÍTULO 6 (PÁGINAS 19, 20, 21)
    ch6 = make_3page_chapter_v2(
        c6_im, 19, 6, "O ABRAÇO MAIS FORTE QUE A TEMPESTADE", "Base Bíblica: Gênesis 42–45; 50:15–21",
        "Quando a fome chegou a Canaã, os irmãos de José vieram ao Egito buscar alimento sem reconhecê-lo. Ao ver que seus irmãos estavam arrependidos e protegiam com coragem o caçula Benjamim, José abriu os braços em lágrimas:\n\n"
        "— Eu sou José! Não tenham medo: vocês pensaram o mal contra mim, mas Deus o transformou em bem para salvar a vida de muita gente! E toda a família de Jacó voltou a se abraçar no Egito.",
        "» CONVERSE COMIGO: O perdão de José curou a família inteira e trouxe o velho pai Jacó de volta à alegria!",
        "Quando os irmãos de José vieram comprar trigo no Egito, José viu que o coração deles havia mudado para melhor. Então ele abriu os braços chorando de alegria: 'Eu sou o seu irmão José! Eu perdoo vocês de todo o coração!' E toda a família se abraçou feliz!",
        "Debaixo de um arco radiante de luz dourada que entrava pelas janelas do pátio egípcio, José abraçou o jovem Benjamim e depois cada um de seus irmãos:\n"
        "— Cheguem perto de mim, meus irmãos! — disse José com ternura. — Deus me enviou adiante de vocês para preservar a vida da nossa família sobre a Terra!\n"
        "E quando as carruagens trouxeram o idoso Jacó ao Egito, pai e filho se abraçaram num reencontro inesquecível.",
        "A REGIÃO DE GÓSEN NO DELTA DO NILO",
        "A família de Jacó (70 pessoas ao todo) instalou-se na fértil região de Gósen, no Delta Oriental do Nilo. Foi ali que os descendentes de Israel cresceram e se multiplicaram até o nascimento de Moisés no Volume 3!",
        "José escolheu retribuir uma ofensa antiga com bondade e perdão. Qual é a diferença que o perdão faz dentro de uma família?",
        dark_mode=True
    )
    pages.extend([("vol2_p19_cap6_perdao.png", ch6[0]), ("vol2_p20_cap6_camadas.png", ch6[1]), ("vol2_p21_cap6_descobertas.png", ch6[2])])

    # PÁGINA 22: PEQUENA GRANDE DESCOBERTA ESPECIAL & GLOSSÁRIO DO VOLUME 2
    p22 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "PEQUENA GRANDE DESCOBERTA  •  ARQUEOLOGIA DO VOLUME 2", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")
    p22 = draw_rounded_panel(p22, (80, 145, PAGE_W - 80, 960), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "1. ARQUEOLOGIA DOS PATRIARCAS E DO EGITO ANTIGO", 120, 175, PAGE_W - 240, f_box_title, fill=(146, 64, 14))
    arq_v2_full = (
        "• As Caravanas de Canaã (Beni Hasan): As pinturas murais egípcias da XII Dinastia comprovam historicamente o trânsito de famílias semitas de Canaã para o Egito usando túnicas coloridas de lã tecida com padrões geométricos, jumentos de carga e liras musicais.\n\n"
        "• Os Poços de Água no Negueve: Em regiões semiáridas como Berseba (onde viveram Abraão e Isaque), cavar um poço até alcançar o lençol subterrâneo garantia vida para centenas de ovelhas e selava tratados de paz entre vizinhos.\n\n"
        "• A Estela da Fome no Nilo: Uma inscrição antiga na ilha de Sehel (no alto Nilo) registra a memória egípcia de um período histórico de sete anos seguidos em que as cheias do Nilo falharam, exigindo administração especial dos grãos!"
    )
    draw_wrapped_text(d22, arq_v2_full, 120, 230, PAGE_W - 240, f_body, fill=(41, 37, 36), line_spacing=1.35)

    p22 = draw_rounded_panel(p22, (80, 1005, PAGE_W - 80, 1885), (224, 242, 254, 255), (2, 132, 199, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "2. PEQUENO GLOSSÁRIO DO EXPLORADOR (VOLUME 2)", 120, 1035, PAGE_W - 240, f_box_title, fill=(7, 89, 133))
    gloss_v2 = (
        "• ALIANÇA: Promessa solene de amizade e fidelidade feita por Deus a Abraão e sua descendência.\n"
        "• ISAQUE ('RISO'): O filho da promessa nascido a Abraão e Sara na velhice, trazendo alegria à tenda.\n"
        "• BETEL ('CASA DE DEUS'): Lugar onde Jacó sonhou com a escadaria luminosa entre a Terra e o Céu.\n"
        "• CELEIRO: Grande armazém construído para conservar o trigo colhido durante os anos de fartura.\n"
        "• PROVIDÊNCIA: O cuidado amoroso de Deus que guia a história e transforma até dificuldades em bem."
    )
    draw_wrapped_text(d22, gloss_v2, 120, 1090, PAGE_W - 240, f_body, fill=(28, 25, 23), line_spacing=1.38)
    p22_rgb = p22.convert("RGB")
    draw_page_footer(p22_rgb, 22, "VOLUME 2  •  ARQUEOLOGIA E GLOSSÁRIO DO EXPLORADOR", dark_mode=False)
    pages.append(("vol2_p22_arqueologia_glossario.png", p22_rgb))

    # PÁGINA 23: BÍBLIA DE PERSONAGENS E CONTINUIDADE HISTÓRICA (VOLUME 2)
    p23 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, f"BÍBLIA DE PERSONAGENS  •  VOLUME 2 ({AUTHOR_UPPER})", 90, 75, PAGE_W - 180, f_h2, fill=(30, 58, 138), align="center")
    char_dir = os.path.join(BASE_DIR, "04-Biblia-de-Personagens")
    sheet_v2_path = os.path.join(char_dir, "char_sheet_abraao_sara_jose.jpg")
    if os.path.exists(sheet_v2_path):
        s_v2 = Image.open(sheet_v2_path).convert("RGB").resize((1400, 788), Image.Resampling.LANCZOS)
        p23.paste(s_v2, (100, 145))
        d23.rectangle([100, 145, 1500, 933], outline=(180, 83, 9), width=4)
        panel_top = 975
    else:
        s1 = Image.open(os.path.join(char_dir, "char_sheet_noe_familia.jpg")).convert("RGB").resize((680, 382), Image.Resampling.LANCZOS)
        s2 = Image.open(os.path.join(char_dir, "char_sheet_moises_miriam.jpg")).convert("RGB").resize((680, 382), Image.Resampling.LANCZOS)
        p23.paste(s1, (90, 150))
        p23.paste(s2, (830, 150))
        d23.rectangle([90, 150, 770, 532], outline=(180, 83, 9), width=3)
        d23.rectangle([830, 150, 1510, 532], outline=(180, 83, 9), width=3)
        panel_top = 575

    p23 = draw_rounded_panel(p23, (85, panel_top, PAGE_W - 85, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, "RECONSTRUÇÃO HISTÓRICA DOS PATRIARCAS E MATRIARCAS (GÊNESIS 12–50)", 125, panel_top + 30, PAGE_W - 250, f_box_title, fill=(146, 64, 14))
    leg_v2 = (
        f"Direção Editorial e Autoral: {AUTHOR_NAME}\n\n"
        "• ABRAÃO E SARA: Patriarca e matriarca seminômades do Crescente Fértil (Idade do Bronze Médio). Vestem mantos de lã tecida em tear manual em tons de índigo, ocre e terracota sobre túnicas de linho cru, com lenços protetores contra o sol do deserto e cajado de pastor.\n\n"
        "• JOSÉ EM CANAÃ E NO EGITO: Na juventude em Hebrom (aos 17 anos), veste a túnica festiva semita de mangas longas com listras geométricas coloridas (estilo Beni Hasan). Na maturidade (aos 30 anos, como governador do Egito), traja linho branco plissado egípcio e colar de turquesa e ouro."
    )
    draw_wrapped_text(d23, leg_v2, 125, panel_top + 85, PAGE_W - 250, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p23_rgb = p23.convert("RGB")
    draw_page_footer(p23_rgb, 23, "VOLUME 2  •  BÍBLIA DE PERSONAGENS E VESTIMENTAS HISTÓRICAS", dark_mode=False)
    pages.append(("vol2_p23_biblia_personagens.png", p23_rgb))

    # PÁGINA 24: CONTRACAPA OFICIAL DO VOLUME 2
    p24 = crop_and_resize(c1_im, PAGE_W, PAGE_H).convert("RGBA")
    p24 = draw_rounded_panel(p24, (110, 110, PAGE_W - 110, PAGE_H - 120), (8, 15, 38, 232), (245, 190, 70, 235), border_width=4, radius=32)
    d24 = ImageDraw.Draw(p24)
    draw_wrapped_text(d24, "AS ESTRELAS DA PROMESSA", 160, 165, PAGE_W - 320, f_h1, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "Volume 2  •  A Grande História da Luz", 160, 238, PAGE_W - 320, f_italic, fill=(186, 230, 253), align="center")
    d24.line([(320, 300), (PAGE_W - 320, 300)], fill=(245, 190, 70, 180), width=2)

    back_v2 = (
        "'Olhe para o céu e conte as estrelas, se é que você pode contá-las!'\n\n"
        "Neste segundo volume da coleção escrita por Fábio Motta e Silva, pequenos exploradores de 4 a 10 anos acompanham a emocionante caminhada da família da promessa: a coragem de Abraão e Sara, o sorriso do bebê Isaque, a escadaria luminosa do sonho de Jacó e a inesquecível jornada de José no Egito.\n\n"
        "Uma história vibrante sobre fé, sabedoria, resiliência e o poder do perdão que une irmãos e restaura famílias inteiras — preparando o caminho para a grande travessia de Moisés e Miriã no Volume 3 (*O Caminho da Liberdade*)!"
    )
    draw_wrapped_text(d24, back_v2, 165, 340, PAGE_W - 330, f_body, fill=(248, 250, 252), line_spacing=1.38)
    d24.line([(320, 1695), (PAGE_W - 320, 1695)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(d24, f"AUTOR: {AUTHOR_UPPER}", 160, 1725, PAGE_W - 320, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "Edição Autônoma Independente  •  Volume 2 (24 Páginas Ilustradas)", 160, 1785, PAGE_W - 320, f_ref, fill=(186, 230, 253), align="center")
    p24_rgb = p24.convert("RGB")
    draw_page_footer(p24_rgb, 24, "CONTRACAPA OFICIAL  •  VOLUME 2: AS ESTRELAS DA PROMESSA", dark_mode=True)
    pages.append(("vol2_p24_contracapa.png", p24_rgb))

    saved = []
    for fname, im in pages:
        fp = os.path.join(p_dir, fname)
        im.save(fp, quality=95)
        saved.append(fp)

    for fname in ["vol2_p01_capa.png", "vol2_p04_cap1_estrelas.png", "vol2_p10_cap3_escada.png", "vol2_p19_cap6_perdao.png", "vol2_p24_contracapa.png"]:
        shutil.copy2(os.path.join(p_dir, fname), os.path.join(BRAIN_DIR, fname))

    # 1. Exportar PDF HD do Volume 2 (24 páginas)
    pdf_v2 = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol2_Piloto_HD.pdf")
    pil_ims = [Image.open(p).convert("RGB") for p in saved]
    pil_ims[0].save(pdf_v2, "PDF", resolution=200.0, save_all=True, append_images=pil_ims[1:], title="A Grande História da Luz - Vol. 2: As Estrelas da Promessa", author=AUTHOR_NAME)

    # 2. Exportar PDF de Impressão 300 DPI com sangria do Volume 2 (24 páginas)
    print_pdf_v2 = os.path.join(BASE_DIR, "13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol2_Print_300DPI_Bleed.pdf")
    print_ims = [crop_and_resize(im, 2438, 3075) for im in pil_ims]
    print_ims[0].save(print_pdf_v2, "PDF", resolution=300.0, save_all=True, append_images=print_ims[1:], title="A Grande História da Luz - Vol. 2 (Print 300 DPI Bleed)", author=AUTHOR_NAME)

    # 3. Exportar EPUB 3 Fixed-Layout (Amazon KDP) do Volume 2 (24 páginas)
    epub_v2 = os.path.join(BASE_DIR, "11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol2_FixedLayout_KDP.epub")
    with zipfile.ZipFile(epub_v2, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>'''
        zf.writestr("META-INF/container.xml", container_xml)
        manifest_items = []
        spine_items = []
        for idx, p_path in enumerate(saved, start=1):
            img_name = f"page_{idx:02d}.jpg"
            xhtml_name = f"page_{idx:02d}.xhtml"
            jpg_temp = p_path.replace(".png", ".jpg")
            Image.open(p_path).convert("RGB").save(jpg_temp, "JPEG", quality=92)
            zf.write(jpg_temp, f"OEBPS/images/{img_name}")
            os.remove(jpg_temp)
            prop = ' properties="cover-image"' if idx == 1 else ''
            manifest_items.append(f'    <item id="img{idx:02d}" href="images/{img_name}" media-type="image/jpeg"{prop}/>')
            manifest_items.append(f'    <item id="page{idx:02d}" href="{xhtml_name}" media-type="application/xhtml+xml"/>')
            spread_prop = "page-spread-right" if idx == 1 or idx % 2 == 1 else "page-spread-left"
            spine_items.append(f'    <itemref idref="page{idx:02d}" properties="{spread_prop}"/>')
            xhtml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head>
  <title>Página {idx}</title>
  <meta name="viewport" content="width=1600, height=2000"/>
  <style type="text/css">
    html, body {{ margin: 0; padding: 0; width: 1600px; height: 2000px; overflow: hidden; background-color: #0b132b; }}
    img {{ width: 1600px; height: 2000px; display: block; }}
  </style>
</head>
<body>
  <img src="images/{img_name}" alt="Página {idx}"/>
</body>
</html>'''
            zf.writestr(f"OEBPS/{xhtml_name}", xhtml_content)

        nav_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head><title>Sumário</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>A Grande História da Luz — Volume 2 ({AUTHOR_NAME})</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — As Estrelas da Promessa</a></li>
      <li><a href="page_02.xhtml">Folha de Rosto e Guia de Leitura</a></li>
      <li><a href="page_03.xhtml">Mapa da Jornada e Sumário</a></li>
      <li><a href="page_04.xhtml">Capítulo 1 — O Contador de Estrelas</a></li>
      <li><a href="page_07.xhtml">Capítulo 2 — O Bebê que Trouxe o Riso</a></li>
      <li><a href="page_10.xhtml">Capítulo 3 — A Escada de Luz no Meio da Noite</a></li>
      <li><a href="page_13.xhtml">Capítulo 4 — O Jovem Sonhador e a Túnica Colorida</a></li>
      <li><a href="page_16.xhtml">Capítulo 5 — Os Sonhos do Faraó e os Celeiros da Vida</a></li>
      <li><a href="page_19.xhtml">Capítulo 6 — O Abraço Mais Forte que a Tempestade</a></li>
      <li><a href="page_22.xhtml">Arqueologia e Glossário do Volume 2</a></li>
      <li><a href="page_23.xhtml">Bíblia de Personagens (Abraão, Sara e José)</a></li>
      <li><a href="page_24.xhtml">Contracapa Oficial</a></li>
    </ol>
  </nav>
</body>
</html>'''
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-vol2-2026</dc:identifier>
    <dc:title>As Estrelas da Promessa — Os amigos que caminharam olhando para o céu (A Grande História da Luz - Vol. 2)</dc:title>
    <dc:language>pt-BR</dc:language>
    <dc:creator>{AUTHOR_NAME}</dc:creator>
    <meta property="dcterms:modified">2026-11-13T18:00:00Z</meta>
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:orientation">portrait</meta>
    <meta property="rendition:spread">landscape</meta>
    <meta name="fixed-layout" content="true"/>
    <meta name="original-resolution" content="1600x2000"/>
    <meta name="book-type" content="children"/>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
{chr(10).join(manifest_items)}
  </manifest>
  <spine>
{chr(10).join(spine_items)}
  </spine>
</package>'''
        zf.writestr("OEBPS/content.opf", opf_content)
    print("   Volume 2 (24 páginas) exportado com sucesso!")

if __name__ == "__main__":
    build_vol2_pages_and_exports()
    print("VOLUME 2 (24 PÁGINAS) CONCLUÍDO COM SUCESSO!")
