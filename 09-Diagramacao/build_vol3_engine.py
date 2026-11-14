#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e de Ilustração — Volume 3 (eBook 3): O Caminho da Liberdade
Subtítulo: O príncipe do Nilo e a travessia do deserto
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Gera a Capa Oficial do Volume 3 (Capa 2 Aventura Infantil com FÁBIO MOTTA E SILVA),
diagrama as 24 páginas completas e sequenciais (PÁGINA 01 a PÁGINA 24) do Volume 3 em Dupla Camada (4-6 e 6-10 anos),
e exporta PDF HD (200 DPI), PDF de Impressão 300 DPI com sangria (24 páginas KDP Print) e EPUB 3 Fixed-Layout (Amazon KDP).
"""

import os
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
BRAIN_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/brain/026b6e7b-1190-4ec1-b3f4-789abc0233f8"
FONT_DIR = os.path.join(BASE_DIR, "03-Identidade-Visual/fonts")
VOL3_DIR = os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade")

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

def draw_page_footer(img, page_num, chapter_label="VOLUME 3  •  O CAMINHO DA LIBERDADE", dark_mode=True):
    draw = ImageDraw.Draw(img)
    f_foot = load_font("atkinson_bold", 22)
    color = (226, 232, 240, 210) if dark_mode else (71, 85, 105, 220)
    line_col = (245, 190, 70, 140) if dark_mode else (180, 83, 9, 120)
    draw.line([(90, PAGE_H - 78), (PAGE_W - 90, PAGE_H - 78)], fill=line_col, width=2)
    draw.text((90, PAGE_H - 62), chapter_label, font=f_foot, fill=color)
    p_str = f"PÁGINA {page_num:02d} DE 24"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def prepare_vol3_assets():
    print("-> Copiando e preparando ilustrações 3D originais do Volume 3 com FÁBIO MOTTA E SILVA...")
    ilus_dir = os.path.join(VOL3_DIR, "ilustracoes")
    p_dir = os.path.join(VOL3_DIR, "paginas_piloto")
    os.makedirs(ilus_dir, exist_ok=True)
    os.makedirs(p_dir, exist_ok=True)

    mapping = [
        ("vol3_capa_base_aventura_1794596842460.jpg", os.path.join(ilus_dir, "vol3_capa_base_aventura.jpg")),
        ("vol3_cap1_cesto_nilo_1794596888777.jpg", os.path.join(ilus_dir, "vol3_cap1_cesto_nilo.jpg")),
        ("vol3_cap2_sarca_luz_1794596959576.jpg", os.path.join(ilus_dir, "vol3_cap2_sarca_luz.jpg")),
        ("vol3_cap3_noite_liberdade_1794598327853.jpg", os.path.join(ilus_dir, "vol3_cap3_noite_liberdade.jpg")),
        ("vol3_cap4_travessia_mar_1794597022524.jpg", os.path.join(ilus_dir, "vol3_cap4_travessia_mar.jpg")),
        ("vol3_cap5_pao_do_ceu_sinai_1794597691202.jpg", os.path.join(ilus_dir, "vol3_cap5_pao_do_ceu_sinai.jpg")),
        ("vol3_cap6_terra_prometida_1794597798763.jpg", os.path.join(ilus_dir, "vol3_cap6_terra_prometida.jpg")),
        ("char_sheet_moises_miriam_1794598522689.jpg", os.path.join(BASE_DIR, "04-Biblia-de-Personagens/char_sheet_moises_miriam.jpg")),
    ]
    for src_name, dst_path in mapping:
        src = os.path.join(BRAIN_DIR, src_name)
        if os.path.exists(src):
            shutil.copy2(src, dst_path)

    aventura_v3 = Image.open(os.path.join(ilus_dir, "vol3_capa_base_aventura.jpg")).convert("RGB")
    cov_rgba = crop_and_resize(aventura_v3, PAGE_W, PAGE_H).convert("RGBA")
    grad = Image.new("RGBA", (PAGE_W, PAGE_H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grad)
    for y in range(520):
        alpha = int(190 * (1 - y / 520.0) ** 1.35)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 18, 44, alpha))
    for y in range(PAGE_H - 360, PAGE_H):
        alpha = int(215 * ((y - (PAGE_H - 360)) / 360.0) ** 1.3)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 16, 38, alpha))
    cov_rgba = Image.alpha_composite(cov_rgba, grad)
    cdraw = ImageDraw.Draw(cov_rgba)

    f_series = load_font("cinzel", 34)
    f_title = load_font("cinzel", 74)
    f_sub = load_font("nunito", 38)
    f_tag = load_font("atkinson_bold", 26)
    f_author = load_font("cinzel", 30)

    cdraw.line([(360, 78), (PAGE_W - 360, 78)], fill=(245, 190, 70, 220), width=3)
    draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 96, PAGE_W - 200, f_series, fill=(240, 246, 255), align="center", shadow=True)
    cdraw.line([(480, 152), (PAGE_W - 480, 152)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(cdraw, "O CAMINHO DA LIBERDADE", 70, 178, PAGE_W - 140, f_title, fill=(255, 224, 115), align="center", shadow=True)
    draw_wrapped_text(cdraw, "O príncipe do Nilo e a travessia do deserto", 120, 285, PAGE_W - 240, f_sub, fill=(255, 255, 255), align="center", shadow=True)

    cov_rgba = draw_rounded_panel(cov_rgba, (220, PAGE_H - 235, PAGE_W - 220, PAGE_H - 70), (12, 22, 48, 222), (245, 190, 70, 235), border_width=3, radius=24)
    cdraw = ImageDraw.Draw(cov_rgba)
    draw_wrapped_text(cdraw, "VOLUME 3  •  A BÍBLIA ILUSTRADA PARA PEQUENOS EXPLORADORES", 240, PAGE_H - 208, PAGE_W - 480, f_tag, fill=(254, 240, 138), align="center")
    draw_wrapped_text(cdraw, AUTHOR_UPPER, 240, PAGE_H - 142, PAGE_W - 480, f_author, fill=(255, 255, 255), align="center")
    cov_path = os.path.join(ilus_dir, "vol3_capa_oficial_aventura.png")
    cov_rgba.convert("RGB").save(cov_path, quality=95)
    shutil.copy2(cov_path, os.path.join(BRAIN_DIR, "vol3_capa_oficial_aventura.png"))

def make_3page_chapter(art_img, start_page, cap_num, cap_title, ref_text, main_narrative, quick_box, seed_4_6, explorer_dialogue, arq_title, arq_text, family_question, dark_mode=False):
    """
    Gera 3 páginas completas para cada capítulo do Volume 3:
    - Página A (start_page): Arte 3D em grande formato + Narrativa Principal + Box Rápido
    - Página B (start_page + 1): Camada Semente (4-6 anos) + Diálogos Literários Completos (Camada 6-10 anos)
    - Página C (start_page + 2): Zoom Cinematográfico Panorâmico + Pequena Grande Descoberta + O Que Você Faria?
    """
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

    # --- PÁGINA A: ABERTURA ILUSTRADA 3D ---
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
    draw_page_footer(pA_rgb, start_page, f"VOLUME 3  •  CAPÍTULO {cap_num}: {cap_title}", dark_mode=dark_mode)

    # --- PÁGINA B: DUPLA CAMADA (4-6 ANOS & DIÁLOGOS 6-10 ANOS) ---
    pB = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    w, h = art_img.size
    left_zoom = art_img.crop((0, int(h * 0.08), int(w * 0.75), int(h * 0.62)))
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
    draw_page_footer(pB_rgb, start_page + 1, f"VOLUME 3  •  CAPÍTULO {cap_num} (DUPLA CAMADA)", dark_mode=dark_mode)

    # --- PÁGINA C: ARQUEOLOGIA, HISTÓRIA E CONVERSA EM FAMÍLIA ---
    pC = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    right_zoom = art_img.crop((int(w * 0.18), int(h * 0.22), w, int(h * 0.88)))
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
    draw_page_footer(pC_rgb, start_page + 2, f"VOLUME 3  •  CAPÍTULO {cap_num} (DESCOBERTAS)", dark_mode=dark_mode)

    return [pA_rgb, pB_rgb, pC_rgb]

def build_vol3_pages_and_exports():
    prepare_vol3_assets()
    f_h1 = load_font("cinzel", 50)
    f_h2 = load_font("cinzel", 36)
    f_body = load_font("nunito", 32)
    f_italic = load_font("nunito_italic", 30)
    f_box_title = load_font("atkinson_bold", 27)
    f_box_body = load_font("atkinson", 25)
    f_ref = load_font("atkinson_bold", 24)

    pages = []
    ilus_dir = os.path.join(VOL3_DIR, "ilustracoes")
    p_dir = os.path.join(VOL3_DIR, "paginas_piloto")

    cesto_im = Image.open(os.path.join(ilus_dir, "vol3_cap1_cesto_nilo.jpg")).convert("RGB")
    sarca_im = Image.open(os.path.join(ilus_dir, "vol3_cap2_sarca_luz.jpg")).convert("RGB")
    noite_im = Image.open(os.path.join(ilus_dir, "vol3_cap3_noite_liberdade.jpg")).convert("RGB")
    mar_im = Image.open(os.path.join(ilus_dir, "vol3_cap4_travessia_mar.jpg")).convert("RGB")
    sinai_im = Image.open(os.path.join(ilus_dir, "vol3_cap5_pao_do_ceu_sinai.jpg")).convert("RGB")
    nebo_im = Image.open(os.path.join(ilus_dir, "vol3_cap6_terra_prometida.jpg")).convert("RGB")

    # PÁGINA 01: CAPA OFICIAL VOLUME 3
    p1 = Image.open(os.path.join(ilus_dir, "vol3_capa_oficial_aventura.png")).convert("RGB")
    pages.append(("vol3_p01_capa.png", p1))

    # PÁGINA 02: FOLHA DE ROSTO, CARTA DE BOAS-VINDAS E GUIA DE LEITURA
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    p2.paste(crop_and_resize(cesto_im, PAGE_W - 180, 680), (90, 75))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([90, 75, PAGE_W - 90, 755], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d2, "O CAMINHO DA LIBERDADE", 100, 785, PAGE_W - 200, f_h1, fill=(146, 64, 14), align="center")
    draw_wrapped_text(d2, f"Volume 3  •  Autor: {AUTHOR_NAME} (Edição Independente)", 100, 850, PAGE_W - 200, f_ref, fill=(30, 58, 138), align="center")
    intro_v3 = (
        "Bem-vindo ao terceiro volume da coleção A Grande História da Luz! Depois que a família de Jacó e José cresceu no Egito, um novo rei subiu ao trono e transformou o povo em escravos. Mas a Luz do Criador jamais esquece os pequeninos!\n\n"
        "Acompanhe a corajosa menina Miriã e seu irmãozinho Moisés desde o cestinho de papiro nas águas do rio Nilo até a sarça que brilhava sem queimar, a travessia do mar e a chegada ao horizonte da Terra Prometida."
    )
    draw_wrapped_text(d2, intro_v3, 110, 910, PAGE_W - 220, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p2 = draw_rounded_panel(p2, (95, 1390, PAGE_W - 95, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "COMO LER ESTE LIVRO EM FAMÍLIA (DUPLA CAMADA 4–10 ANOS):", 135, 1420, PAGE_W - 270, f_box_title, fill=(146, 64, 14))
    guia_v3 = (
        "• Cada um dos 6 capítulos conta com 3 páginas completas (Páginas 04 a 21).\n"
        "• Na 1ª página do capítulo, contemple a grande ilustração 3D e o resumo narrativo.\n"
        "• Na 2ª página, escolha entre a Camada Semente (4–6 anos) ou os Diálogos da Camada Explorador (6–10 anos).\n"
        "• Na 3ª página, descubra segredos arqueológicos do Egito e do Sinai e converse em família!"
    )
    draw_wrapped_text(d2, guia_v3, 135, 1475, PAGE_W - 270, f_box_body, fill=(68, 64, 60), line_spacing=1.42)
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 2, "FOLHA DE ROSTO E GUIA DE LEITURA  •  VOLUME 3", dark_mode=False)
    pages.append(("vol3_p02_folha_rosto.png", p2_rgb))

    # PÁGINA 03: MAPA DA JORNADA DO ÊXODO E SUMÁRIO DOS 6 CAPÍTULOS
    p3_map = Image.new("RGBA", (PAGE_W, PAGE_H), (12, 20, 40, 255))
    p3_map.paste(crop_and_resize(nebo_im, PAGE_W - 140, 600), (70, 70))
    dm = ImageDraw.Draw(p3_map)
    dm.rectangle([70, 70, PAGE_W - 70, 670], outline=(245, 190, 70), width=4)
    draw_wrapped_text(dm, "MAPA DA JORNADA: DO RIO NILO À TERRA PROMETIDA", 90, 700, PAGE_W - 180, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(dm, f"Roteiro e Direção Editorial: {AUTHOR_NAME}", 90, 752, PAGE_W - 180, f_ref, fill=(186, 230, 253), align="center")
    p3_map = draw_rounded_panel(p3_map, (85, 810, PAGE_W - 85, 1885), (30, 41, 59, 240), (245, 190, 70, 220), border_width=3, radius=24)
    dm = ImageDraw.Draw(p3_map)
    sum_txt = (
        "• CAPÍTULO 1 — O Pequeno Barco de Papiro no Rio Nilo (Êxodo 1–2 | Págs. 04 a 06):\n"
        "  A coragem de Joquebede e Miriã, o cestinho entre os juncos e a compaixão da filha do Faraó.\n\n"
        "• CAPÍTULO 2 — O Arbusto que Brilhava Sem Queimar (Êxodo 3–4 | Págs. 07 a 09):\n"
        "  O pastor Moisés no monte Horebe e o chamado da Luz na Sarça Ardente.\n\n"
        "• CAPÍTULO 3 — A Noite da Esperança e da Liberdade (Êxodo 7–12 | Págs. 10 a 12):\n"
        "  Os sinais diante do coração endurecido do Faraó e a primeira Páscoa das famílias.\n\n"
        "• CAPÍTULO 4 — Um Caminho no Meio do Mar (Êxodo 14–15 | Págs. 13 a 15):\n"
        "  A Coluna de Luz, o vento que abriu as águas e a dança alegre do tamborim de Miriã.\n\n"
        "• CAPÍTULO 5 — O Pão do Céu e a Montanha da Luz (Êxodo 16–20 | Págs. 16 a 18):\n"
        "  O maná da manhã, a água brotando da rocha e as Dez Palavras de amor no monte Sinai.\n\n"
        "• CAPÍTULO 6 — O Horizonte da Terra Prometida (Deuteronômio 31–34 | Págs. 19 a 21):\n"
        "  Moisés e Josué no alto do monte Nebo contemplando o vale verdejante do rio Jordão."
    )
    draw_wrapped_text(dm, sum_txt, 125, 845, PAGE_W - 250, f_box_body, fill=(248, 250, 252), line_spacing=1.35)
    p3_map_rgb = p3_map.convert("RGB")
    draw_page_footer(p3_map_rgb, 3, "SUMÁRIO VISUAL E ROTA DO ÊXODO  •  VOLUME 3", dark_mode=True)
    pages.append(("vol3_p03_mapa_sumario.png", p3_map_rgb))

    # CAPÍTULO 1 (PÁGINAS 04, 05, 06)
    c1_pages = make_3page_chapter(
        cesto_im, 4, 1, "O PEQUENO BARCO DE PAPIRO NO RIO NILO", "Base Bíblica: Êxodo 1:8–2:10",
        "No Egito antigo, às margens do grande rio Nilo, nasceu um bebê que corria perigo por causa de um decreto cruel do Faraó. Sua mãe, Joquebede, colheu hastes de papiro, trançou um cesto bem firme e o calafetou com betume e piche.\n\n"
        "— Fique de olho nele, Miriã — sussurrou a mãe. — A Luz do Criador vai guardar o seu irmãozinho!\n"
        "Quando a filha do Faraó abriu o cesto, sentiu compaixão do bebê, acolheu-o e deu-lhe o nome de Moisés ('tirado das águas')!",
        "» PEQUENA GRANDE DESCOBERTA: Em hebraico, o cestinho de papiro de Moisés chama-se 'Tevah' — a mesma palavra usada para a Arca de Noé!",
        "Há muito tempo, no rio Nilo cheio de flores de lótus, uma mamãe colocou seu bebê num cestinho impermeável entre os juncos. A irmãzinha Miriã ficou vigiando escondida até a princesa do Egito encontrar o bebê e chamar a própria mamãe dele para cuidar de Moisés!",
        "Escondida entre as hastes verdes de papiro, a pequena Miriã viu a princesa segurar o bebê que chorava. Respirou fundo, criou coragem e aproximou-se com respeito:\n"
        "— Princesa, quer que eu chame uma mulher dentre as hebreias para amamentar e cuidar deste menino para a senhora?\n"
        "— Vá chamar! — respondeu a filha do Faraó com um sorriso bondoso.\n"
        "Miriã correu como o vento e trouxe a própria mãe, Joquebede! Assim, o pequeno Moisés cresceu seguro nos braços de sua família antes de ser educado no palácio.",
        "O PAPIRO E O RIO NILO NO EGITO ANTIGO",
        "A planta do papiro crescia nas margens rasas do Nilo e chegava a três metros de altura! Seus caules triangulares flutuavam muito bem e eram usados pelos egípcios para fazer barcos leves, cestos, sandálias e folhas de escrita.",
        "Miriã teve muita coragem e presença de espírito para proteger seu irmãozinho. De que maneiras você gosta de ajudar e proteger quem é menor que você?",
        dark_mode=False
    )
    pages.append(("vol3_p02_cesto_nilo.png", c1_pages[0]))
    pages.append(("vol3_p05_cap1_camadas.png", c1_pages[1]))
    pages.append(("vol3_p06_cap1_descobertas.png", c1_pages[2]))

    # CAPÍTULO 2 (PÁGINAS 07, 08, 09)
    c2_pages = make_3page_chapter(
        sarca_im, 7, 2, "O ARBUSTO QUE BRILHAVA SEM QUEIMAR", "Base Bíblica: Êxodo 3:1–4:17 (A Sarça de Luz)",
        "Cuidando de ovelhas no monte Horebe, Moisés viu uma maravilha: um arbusto do deserto brilhava com chamas douradas e azuis da Presença Divina, mas nenhuma folha se queimava!\n\n"
        "— Moisés! Moisés! Tire as sandálias dos pés, porque este lugar é sagrado. Eu vi o sofrimento do meu povo no Egito e estou enviando você para libertá-los!\n"
        "— Eu estarei com você! — prometeu a Luz. — E o seu irmão Arão irá ao seu lado!",
        "» O QUE VOCÊ FARIA? Moisés achava que não falava bem, mas descobriu que não estava sozinho!",
        "No silêncio da montanha, o pastor Moisés viu um arbusto todo iluminado por uma luz dourada e azul que não queimava os galhos! Daquela Luz saiu a voz amorosa de Deus chamando Moisés pelo nome e dizendo: 'Não tenha medo, Eu estarei com você para libertar o meu povo!'",
        "Moisés cobriu o rosto diante daquele esplendor luminoso e abriu seu coração com sinceridade:\n"
        "— Ó Senhor, quem sou eu para ir ao Faraó? Eu nunca fui bom para falar em público, minhas palavras se atrapalham!\n"
        "A Luz brilhou ainda mais suave ao redor do cajado de madeira de acácia:\n"
        "— Quem deu a boca ao ser humano? Eu estarei com você quando falar, e seu irmão Arão caminhará ao seu lado!",
        "OS PASTORES DE MIDIÃ E O MONTE HOREBE",
        "Antes de liderar multidões pelo deserto, Moisés passou quarenta anos cuidando das ovelhas de seu sogro Jetro em Midiã. Ali ele aprendeu a conhecer cada trilha, poço de água e sombra das montanhas do Sinai.",
        "Quando você precisa apresentar um trabalho ou falar em público e sente frio na barriga, quem ajuda você a se sentir mais confiante?",
        dark_mode=True
    )
    pages.append(("vol3_p03_sarca_luz.png", c2_pages[0]))
    pages.append(("vol3_p08_cap2_camadas.png", c2_pages[1]))
    pages.append(("vol3_p09_cap2_descobertas.png", c2_pages[2]))

    # CAPÍTULO 3 (PÁGINAS 10, 11, 12)
    c3_pages = make_3page_chapter(
        noite_im, 10, 3, "A NOITE DA ESPERANÇA E DA LIBERDADE", "Base Bíblica: Êxodo 7–12 (A Primeira Páscoa)",
        "Moisés e Arão pediram muitas vezes ao Faraó que deixasse o povo ir, mas o rei endureceu o coração diante dos grandes sinais na natureza. Até que chegou a noite decisiva da libertação!\n\n"
        "Reunidas em suas casas de tijolos de barro, com as sandálias nos pés e o cajado na mão, as famílias repartiram o pão sem fermento sob o arco luminoso de proteção do Criador. Antes do amanhecer, as portas da liberdade finalmente se abriram!",
        "» PEQUENA GRANDE DESCOBERTA: A palavra 'Páscoa' vem do hebraico 'Pesach' ('passar sobre / proteger com amor')!",
        "O rei do Egito tinha o coração duro como pedra e não queria deixar as famílias saírem. Mas na noite da Páscoa, cada família jantou unida dentro de casa sob a proteção da Luz de Deus. Naquela mesma madrugada, o Faraó finalmente deixou o povo partir em liberdade!",
        "Dentro da pequena casa em Gósen, as crianças amarravam as sandálias de couro enquanto o pai segurava o cajado de viagem:\n"
        "— Papai, por que estamos comendo este pão achatadinho tão depressa? — perguntou o filho menor.\n"
        "— É o pão da pressa, meu filho! — respondeu a mãe com os olhos brilhando de esperança. — Hoje mesmo a Luz do Senhor vai abrir as portas do Egito para caminharmos como um povo livre!",
        "OS TIJOLOS DE BARRO E O PÃO SEM FERMENTO (MATZÁ)",
        "Como o povo precisou sair do Egito antes que a massa do pão tivesse tempo de fermentar e crescer, o pão assado rapidamente sobre pedras quentes ficou fininho e crocante — lembrado até hoje na festa da Páscoa!",
        "Por que a teimosia e o orgulho do Faraó trouxeram tanta tristeza, enquanto saber ouvir bons conselhos traz paz para todo mundo?",
        dark_mode=True
    )
    pages.append(("vol3_p04_noite_liberdade.png", c3_pages[0]))
    pages.append(("vol3_p11_cap3_camadas.png", c3_pages[1]))
    pages.append(("vol3_p12_cap3_descobertas.png", c3_pages[2]))

    # CAPÍTULO 4 (PÁGINAS 13, 14, 15)
    c4_pages = make_3page_chapter(
        mar_im, 13, 4, "UM CAMINHO NO MEIO DO MAR", "Base Bíblica: Êxodo 14:13–31; 15:20–21",
        "Diante das águas profundas do mar, o povo sentiu medo ao ouvir os carros do Faraó se aproximando. Mas Moisés disse com firmeza:\n"
        "— Não tenham medo! Fiquem firmes e vejam o livramento que o Senhor fará hoje!\n\n"
        "Guiado pela Coluna de Luz, um vento fortíssimo soprou a noite inteira, abrindo duas muralhas de água cristalina e revelando um caminho seco no meio do mar! Na outra margem, Miriã pegou seu tamborim e liderou a dança da liberdade.",
        "» CONVERSE COMIGO: Qual música deixa a sua família mais alegre quando vocês vencem um dia difícil?",
        "Quando chegaram à beira do mar, parecia que não havia saída! Mas a Coluna de Luz protegeu as famílias e um vento forte abriu um corredor enxuto bem no meio das águas! Do outro lado, Miriã tocou seu tamborim e todos cantaram de alegria!",
        "Enquanto caminhavam pelo leito firme entre as duas paredes de água azul-turquesa iluminadas pela Coluna de Luz, as crianças seguravam a mão dos pais e dos avós sem tropeçar.\n"
        "Assim que o último pé tocou a praia segura do outro lado e o sol da manhã despontou, Miriã ergueu seu tamborim de madeira adornado com fitas coloridas e cantou:\n"
        "— Cantem ao Senhor, porque Ele fez maravilhas e nos conduziu em segurança!",
        "A COLUNA DE NUVEM E LUZ NO DESERTO",
        "No deserto escaldante do Sinai, o calor do dia chega a 40°C e a noite é muito fria e escura. Na narrativa de Êxodo, a Presença Divina acompanhava o acampamento como nuvem fresca de sombra durante o dia e coluna de luz aquecedora à noite!",
        "Quando um problema parece grande como um mar fechado, o que ajuda você a manter a calma e dar o próximo passo com fé?",
        dark_mode=True
    )
    pages.append(("vol3_p05_travessia_mar.png", c4_pages[0]))
    pages.append(("vol3_p14_cap4_camadas.png", c4_pages[1]))
    pages.append(("vol3_p15_cap4_descobertas.png", c4_pages[2]))

    # CAPÍTULO 5 (PÁGINAS 16, 17, 18)
    c5_pages = make_3page_chapter(
        sinai_im, 16, 5, "O PÃO DO CÉU E A MONTANHA DA LUZ", "Base Bíblica: Êxodo 16–20 (Maná, Rocha e Sinai)",
        "No deserto, a Presença Divina nunca deixou faltar cuidado: a cada manhã, o chão amanhecia coberto pelo maná — floquinhos brancos doces como mel — e da rocha seca brotou água fresca para matar a sede das crianças e dos rebanhos!\n\n"
        "Ao pé do monte Sinai coroado de luz dourada e safira, o povo recebeu as Dez Palavras da Vida: leis de amor para honrar a Deus, respeitar os pais, dizer a verdade e proteger o próximo.",
        "» VOCÊ PERCEBEU? As Dez Palavras ensinaram um povo recém-liberto a viver em comunidade com justiça e paz!",
        "No deserto não havia padarias nem rios, mas todas as manhãs caía do céu um pãozinho doce como mel chamado Maná, e da pedra saía água fresquinha! Depois, no monte Sinai, Deus entregou dez conselhos de amor para que todos vivessem como irmãos.",
        "Logo cedo, quando o orvalho evaporava na areia dourada, as crianças saíam das tendas com cestinhos trançados:\n"
        "— Manhu? ('O que é isto?') — perguntavam elas, provando os floquinhos brancos que tinham gosto de bolacha com mel.\n"
        "— É o pão que o Senhor nos dá a cada manhã — explicava Moisés. — Colham o suficiente para hoje e repartam de modo que ninguém tenha falta!",
        "AS DEZ PALAVRAS E O DESCANSO PARA TODOS",
        "Na antiguidade, escravos nunca tinham folga. No monte Sinai, uma das leis mais revolucionárias dizia que a cada sete dias TODAS as pessoas — inclusive os trabalhadores, os estrangeiros e até os animais — tinham direito sagrado ao descanso!",
        "Por que regras de respeito — como não mentir, não pegar o que é do outro e honrar os pais — deixam a nossa casa e a escola muito mais felizes?",
        dark_mode=False
    )
    pages.append(("vol3_p06_pao_do_ceu_sinai.png", c5_pages[0]))
    pages.append(("vol3_p17_cap5_camadas.png", c5_pages[1]))
    pages.append(("vol3_p18_cap5_descobertas.png", c5_pages[2]))

    # CAPÍTULO 6 (PÁGINAS 19, 20, 21)
    c6_pages = make_3page_chapter(
        nebo_im, 19, 6, "O HORIZONTE DA TERRA PROMETIDA", "Base Bíblica: Números 13–14; Deuteronômio 31 e 34",
        "Depois de quarenta anos de aprendizado pelo deserto, Moisés subiu ao topo do monte Nebo ao lado do jovem Josué. Lá de cima, sob um arco luminoso de esperança, contemplou o vale do rio Jordão e os olivais verdejantes da Terra Prometida.\n\n"
        "— Seja forte e corajoso, Josué! — abençoou Moisés com o coração em paz. — A Luz do Senhor irá adiante de vocês, e Ele jamais os deixará!",
        "» O QUE VOCÊ FARIA? Moisés passou a missão adiante encorajando o jovem Josué com carinho!",
        "Depois de uma longa caminhada pelo deserto, o sábio Moisés subiu ao alto do monte Nebo com seu ajudante Josué. Lá de cima eles viram o rio Jordão e as árvores verdinhas da Terra Prometida! Moisés abençoou Josué dizendo: 'Seja forte e corajoso!'",
        "O vento suave da tarde balançava o manto de Moisés no alto do monte Pisga (Nebo). Com os olhos cheios de gratidão por tudo o que havia vivido desde o cestinho no Nilo, ele pousou as mãos sobre os ombros de Josué:\n"
        "— Você guiará estas famílias até a terra que o Senhor prometeu aos nossos antepassados Abraão, Isaque e Jacó. Não tenha medo nem desanime, pois a Presença Luminosa caminhará à sua frente!",
        "A VISTA REAL DO MONTE NEBO",
        "Do alto do Monte Nebo (na atual Jordânia, a 817 metros de altitude), em dias claros é possível avistar a olho nu exatamente a paisagem descrita em Deuteronômio 34: o Mar Morto, o vale verde do rio Jordão, Jericó e as colinas de Judá!",
        "Quem foi um professor, avô, avó ou pessoa mais velha que já ensinou algo muito importante que você vai guardar para a vida inteira?",
        dark_mode=False
    )
    pages.append(("vol3_p07_terra_prometida.png", c6_pages[0]))
    pages.append(("vol3_p20_cap6_camadas.png", c6_pages[1]))
    pages.append(("vol3_p21_cap6_descobertas.png", c6_pages[2]))

    # PÁGINA 22: PEQUENA GRANDE DESCOBERTA ESPECIAL — ARQUEOLOGIA DO EGITO E DO SINAI
    p22 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "PEQUENA GRANDE DESCOBERTA  •  ARQUEOLOGIA DO VOLUME 3", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")
    p22 = draw_rounded_panel(p22, (80, 145, PAGE_W - 80, 960), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "1. TRÊS TESOUROS HISTÓRICOS DO EGITO E DO DESERTO", 120, 175, PAGE_W - 240, f_box_title, fill=(146, 64, 14))
    arq_v3_full = (
        "• Os Tijolos de Lama e Palha (Êxodo 5): Escavações arqueológicas no Delta Oriental do Nilo (região de Ávaris / Pi-Ramessés) revelaram imensos armazéns reais erguidos com milhões de tijolos de barro do Nilo misturado com palha picada. Sem a palha, a argila rachava ao secar ao sol!\n\n"
        "• O Tamborim de Miriã (Tof): Pinturas e relevos do Antigo Oriente Próximo mostram mulheres tocando o 'tof' (adufe ou tamborim circular de madeira revestido de couro) em danças coletivas de celebração e ação de graças.\n\n"
        "• A Madeira de Acácia do Sinai: A árvore usada na construção da Arca da Aliança e do Tabernáculo portátil (acácia-do-deserto) é a única árvore nativa capaz de crescer nas wadis (vales secos) da península do Sinai, tendo madeira extremamente resistente!"
    )
    draw_wrapped_text(d22, arq_v3_full, 120, 230, PAGE_W - 240, f_body, fill=(41, 37, 36), line_spacing=1.35)

    p22 = draw_rounded_panel(p22, (80, 1005, PAGE_W - 80, 1885), (224, 242, 254, 255), (2, 132, 199, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, "2. PEQUENO GLOSSÁRIO DO EXPLORADOR (VOLUME 3)", 120, 1035, PAGE_W - 240, f_box_title, fill=(7, 89, 133))
    gloss_v3 = (
        "• PAPIRO: Planta aquática alta das margens do rio Nilo usada para cestos, barcos e rolos de escrita.\n"
        "• HOREBE / SINAI: Cadeia de montanhas rochosas onde Moisés viu a Sarça de Luz e recebeu as Dez Palavras.\n"
        "• PÁSCOA (PESACH): Festa da liberdade que recorda a proteção divina sobre as famílias na saída do Egito.\n"
        "• MANÁ: Alimento branco e adocicado recolhido a cada manhã no acampamento do deserto.\n"
        "• TABERNÁCULO: A grande tenda sagrada portátil que caminhava com o povo pelo deserto como sinal da Presença de Deus."
    )
    draw_wrapped_text(d22, gloss_v3, 120, 1090, PAGE_W - 240, f_body, fill=(28, 25, 23), line_spacing=1.38)
    p22_rgb = p22.convert("RGB")
    draw_page_footer(p22_rgb, 22, "VOLUME 3  •  ARQUEOLOGIA E GLOSSÁRIO DO EXPLORADOR", dark_mode=False)
    pages.append(("vol3_p22_arqueologia_glossario.png", p22_rgb))

    # PÁGINA 23: BÍBLIA DE PERSONAGENS DO VOLUME 3 (MIRIÃ E MOISÉS)
    p23 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, f"BÍBLIA DE PERSONAGENS  •  VOLUME 3 ({AUTHOR_UPPER})", 90, 75, PAGE_W - 180, f_h2, fill=(30, 58, 138), align="center")
    sheet_mm = Image.open(os.path.join(BASE_DIR, "04-Biblia-de-Personagens/char_sheet_moises_miriam.jpg")).convert("RGB").resize((1400, 788), Image.Resampling.LANCZOS)
    p23.paste(sheet_mm, (100, 145))
    d23.rectangle([100, 145, 1500, 933], outline=(180, 83, 9), width=4)

    p23 = draw_rounded_panel(p23, (85, 975, PAGE_W - 85, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, "RECONSTRUÇÃO HISTÓRICA E ANTROPOLÓGICA LEVANTINA", 125, 1005, PAGE_W - 250, f_box_title, fill=(146, 64, 14))
    leg_mm = (
        f"Direção Editorial e Autoral: {AUTHOR_NAME}\n\n"
        "• MIRIÃ (À ESQUERDA): Representada como uma jovem hebreia do Delta do Nilo com traços levantinos autênticos (pele morena-oliva aquecida pelo sol, olhos castanhos expressivos, cabelos escuros cacheados presos por faixa tecida). Veste túnica de linho cru com bordados geométricos azul-turquesa e segura o 'tof' (tamborim de madeira e couro).\n\n"
        "• MOISÉS (À DIREITA): Representado em sua maturidade como pastor em Midiã e líder do Êxodo. Veste túnica de lã não tingida, manto terracota e azul-índigo para proteção contra o vento do Sinai, sandálias de couro amarradas às canelas e cajado rústico de madeira de acácia."
    )
    draw_wrapped_text(d23, leg_mm, 125, 1060, PAGE_W - 250, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p23_rgb = p23.convert("RGB")
    draw_page_footer(p23_rgb, 23, "VOLUME 3  •  BÍBLIA DE PERSONAGENS (MIRIÃ E MOISÉS)", dark_mode=False)
    pages.append(("vol3_p08_descobertas_e_personagens.png", p23_rgb))

    # PÁGINA 24: CONTRACAPA OFICIAL DO VOLUME 3
    p24 = crop_and_resize(mar_im, PAGE_W, PAGE_H).convert("RGBA")
    p24 = draw_rounded_panel(p24, (110, 110, PAGE_W - 110, PAGE_H - 120), (8, 15, 38, 232), (245, 190, 70, 235), border_width=4, radius=32)
    d24 = ImageDraw.Draw(p24)
    draw_wrapped_text(d24, "O CAMINHO DA LIBERDADE", 160, 165, PAGE_W - 320, f_h1, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "Volume 3  •  A Grande História da Luz", 160, 238, PAGE_W - 320, f_italic, fill=(186, 230, 253), align="center")
    d24.line([(320, 300), (PAGE_W - 320, 300)], fill=(245, 190, 70, 180), width=2)

    back_v3 = (
        "De um pequeno cesto de papiro flutuando entre os juncos do rio Nilo até o topo iluminado do monte Sinai, descubra uma das maiores aventuras de fé, coragem e liberdade de todos os tempos!\n\n"
        "Neste terceiro volume da coleção escrita por Fábio Motta e Silva, as crianças caminham ao lado de Miriã, Moisés, Arão e Josué, aprendendo que a Luz de Deus ouve o clamor de quem sofre, abre caminhos onde parece impossível e nos ensina a viver em liberdade e amor.\n\n"
        "NO PRÓXIMO VOLUME (VOLUME 4 — CORAGEM NA TERRA PROMETIDA):\n"
        "Acompanhe Josué na travessia do rio Jordão, a sábia juíza Débora sob a palmeira, a doce amizade de Rute e Noemi nos campos de Belém e o pequeno Samuel ouvindo o chamado da Luz no silêncio da noite!"
    )
    draw_wrapped_text(d24, back_v3, 165, 340, PAGE_W - 330, f_body, fill=(248, 250, 252), line_spacing=1.38)
    d24.line([(320, 1695), (PAGE_W - 320, 1695)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(d24, f"AUTOR: {AUTHOR_UPPER}", 160, 1725, PAGE_W - 320, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "Edição Autônoma Independente  •  Volume 3 (24 Páginas Ilustradas)", 160, 1785, PAGE_W - 320, f_ref, fill=(186, 230, 253), align="center")
    p24_rgb = p24.convert("RGB")
    draw_page_footer(p24_rgb, 24, "CONTRACAPA OFICIAL  •  VOLUME 3: O CAMINHO DA LIBERDADE", dark_mode=True)
    pages.append(("vol3_p24_contracapa.png", p24_rgb))

    saved = []
    for fname, im in pages:
        fp = os.path.join(p_dir, fname)
        im.save(fp, quality=95)
        saved.append(fp)
        shutil.copy2(fp, os.path.join(BRAIN_DIR, fname))

    shutil.copy2(os.path.join(p_dir, "vol3_p05_travessia_mar.png"), os.path.join(p_dir, "vol3_p04_travessia_mar.png"))
    shutil.copy2(os.path.join(p_dir, "vol3_p05_travessia_mar.png"), os.path.join(BRAIN_DIR, "vol3_p04_travessia_mar.png"))

    # 1. Exportar PDF HD do Volume 3 (24 páginas)
    pdf_v3 = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol3_Piloto_HD.pdf")
    pil_ims = [Image.open(p).convert("RGB") for p in saved]
    pil_ims[0].save(pdf_v3, "PDF", resolution=200.0, save_all=True, append_images=pil_ims[1:], title="A Grande História da Luz - Vol. 3: O Caminho da Liberdade", author=AUTHOR_NAME)

    # 2. Exportar PDF de Impressão 300 DPI com sangria do Volume 3 (24 páginas)
    print_pdf_v3 = os.path.join(BASE_DIR, "13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol3_Print_300DPI_Bleed.pdf")
    print_ims = [crop_and_resize(im, 2438, 3075) for im in pil_ims]
    print_ims[0].save(print_pdf_v3, "PDF", resolution=300.0, save_all=True, append_images=print_ims[1:], title="A Grande História da Luz - Vol. 3 (Print 300 DPI Bleed)", author=AUTHOR_NAME)

    # 3. Exportar EPUB 3 Fixed-Layout (Amazon KDP) do Volume 3 (24 páginas)
    epub_v3 = os.path.join(BASE_DIR, "11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol3_FixedLayout_KDP.epub")
    with zipfile.ZipFile(epub_v3, "w") as zf:
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
    <h1>A Grande História da Luz — Volume 3 ({AUTHOR_NAME})</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — O Caminho da Liberdade</a></li>
      <li><a href="page_02.xhtml">Folha de Rosto e Guia de Leitura</a></li>
      <li><a href="page_03.xhtml">Mapa da Jornada e Sumário</a></li>
      <li><a href="page_04.xhtml">Capítulo 1 — O Pequeno Barco de Papiro no Nilo</a></li>
      <li><a href="page_07.xhtml">Capítulo 2 — O Arbusto que Brilhava Sem Queimar</a></li>
      <li><a href="page_10.xhtml">Capítulo 3 — A Noite da Esperança e da Liberdade</a></li>
      <li><a href="page_13.xhtml">Capítulo 4 — Um Caminho no Meio do Mar</a></li>
      <li><a href="page_16.xhtml">Capítulo 5 — O Pão do Céu e a Montanha da Luz</a></li>
      <li><a href="page_19.xhtml">Capítulo 6 — O Horizonte da Terra Prometida</a></li>
      <li><a href="page_22.xhtml">Arqueologia e Glossário do Volume 3</a></li>
      <li><a href="page_23.xhtml">Bíblia de Personagens (Miriã e Moisés)</a></li>
      <li><a href="page_24.xhtml">Contracapa Oficial</a></li>
    </ol>
  </nav>
</body>
</html>'''
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-vol3-2026</dc:identifier>
    <dc:title>O Caminho da Liberdade — O príncipe do Nilo e a travessia do deserto (A Grande História da Luz - Vol. 3)</dc:title>
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
    print("   Volume 3 (24 páginas) exportado com sucesso!")

if __name__ == "__main__":
    build_vol3_pages_and_exports()
    print("VOLUME 3 (24 PÁGINAS) CONCLUÍDO COM SUCESSO!")
