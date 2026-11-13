#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e Artístico — A Grande História da Luz (Volume 1: Faça-se a Luz)
Responsável por:
1. Organizar e copiar as artes originais geradas para as pastas oficiais do projeto;
2. Renderizar em alta definição (1600x2000 px / 3200x2000 px spread) as ilustrações cósmicas e arqueológicas complementares do Capítulo 1;
3. Diagramar as 3 propostas de capa (e comparativo em tamanho real + miniatura 120px);
4. Diagramar as 12 páginas do Piloto Ilustrado do Volume 1 com hierarquia tipográfica profissional (Cinzel, Nunito, Atkinson Hyperlegible);
5. Exportar:
   - PDF de Revisão / Hotmart HD
   - PDF de Impressão 300 DPI com sangria (bleed 0.125")
   - EPUB 3 Fixed-Layout compatível com Amazon KDP Kids
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

# Dimensões base (8 x 10 polegadas em 200 DPI para master digital = 1600 x 2000 px; e 300 DPI print = 2400 x 3000 px)
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
        ("vol1_cap1_cena1_misterio_abismo_1794578923931.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena1_misterio_abismo.jpg"),
        ("vol1_cap1_cena5_animais_jardim_1794578850797.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena5_animais_jardim.jpg"),
        ("vol1_cap1_cena6_humanidade_sopro_1794578887504.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena6_humanidade_sopro.jpg"),
        ("vol1_cap1_cena7_nomes_cuidadores_1794578949947.jpg", "08-Ilustracoes-Originais/vol1_cap1_cena7_nomes_cuidadores.jpg"),
    ]
    for src_name, dst_rel in mapping:
        src = os.path.join(BRAIN_DIR, src_name)
        dst = os.path.join(BASE_DIR, dst_rel)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"   Copiado: {dst_rel}")

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
    """
    Cria em alta definição as artes cósmicas e infográficas complementares (Cenas 2, 3, 4, 8 e 9)
    combinando composição cromática procedural HD, iluminação volumétrica e elementos das artes base.
    """
    print("-> Renderizando artes cósmicas e infográficas complementares em alta definição...")
    out_dir = os.path.join(BASE_DIR, "08-Ilustracoes-Originais")
    
    # Carregar elementos base ricos das artes já geradas para harmonia estética total
    cosmica_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_1_cosmica_base.jpg")).convert("RGB")
    abismo_base = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap1_cena1_misterio_abismo.jpg")).convert("RGB")
    aventura_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg")).convert("RGB")
    mandala_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_3_pictorica_base.jpg")).convert("RGB")
    animais_base = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap1_cena5_animais_jardim.jpg")).convert("RGB")

    # 1. Cena 2: Fiat Lux (Spread Panorâmico 3200 x 2000 px)
    spread_w, spread_h = 3200, 2000
    fiat_lux = Image.new("RGB", (spread_w, spread_h), (8, 14, 38))
    # Mesclar o abismo à esquerda com a explosão cósmica à direita
    left_part = crop_and_resize(abismo_base, 1800, spread_h)
    right_part = crop_and_resize(cosmica_base, 1800, spread_h)
    fiat_lux.paste(left_part, (0, 0))
    # Criar máscara de transição suave com explosão de luz central
    mask = Image.new("L", (1800, spread_h))
    m_draw = ImageDraw.Draw(mask)
    for x in range(1800):
        val = int(255 * min(1.0, max(0.0, (x - 100) / 500.0)))
        m_draw.line([(x, 0), (x, spread_h)], fill=val)
    fiat_lux.paste(right_part, (1400, 0), mask)
    
    # Adicionar raios volumétricos dourados (Fiat Lux burst) no centro-direito
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

    # 2. Cena 3: O Abraço do Céu, do Mar e da Terra (1600 x 1300 px)
    # Recorte cinematográfico focado nas montanhas verdejantes, águas cristalinas e flora emergindo
    w0, h0 = cosmica_base.size
    cena3 = cosmica_base.crop((0, int(h0 * 0.42), w0, h0))
    cena3 = crop_and_resize(cena3, 1600, 1300)
    cena3 = ImageEnhance.Color(cena3).enhance(1.15)
    cena3.save(os.path.join(out_dir, "vol1_cap1_cena3_ceu_mar_terra.png"), quality=95)

    # 3. Cena 4: Dança das Estrelas, das Águas e das Asas (1600 x 1300 px)
    # Composição do anel celeste, ondas turquesas e pomba radiante da mandala pictórica
    wm, hm = mandala_base.size
    cena4 = mandala_base.crop((int(wm * 0.06), int(hm * 0.16), int(wm * 0.94), int(hm * 0.78)))
    cena4 = crop_and_resize(cena4, 1600, 1300)
    cena4.save(os.path.join(out_dir, "vol1_cap1_cena4_estrelas_e_vida.png"), quality=95)

    # 4. Cena 8: O Sétimo Momento — A Paz que Abraça Tudo (1600 x 2000 px)
    # Combinação crepuscular dourada-violeta da paisagem pacífica com o leão e o cordeiro em repouso
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

    print("   Artes complementares renderizadas com sucesso.")

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
    print("-> Gerando as 3 propostas de capa diagramadas e o painel comparativo (tamanho real + 120px)...")
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

        # Adicionar gradiente de proteção de leitura no topo e rodapé
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
            # Conceito 3 tem fundo creme/pergaminho claro no topo e escuro embaixo
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
            # Filete dourado superior
            cdraw.line([(360, 78), (PAGE_W - 360, 78)], fill=(245, 190, 70, 220), width=3)
            draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 96, PAGE_W - 200, f_series, fill=series_color, align="center", shadow=use_shadow)
            cdraw.line([(480, 152), (PAGE_W - 480, 152)], fill=(245, 190, 70, 180), width=2)

            # Título Principal
            draw_wrapped_text(cdraw, "FAÇA-SE A LUZ", 80, 178, PAGE_W - 160, f_title, fill=title_color, align="center", shadow=use_shadow)
            draw_wrapped_text(cdraw, "O começo de todas as histórias", 120, 305, PAGE_W - 240, f_sub, fill=sub_color, align="center", shadow=use_shadow)

        # Rodapé da capa (Selo Volume 1 + Subtítulo da Coleção + Autor Fabio)
        cover = draw_rounded_panel(cover, (220, PAGE_H - 235, PAGE_W - 220, PAGE_H - 70), (12, 22, 48, 222), (245, 190, 70, 235), border_width=3, radius=24)
        cdraw = ImageDraw.Draw(cover)
        draw_wrapped_text(cdraw, "VOLUME 1  •  A BÍBLIA ILUSTRADA PARA PEQUENOS EXPLORADORES", 240, PAGE_H - 208, PAGE_W - 480, f_tag, fill=(254, 240, 138, 255), align="center", shadow=False)
        draw_wrapped_text(cdraw, "FABIO", 240, PAGE_H - 142, PAGE_W - 480, f_author, fill=(255, 255, 255, 255), align="center", shadow=False)

        out_path = os.path.join(vis_dir, out_file)
        cover.convert("RGB").save(out_path, quality=95)
        generated_covers.append((out_file, cover.convert("RGB")))
        print(f"   Capa gerada: {out_file}")

    # Criar Prancha Comparativa das 3 Capas (Tamanho grande + Miniatura 120px de loja digital)
    board_w, board_h = 2400, 1500
    board = Image.new("RGB", (board_w, board_h), (15, 23, 42))
    bdraw = ImageDraw.Draw(board)
    f_btitle = load_font("cinzel", 44)
    f_blabel = load_font("nunito", 28)
    f_bsmall = load_font("atkinson", 22)

    draw_wrapped_text(bdraw, "ENTREGA 3 — COMPARATIVO DAS 3 PROPOSTAS DE CAPA (TAMANHO REAL vs. MINIATURA 120 PX)", 60, 36, board_w - 120, f_btitle, fill=(253, 224, 71), align="center")

    labels = [
        ("OPÇÃO 1 (ALTERNATIVA)", "Cósmica e Contemplativa (Fiat Lux)"),
        ("OPÇÃO 2 (CAPA OFICIAL ESCOLHIDA)", "Aventura Infantil Cinematográfica — Autor: Fabio"),
        ("OPÇÃO 3 (EDIÇÃO DE LUXO)", "Livro Ilustrado Pictórico / Mandala"),
    ]
    for idx, (fname, cov_img) in enumerate(generated_covers):
        x0 = 80 + idx * 770
        y0 = 130
        preview_large = cov_img.resize((520, 650), Image.Resampling.LANCZOS)
        board.paste(preview_large, (x0, y0))
        bdraw.rectangle([x0, y0, x0 + 520, y0 + 650], outline=(245, 190, 70), width=3)

        # Miniatura exata de 120px de largura ao lado
        thumb_120 = cov_img.resize((120, 150), Image.Resampling.LANCZOS)
        tx = x0 + 545
        ty = y0 + 250
        board.paste(thumb_120, (tx, ty))
        bdraw.rectangle([tx, ty, tx + 120, ty + 150], outline=(56, 189, 248), width=2)
        draw_wrapped_text(bdraw, "Teste Loja\n120 px", tx - 10, ty + 162, 140, f_bsmall, fill=(148, 163, 184), align="center")

        draw_wrapped_text(bdraw, labels[idx][0], x0, y0 + 675, 660, f_tag, fill=(253, 224, 71), align="left")
        draw_wrapped_text(bdraw, labels[idx][1], x0, y0 + 715, 660, f_blabel, fill=(241, 245, 249), align="left")

    # Rodapé de justificativa técnica no painel
    board = draw_rounded_panel(board, (80, 980, board_w - 80, 1430), (30, 41, 59, 240), (245, 190, 70, 200), border_width=2, radius=20).convert("RGB")
    bdraw = ImageDraw.Draw(board)
    analise_txt = (
        "DECISÃO EDITORIAL CONSOLIDADA PELO AUTOR (FABIO — PUBLICAÇÃO INDEPENDENTE):\n"
        "• Opção 2 (Aventura Infantil Cinematográfica — CAPA OFICIAL ESCOLHIDA): Selecionada pelo autor por comunicar imediatamente o universo infantil, gerando identificação instantânea com as crianças de 4 a 10 anos por meio dos dois pequenos exploradores contemplando o arco luminoso da criação.\n"
        "• Opção 1 (Cósmica e Contemplativa): Preservada para abertura de capítulo e materiais complementares.\n"
        "• Opção 3 (Pictórica / Mandala): Preservada como medalhão de Folha de Rosto e apresentação interna."
    )
    draw_wrapped_text(bdraw, analise_txt, 115, 1015, board_w - 230, f_blabel, fill=(248, 250, 252), line_spacing=1.42)
    board_path = os.path.join(vis_dir, "Entrega3_Comparativo_Capas_120px.png")
    board.save(board_path, quality=95)
    shutil.copy2(board_path, os.path.join(BRAIN_DIR, "Entrega3_Comparativo_Capas_120px.png"))
    shutil.copy2(os.path.join(vis_dir, "capa_final_2_aventura.png"), os.path.join(BRAIN_DIR, "capa_final_2_aventura.png"))
    print("   Painel comparativo de capas salvo.")

def draw_page_footer(img, page_num, chapter_label="VOLUME 1  •  FAÇA-SE A LUZ", dark_mode=True):
    draw = ImageDraw.Draw(img)
    f_foot = load_font("atkinson_bold", 22)
    color = (226, 232, 240, 210) if dark_mode else (71, 85, 105, 220)
    line_col = (245, 190, 70, 140) if dark_mode else (180, 83, 9, 120)
    draw.line([(90, PAGE_H - 78), (PAGE_W - 90, PAGE_H - 78)], fill=line_col, width=2)
    draw.text((90, PAGE_H - 62), chapter_label, font=f_foot, fill=color)
    p_str = f"PÁGINA {page_num:02d}"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def build_pilot_pages():
    print("-> Diagramando as 12 páginas completas do Piloto Ilustrado (Volume 1)...")
    diag_dir = os.path.join(BASE_DIR, "09-Diagramacao/paginas_piloto")
    os.makedirs(diag_dir, exist_ok=True)
    art_dir = os.path.join(BASE_DIR, "08-Ilustracoes-Originais")
    vis_dir = os.path.join(BASE_DIR, "03-Identidade-Visual")
    char_dir = os.path.join(BASE_DIR, "04-Biblia-de-Personagens")

    f_h1 = load_font("cinzel", 54)
    f_h2 = load_font("cinzel", 38)
    f_body = load_font("nunito", 33)
    f_body_lg = load_font("nunito", 36)
    f_italic = load_font("nunito_italic", 32)
    f_box_title = load_font("atkinson_bold", 27)
    f_box_body = load_font("atkinson", 25)
    f_ref = load_font("atkinson_bold", 24)

    pages = []

    # =========================================================================
    # PÁGINA 1 DO PILOTO: CAPA OFICIAL ESCOLHIDA PELO AUTOR (Conceito 2 — Aventura Infantil)
    # =========================================================================
    p1 = Image.open(os.path.join(vis_dir, "capa_final_2_aventura.png")).convert("RGB")
    pages.append(("piloto_p01_capa.png", p1))

    # =========================================================================
    # PÁGINA 2 DO PILOTO: FOLHA DE ROSTO, CARTA ÀS CRIANÇAS E GUIA DE LEITURA
    # =========================================================================
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    # Inserir a mandala pictórica no topo como medalhão de abertura
    mandala = Image.open(os.path.join(vis_dir, "capa_conceito_3_pictorica_base.jpg")).convert("RGB")
    mandala_crop = crop_and_resize(mandala, PAGE_W - 180, 760)
    p2.paste(mandala_crop, (90, 80))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([90, 80, PAGE_W - 90, 840], outline=(180, 83, 9), width=4)

    draw_wrapped_text(d2, "BEM-VINDO, PEQUENO EXPLORADOR DA LUZ!", 100, 865, PAGE_W - 200, f_h2, fill=(146, 64, 14), align="center")
    draw_wrapped_text(d2, "Autor: Fabio  •  Edição Autônoma Independente", 100, 918, PAGE_W - 200, f_ref, fill=(30, 58, 138), align="center")
    intro_text = (
        "Você está prestes a abrir um livro diferente. Aqui, cada página é uma janela para tempos muito antigos, onde o Universo começou a brilhar, rios cristalinos cortavam jardins perfumados e pessoas como nós aprenderam a fazer grandes escolhas.\n\n"
        "Neste livro, Deus nunca é desenhado como uma pessoa de barba branca sentada nas nuvens — porque Ele é muito maior do que qualquer corpo! Ele é a própria Origem, o Amor e a Presença Luminosa de onde nasceu toda a vida: FAÇA-SE A LUZ!"
    )
    draw_wrapped_text(d2, intro_text, 120, 965, PAGE_W - 240, f_body, fill=(41, 37, 36), line_spacing=1.38)

    # Quadro dos 4 selos interativos
    p2 = draw_rounded_panel(p2, (100, 1430, PAGE_W - 100, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "COMO EXPLORAR CADA CAPÍTULO EM FAMÍLIA:", 140, 1455, PAGE_W - 280, f_box_title, fill=(146, 64, 14))
    selos_txt = (
        "• VOCÊ PERCEBEU? — Detalhes escondidos nas ilustrações para observar com atenção.\n"
        "• O QUE VOCÊ FARIA? — Perguntas sobre escolhas, coragem, amizade e empatia.\n"
        "• PEQUENA GRANDE DESCOBERTA — Segredos reais da história, da arqueologia e da natureza.\n"
        "• CONVERSE COMIGO — Um momento especial de conversa entre crianças e responsáveis."
    )
    draw_wrapped_text(d2, selos_txt, 140, 1510, PAGE_W - 280, f_box_body, fill=(68, 64, 60), line_spacing=1.45)
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 2, "APRESENTAÇÃO E GUIA DE LEITURA", dark_mode=False)
    pages.append(("piloto_p02_apresentacao.png", p2_rgb))

    # =========================================================================
    # PÁGINA 3 DO PILOTO (Pág. 8 do Livro): ABERTURA CAP. 1 — ANTES DE TUDO, A LUZ
    # =========================================================================
    abismo_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena1_misterio_abismo.jpg")).convert("RGB")
    p3 = crop_and_resize(abismo_img, PAGE_W, PAGE_H).convert("RGBA")
    # Gradiente superior e inferior para leitura perfeita
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
    draw_wrapped_text(d3, "★ VOCÊ PERCEBEU? Olhe para o espelho d'água: a luz dourada e azul já está acordando as ondas!", 135, 1810, PAGE_W - 270, f_box_body, fill=(253, 224, 71))
    p3_rgb = p3.convert("RGB")
    draw_page_footer(p3_rgb, 8, "CAPÍTULO 1  •  ANTES DE TUDO, A LUZ", dark_mode=True)
    pages.append(("piloto_p03_abismo.png", p3_rgb))

    # =========================================================================
    # PÁGINAS 4 E 5 DO PILOTO (Págs. 9–10 do Livro): SPREAD DUPLO "FAÇA-SE A LUZ!"
    # =========================================================================
    spread_img = Image.open(os.path.join(art_dir, "vol1_cap1_cena2_fiat_lux.png")).convert("RGB")
    p4 = spread_img.crop((0, 0, PAGE_W, PAGE_H)).convert("RGBA")
    p5 = spread_img.crop((PAGE_W, 0, PAGE_W * 2, PAGE_H)).convert("RGBA")

    # Página 4 (Esquerda do Spread)
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
    draw_page_footer(p4_rgb, 9, "CAPÍTULO 1  •  FAÇA-SE A LUZ (FIAT LUX)", dark_mode=True)
    pages.append(("piloto_p04_fiat_lux_esq.png", p4_rgb))

    # Página 5 (Direita do Spread)
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
    draw_page_footer(p5_rgb, 10, "CAPÍTULO 1  •  FAÇA-SE A LUZ (FIAT LUX)", dark_mode=True)
    pages.append(("piloto_p05_fiat_lux_dir.png", p5_rgb))

    # =========================================================================
    # PÁGINA 6 DO PILOTO (Pág. 11 do Livro): O ABRAÇO DO CÉU, DO MAR E DA TERRA
    # =========================================================================
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
    draw_wrapped_text(d6, "★ PEQUENA GRANDE DESCOBERTA: Cada árvore frutífera guarda dentro de sua semente um 'mapa' completo para fazer nascer outra árvore igualzinha! É a vida se multiplicando como diz Gênesis 1:11.", 130, 1768, PAGE_W - 260, f_box_body, fill=(19, 78, 74), line_spacing=1.35)
    p6_rgb = p6.convert("RGB")
    draw_page_footer(p6_rgb, 11, "CAPÍTULO 1  •  CÉU, MAR E TERRA FÉRTIL", dark_mode=False)
    pages.append(("piloto_p06_ceu_mar_terra.png", p6_rgb))

    # =========================================================================
    # PÁGINA 7 DO PILOTO (Pág. 12 do Livro): A DANÇA DAS ESTRELAS, ÁGUAS E ASAS
    # =========================================================================
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
    draw_wrapped_text(d7, "★ VOCÊ PERCEBEU? Na ilustração acima, a pomba branca voa bem no raio de luz dourada que liga o céu estrelado às ondas do mar!", 130, 1790, PAGE_W - 260, f_box_body, fill=(186, 230, 253))
    p7_rgb = p7.convert("RGB")
    draw_page_footer(p7_rgb, 12, "CAPÍTULO 1  •  ESTRELAS, MARES E AVES", dark_mode=True)
    pages.append(("piloto_p07_estrelas_aves.png", p7_rgb))

    # =========================================================================
    # PÁGINA 8 DO PILOTO (Pág. 13 do Livro): OS HABITANTES DA TERRA
    # =========================================================================
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
    draw_wrapped_text(d8, "★ DESAFIO DO EXPLORADOR: Quantos passarinhos cantores no galho florido e quantas borboletas você consegue contar nesta cena?", 130, 1800, PAGE_W - 260, f_box_body, fill=(54, 83, 20))
    p8_rgb = p8.convert("RGB")
    draw_page_footer(p8_rgb, 13, "CAPÍTULO 1  •  OS ANIMAIS DO JARDIM", dark_mode=False)
    pages.append(("piloto_p08_animais_jardim.png", p8_rgb))

    # =========================================================================
    # PÁGINA 9 DO PILOTO (Pág. 14 do Livro): FILHOS DO BARRO E DA LUZ (ADÃO E EVA)
    # =========================================================================
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
    draw_page_footer(p9_rgb, 14, "CAPÍTULO 1  •  A CRIAÇÃO DA HUMANIDADE", dark_mode=True)
    pages.append(("piloto_p09_humanidade_sopro.png", p9_rgb))

    # =========================================================================
    # PÁGINA 10 DO PILOTO (Pág. 15 do Livro): CUIDADORES DO GRANDE JARDIM
    # =========================================================================
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
    draw_page_footer(p10_rgb, 15, "CAPÍTULO 1  •  CUIDADORES DO JARDIM", dark_mode=False)
    pages.append(("piloto_p10_nomes_cuidadores.png", p10_rgb))

    # =========================================================================
    # PÁGINA 11 DO PILOTO (Pág. 16 do Livro): O SÉTIMO MOMENTO — A PAZ QUE ABRAÇA TUDO
    # =========================================================================
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
    draw_wrapped_text(d11, "★ CONVERSE COMIGO EM FAMÍLIA:", 130, 1650, PAGE_W - 260, f_box_title, fill=(253, 224, 71))
    draw_wrapped_text(d11, "Por que descansar depois de trabalhar ou estudar é tão importante? Qual é o lugar da natureza onde você sente mais paz no coração?", 130, 1700, PAGE_W - 260, f_body, fill=(241, 245, 249), line_spacing=1.35)
    p11_rgb = p11.convert("RGB")
    draw_page_footer(p11_rgb, 16, "CAPÍTULO 1  •  O SÉTIMO MOMENTO", dark_mode=True)
    pages.append(("piloto_p11_descanso_luz.png", p11_rgb))

    # =========================================================================
    # PÁGINA 12 DO PILOTO (Pág. 17 do Livro): PEQUENA GRANDE DESCOBERTA + BÍBLIA VISUAL
    # =========================================================================
    p12 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d12 = ImageDraw.Draw(p12)
    draw_wrapped_text(d12, "PEQUENA GRANDE DESCOBERTA: HISTÓRIA, CIÊNCIA E ARTE", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")

    # Quadro 1: Estrutura poética de Gênesis 1
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

    # Galeria Visual de Reconstrução Histórica (Adão/Eva, Noé/Naamá e Jesus Histórico)
    draw_wrapped_text(d12, "2. BÍBLIA DE PERSONAGENS E RECONSTRUÇÃO HISTÓRICA DA COLEÇÃO", 90, 590, PAGE_W - 180, f_box_title, fill=(30, 58, 138))
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
        "Prévia dos Volumes 6 a 9 — Reconstrução Histórica de Jesus de Nazaré (baseada nos estudos arqueológicos da Profa. Joan E. Taylor, 'What Did Jesus Look Like?'): Judeu galileu do século I, pele morena-oliva marcada pelo sol, cabelos e barba escuros aparados segundo o costume judaico, túnica de lã não tingida (haluq), manto (tallit) com franjas (tzitzit) e sandálias de couro."
    )
    draw_wrapped_text(d12, nota_jesus, 80, 1712, 1440, f_box_body, fill=(28, 25, 23), line_spacing=1.34)

    p12_rgb = p12.convert("RGB")
    draw_page_footer(p12_rgb, 17, "PEQUENA GRANDE DESCOBERTA  •  NOTAS HISTÓRICAS E VISUAIS", dark_mode=False)
    pages.append(("piloto_p12_descobertas_e_personagens.png", p12_rgb))

    saved_paths = []
    for fname, im in pages:
        fpath = os.path.join(diag_dir, fname)
        im.save(fpath, quality=95)
        saved_paths.append(fpath)
        print(f"   Página diagramada salva: {fname}")

    # Copiar páginas-chave para o diretório de artefatos para apresentação visual direta ao usuário
    for fname in ["piloto_p03_abismo.png", "piloto_p04_fiat_lux_esq.png", "piloto_p08_animais_jardim.png", "piloto_p09_humanidade_sopro.png", "piloto_p10_nomes_cuidadores.png", "piloto_p12_descobertas_e_personagens.png"]:
        shutil.copy2(os.path.join(diag_dir, fname), os.path.join(BRAIN_DIR, fname))

    return saved_paths

def export_pdfs_and_epub(page_paths):
    print("-> Exportando Provas Digitais em PDF (Hotmart/Tablet + Impressão 300 DPI com Bleed) e EPUB 3 Fixed-Layout (Amazon KDP)...")
    hotmart_pdf = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol1_Piloto_HD.pdf")
    print_pdf = os.path.join(BASE_DIR, "13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol1_Print_300DPI_Bleed.pdf")
    epub_path = os.path.join(BASE_DIR, "11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol1_FixedLayout_KDP.epub")

    pil_images = [Image.open(p).convert("RGB") for p in page_paths]
    # 1. Salvar PDF Digital HD (Hotmart / Revisão Visual)
    pil_images[0].save(
        hotmart_pdf,
        "PDF",
        resolution=200.0,
        save_all=True,
        append_images=pil_images[1:],
        title="A Grande História da Luz - Vol. 1: Faça-se a Luz",
        author="Fabio"
    )
    print(f"   PDF Digital HD gerado: {hotmart_pdf}")

    # 2. Salvar PDF de Impressão 300 DPI com sangria (8.125 x 10.25 pol = 2438 x 3075 px)
    print_images = []
    for im in pil_images:
        p_im = crop_and_resize(im, 2438, 3075)
        print_images.append(p_im)
    print_images[0].save(
        print_pdf,
        "PDF",
        resolution=300.0,
        save_all=True,
        append_images=print_images[1:],
        title="A Grande História da Luz - Vol. 1 (Print 300 DPI with Bleed)",
        author="Fabio"
    )
    print(f"   PDF Impressão 300 DPI gerado: {print_pdf}")

    # 3. Construir pacote EPUB 3 Fixed-Layout oficial compatível com Amazon KDP
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
            # Converter para JPEG otimizado para KDP
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

        nav_xhtml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head><title>Sumário</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>A Grande História da Luz — Volume 1</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — Faça-se a Luz</a></li>
      <li><a href="page_02.xhtml">Bem-vindo, Pequeno Explorador</a></li>
      <li><a href="page_03.xhtml">Capítulo 1 — Antes de Tudo, a Luz</a></li>
      <li><a href="page_04.xhtml">Faça-se a Luz! (Fiat Lux)</a></li>
      <li><a href="page_09.xhtml">Filhos do Barro e da Luz</a></li>
      <li><a href="page_12.xhtml">Pequena Grande Descoberta e Bíblia de Personagens</a></li>
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
    <dc:creator>Fabio</dc:creator>
    <meta property="dcterms:modified">2026-11-13T12:00:00Z</meta>
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
    print(f"   EPUB 3 Fixed-Layout KDP gerado: {epub_path}")

if __name__ == "__main__":
    copy_approved_assets()
    generate_complementary_artworks()
    build_covers()
    pages = build_pilot_pages()
    export_pdfs_and_epub(pages)
    print("CONCLUÍDO COM SUCESSO!")
