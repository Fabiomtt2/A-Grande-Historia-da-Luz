#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e Artístico — A Grande História da Luz (Volume 1: Faça-se a Luz)
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Responsável por:
1. Organizar e copiar as artes originais geradas para as pastas oficiais do projeto;
2. Renderizar em alta definição (1600x2000 px / 3200x2000 px spread) as ilustrações cósmicas e arqueológicas complementares;
3. Diagramar as 3 propostas de capa com o crédito autoral FÁBIO MOTTA E SILVA (e comparativo em tamanho real + miniatura 120px);
4. Diagramar as 24 páginas completas e sequenciais (PÁGINA 01 a PÁGINA 24) do Volume 1 com Dupla Camada (4-6 e 6-10 anos) e hierarquia tipográfica profissional (Cinzel, Nunito, Atkinson Hyperlegible);
5. Exportar:
   - PDF Digital HD (Hotmart / Kiwify / Apple Books - 200 DPI, 24 páginas)
   - PDF de Impressão Gráfica / KDP Print (300 DPI com sangria / bleed 0.125", 24 páginas — mínimo oficial da Amazon KDP Print)
   - EPUB 3 Fixed-Layout compatível com Amazon KDP Kids (24 páginas)
"""

import os
import sys
import math
import random
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
BRAIN_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/brain/026b6e7b-1190-4ec1-b3f4-789abc0233f8"
FONT_DIR = os.path.join(BASE_DIR, "03-Identidade-Visual/fonts")

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
    p = paths.get(name, paths["nunito"])
    try:
        return ImageFont.truetype(p, size)
    except Exception:
        return ImageFont.load_default()

def copy_approved_assets():
    print("-> Copiando e organizando ativos visuais aprovados...")
    mapping = [
        ("capa_conceito_1_cosmica_base_v2_1794578842801.jpg", "03-Identidade-Visual/capa_conceito_1_cosmica_base.jpg"),
        ("capa_conceito_2_aventura_base_1794578887466.jpg", "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg"),
        ("capa_conceito_3_pictorica_base_1794578947539.jpg", "03-Identidade-Visual/capa_conceito_3_pictorica_base.jpg"),
        ("char_sheet_adao_eva_1794578814115.jpg", "04-Biblia-de-Personagens/char_sheet_adao_eva.jpg"),
        ("char_sheet_noe_familia_1794578839466.jpg", "04-Biblia-de-Personagens/char_sheet_noe_familia.jpg"),
        ("char_sheet_jesus_historico_1794578973254.jpg", "04-Biblia-de-Personagens/char_sheet_jesus_historico.jpg"),
        ("char_sheet_moises_miriam_1794598522689.jpg", "04-Biblia-de-Personagens/char_sheet_moises_miriam.jpg"),
        ("vol1_cap1_cena1_misterio_abismo_1794578923931.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena1_misterio_abismo.jpg"),
        ("vol1_cap1_cena5_animais_jardim_1794578850797.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena5_animais_jardim.jpg"),
        ("vol1_cap1_cena6_humanidade_sopro_1794578887504.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena6_humanidade_sopro.jpg"),
        ("vol1_cap1_cena7_nomes_cuidadores_1794578949947.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena7_nomes_cuidadores.jpg"),
        ("vol1_cap2_jardim_eden_1794597077896.jpg", "08-Ilustracoes-Originais/vol1_cap2_jardim_eden.jpg"),
        ("vol1_cap3_escolha_jardim_1794597406575.jpg", "08-Ilustracoes-Originais/vol1_cap3_escolha_jardim.jpg"),
        ("vol1_cap4_caim_abel_1794597513298.jpg", "08-Ilustracoes-Originais/vol1_cap4_caim_abel.jpg"),
        ("vol1_cap5_arca_noe_1794597135841.jpg", "08-Ilustracoes-Originais/vol1_cap5_arca_noe.jpg"),
        ("vol1_cap6_torre_babel_1794597605073.jpg", "08-Ilustracoes-Originais/vol1_cap6_torre_babel.jpg"),
    ]
    for src_name, dst_rel in mapping:
        src = os.path.join(BRAIN_DIR, src_name)
        dst = os.path.join(BASE_DIR, dst_rel)
        if os.path.exists(src):
            shutil.copy2(src, dst)

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

def generate_complementary_artworks():
    print("-> Renderizando artes cósmicas e infográficas complementares em alta definição...")
    out_dir = os.path.join(BASE_DIR, "08-Ilustracoes-Originais")
    cosmica_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_1_cosmica_base.jpg")).convert("RGB")
    abismo_base = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap1_cena1_misterio_abismo.jpg")).convert("RGB")
    mandala_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_3_pictorica_base.jpg")).convert("RGB")

    # 1. Cena 2: Fiat Lux (Spread Panorâmico 3200 x 2000 px)
    spread_w, spread_h = 3200, 2000
    fiat_lux = Image.new("RGB", (spread_w, spread_h), (8, 14, 38))
    left_part = crop_and_resize(abismo_base, 1800, spread_h)
    right_part = crop_and_resize(cosmica_base, 1800, spread_h)
    fiat_lux.paste(left_part, (0, 0))
    mask = Image.new("L", (1800, spread_h))
    m_draw = ImageDraw.Draw(mask)
    for x in range(1800):
        val = int(255 * min(1.0, max(0.0, (x - 100) / 500.0)))
        m_draw.line([(x, 0), (x, spread_h)], fill=val)
    fiat_lux.paste(right_part, (1400, 0), mask)

    overlay = Image.new("RGBA", (spread_w, spread_h), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    cx, cy = 1950, 950
    random.seed(42)
    for i in range(90):
        angle = (i / 90.0) * 2 * math.pi + random.uniform(-0.02, 0.02)
        length = random.randint(900, 2200)
        ex = cx + int(math.cos(angle) * length)
        ey = cy + int(math.sin(angle) * length)
        width = random.randint(8, 36)
        color = (255, 225, 130, random.randint(18, 55)) if i % 2 == 0 else (100, 200, 255, random.randint(15, 40))
        odraw.line([(cx, cy), (ex, ey)], fill=color, width=width)
    for r in range(600, 20, -15):
        alpha = int(110 * (1 - r / 600.0) ** 2)
        odraw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 240, 180, alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=18))
    fiat_lux = Image.alpha_composite(fiat_lux.convert("RGBA"), overlay).convert("RGB")
    fiat_lux.save(os.path.join(out_dir, "vol1_cap1_cena2_fiat_lux.png"), quality=95)

    # 2. Cena 3: O Abraço do Céu, do Mar e da Terra
    w0, h0 = cosmica_base.size
    cena3 = cosmica_base.crop((0, int(h0 * 0.42), w0, h0))
    cena3 = crop_and_resize(cena3, 1600, 1300)
    cena3 = ImageEnhance.Color(cena3).enhance(1.15)
    cena3.save(os.path.join(out_dir, "vol1_cap1_cena3_ceu_mar_terra.png"), quality=95)

    # 3. Cena 4: Dança das Estrelas, das Águas e das Asas
    wm, hm = mandala_base.size
    cena4 = mandala_base.crop((int(wm * 0.06), int(hm * 0.16), int(wm * 0.94), int(hm * 0.78)))
    cena4 = crop_and_resize(cena4, 1600, 1300)
    cena4.save(os.path.join(out_dir, "vol1_cap1_cena4_estrelas_e_vida.png"), quality=95)

    # 4. Cena 8: O Sétimo Momento — A Paz que Abraça Tudo
    cena8 = Image.new("RGB", (1600, 2000), (15, 23, 42))
    top_sky = crop_and_resize(cosmica_base.crop((0, 0, w0, int(h0 * 0.65))), 1600, 1150)
    bottom_eden = crop_and_resize(mandala_base.crop((int(wm * 0.05), int(hm * 0.52), int(wm * 0.95), int(hm * 0.96))), 1600, 1050)
    cena8.paste(top_sky, (0, 0))
    mask8 = Image.new("L", (1600, 1050))
    md8 = ImageDraw.Draw(mask8)
    for y in range(1050):
        val = int(255 * min(1.0, max(0.0, y / 260.0)))
        md8.line([(0, y), (1600, y)], fill=val)
    cena8.paste(bottom_eden, (0, 950), mask8)
    cena8.save(os.path.join(out_dir, "vol1_cap1_cena8_descanso_luz.png"), quality=95)

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

def build_covers():
    print("-> Gerando as 3 propostas de capa diagramadas com FÁBIO MOTTA E SILVA e o painel comparativo...")
    vis_dir = os.path.join(BASE_DIR, "03-Identidade-Visual")
    f_series = load_font("cinzel", 34)
    f_title = load_font("cinzel", 96)
    f_sub = load_font("nunito", 40)
    f_tag = load_font("atkinson_bold", 26)
    f_author = load_font("cinzel", 30)

    configs = [
        ("capa_conceito_1_cosmica_base.jpg", "capa_final_1_cosmica.png", "dark_top"),
        ("capa_conceito_2_aventura_base.jpg", "capa_final_2_aventura.png", "gradient_top"),
        ("capa_conceito_3_pictorica_base.jpg", "capa_final_3_pictorica.png", "light_top"),
    ]
    generated_covers = []
    for base_file, out_file, style_mode in configs:
        base_img = Image.open(os.path.join(vis_dir, base_file)).convert("RGB")
        cover = crop_and_resize(base_img, PAGE_W, PAGE_H).convert("RGBA")

        grad = Image.new("RGBA", (PAGE_W, PAGE_H), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(grad)
        if style_mode in ("dark_top", "gradient_top"):
            for y in range(520):
                alpha = int(185 * (1 - y / 520.0) ** 1.4)
                gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 15, 38, alpha))
            for y in range(PAGE_H - 360, PAGE_H):
                alpha = int(210 * ((y - (PAGE_H - 360)) / 360.0) ** 1.3)
                gdraw.line([(0, y), (PAGE_W, y)], fill=(6, 12, 30, alpha))
            title_color = (255, 224, 115, 255)
            series_color = (240, 246, 255, 255)
            sub_color = (255, 255, 255, 255)
            use_shadow = True
        else:
            for y in range(PAGE_H - 340, PAGE_H):
                alpha = int(215 * ((y - (PAGE_H - 340)) / 340.0) ** 1.3)
                gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 22, 38, alpha))
            title_color = (146, 64, 14, 255)
            series_color = (30, 58, 138, 255)
            sub_color = (28, 25, 23, 255)
            use_shadow = False

        cover = Image.alpha_composite(cover, grad)
        cdraw = ImageDraw.Draw(cover)

        if style_mode == "light_top":
            f_title_c3 = load_font("cinzel", 82)
            f_sub_c3 = load_font("nunito", 34)
            cdraw.line([(360, 48), (PAGE_W - 360, 48)], fill=(180, 83, 9, 200), width=3)
            draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 62, PAGE_W - 200, f_series, fill=series_color, align="center", shadow=False)
            draw_wrapped_text(cdraw, "FAÇA-SE A LUZ", 80, 118, PAGE_W - 160, f_title_c3, fill=title_color, align="center", shadow=False)
            draw_wrapped_text(cdraw, "O começo de todas as histórias", 120, 218, PAGE_W - 240, f_sub_c3, fill=sub_color, align="center", shadow=False)
        else:
            cdraw.line([(360, 78), (PAGE_W - 360, 78)], fill=(245, 190, 70, 220), width=3)
            draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 96, PAGE_W - 200, f_series, fill=series_color, align="center", shadow=use_shadow)
            cdraw.line([(480, 152), (PAGE_W - 480, 152)], fill=(245, 190, 70, 180), width=2)
            draw_wrapped_text(cdraw, "FAÇA-SE A LUZ", 80, 178, PAGE_W - 160, f_title, fill=title_color, align="center", shadow=use_shadow)
            draw_wrapped_text(cdraw, "O começo de todas as histórias", 120, 305, PAGE_W - 240, f_sub, fill=sub_color, align="center", shadow=use_shadow)

        cover = draw_rounded_panel(cover, (220, PAGE_H - 235, PAGE_W - 220, PAGE_H - 70), (12, 22, 48, 222), (245, 190, 70, 235), border_width=3, radius=24)
        cdraw = ImageDraw.Draw(cover)
        draw_wrapped_text(cdraw, "VOLUME 1  •  A BÍBLIA ILUSTRADA PARA PEQUENOS EXPLORADORES", 240, PAGE_H - 208, PAGE_W - 480, f_tag, fill=(254, 240, 138, 255), align="center", shadow=False)
        draw_wrapped_text(cdraw, AUTHOR_UPPER, 240, PAGE_H - 142, PAGE_W - 480, f_author, fill=(255, 255, 255, 255), align="center", shadow=False)

        out_path = os.path.join(vis_dir, out_file)
        cover.convert("RGB").save(out_path, quality=95)
        generated_covers.append((out_file, cover.convert("RGB")))

    board_w, board_h = 2400, 1500
    board = Image.new("RGB", (board_w, board_h), (15, 23, 42))
    bdraw = ImageDraw.Draw(board)
    f_btitle = load_font("cinzel", 44)
    f_blabel = load_font("nunito", 28)
    f_bsmall = load_font("atkinson", 22)

    draw_wrapped_text(bdraw, "ENTREGA 3 — COMPARATIVO DAS 3 PROPOSTAS DE CAPA (TAMANHO REAL vs. MINIATURA 120 PX)", 60, 36, board_w - 120, f_btitle, fill=(253, 224, 71), align="center")

    labels = [
        ("OPÇÃO 1 (ALTERNATIVA)", "Cósmica e Contemplativa (Fiat Lux)"),
        ("OPÇÃO 2 (CAPA OFICIAL ESCOLHIDA)", f"Aventura Infantil Cinematográfica — Autor: {AUTHOR_NAME}"),
        ("OPÇÃO 3 (EDIÇÃO DE LUXO)", "Livro Ilustrado Pictórico / Mandala"),
    ]
    for idx, (fname, cov_img) in enumerate(generated_covers):
        x0 = 80 + idx * 770
        y0 = 130
        preview_large = cov_img.resize((520, 650), Image.Resampling.LANCZOS)
        board.paste(preview_large, (x0, y0))
        bdraw.rectangle([x0, y0, x0 + 520, y0 + 650], outline=(245, 190, 70), width=3)

        thumb_120 = cov_img.resize((120, 150), Image.Resampling.LANCZOS)
        tx = x0 + 545
        ty = y0 + 250
        board.paste(thumb_120, (tx, ty))
        bdraw.rectangle([tx, ty, tx + 120, ty + 150], outline=(56, 189, 248), width=2)
        draw_wrapped_text(bdraw, "Teste Loja\n120 px", tx - 10, ty + 162, 140, f_bsmall, fill=(148, 163, 184), align="center")

        draw_wrapped_text(bdraw, labels[idx][0], x0, y0 + 675, 660, f_tag, fill=(253, 224, 71), align="left")
        draw_wrapped_text(bdraw, labels[idx][1], x0, y0 + 715, 660, f_blabel, fill=(241, 245, 249), align="left")

    board = draw_rounded_panel(board, (80, 980, board_w - 80, 1430), (30, 41, 59, 240), (245, 190, 70, 200), border_width=2, radius=20).convert("RGB")
    bdraw = ImageDraw.Draw(board)
    analise_txt = (
        f"DECISÃO EDITORIAL CONSOLIDADA PELO AUTOR ({AUTHOR_UPPER} — PUBLICAÇÃO INDEPENDENTE):\n"
        "• Opção 2 (Aventura Infantil Cinematográfica — CAPA OFICIAL ESCOLHIDA): Selecionada pelo autor por comunicar imediatamente o universo infantil, gerando identificação instantânea com as crianças de 4 a 10 anos por meio dos dois pequenos exploradores contemplando o arco luminoso da criação.\n"
        "• Opção 1 (Cósmica e Contemplativa): Preservada para abertura de capítulo e materiais complementares.\n"
        "• Opção 3 (Pictórica / Mandala): Preservada como medalhão de Folha de Rosto e apresentação interna."
    )
    draw_wrapped_text(bdraw, analise_txt, 115, 1015, board_w - 230, f_blabel, fill=(248, 250, 252), line_spacing=1.42)
    board_path = os.path.join(vis_dir, "Entrega3_Comparativo_Capas_120px.png")
    board.save(board_path, quality=95)
    shutil.copy2(board_path, os.path.join(BRAIN_DIR, "Entrega3_Comparativo_Capas_120px.png"))
    shutil.copy2(os.path.join(vis_dir, "capa_final_2_aventura.png"), os.path.join(BRAIN_DIR, "capa_final_2_aventura.png"))

def draw_page_footer(img, page_num, chapter_label="VOLUME 1  •  FAÇA-SE A LUZ", dark_mode=True):
    draw = ImageDraw.Draw(img)
    f_foot = load_font("atkinson_bold", 22)
    color = (226, 232, 240, 210) if dark_mode else (71, 85, 105, 220)
    line_col = (245, 190, 70, 140) if dark_mode else (180, 83, 9, 120)
    draw.line([(90, PAGE_H - 78), (PAGE_W - 90, PAGE_H - 78)], fill=line_col, width=2)
    draw.text((90, PAGE_H - 62), chapter_label, font=f_foot, fill=color)
    p_str = f"PÁGINA {page_num:02d} DE 24"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def make_companion_page(art_img, page_num, cap_title, ref_text, seed_4_6, explorer_dialogue, discovery_title, discovery_text, question_text, dark_mode=False):
    """
    Cria a segunda página de cada capítulo (Páginas 14, 16, 18, 20, 22) com recorte panorâmico de detalhe
    da arte 3D, Camada Semente (4-6 anos), Diálogos dramáticos (6-10 anos), Descoberta Arqueológica e Pergunta Familiar.
    """
    bg_col = (15, 23, 42, 255) if dark_mode else (253, 251, 247, 255)
    p = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    f_h2 = load_font("cinzel", 34)
    f_body = load_font("nunito", 31)
    f_box_title = load_font("atkinson_bold", 26)
    f_box_body = load_font("atkinson", 24)
    f_ref = load_font("atkinson_bold", 23)

    # Banner panorâmico superior com zoom cinematográfico na ilustração 3D
    w, h = art_img.size
    zoom_crop = art_img.crop((int(w * 0.08), int(h * 0.15), int(w * 0.92), int(h * 0.65)))
    banner = crop_and_resize(zoom_crop, PAGE_W - 140, 470)
    p.paste(banner, (70, 65))
    d = ImageDraw.Draw(p)
    border_c = (245, 190, 70) if dark_mode else (180, 83, 9)
    d.rectangle([70, 65, PAGE_W - 70, 535], outline=border_c, width=4)

    title_c = (253, 224, 71) if dark_mode else (146, 64, 14)
    ref_c = (186, 230, 253) if dark_mode else (30, 58, 138)
    body_c = (248, 250, 252) if dark_mode else (41, 37, 36)

    draw_wrapped_text(d, cap_title, 90, 560, PAGE_W - 180, f_h2, fill=title_c)
    draw_wrapped_text(d, f"{ref_text}  |  Autor: {AUTHOR_NAME}", 90, 610, PAGE_W - 180, f_ref, fill=ref_c)

    # Quadro 1: Camada Semente (4 a 6 anos — Leitura Compartilhada em Voz Alta)
    seed_bg = (30, 41, 59, 240) if dark_mode else (254, 243, 199, 255)
    seed_bd = (245, 190, 70, 230) if dark_mode else (217, 119, 6, 255)
    seed_tc = (254, 240, 138) if dark_mode else (146, 64, 14)
    p = draw_rounded_panel(p, (85, 660, PAGE_W - 85, 965), seed_bg, seed_bd, border_width=3, radius=20)
    d = ImageDraw.Draw(p)
    draw_wrapped_text(d, "» CAMADA SEMENTE (4 A 6 ANOS — LEITURA EM VOZ ALTA):", 115, 682, PAGE_W - 230, f_box_title, fill=seed_tc)
    draw_wrapped_text(d, seed_4_6, 115, 725, PAGE_W - 230, f_body, fill=body_c, line_spacing=1.32)

    # Narrativa & Diálogos (Camada Explorador 6 a 10 anos)
    draw_wrapped_text(d, "DIÁLOGOS E DESCOBERTAS (CAMADA EXPLORADOR 6–10 ANOS):", 90, 995, PAGE_W - 180, f_box_title, fill=title_c)
    draw_wrapped_text(d, explorer_dialogue, 90, 1040, PAGE_W - 180, f_body, fill=body_c, line_spacing=1.34)

    # Quadro 2: Pequena Grande Descoberta (Arqueologia & História)
    disc_bg = (20, 45, 76, 240) if dark_mode else (224, 242, 254, 255)
    disc_bd = (56, 189, 248, 220) if dark_mode else (2, 132, 199, 255)
    disc_tc = (186, 230, 253) if dark_mode else (7, 89, 133)
    p = draw_rounded_panel(p, (85, 1455, PAGE_W - 85, 1695), disc_bg, disc_bd, border_width=2, radius=18)
    d = ImageDraw.Draw(p)
    draw_wrapped_text(d, f"» {discovery_title}", 115, 1478, PAGE_W - 230, f_box_title, fill=disc_tc)
    draw_wrapped_text(d, discovery_text, 115, 1520, PAGE_W - 230, f_box_body, fill=body_c, line_spacing=1.32)

    # Quadro 3: Pergunta Interativa em Família
    q_bg = (30, 58, 47, 240) if dark_mode else (236, 252, 203, 255)
    q_bd = (74, 222, 128, 220) if dark_mode else (101, 163, 13, 255)
    q_tc = (187, 247, 208) if dark_mode else (54, 83, 20)
    p = draw_rounded_panel(p, (85, 1715, PAGE_W - 85, 1895), q_bg, q_bd, border_width=2, radius=18)
    d = ImageDraw.Draw(p)
    draw_wrapped_text(d, f"» CONVERSE COMIGO EM FAMÍLIA: {question_text}", 115, 1740, PAGE_W - 230, f_box_body, fill=q_tc, line_spacing=1.32)

    p_rgb = p.convert("RGB")
    draw_page_footer(p_rgb, page_num, cap_title, dark_mode=dark_mode)
    return p_rgb

def build_pilot_pages():
    print("-> Diagramando as 24 páginas completas e sequenciais do Volume 1...")
    diag_dir = os.path.join(BASE_DIR, "09-Diagramacao/paginas_piloto")
    os.makedirs(diag_dir, exist_ok=True)
    art_dir = os.path.join(BASE_DIR, "08-Ilustracoes-Originais")
    vis_dir = os.path.join(BASE_DIR, "03-Identidade-Visual")
    char_dir = os.path.join(BASE_DIR, "04-Biblia-de-Personagens")

    f_h1 = load_font("cinzel", 54)
    f_h2 = load_font("cinzel", 36)
    f_body = load_font("nunito", 32)
    f_italic = load_font("nunito_italic", 32)
    f_box_title = load_font("atkinson_bold", 27)
    f_box_body = load_font("atkinson", 25)
    f_ref = load_font("atkinson_bold", 24)

    pages = []

    # PÁGINA 01: CAPA OFICIAL ESCOLHIDA PELO AUTOR (Conceito 2 — Aventura Infantil)
    p1 = Image.open(os.path.join(vis_dir, "capa_final_2_aventura.png")).convert("RGB")
    pages.append(("piloto_p01_capa.png", p1))

    # PÁGINA 02: FOLHA DE ROSTO, CARTA ÀS CRIANÇAS E GUIA DE LEITURA
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    mandala = Image.open(os.path.join(vis_dir, "capa_conceito_3_pictorica_base.jpg")).convert("RGB")
    mandala_crop = crop_and_resize(mandala, PAGE_W - 180, 740)
    p2.paste(mandala_crop, (90, 75))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([90, 75, PAGE_W - 90, 815], outline=(180, 83, 9), width=4)

    draw_wrapped_text(d2, "BEM-VINDO, PEQUENO EXPLORADOR DA LUZ!", 100, 845, PAGE_W - 200, f_h2, fill=(146, 64, 14), align="center")
    draw_wrapped_text(d2, f"Autor: {AUTHOR_NAME}  •  Edição Autônoma Independente", 100, 900, PAGE_W - 200, f_ref, fill=(30, 58, 138), align="center")
    intro_text = (
        "Você está prestes a abrir um livro diferente. Aqui, cada página é uma janela para tempos muito antigos, onde o Universo começou a brilhar, rios cristalinos cortavam jardins perfumados e pessoas como nós aprenderam a fazer grandes escolhas.\n\n"
        "Neste livro, Deus nunca é desenhado como uma pessoa de barba branca sentada nas nuvens — porque Ele é muito maior do que qualquer corpo! Ele é a própria Origem, o Amor e a Presença Luminosa de onde nasceu toda a vida: FAÇA-SE A LUZ!"
    )
    draw_wrapped_text(d2, intro_text, 120, 955, PAGE_W - 240, f_body, fill=(41, 37, 36), line_spacing=1.36)

    p2 = draw_rounded_panel(p2, (100, 1420, PAGE_W - 100, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "COMO EXPLORAR CADA CAPÍTULO EM FAMÍLIA (DUPLA CAMADA):", 140, 1445, PAGE_W - 280, f_box_title, fill=(146, 64, 14))
    selos_txt = (
        "• CAMADA SEMENTE (4–6 anos): Texto curto e musical para leitura compartilhada em voz alta.\n"
        "• CAMADA EXPLORADOR (6–10 anos): Narrativa completa com diálogos e contexto bíblico fiel.\n"
        "• PEQUENA GRANDE DESCOBERTA: Segredos reais da história, da arqueologia e da natureza.\n"
        "• CONVERSE COMIGO / O QUE VOCÊ FARIA?: Perguntas sobre escolhas, coragem e empatia."
    )
    draw_wrapped_text(d2, selos_txt, 140, 1500, PAGE_W - 280, f_box_body, fill=(68, 64, 60), line_spacing=1.45)
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 2, "FOLHA DE ROSTO E GUIA DE LEITURA", dark_mode=False)
    pages.append(("piloto_p02_apresentacao.png", p2_rgb))

    # PÁGINA 03: MAPA DO MUNDO DE GÊNESIS 1–11 E LINHA DO TEMPO DOS 6 CAPÍTULOS
    p3_map = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    eden_map_bg = Image.open(os.path.join(art_dir, "vol1_cap2_jardim_eden.jpg")).convert("RGB")
    p3_map.paste(crop_and_resize(eden_map_bg, PAGE_W - 140, 620), (70, 70))
    dm = ImageDraw.Draw(p3_map)
    dm.rectangle([70, 70, PAGE_W - 70, 690], outline=(245, 190, 70), width=4)
    draw_wrapped_text(dm, "MAPA DE EXPLORAÇÃO DO VOLUME 1 (GÊNESIS 1 A 11)", 90, 725, PAGE_W - 180, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(dm, f"Roteiro e Direção Editorial: {AUTHOR_NAME}", 90, 778, PAGE_W - 180, f_ref, fill=(186, 230, 253), align="center")

    p3_map = draw_rounded_panel(p3_map, (85, 835, PAGE_W - 85, 1885), (30, 41, 59, 240), (245, 190, 70, 220), border_width=3, radius=24)
    dm = ImageDraw.Draw(p3_map)
    sumario_v1 = (
        "• CAPÍTULO 1 — Antes de Tudo, a Luz (Gênesis 1:1–2:3 | Págs. 04 a 12):\n"
        "  O poema cósmico dos seis momentos da Criação, o surgimento da vida e o descanso do sétimo momento.\n\n"
        "• CAPÍTULO 2 — O Jardim das Águas Vivas (Gênesis 2:8–25 | Págs. 13 e 14):\n"
        "  Os quatro grandes rios do Éden (Pisom, Giom, Tigre e Eufrates), a Árvore da Vida e a missão humana.\n\n"
        "• CAPÍTULO 3 — Onde Você Está? O Fio da Promessa (Gênesis 3:1–24 | Págs. 15 e 16):\n"
        "  A escolha interrompida no jardim, o chamado amoroso da Luz e a promessa de redenção.\n\n"
        "• CAPÍTULO 4 — Dois Irmãos e o Segredo do Coração (Gênesis 4:1–16 | Págs. 17 e 18):\n"
        "  Caim e Abel, o valor da sinceridade e como vencer o ciúme e a raiva no coração.\n\n"
        "• CAPÍTULO 5 — A Grande Arca e o Arco da Aliança (Gênesis 6:9–9:17 | Págs. 19 e 20):\n"
        "  Noé, Naamá e seus filhos, o grande abrigo de cipreste e o arco-íris da paz com toda a Terra.\n\n"
        "• CAPÍTULO 6 — A Cidade de Tijolos e o Mundo Inteiro (Gênesis 11:1–9 | Págs. 21 e 22):\n"
        "  O zigurate mesopotâmico de Babel e o espalhamento das famílias e línguas pelo mundo."
    )
    draw_wrapped_text(dm, sumario_v1, 125, 870, PAGE_W - 250, f_box_body, fill=(248, 250, 252), line_spacing=1.35)
    p3_map_rgb = p3_map.convert("RGB")
    draw_page_footer(p3_map_rgb, 3, "SUMÁRIO VISUAL E LINHA DO TEMPO  •  VOLUME 1", dark_mode=True)
    pages.append(("piloto_p03_mapa_sumario.png", p3_map_rgb))

    # PÁGINA 04: ABERTURA CAP. 1 — ANTES DE TUDO, A LUZ
    abismo_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena1_misterio_abismo.jpg")).convert("RGB")
    p3 = crop_and_resize(abismo_img, PAGE_W, PAGE_H).convert("RGBA")
    p3 = draw_rounded_panel(p3, (90, 85, PAGE_W - 90, 340), (8, 15, 38, 200), (245, 190, 70, 210), border_width=3, radius=24)
    p3 = draw_rounded_panel(p3, (90, 1240, PAGE_W - 90, 1890), (8, 15, 38, 215), (56, 189, 248, 190), border_width=3, radius=26)
    d3 = ImageDraw.Draw(p3)
    draw_wrapped_text(d3, "CAPÍTULO 1  •  BASEADO EM GÊNESIS 1:1–2", 130, 112, PAGE_W - 260, f_ref, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d3, "ANTES DE TUDO, A LUZ", 130, 162, PAGE_W - 260, f_h1, fill=(255, 255, 255), align="center", shadow=True)
    draw_wrapped_text(d3, "O mistério silencioso antes da primeira manhã do Universo", 130, 245, PAGE_W - 260, f_italic, fill=(186, 230, 253), align="center")
    t_p3 = (
        "Feche os olhos por um instante.\n"
        "Imagine um tempo antes de existir o seu quarto, antes das ruas, antes das árvores e até antes das estrelas.\n"
        "Não havia relógios fazendo tique-taque. Não havia manhã nem noite. Tudo era um imenso oceano escuro e silencioso, chamado pelos antigos de Tehom.\n\n"
        "Mas aquele escuro não estava vazio nem sozinho. Sobre as águas quietas pairava o Ruach — o Sopro da Presença de Deus — como uma brisa viva, morna e luminosa, esperando o momento exato de cantar a primeira música da criação."
    )
    draw_wrapped_text(d3, t_p3, 135, 1280, PAGE_W - 270, f_body, fill=(248, 250, 252), line_spacing=1.36)
    draw_wrapped_text(d3, "» VOCÊ PERCEBEU? Olhe para o espelho d'água: a luz dourada e azul já está acordando as ondas!", 135, 1810, PAGE_W - 270, f_box_body, fill=(253, 224, 71))
    p3_rgb = p3.convert("RGB")
    draw_page_footer(p3_rgb, 4, "CAPÍTULO 1  •  ANTES DE TUDO, A LUZ", dark_mode=True)
    pages.append(("piloto_p03_abismo.png", p3_rgb))

    # PÁGINAS 05 E 06: SPREAD DUPLO "FAÇA-SE A LUZ!"
    spread_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena2_fiat_lux.png")).convert("RGB")
    p4 = spread_img.crop((0, 0, PAGE_W, PAGE_H)).convert("RGBA")
    p5 = spread_img.crop((PAGE_W, 0, PAGE_W * 2, PAGE_H)).convert("RGBA")

    p4 = draw_rounded_panel(p4, (90, 1180, PAGE_W - 90, 1885), (10, 18, 44, 215), (245, 190, 70, 220), border_width=3, radius=26)
    d4 = ImageDraw.Draw(p4)
    draw_wrapped_text(d4, "O CHAMADO QUE ACORDOU O UNIVERSO", 135, 1215, PAGE_W - 270, f_h2, fill=(253, 224, 71))
    t_p4 = (
        "Então, no coração daquele grande silêncio, a Presença Criadora falou.\n"
        "Não foi um grito de trovão assustador. Foi um chamado cheio de vida e alegria que atravessou toda a escuridão:\n\n"
        "— FAÇA-SE A LUZ!  [Gênesis 1:3]\n\n"
        "No mesmo instante, o Universo inteiro estremeceu de beleza! Fitas douradas mais quentes que o mel e raios azuis como safiras correram pelo espaço, abrindo caminho como uma cortina que se levanta pela manhã."
    )
    draw_wrapped_text(d4, t_p4, 135, 1290, PAGE_W - 270, f_body, fill=(255, 255, 255), line_spacing=1.36)
    p4_rgb = p4.convert("RGB")
    draw_page_footer(p4_rgb, 5, "CAPÍTULO 1  •  FAÇA-SE A LUZ (FIAT LUX)", dark_mode=True)
    pages.append(("piloto_p04_fiat_lux_esq.png", p4_rgb))

    p5 = draw_rounded_panel(p5, (90, 1320, PAGE_W - 90, 1885), (10, 18, 44, 215), (245, 190, 70, 220), border_width=3, radius=26)
    d5 = ImageDraw.Draw(p5)
    t_p5 = (
        "A Presença Divina contemplou aquele clarão maravilhoso e viu que a luz era muito boa.\n\n"
        "Com ternura, a claridade recebeu o nome de DIA, para despertar a vida; e a escuridão suave recebeu o nome de NOITE, para guardar o descanso e os sonhos.  [Gênesis 1:4–5]\n\n"
        "Assim vieram a tarde e a manhã: o primeiro grande momento da história da criação."
    )
    draw_wrapped_text(d5, t_p5, 135, 1360, PAGE_W - 270, f_body, fill=(255, 255, 255), line_spacing=1.36)
    draw_wrapped_text(d5, "» CONVERSE COMIGO: Como você se sente quando acorda e vê a luz do sol entrando pela janela?", 135, 1795, PAGE_W - 270, f_box_body, fill=(253, 224, 71))
    p5_rgb = p5.convert("RGB")
    draw_page_footer(p5_rgb, 6, "CAPÍTULO 1  •  FAÇA-SE A LUZ (FIAT LUX)", dark_mode=True)
    pages.append(("piloto_p05_fiat_lux_dir.png", p5_rgb))

    # PÁGINA 07: O ABRAÇO DO CÉU, DO MAR E DA TERRA
    p6 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    cena3_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena3_ceu_mar_terra.png")).convert("RGB")
    p6.paste(crop_and_resize(cena3_img, PAGE_W - 140, 1060), (70, 70))
    d6 = ImageDraw.Draw(p6)
    d6.rectangle([70, 70, PAGE_W - 70, 1130], outline=(13, 148, 136), width=4)
    draw_wrapped_text(d6, "O ABRAÇO DO CÉU, DO MAR E DA TERRA", 100, 1165, PAGE_W - 200, f_h2, fill=(15, 118, 110))
    draw_wrapped_text(d6, "Base Bíblica: Gênesis 1:6–13 (O Segundo e o Terceiro Momento)", 100, 1222, PAGE_W - 200, f_ref, fill=(180, 83, 9))
    t_p6 = (
        "A luz agora iluminava um mundo coberto de água. Então, um grande fôlego abriu espaço entre as nuvens lá no alto e as ondas cá embaixo: nasceu o CÉU azul, vasto como uma tenda brilhante!\n\n"
        "Logo depois, as águas correram para se abraçar nos oceanos, e do fundo das ondas subiram montanhas de rocha, vales e praias de areia dourada: era a TERRA seca.\n\n"
        "Ao toque quente da Luz, o chão começou a se vestir de verde: brotaram tapetes de musgo macio, samambaias gigantes, figueiras carregadas de frutos doces e flores perfumadas de todas as cores!"
    )
    draw_wrapped_text(d6, t_p6, 100, 1275, PAGE_W - 200, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p6 = draw_rounded_panel(p6, (100, 1745, PAGE_W - 100, 1890), (204, 251, 241, 255), (13, 148, 136, 255), border_width=2, radius=18)
    d6 = ImageDraw.Draw(p6)
    draw_wrapped_text(d6, "» PEQUENA GRANDE DESCOBERTA: Cada árvore frutífera guarda dentro de sua semente um 'mapa' completo para fazer nascer outra árvore igualzinha! É a vida se multiplicando como diz Gênesis 1:11.", 130, 1768, PAGE_W - 260, f_box_body, fill=(19, 78, 74), line_spacing=1.35)
    p6_rgb = p6.convert("RGB")
    draw_page_footer(p6_rgb, 7, "CAPÍTULO 1  •  CÉU, MAR E TERRA FÉRTIL", dark_mode=False)
    pages.append(("piloto_p06_ceu_mar_terra.png", p6_rgb))

    # PÁGINA 08: A DANÇA DAS ESTRELAS, ÁGUAS E ASAS
    p7 = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    cena4_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena4_estrelas_e_vida.png")).convert("RGB")
    p7.paste(crop_and_resize(cena4_img, PAGE_W - 140, 1060), (70, 70))
    d7 = ImageDraw.Draw(p7)
    d7.rectangle([70, 70, PAGE_W - 70, 1130], outline=(245, 190, 70), width=4)
    draw_wrapped_text(d7, "A DANÇA DAS ESTRELAS, DAS ÁGUAS E DAS ASAS", 100, 1165, PAGE_W - 200, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d7, "Base Bíblica: Gênesis 1:14–23 (O Quarto e o Quinto Momento)", 100, 1222, PAGE_W - 200, f_ref, fill=(125, 211, 252))
    t_p7 = (
        "No alto do firmamento acenderam-se duas grandes lâmpadas e milhões de faíscas: o Sol dourado para aquecer o dia, e a Lua prateada rodeada de constelações para iluminar a noite e marcar as estações do ano.\n\n"
        "Mas uma casa tão bonita precisava de moradores! De repente, os mares se encheram de peixes cintilantes, corais e grandes baleias que soltavam chafarizes de espuma para o ar.\n\n"
        "E, no mesmo instante, o vento ganhou asas: pombas brancas, garças e passarinhos coloridos subiram cantando entre as nuvens sob a bênção da Luz: 'Cresçam, multipliquem-se e encham as águas e o céu!'"
    )
    draw_wrapped_text(d7, t_p7, 100, 1275, PAGE_W - 200, f_body, fill=(241, 245, 249), line_spacing=1.36)
    p7 = draw_rounded_panel(p7, (100, 1765, PAGE_W - 100, 1890), (30, 41, 59, 240), (56, 189, 248, 220), border_width=2, radius=18)
    d7 = ImageDraw.Draw(p7)
    draw_wrapped_text(d7, "» VOCÊ PERCEBEU? Na ilustração acima, a pomba branca voa bem no raio de luz dourada que liga o céu estrelado às ondas do mar!", 130, 1790, PAGE_W - 260, f_box_body, fill=(186, 230, 253))
    p7_rgb = p7.convert("RGB")
    draw_page_footer(p7_rgb, 8, "CAPÍTULO 1  •  ESTRELAS, MARES E AVES", dark_mode=True)
    pages.append(("piloto_p07_estrelas_aves.png", p7_rgb))

    # PÁGINA 09: OS HABITANTES DA TERRA
    p8 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    cena5_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena5_animais_jardim.jpg")).convert("RGB")
    p8.paste(crop_and_resize(cena5_img, PAGE_W - 120, 1140), (60, 60))
    d8 = ImageDraw.Draw(p8)
    d8.rectangle([60, 60, PAGE_W - 60, 1200], outline=(101, 163, 13), width=4)
    draw_wrapped_text(d8, "OS HABITANTES DA TERRA", 100, 1235, PAGE_W - 200, f_h2, fill=(63, 98, 18))
    draw_wrapped_text(d8, "Base Bíblica: Gênesis 1:24–25", 100, 1292, PAGE_W - 200, f_ref, fill=(180, 83, 9))
    t_p8 = (
        "Quando o sol do sexto momento brilhou sobre os campos floridos, a terra inteira ganhou movimento!\n\n"
        "Pelas colinas e florestas surgiram animais de todos os tamanhos e jeitos: o cervo malhado de passos leves, o elefantinho brincalhão que espirrava água fresca no riacho, borboletas cor de laranja e azul, e o grande leão de juba dourada que descansava em paz na grama macia.\n\n"
        "Cada criatura tinha sua própria voz, seu ritmo e seu lugar especial na grande família da natureza. E a Presença Criadora viu que tudo aquilo era bom."
    )
    draw_wrapped_text(d8, t_p8, 100, 1345, PAGE_W - 200, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p8 = draw_rounded_panel(p8, (100, 1775, PAGE_W - 100, 1890), (236, 252, 203, 255), (101, 163, 13, 255), border_width=2, radius=18)
    d8 = ImageDraw.Draw(p8)
    draw_wrapped_text(d8, "» DESAFIO DO EXPLORADOR: Quantos passarinhos cantores no galho florido e quantas borboletas você consegue contar nesta cena?", 130, 1800, PAGE_W - 260, f_box_body, fill=(54, 83, 20))
    p8_rgb = p8.convert("RGB")
    draw_page_footer(p8_rgb, 9, "CAPÍTULO 1  •  OS ANIMAIS DO JARDIM", dark_mode=False)
    pages.append(("piloto_p08_animais_jardim.png", p8_rgb))

    # PÁGINA 10: FILHOS DO BARRO E DA LUZ (ADÃO E EVA)
    cena6_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena6_humanidade_sopro.jpg")).convert("RGB")
    p9 = crop_and_resize(cena6_img, PAGE_W, PAGE_H).convert("RGBA")
    p9 = draw_rounded_panel(p9, (80, 1180, PAGE_W - 80, 1890), (20, 28, 18, 222), (245, 190, 70, 230), border_width=3, radius=26)
    d9 = ImageDraw.Draw(p9)
    draw_wrapped_text(d9, "FILHOS DO BARRO E DA LUZ", 125, 1212, PAGE_W - 250, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d9, "Base Bíblica: Gênesis 1:26–27; 2:7  |  Diálogo de Dramatização Literária", 125, 1266, PAGE_W - 250, f_ref, fill=(186, 230, 253))
    t_p9 = (
        "Faltava alguém muito especial: alguém capaz de olhar para as estrelas e fazer perguntas, cantar, abraçar e cuidar daquele jardim inteiro.\n"
        "Da terra fértil banhada pelo Sopro Divino (Ruach), despertaram os primeiros seres humanos — Adão e Eva — criados à imagem e semelhança do Amor de Deus, não no formato de um corpo físico, mas na capacidade de amar, criar e proteger a vida!\n\n"
        "Adão abriu os olhos escuros devagar, sentiu o calor da fita de luz nas mãos e olhou para Eva:\n"
        "— Você está ouvindo isso? — sussurrou ele, sorrindo.\n"
        "— É a canção da água e das árvores! — respondeu Eva, maravilhada. — Parece que o mundo inteiro estava esperando por nós!"
    )
    draw_wrapped_text(d9, t_p9, 125, 1315, PAGE_W - 250, f_body, fill=(248, 250, 252), line_spacing=1.33)
    p9_rgb = p9.convert("RGB")
    draw_page_footer(p9_rgb, 10, "CAPÍTULO 1  •  A CRIAÇÃO DA HUMANIDADE", dark_mode=True)
    pages.append(("piloto_p09_humanidade_sopro.png", p9_rgb))

    # PÁGINA 11: CUIDADORES DO GRANDE JARDIM
    cena7_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena7_nomes_cuidadores.jpg")).convert("RGB")
    p10 = crop_and_resize(cena7_img, PAGE_W, PAGE_H).convert("RGBA")
    p10 = draw_rounded_panel(p10, (80, 1220, PAGE_W - 80, 1890), (253, 251, 247, 235), (101, 163, 13, 240), border_width=3, radius=26)
    d10 = ImageDraw.Draw(p10)
    draw_wrapped_text(d10, "GUARDIÕES E AMIGOS DA VIDA", 125, 1250, PAGE_W - 250, f_h2, fill=(63, 98, 18))
    draw_wrapped_text(d10, "Base Bíblica: Gênesis 1:28–30; 2:15, 19–20", 125, 1304, PAGE_W - 250, f_ref, fill=(180, 83, 9))
    t_p10 = (
        "A Presença Luminosa abençoou Adão e Eva com uma missão bonita: eles não eram donos da Terra para estragá-la, mas guardiões e cuidadores daquela grande casa viva.\n\n"
        "Junto ao riacho cristalino, uma raposinha ruiva aproximou o focinho curioso, um cordeirinho macio encostou no braço de Adão e uma pomba branca pousou na mão aberta de Eva.\n"
        "— Você tem penas brancas como as nuvens da manhã: vai se chamar Pomba! — disse Eva com ternura.\n"
        "— E enquanto cuidarmos deste jardim e uns dos outros, a Luz estará sempre em nossa casa — completou Adão."
    )
    draw_wrapped_text(d10, t_p10, 125, 1352, PAGE_W - 250, f_body, fill=(28, 25, 23), line_spacing=1.34)
    draw_wrapped_text(d10, "» O QUE VOCÊ FARIA? Se você encontrasse um passarinho ou um filhote precisando de cuidado perto da sua casa, como você o ajudaria?", 125, 1795, PAGE_W - 250, f_box_body, fill=(146, 64, 14))
    p10_rgb = p10.convert("RGB")
    draw_page_footer(p10_rgb, 11, "CAPÍTULO 1  •  CUIDADORES DO JARDIM", dark_mode=False)
    pages.append(("piloto_p10_nomes_cuidadores.png", p10_rgb))

    # PÁGINA 12: O SÉTIMO MOMENTO — A PAZ QUE ABRAÇA TUDO
    cena8_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena8_descanso_luz.png")).convert("RGB")
    p11 = crop_and_resize(cena8_img, PAGE_W, PAGE_H).convert("RGBA")
    p11 = draw_rounded_panel(p11, (85, 85, PAGE_W - 85, 760), (10, 18, 44, 215), (245, 190, 70, 220), border_width=3, radius=26)
    d11 = ImageDraw.Draw(p11)
    draw_wrapped_text(d11, "O SÉTIMO MOMENTO: A PAZ QUE ABRAÇA TUDO", 130, 118, PAGE_W - 260, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d11, "Base Bíblica: Gênesis 1:31–2:3 (O Descanso Sagrado)", 130, 174, PAGE_W - 260, f_ref, fill=(186, 230, 253))
    t_p11 = (
        "Quando tudo estava pronto — a luz e a noite, o céu e o mar, as árvores, os astros, os pássaros, os peixes, os animais do campo e a família humana —, a Presença Criadora contemplou o Universo inteiro e viu que tudo era MUITO BOM.\n\n"
        "Então chegou o sétimo momento: um tempo sagrado de paz, silêncio feliz e descanso, em que toda a criação apenas respirou junta sob a luz dourada do entardecer."
    )
    draw_wrapped_text(d11, t_p11, 130, 228, PAGE_W - 260, f_body, fill=(248, 250, 252), line_spacing=1.38)
    p11 = draw_rounded_panel(p11, (85, 1620, PAGE_W - 85, 1890), (15, 23, 42, 228), (56, 189, 248, 220), border_width=3, radius=24)
    d11 = ImageDraw.Draw(p11)
    draw_wrapped_text(d11, "» CONVERSE COMIGO EM FAMÍLIA:", 130, 1650, PAGE_W - 260, f_box_title, fill=(253, 224, 71))
    draw_wrapped_text(d11, "Por que descansar depois de trabalhar ou estudar é tão importante? Qual é o lugar da natureza onde você sente mais paz no coração?", 130, 1700, PAGE_W - 260, f_body, fill=(241, 245, 249), line_spacing=1.35)
    p11_rgb = p11.convert("RGB")
    draw_page_footer(p11_rgb, 12, "CAPÍTULO 1  •  O SÉTIMO MOMENTO", dark_mode=True)
    pages.append(("piloto_p11_descanso_luz.png", p11_rgb))

    # PÁGINA 13: CAPÍTULO 2 (PARTE 1) — O JARDIM DAS ÁGUAS VIVAS
    p13 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    c2_img = Image.open(os.path.join(art_dir, "vol1_cap2_jardim_eden.jpg")).convert("RGB")
    p13.paste(crop_and_resize(c2_img, PAGE_W - 140, 1020), (70, 70))
    d13 = ImageDraw.Draw(p13)
    d13.rectangle([70, 70, PAGE_W - 70, 1090], outline=(101, 163, 13), width=4)
    draw_wrapped_text(d13, "CAPÍTULO 2  •  O JARDIM DAS ÁGUAS VIVAS", 90, 1125, PAGE_W - 180, f_h2, fill=(63, 98, 18))
    draw_wrapped_text(d13, f"Base Bíblica: Gênesis 2:8–25  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=(180, 83, 9))
    t_p13 = (
        "No coração do Éden brotava uma fonte cristalina que se dividia em quatro grandes rios: Pisom, Giom, Tigre e Eufrates. No alto da colina central brilhava a Árvore da Vida, cujas folhas refletiam a luz dourada do Criador.\n\n"
        "Adão e Eva caminhavam de mãos dadas pelos pomares de figos, romãs e oliveiras, aprendendo a cultivar a terra com carinho e a chamar cada animal pelo nome."
    )
    draw_wrapped_text(d13, t_p13, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p13 = draw_rounded_panel(p13, (90, 1745, PAGE_W - 90, 1890), (236, 252, 203, 255), (101, 163, 13, 255), border_width=2, radius=18)
    d13 = ImageDraw.Draw(p13)
    draw_wrapped_text(d13, "» PEQUENA GRANDE DESCOBERTA: Os rios Tigre e Eufrates existem até hoje no Oriente Médio! Foi entre as águas deles que nasceram as primeiras cidades e pomares da antiguidade.", 120, 1770, PAGE_W - 240, f_box_body, fill=(54, 83, 20))
    p13_rgb = p13.convert("RGB")
    draw_page_footer(p13_rgb, 13, "VOLUME 1  •  CAPÍTULO 2: O JARDIM DAS ÁGUAS VIVAS", dark_mode=False)
    pages.append(("piloto_p13_cap2_jardim_eden.png", p13_rgb))

    # PÁGINA 14: CAPÍTULO 2 (PARTE 2) — DUPLA CAMADA E DIÁLOGOS DO ÉDEN
    p14_c2 = make_companion_page(
        c2_img, 14,
        "CAPÍTULO 2  •  OS QUATRO RIOS E A MISSÃO NO ÉDEN",
        "Base Bíblica: Gênesis 2:10–25",
        "No meio do jardim do Éden nascia um rio fresquinho que se dividia em quatro braços para regar toda a terra! Deus colocou o ser humano ali para cultivar as plantas e guardar o jardim com amor, onde ninguém ficava sozinho.",
        "— Olhe como a água corre limpa entre as pedras de ônix, Adão! — disse Eva, colhendo um figo maduro.\n"
        "— Cada gota leva vida para as árvores do vale — respondeu Adão. — A Presença Luminosa nos deu mãos inteligentes para plantar, podar e proteger este lugar.\n"
        "No Éden, o trabalho não era um peso cansativo, mas uma parceria alegre entre a humanidade, a natureza e o Criador.",
        "ARQUEOLOGIA E BOTÂNICA DO ORIENTE PRÓXIMO",
        "As árvores mencionadas nos textos bíblicos mais antigos — como a figueira, a romãzeira, a oliveira e o cedro — são espécies reais nativas do Crescente Fértil, cultivadas há milhares de anos.",
        "Qual planta, flor ou árvore você mais gosta de ver perto da sua casa ou nos parques da sua cidade?",
        dark_mode=False
    )
    pages.append(("piloto_p14_cap2_dialogos.png", p14_c2))

    # PÁGINA 15: CAPÍTULO 3 (PARTE 1) — A ESCOLHA INTERROMPIDA E O FIO DA PROMESSA
    p15 = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    c3_img = Image.open(os.path.join(art_dir, "vol1_cap3_escolha_jardim.jpg")).convert("RGB")
    p15.paste(crop_and_resize(c3_img, PAGE_W - 140, 1020), (70, 70))
    d15 = ImageDraw.Draw(p15)
    d15.rectangle([70, 70, PAGE_W - 70, 1090], outline=(245, 190, 70), width=4)
    draw_wrapped_text(d15, "CAPÍTULO 3  •  ONDE VOCÊ ESTÁ? O FIO DA PROMESSA", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d15, f"Base Bíblica: Gênesis 3:1–24  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=(186, 230, 253))
    t_p15 = (
        "Quando Adão e Eva desconfiaram da sabedoria do Criador e tomaram do fruto que não deviam, sentiram medo e se esconderam entre as samambaias do jardim na brisa da tarde.\n\n"
        "Mas a Luz de Deus não desistiu deles! Uma fita dourada e mansa entrou entre as árvores chamando com amor: 'Onde você está?'. Mesmo saindo do jardim, eles levaram consigo a promessa de que um dia a Luz venceria toda sombra."
    )
    draw_wrapped_text(d15, t_p15, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.36)
    p15 = draw_rounded_panel(p15, (90, 1745, PAGE_W - 90, 1890), (30, 41, 59, 240), (245, 190, 70, 220), border_width=2, radius=18)
    d15 = ImageDraw.Draw(p15)
    draw_wrapped_text(d15, "» O QUE VOCÊ FARIA? Quando cometemos um erro em casa ou na escola, por que pedir desculpas e falar a verdade é sempre melhor do que se esconder?", 120, 1770, PAGE_W - 240, f_box_body, fill=(253, 224, 71))
    p15_rgb = p15.convert("RGB")
    draw_page_footer(p15_rgb, 15, "VOLUME 1  •  CAPÍTULO 3: O FIO DA PROMESSA", dark_mode=True)
    pages.append(("piloto_p14_cap3_escolha_jardim.png", p15_rgb))

    # PÁGINA 16: CAPÍTULO 3 (PARTE 2) — DUPLA CAMADA E O CUIDADO NA PARTIDA
    p16_c3 = make_companion_page(
        c3_img, 16,
        "CAPÍTULO 3  •  A VOZ NA BRISA DA TARDE E AS TÚNICAS DE CUIDADO",
        "Base Bíblica: Gênesis 3:8–21",
        "Adão e Eva ficaram com vergonha depois de desobedecer e se esconderam atrás das folhas. Mas Deus veio conversar com eles na brisa fresca da tarde, fez roupas fortes para protegê-los do frio e prometeu que o amor nunca os abandonaria.",
        "— Eu ouvi a Tua voz no jardim e tive medo — confessou Adão, saindo de trás das samambaias.\n"
        "Em vez de abandonar o casal, o Criador preparou túnicas resistentes para vesti-los antes da caminhada fora do Éden e acendeu no coração deles o Fio da Promessa: a semente do bem venceria o mal!",
        "POR QUE DEUS PERGUNTOU 'ONDE VOCÊ ESTÁ?'",
        "Os antigos sábios explicam que Deus sabia exatamente onde Adão e Eva estavam escondidos; a pergunta 'Onde você está?' (Ayekah, em hebraico) era um convite amoroso para que eles abrissem o coração com sinceridade.",
        "Quem são as pessoas que sempre acolhem você com amor mesmo quando você precisa corrigir um erro?",
        dark_mode=True
    )
    pages.append(("piloto_p16_cap3_dialogos.png", p16_c3))

    # PÁGINA 17: CAPÍTULO 4 (PARTE 1) — DOIS IRMÃOS E O SEGREDO DO CORAÇÃO
    p17 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    c4_img = Image.open(os.path.join(art_dir, "vol1_cap4_caim_abel.jpg")).convert("RGB")
    p17.paste(crop_and_resize(c4_img, PAGE_W - 140, 1020), (70, 70))
    d17 = ImageDraw.Draw(p17)
    d17.rectangle([70, 70, PAGE_W - 70, 1090], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d17, "CAPÍTULO 4  •  DOIS IRMÃOS E O SEGREDO DO CORAÇÃO", 90, 1125, PAGE_W - 180, f_h2, fill=(146, 64, 14))
    draw_wrapped_text(d17, f"Base Bíblica: Gênesis 4:1–16 (Caim e Abel)  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=(30, 58, 138))
    t_p17 = (
        "Caim cultivava o trigo dourado e os frutos da terra; seu irmão Abel cuidava das ovelhas com ternura. Quando trouxeram suas ofertas, Abel entregou o melhor com um coração sincero e grato.\n\n"
        "Ao ver Caim entristecido pela inveja, a Presença Luminosa sussurrou ao seu coração: 'Se você fizer o bem, não terá paz? A raiva fica espreitando à porta, mas você pode escolher dominá-la com o amor!'"
    )
    draw_wrapped_text(d17, t_p17, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.36)
    p17 = draw_rounded_panel(p17, (90, 1745, PAGE_W - 90, 1890), (254, 243, 199, 255), (217, 119, 6, 255), border_width=2, radius=18)
    d17 = ImageDraw.Draw(p17)
    draw_wrapped_text(d17, "» CONVERSE COMIGO: O que ajuda você a acalmar o coração quando sente ciúmes ou chateação com um irmão ou amigo?", 120, 1775, PAGE_W - 240, f_box_body, fill=(146, 64, 14))
    p17_rgb = p17.convert("RGB")
    draw_page_footer(p17_rgb, 17, "VOLUME 1  •  CAPÍTULO 4: CAIM E ABEL", dark_mode=False)
    pages.append(("piloto_p15_cap4_caim_abel.png", p17_rgb))

    # PÁGINA 18: CAPÍTULO 4 (PARTE 2) — DUPLA CAMADA E EDUCAÇÃO EMOCIONAL
    p18_c4 = make_companion_page(
        c4_img, 18,
        "CAPÍTULO 4  •  GUARDIÕES DOS NOSSOS IRMÃOS",
        "Base Bíblica: Gênesis 4:6–16; 4:25",
        "Caim trabalhava na plantação e Abel cuidava das ovelhinhas. Deus ensinou a Caim um segredo precioso: quando a raiva ou a inveja baterem à porta do coração, nós não precisamos abrir — podemos escolher a paz e cuidar do nosso irmão!",
        "— Por que o seu rosto está tão fechado, Caim? — sussurrou a Voz luminosa como um conselho de pai.\n"
        "Infelizmente, Caim não ouviu o conselho da Luz e feriu seu irmão no campo, trazendo grande tristeza à família. Mas a história não terminou na sombra: mais tarde nasceu Sete, renovando a esperança das famílias que invocavam o nome do Senhor.",
        "AS PRIMEIRAS PROFISSÕES DA HUMANIDADE",
        "Gênesis 4 retrata a transição histórica do Neolítico no Oriente Próximo: o surgimento conjunto da agricultura (cultivo de cereais como trigo e cevada) e do pastoreio de ovelhas e cabras.",
        "Como você pode demonstrar hoje que é um verdadeiro amigo e protetor dos seus irmãos ou colegas?",
        dark_mode=False
    )
    pages.append(("piloto_p18_cap4_dialogos.png", p18_c4))

    # PÁGINA 19: CAPÍTULO 5 (PARTE 1) — A GRANDE ARCA E O ARCO NO CÉU
    p19 = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    c5_img = Image.open(os.path.join(art_dir, "vol1_cap5_arca_noe.jpg")).convert("RGB")
    p19.paste(crop_and_resize(c5_img, PAGE_W - 140, 1020), (70, 70))
    d19 = ImageDraw.Draw(p19)
    d19.rectangle([70, 70, PAGE_W - 70, 1090], outline=(245, 190, 70), width=4)
    draw_wrapped_text(d19, "CAPÍTULO 5  •  A GRANDE ARCA E O ARCO DA ALIANÇA", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d19, f"Base Bíblica: Gênesis 6:9–9:17  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=(186, 230, 253))
    t_p19 = (
        "Quando a violência ameaçou estragar a Terra, Noé e sua família ouviram a voz da Luz e construíram uma grande Arca de madeira de cipreste calafetada com betume, um verdadeiro abrigo flutuante para salvar a vida!\n\n"
        "Casais de elefantes, leões, girafas, cervos e pombas subiram a rampa sob um feixe dourado de esperança. E depois das águas, o arco-íris brilhou nas nuvens como sinal eterno da paz de Deus com toda criatura viva."
    )
    draw_wrapped_text(d19, t_p19, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.36)
    p19 = draw_rounded_panel(p19, (90, 1745, PAGE_W - 90, 1890), (30, 41, 59, 240), (56, 189, 248, 220), border_width=2, radius=18)
    d19 = ImageDraw.Draw(p19)
    draw_wrapped_text(d19, "» VOCÊ PERCEBEU? Em hebraico, a palavra 'Tevah' é usada apenas duas vezes na Bíblia: para a Arca de Noé e para o cestinho de Moisés no Nilo! Ambos salvaram a vida sobre as águas.", 120, 1770, PAGE_W - 240, f_box_body, fill=(186, 230, 253))
    p19_rgb = p19.convert("RGB")
    draw_page_footer(p19_rgb, 19, "VOLUME 1  •  CAPÍTULO 5: A ARCA DE NOÉ", dark_mode=True)
    pages.append(("piloto_p16_cap5_arca_noe.png", p19_rgb))

    # PÁGINA 20: CAPÍTULO 5 (PARTE 2) — DUPLA CAMADA, A POMBA E O RAMO DE OLIVEIRA
    p20_c5 = make_companion_page(
        c5_img, 20,
        "CAPÍTULO 5  •  O RAMO DE OLIVEIRA E A PROMESSA NAS NUVENS",
        "Base Bíblica: Gênesis 8:1–9:17",
        "Dentro da grande Arca, Noé e sua família alimentaram os bichinhos com todo o carinho enquanto a chuva caía lá fora. Quando a pomba branca voltou trazendo uma folhinha verde de oliveira no bico, todos comemoraram: a terra estava seca e um lindo arco-íris brilhou no céu!",
        "— Olhem! A pomba trouxe um raminho fresco de oliveira! — exclamou Naamá, esposa de Noé, apontando para a janela do alto da Arca.\n"
        "Quando desceram nas montanhas de Ararate, o céu inteiro se iluminou com um arco de sete cores radiantes, selando a aliança do Criador com as pessoas, os animais e as estações da Terra.",
        "ENGENHARIA ANTIGA: MADEIRA DE GOFER E BETUME",
        "Na antiga Mesopotâmia, o betume natural (asfalto mineral impermeável) era usado para vedar embarcações de madeira e cestos de junco, impedindo que a água entrasse pelas frestas.",
        "Quando você vê um arco-íris no céu depois da chuva, que sentimento bom ele desperta em você?",
        dark_mode=True
    )
    pages.append(("piloto_p20_cap5_dialogos.png", p20_c5))

    # PÁGINA 21: CAPÍTULO 6 (PARTE 1) — A CIDADE DE TIJOLOS E O MUNDO INTEIRO
    p21 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    c6_img = Image.open(os.path.join(art_dir, "vol1_cap6_torre_babel.jpg")).convert("RGB")
    p21.paste(crop_and_resize(c6_img, PAGE_W - 140, 1020), (70, 70))
    d21 = ImageDraw.Draw(p21)
    d21.rectangle([70, 70, PAGE_W - 70, 1090], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d21, "CAPÍTULO 6  •  A CIDADE DE TIJOLOS E O MUNDO INTEIRO", 90, 1125, PAGE_W - 180, f_h2, fill=(146, 64, 14))
    draw_wrapped_text(d21, f"Base Bíblica: Gênesis 11:1–9  |  Autor: {AUTHOR_NAME}", 90, 1180, PAGE_W - 180, f_ref, fill=(30, 58, 138))
    t_p21 = (
        "Na planície de Sinar, os homens aprenderam a assar tijolos de barro e quiseram levantar um imenso zigurate em degraus para ficar presos num só lugar e buscar fama apenas para si mesmos.\n\n"
        "Mas o sonho da Presença Criadora era um mundo cheio de cores, culturas e línguas diferentes! Sob o arco de luz dourada e safira, as famílias partiram por muitos caminhos para habitar toda a Terra — preparando o cenário para o chamado de Abraão no Volume 2!"
    )
    draw_wrapped_text(d21, t_p21, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p21 = draw_rounded_panel(p21, (90, 1745, PAGE_W - 90, 1890), (254, 243, 199, 255), (217, 119, 6, 255), border_width=2, radius=18)
    d21 = ImageDraw.Draw(p21)
    draw_wrapped_text(d21, "» PEQUENA GRANDE DESCOBERTA: A Torre de Babel não era redonda como nas pinturas medievais, mas um Zigurate mesopotâmico em degraus quadrados, feito de tijolos de barro e betume!", 120, 1770, PAGE_W - 240, f_box_body, fill=(146, 64, 14))
    p21_rgb = p21.convert("RGB")
    draw_page_footer(p21_rgb, 21, "VOLUME 1  •  CAPÍTULO 6: O ZIGURATE DE BABEL", dark_mode=False)
    pages.append(("piloto_p17_cap6_torre_babel.png", p21_rgb))

    # PÁGINA 22: CAPÍTULO 6 (PARTE 2) — DUPLA CAMADA E PONTE PARA O VOLUME 2
    p22_c6 = make_companion_page(
        c6_img, 22,
        "CAPÍTULO 6  •  MUITAS LÍNGUAS, UMA SÓ FAMÍLIA HUMANA",
        "Base Bíblica: Gênesis 10:1–11:9",
        "Os construtores de Babel queriam que todo mundo fosse igualzinho e morasse num lugar só. Mas Deus soprou novas palavras no coração das famílias para que elas viajassem pelas montanhas, ilhas e desertos, enchendo a Terra inteira de vida!",
        "— Ouçam! Aquela família está falando palavras novas e melodiosas! — disseram as crianças junto às tendas.\n"
        "Em vez de ficarem trancados em torno de uma torre de orgulho, os povos abriram caminhos rumo ao norte, ao sul, ao leste e ao oeste. E foi de uma dessas cidades da Mesopotâmia que, no próximo volume, um amigo chamado Abraão olharia para as estrelas!",
        "OS ZIGURATES DA MESOPOTÂMIA",
        "Arqueólogos descobriram dezenas de zigurates no atual Iraque (antiga Sinar/Babilônia): grandes templos escalonados com escadarias externas construídos com milhões de tijolos cozidos ao fogo.",
        "Você conhece alguma palavra em outra língua? Como é bonito ver que pessoas de diferentes países fazem parte da mesma família humana!",
        dark_mode=False
    )
    pages.append(("piloto_p22_cap6_dialogos.png", p22_c6))

    # PÁGINA 23: PEQUENA GRANDE DESCOBERTA + BÍBLIA DE PERSONAGENS
    p12 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d12 = ImageDraw.Draw(p12)
    draw_wrapped_text(d12, "PEQUENA GRANDE DESCOBERTA: HISTÓRIA, CIÊNCIA E ARTE", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")
    p12 = draw_rounded_panel(p12, (80, 150, PAGE_W - 80, 560), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=22)
    d12 = ImageDraw.Draw(p12)
    draw_wrapped_text(d12, "1. O SEGREDO MUSICAL DO POEMA DE GÊNESIS 1", 120, 175, PAGE_W - 240, f_box_title, fill=(146, 64, 14))
    poema_txt = (
        "Você sabia que o primeiro capítulo da Bíblia foi escrito em hebraico antigo como uma canção cheia de ritmo? Observe como os seis momentos da criação formam dois grupos perfeitamente combinados:\n"
        "• Momentos 1, 2 e 3 (Os Espaços da Casa): 1º Luz e Noite  |  2º Céu e Mares  |  3º Terra Seca e Plantas.\n"
        "• Momentos 4, 5 e 6 (Os Moradores da Casa): 4º Sol, Lua e Estrelas  |  5º Peixes e Aves  |  6º Animais e Seres Humanos.\n"
        "A ciência estuda COMO e há quantos bilhões de anos as galáxias e os seres vivos se formaram; já o poema de Gênesis nos ensina QUEM deu origem a tudo por amor e por que cada vida tem um valor infinito!"
    )
    draw_wrapped_text(d12, poema_txt, 120, 225, PAGE_W - 240, f_box_body, fill=(41, 37, 36), line_spacing=1.38)

    draw_wrapped_text(d12, f"2. BÍBLIA DE PERSONAGENS DA COLEÇÃO (DIREÇÃO: {AUTHOR_UPPER})", 90, 590, PAGE_W - 180, f_box_title, fill=(30, 58, 138))
    sheet_ae = Image.open(os.path.join(char_dir, "char_sheet_adao_eva.jpg")).convert("RGB").resize((700, 394), Image.Resampling.LANCZOS)
    sheet_noe = Image.open(os.path.join(char_dir, "char_sheet_noe_familia.jpg")).convert("RGB").resize((700, 394), Image.Resampling.LANCZOS)
    sheet_jesus = Image.open(os.path.join(char_dir, "char_sheet_jesus_historico.jpg")).convert("RGB").resize((1040, 585), Image.Resampling.LANCZOS)

    p12.paste(sheet_ae, (80, 640))
    p12.paste(sheet_noe, (820, 640))
    d12.rectangle([80, 640, 780, 1034], outline=(180, 83, 9), width=3)
    d12.rectangle([820, 640, 1520, 1034], outline=(180, 83, 9), width=3)
    draw_wrapped_text(d12, "Adão e Eva (Capítulos 1–4): Fenótipo levantino e continuidade facial.", 80, 1044, 700, f_box_body, fill=(68, 64, 60))
    draw_wrapped_text(d12, "Noé e Naamá (Capítulo 5): Tradição mesopotâmica, linho, lã e ferramentas.", 820, 1044, 700, f_box_body, fill=(68, 64, 60))

    p12.paste(sheet_jesus, (280, 1110))
    d12.rectangle([280, 1110, 1320, 1695], outline=(30, 58, 138), width=3)
    nota_jesus = (
        "Prévia dos Volumes 6 a 9 — Reconstrução Histórica de Jesus de Nazaré (baseada nos estudos arqueológicos da Profa. Joan E. Taylor): Judeu galileu do século I, pele morena-oliva marcada pelo sol, cabelos e barba escuros aparados segundo o costume judaico, túnica de lã não tingida (haluq), manto (tallit) com franjas (tzitzit) e sandálias de couro."
    )
    draw_wrapped_text(d12, nota_jesus, 80, 1712, 1440, f_box_body, fill=(28, 25, 23), line_spacing=1.34)
    p12_rgb = p12.convert("RGB")
    draw_page_footer(p12_rgb, 23, "PEQUENA GRANDE DESCOBERTA  •  NOTAS HISTÓRICAS E VISUAIS", dark_mode=False)
    pages.append(("piloto_p12_descobertas_e_personagens.png", p12_rgb))

    # PÁGINA 24: CONTRACAPA OFICIAL DO VOLUME 1 (SINOPSE + PLANO DOS 10 VOLUMES + AUTOR FÁBIO MOTTA E SILVA)
    p24 = crop_and_resize(Image.open(os.path.join(vis_dir, "capa_conceito_1_cosmica_base.jpg")).convert("RGB"), PAGE_W, PAGE_H).convert("RGBA")
    p24 = draw_rounded_panel(p24, (110, 110, PAGE_W - 110, PAGE_H - 120), (8, 15, 38, 232), (245, 190, 70, 235), border_width=4, radius=32)
    d24 = ImageDraw.Draw(p24)
    draw_wrapped_text(d24, "A GRANDE HISTÓRIA DA LUZ", 160, 165, PAGE_W - 320, f_h1, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "A Bíblia Ilustrada para Pequenos Exploradores (4 a 10 anos)", 160, 240, PAGE_W - 320, f_italic, fill=(186, 230, 253), align="center")
    d24.line([(320, 305), (PAGE_W - 320, 305)], fill=(245, 190, 70, 180), width=2)

    sinopse_back = (
        "No princípio, antes das montanhas, dos oceanos e das estrelas, uma Voz amorosa ecoou no Universo: 'FAÇA-SE A LUZ!'.\n\n"
        "Neste primeiro volume da coleção escrita por Fábio Motta e Silva, crianças de 4 a 10 anos e suas famílias embarcam numa jornada cinematográfica em 3D pelos capítulos iniciais de Gênesis: o despertar do Cosmos, os quatro rios do Éden, as escolhas do coração, a grande Arca de Noé e o Zigurate de Babel.\n\n"
        "CONHEÇA OS 10 VOLUMES DA COLEÇÃO:\n"
        "• Vol. 1: Faça-se a Luz (A Criação, o Jardim, a Arca e Babel)\n"
        "• Vol. 2: As Estrelas da Promessa (Abraão, Sara, Isaque, Jacó e José no Egito)\n"
        "• Vol. 3: O Caminho da Liberdade (Moisés, Miriã e a Travessia do Mar)\n"
        "• Vol. 4: Coragem na Terra Prometida (Josué, Débora, Rute e Samuel)\n"
        "• Vol. 5: O Pastor, a Harpa e o Templo (Davi, os Salmos e Salomão)\n"
        "• Vol. 6: Mensageiros da Esperança (Elias, Eliseu, Isaías, Jonas, Ester e Daniel)\n"
        "• Vol. 7: A Estrela de Belém (O Nascimento e a Infância de Jesus)\n"
        "• Vol. 8: O Contador de Histórias da Galileia (As Parábolas e Sinais de Jesus)\n"
        "• Vol. 9: O Jardim da Manhã luminosa (A Entrega, a Ressurreição e a Paz)\n"
        "• Vol. 10: O Vento que Espalhou a Luz (Os Primeiros Amigos e a Nova Criação)"
    )
    draw_wrapped_text(d24, sinopse_back, 165, 340, PAGE_W - 330, f_body, fill=(248, 250, 252), line_spacing=1.34)
    d24.line([(320, 1695), (PAGE_W - 320, 1695)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(d24, f"AUTOR: {AUTHOR_UPPER}", 160, 1725, PAGE_W - 320, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, "Edição Autônoma Independente  •  Volume 1 (24 Páginas Ilustradas)", 160, 1785, PAGE_W - 320, f_ref, fill=(186, 230, 253), align="center")
    p24_rgb = p24.convert("RGB")
    draw_page_footer(p24_rgb, 24, "CONTRACAPA OFICIAL  •  COLEÇÃO A GRANDE HISTÓRIA DA LUZ", dark_mode=True)
    pages.append(("piloto_p24_contracapa.png", p24_rgb))

    saved_paths = []
    for fname, im in pages:
        fpath = os.path.join(diag_dir, fname)
        im.save(fpath, quality=95)
        saved_paths.append(fpath)
        print(f"   Página Volume 1 salva: {fname}")

    for fname in [
        "piloto_p01_capa.png", "piloto_p02_apresentacao.png", "piloto_p03_abismo.png",
        "piloto_p04_fiat_lux_esq.png", "piloto_p08_animais_jardim.png",
        "piloto_p09_humanidade_sopro.png", "piloto_p10_nomes_cuidadores.png", "piloto_p12_descobertas_e_personagens.png",
        "piloto_p13_cap2_jardim_eden.png", "piloto_p14_cap3_escolha_jardim.png", "piloto_p15_cap4_caim_abel.png",
        "piloto_p16_cap5_arca_noe.png", "piloto_p17_cap6_torre_babel.png", "piloto_p24_contracapa.png"
    ]:
        src_p = os.path.join(diag_dir, fname)
        if os.path.exists(src_p):
            shutil.copy2(src_p, os.path.join(BRAIN_DIR, fname))

    return saved_paths

def export_pdfs_and_epub(page_paths):
    print("-> Exportando Volume 1 (24 páginas): PDF HD (Hotmart), PDF Print 300 DPI (KDP Print) e EPUB 3 Fixed-Layout...")
    hotmart_pdf = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol1_Piloto_HD.pdf")
    print_pdf = os.path.join(BASE_DIR, "13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol1_Print_300DPI_Bleed.pdf")
    epub_path = os.path.join(BASE_DIR, "11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol1_FixedLayout_KDP.epub")

    pil_images = [Image.open(p).convert("RGB") for p in page_paths]
    pil_images[0].save(
        hotmart_pdf,
        "PDF",
        resolution=200.0,
        save_all=True,
        append_images=pil_images[1:],
        title="A Grande História da Luz - Vol. 1: Faça-se a Luz",
        author=AUTHOR_NAME
    )

    print_images = [crop_and_resize(im, 2438, 3075) for im in pil_images]
    print_images[0].save(
        print_pdf,
        "PDF",
        resolution=300.0,
        save_all=True,
        append_images=print_images[1:],
        title="A Grande História da Luz - Vol. 1 (Print 300 DPI with Bleed)",
        author=AUTHOR_NAME
    )

    with zipfile.ZipFile(epub_path, "w") as zf:
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
        for idx, p_path in enumerate(page_paths, start=1):
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
    <h1>A Grande História da Luz — Volume 1 ({AUTHOR_NAME})</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — Faça-se a Luz</a></li>
      <li><a href="page_02.xhtml">Folha de Rosto e Guia de Leitura</a></li>
      <li><a href="page_03.xhtml">Mapa de Exploração e Sumário</a></li>
      <li><a href="page_04.xhtml">Capítulo 1 — Antes de Tudo, a Luz</a></li>
      <li><a href="page_13.xhtml">Capítulo 2 — O Jardim das Águas Vivas</a></li>
      <li><a href="page_15.xhtml">Capítulo 3 — Onde Você Está? O Fio da Promessa</a></li>
      <li><a href="page_17.xhtml">Capítulo 4 — Dois Irmãos e o Segredo do Coração</a></li>
      <li><a href="page_19.xhtml">Capítulo 5 — A Grande Arca e o Arco da Aliança</a></li>
      <li><a href="page_21.xhtml">Capítulo 6 — A Cidade de Tijolos e o Mundo Inteiro</a></li>
      <li><a href="page_23.xhtml">Pequena Grande Descoberta e Bíblia de Personagens</a></li>
      <li><a href="page_24.xhtml">Contracapa Oficial</a></li>
    </ol>
  </nav>
</body>
</html>'''
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-vol1-2026</dc:identifier>
    <dc:title>Faça-se a Luz — O começo de todas as histórias (A Grande História da Luz - Vol. 1)</dc:title>
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
    print(f"   Volume 1 (24 páginas) exportado com sucesso!")

if __name__ == "__main__":
    copy_approved_assets()
    generate_complementary_artworks()
    build_covers()
    pages = build_pilot_pages()
    export_pdfs_and_epub(pages)
    print("VOLUME 1 (24 PÁGINAS) CONCLUÍDO COM SUCESSO!")
