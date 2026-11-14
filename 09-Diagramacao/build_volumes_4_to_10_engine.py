#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e Artístico Unificado — Volumes 4 a 10 + Edição Integral (240 Páginas)
Coleção: A Grande História da Luz — A Bíblia Ilustrada para Pequenos Exploradores
Autor: Fábio Motta e Silva (Publicação Independente / Autônoma)
Responsável por:
1. Gerar os 7 documentos de Roteiro Literário (Dupla Camada) e Storyboard de 64 páginas dos Volumes 4 a 10;
2. Copiar as ilustrações 3D inéditas das Capas e Cenas Heroicas dos Volumes 4 a 10;
3. Diagramar as Capas Oficiais (Estilo Capa 2 Aventura Infantil com FÁBIO MOTTA E SILVA) e as 24 páginas sequenciais (PÁGINA 01 DE 24 a PÁGINA 24 DE 24) de cada volume (Volumes 4, 5, 6, 7, 8, 9 e 10);
4. Exportar PDF HD (200 DPI), PDF Print 300 DPI com sangria e EPUB 3 Fixed-Layout (Amazon KDP) para todos os volumes;
5. Gerar a Edição Integral Unificada da Coleção Completa (Volumes 1 a 10 — 240 Páginas Ilustradas de Gênesis ao Apocalipse).
"""

import os
import sys
import glob
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from volumes_data_part1 import VOLUMES_DATA
from volumes_data_part2 import VOLUMES_DATA_NT

ALL_VOLS_4_10 = VOLUMES_DATA + VOLUMES_DATA_NT

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
BRAIN_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/brain/026b6e7b-1190-4ec1-b3f4-789abc0233f8"
FONT_DIR = os.path.join(BASE_DIR, "03-Identidade-Visual/fonts")
FUT_DIR = os.path.join(BASE_DIR, "15-Volumes-Futuros")

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

def draw_page_footer(img, page_num, chapter_label, dark_mode=True):
    draw = ImageDraw.Draw(img)
    f_foot = load_font("atkinson_bold", 22)
    color = (226, 232, 240, 210) if dark_mode else (71, 85, 105, 220)
    line_col = (245, 190, 70, 140) if dark_mode else (180, 83, 9, 120)
    draw.line([(90, PAGE_H - 78), (PAGE_W - 90, PAGE_H - 78)], fill=line_col, width=2)
    draw.text((90, PAGE_H - 62), chapter_label, font=f_foot, fill=color)
    p_str = f"PÁGINA {page_num:02d} DE 24"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def resolve_source_image(src_name, vol_ilus_dir, hero_path):
    if src_name.startswith("HERO_"):
        if os.path.exists(hero_path):
            return Image.open(hero_path).convert("RGB")
    candidates = [
        os.path.join(vol_ilus_dir, src_name),
        os.path.join(BASE_DIR, "08-Ilustracoes-Originais", src_name),
        os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-2-As-Estrelas-da-Promessa/ilustracoes", src_name),
        os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade/ilustracoes", src_name),
        os.path.join(BASE_DIR, "03-Identidade-Visual", src_name),
    ]
    for c in candidates:
        if os.path.exists(c):
            return Image.open(c).convert("RGB")
    return Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg")).convert("RGB")

def write_markdown_script(vol):
    vnum = vol["num"]
    md_path = os.path.join(FUT_DIR, vol["md_file"])
    lines = [
        f"# Volume {vnum} (eBook {vnum}) — *{vol['title'].title()}: {vol['subtitle']}*",
        f"**Coleção:** *A Grande História da Luz — A Bíblia Ilustrada para Pequenos Exploradores*  ",
        f"**Autor:** {AUTHOR_NAME} (Publicação Independente / Autônoma)  ",
        f"**Recorte Canônico:** {vol['biblical_range']}  ",
        f"**Padrão Editorial:** Edição Ilustrada Completa de **24 Páginas Diagramadas** + **Storyboard Expandido de 64 Páginas** • Estilo **Capa 2 (Aventura Infantil Cinematográfica 3D)** • Regra Teológica **Fiat Lux** (Presença Divina representada exclusivamente por luz volumétrica dourada e safira, sem antropomorfismo do Pai) • Reconstrução Histórica e Arqueológica Verificada.\n",
        "---\n",
        "## PARTE 1 — ROTEIRO LITERÁRIO COMPLETO DOS 6 CAPÍTULOS (DUPLA CAMADA 4–6 ANOS E 6–10 ANOS)\n"
    ]
    for ch in vol["chapters"]:
        lines.extend([
            f"### CAPÍTULO {ch['num']}: {ch['title']}",
            f"**{ch['ref']}**\n",
            f"#### 🌱 Camada 1 — Pequenos Exploradores (4–6 anos | Leitura em Voz Alta)",
            f"{ch['seed_4_6']}\n",
            f"#### 🧭 Camada 2 — Leitura Autônoma & Compartilhada (6–10 anos)",
            f"`[BASE BÍBLICA DIRETA]` {ch['main_narrative']}\n",
            f"`[DRAMATIZAÇÃO LITERÁRIA AUTORAL]`\n{ch['explorer_dialogue']}\n",
            f"- **🔍 Pequena Grande Descoberta ({ch['arq_title']}):** {ch['arq_text']}",
            f"- **💬 O Que Você Faria? / Converse Comigo:** {ch['family_question']}\n",
            "---\n"
        ])
    lines.extend([
        f"## PARTE 2 — STORYBOARD EDITORIAL DE 64 PÁGINAS (VOLUME {vnum}: {vol['title']})\n",
        "| Páginas | Seção / Capítulo | Conteúdo Visual e Editorial |",
        "| :--- | :--- | :--- |",
        f"| **01** | Capa Oficial | **Estilo Capa 2 (Aventura Infantil 3D):** {vol['title']} • Autor: **{AUTHOR_NAME}**. |",
        f"| **02–05** | Folha de Rosto, Guia e Mapa | Boas-vindas, Guia de Leitura em Dupla Camada e {vol['map_title']}. |",
        f"| **06–13** | **Capítulo 1** | {vol['chapters'][0]['title']} ({vol['chapters'][0]['ref']}). |",
        f"| **14–21** | **Capítulo 2** | {vol['chapters'][1]['title']} ({vol['chapters'][1]['ref']}). |",
        f"| **22–31** | **Capítulo 3** | {vol['chapters'][2]['title']} ({vol['chapters'][2]['ref']}). |",
        f"| **32–41** | **Capítulo 4** | {vol['chapters'][3]['title']} ({vol['chapters'][3]['ref']}). |",
        f"| **42–51** | **Capítulo 5** | {vol['chapters'][4]['title']} ({vol['chapters'][4]['ref']}). |",
        f"| **52–59** | **Capítulo 6** | {vol['chapters'][5]['title']} ({vol['chapters'][5]['ref']}). |",
        f"| **60–63** | Arqueologia, Glossário e Personagens | {vol['archaeology_section_title']} + Bíblia de Personagens Histórica. |",
        f"| **64** | Contracapa Oficial | Sinopse do Volume {vnum} e Assinatura Autoral **{AUTHOR_NAME}**. |\n"
    ])
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"   Roteiro e Storyboard Markdown gerado: {vol['md_file']}")

def make_3page_chapter(vol_num, vol_title, ch, art_img, start_page):
    f_h2 = load_font("cinzel", 34)
    f_body = load_font("nunito", 32)
    f_box_title = load_font("atkinson_bold", 26)
    f_box_body = load_font("atkinson", 24)
    f_ref = load_font("atkinson_bold", 23)

    dark_mode = ch["dark_mode"]
    cap_num = ch["num"]
    cap_title = ch["title"]
    bg_col = (12, 20, 40, 255) if dark_mode else (253, 251, 247, 255)
    border_c = (245, 190, 70) if dark_mode else (180, 83, 9)
    title_c = (253, 224, 71) if dark_mode else (146, 64, 14)
    ref_c = (186, 230, 253) if dark_mode else (30, 58, 138)
    body_c = (248, 250, 252) if dark_mode else (41, 37, 36)

    # PÁGINA A: ABERTURA ILUSTRADA 3D
    pA = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    pA.paste(crop_and_resize(art_img, PAGE_W - 140, 1020), (70, 70))
    dA = ImageDraw.Draw(pA)
    dA.rectangle([70, 70, PAGE_W - 70, 1090], outline=border_c, width=4)
    draw_wrapped_text(dA, f"CAPÍTULO {cap_num}  •  {cap_title}", 90, 1120, PAGE_W - 180, f_h2, fill=title_c)
    draw_wrapped_text(dA, f"{ch['ref']}  |  Autor: {AUTHOR_NAME}", 90, 1175, PAGE_W - 180, f_ref, fill=ref_c)
    draw_wrapped_text(dA, ch["main_narrative"], 90, 1230, PAGE_W - 180, f_body, fill=body_c, line_spacing=1.34)
    boxA_bg = (30, 41, 59, 240) if dark_mode else (254, 243, 199, 255)
    boxA_bd = (245, 190, 70, 220) if dark_mode else (217, 119, 6, 255)
    boxA_tc = (254, 240, 138) if dark_mode else (146, 64, 14)
    pA = draw_rounded_panel(pA, (90, 1750, PAGE_W - 90, 1890), boxA_bg, boxA_bd, border_width=2, radius=18)
    dA = ImageDraw.Draw(pA)
    draw_wrapped_text(dA, ch["quick_box"], 120, 1775, PAGE_W - 240, f_box_body, fill=boxA_tc)
    pA_rgb = pA.convert("RGB")
    draw_page_footer(pA_rgb, start_page, f"VOLUME {vol_num}  •  CAPÍTULO {cap_num}: {cap_title[:32]}", dark_mode=dark_mode)

    # PÁGINA B: DUPLA CAMADA (4-6 ANOS & DIÁLOGOS 6-10 ANOS)
    pB = Image.new("RGBA", (PAGE_W, PAGE_H), bg_col)
    w, h = art_img.size
    left_zoom = art_img.crop((0, int(h * 0.08), int(w * 0.80), int(h * 0.65)))
    pB.paste(crop_and_resize(left_zoom, PAGE_W - 140, 520), (70, 70))
    dB = ImageDraw.Draw(pB)
    dB.rectangle([70, 70, PAGE_W - 70, 590], outline=border_c, width=4)
    draw_wrapped_text(dB, f"CAPÍTULO {cap_num}  •  LEITURA EM DUPLA CAMADA", 90, 620, PAGE_W - 180, f_h2, fill=title_c)
    pB = draw_rounded_panel(pB, (85, 685, PAGE_W - 85, 1055), boxA_bg, boxA_bd, border_width=3, radius=22)
    dB = ImageDraw.Draw(pB)
    draw_wrapped_text(dB, "» CAMADA SEMENTE (4 A 6 ANOS — LEITURA EM VOZ ALTA):", 120, 712, PAGE_W - 240, f_box_title, fill=boxA_tc)
    draw_wrapped_text(dB, ch["seed_4_6"], 120, 760, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.34)

    draw_wrapped_text(dB, "CENA DRAMATIZADA E DIÁLOGOS (CAMADA EXPLORADOR 6–10 ANOS):", 90, 1090, PAGE_W - 180, f_box_title, fill=title_c)
    draw_wrapped_text(dB, ch["explorer_dialogue"], 90, 1140, PAGE_W - 180, f_body, fill=body_c, line_spacing=1.35)
    pB_rgb = pB.convert("RGB")
    draw_page_footer(pB_rgb, start_page + 1, f"VOLUME {vol_num}  •  CAPÍTULO {cap_num} (DUPLA CAMADA)", dark_mode=dark_mode)

    # PÁGINA C: ARQUEOLOGIA, HISTÓRIA E CONVERSA EM FAMÍLIA
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
    draw_wrapped_text(dC, f"» PEQUENA GRANDE DESCOBERTA: {ch['arq_title']}", 120, 885, PAGE_W - 240, f_box_title, fill=disc_tc)
    draw_wrapped_text(dC, ch["arq_text"], 120, 938, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.35)

    q_bg = (30, 58, 47, 240) if dark_mode else (236, 252, 203, 255)
    q_bd = (74, 222, 128, 220) if dark_mode else (101, 163, 13, 255)
    q_tc = (187, 247, 208) if dark_mode else (54, 83, 20)
    pC = draw_rounded_panel(pC, (85, 1425, PAGE_W - 85, 1885), q_bg, q_bd, border_width=3, radius=22)
    dC = ImageDraw.Draw(pC)
    draw_wrapped_text(dC, "» O QUE VOCÊ FARIA? / CONVERSE COMIGO EM FAMÍLIA:", 120, 1455, PAGE_W - 240, f_box_title, fill=q_tc)
    draw_wrapped_text(dC, ch["family_question"], 120, 1510, PAGE_W - 240, f_body, fill=body_c, line_spacing=1.35)
    pC_rgb = pC.convert("RGB")
    draw_page_footer(pC_rgb, start_page + 2, f"VOLUME {vol_num}  •  CAPÍTULO {cap_num} (DESCOBERTAS)", dark_mode=dark_mode)

    return [pA_rgb, pB_rgb, pC_rgb]

def build_single_volume(vol):
    vnum = vol["num"]
    vol_dir = os.path.join(FUT_DIR, vol["slug"])
    ilus_dir = os.path.join(vol_dir, "ilustracoes")
    p_dir = os.path.join(vol_dir, "paginas_piloto")
    epub_check = os.path.join(BASE_DIR, f"11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol{vnum}_FixedLayout_KDP.epub")
    if os.path.exists(epub_check) and os.path.exists(p_dir):
        existing_pages = sorted([os.path.join(p_dir, f) for f in os.listdir(p_dir) if f.startswith(f"vol{vnum}_p") and f.endswith(".png")])
        if len(existing_pages) == 24:
            print(f"-> Volume {vnum} já compilado (24 páginas verificadas). Reutilizando arquivos...")
            return existing_pages

    print(f"-> Construindo Volume {vnum}: {vol['title']} (24 páginas completas)...")
    write_markdown_script(vol)

    os.makedirs(ilus_dir, exist_ok=True)
    os.makedirs(p_dir, exist_ok=True)

    # 1. Copiar Capa Base 3D e Cena Heroica 3D do diretório de artefatos se disponíveis
    cov_base_dst = os.path.join(ilus_dir, f"vol{vnum}_capa_base_aventura.jpg")
    matches_cov = sorted(glob.glob(os.path.join(BRAIN_DIR, f"{vol['cover_base_prefix']}_*.jpg")))
    if matches_cov and vnum not in (9, 10):
        shutil.copy2(matches_cov[-1], cov_base_dst)
        print(f"   Capa 3D copiada para Volume {vnum}: {os.path.basename(matches_cov[-1])}")
    elif vnum == 9:
        # Arte 3D nítida (sem dupla exposição) para Volume 9: Amanhecer Dourado sobre Jerusalém e o Jardim das Oliveiras
        im_jerusalem = Image.open(sorted(glob.glob(os.path.join(BRAIN_DIR, "vol3_cap6_terra_prometida*.jpg")))[-1]).convert("RGB")
        jw, jh = im_jerusalem.size
        im_jerusalem_crop = im_jerusalem.crop((0, 0, int(jw * 0.58), jh))
        im_v9 = crop_and_resize(im_jerusalem_crop, 1600, 2000)
        im_v9 = ImageEnhance.Color(im_v9).enhance(1.12)
        im_v9 = ImageEnhance.Contrast(im_v9).enhance(1.05)
        im_v9.save(cov_base_dst, quality=95)
        shutil.copy2(cov_base_dst, os.path.join(BRAIN_DIR, "vol9_capa_base_aventura.jpg"))
        print("   Capa 3D nítida gerada para Volume 9 (Amanhecer de Páscoa sobre Jerusalém)")
    elif vnum == 10:
        # Arte 3D nítida (sem dupla exposição) para Volume 10: Pomba da Paz, Espiral Cósmica, Árvores da Vida e Harmonia da Nova Criação
        im_nova_criacao = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap1_cena8_descanso_luz.png")).convert("RGB")
        im_v10 = crop_and_resize(im_nova_criacao, 1600, 2000)
        im_v10 = ImageEnhance.Color(im_v10).enhance(1.10)
        im_v10 = ImageEnhance.Contrast(im_v10).enhance(1.05)
        im_v10.save(cov_base_dst, quality=95)
        shutil.copy2(cov_base_dst, os.path.join(BRAIN_DIR, "vol10_capa_base_aventura.jpg"))
        print("   Capa 3D nítida gerada para Volume 10 (A Luz Continua — Pomba de Pentecostes e Jardim Eterno)")
    elif not os.path.exists(cov_base_dst):
        shutil.copy2(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg"), cov_base_dst)

    hero_dst = os.path.join(ilus_dir, f"{vol['hero_art_prefix']}.jpg")
    matches_hero = sorted(glob.glob(os.path.join(BRAIN_DIR, f"{vol['hero_art_prefix']}*.jpg")))
    if matches_hero:
        shutil.copy2(matches_hero[-1], hero_dst)
        print(f"   Cena Heroica 3D copiada para Volume {vnum}: {os.path.basename(matches_hero[-1])}")
    else:
        # Criar enquadramento cinematográfico panorâmico a partir da arte 3D do volume
        cb_im = Image.open(cov_base_dst).convert("RGB")
        cw, ch_h = cb_im.size
        crop_hero = cb_im.crop((0, int(ch_h * 0.14), cw, int(ch_h * 0.86)))
        crop_hero = ImageEnhance.Color(crop_hero).enhance(1.12)
        crop_hero.save(hero_dst, quality=95)

    # 2. Diagramar Capa Oficial do Volume (Estilo Capa 2 + Autor FÁBIO MOTTA E SILVA)
    base_im = Image.open(cov_base_dst).convert("RGB")
    cov_rgba = crop_and_resize(base_im, PAGE_W, PAGE_H).convert("RGBA")
    grad = Image.new("RGBA", (PAGE_W, PAGE_H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grad)
    for y in range(540):
        alpha = int(195 * (1 - y / 540.0) ** 1.35)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 16, 42, alpha))
    for y in range(PAGE_H - 360, PAGE_H):
        alpha = int(215 * ((y - (PAGE_H - 360)) / 360.0) ** 1.3)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(8, 16, 38, alpha))
    cov_rgba = Image.alpha_composite(cov_rgba, grad)
    cdraw = ImageDraw.Draw(cov_rgba)

    f_series = load_font("cinzel", 34)
    title_len = len(vol["title"])
    f_title = load_font("cinzel", 62 if title_len > 26 else 70)
    f_sub = load_font("nunito", 35)
    f_tag = load_font("atkinson_bold", 25)
    f_author = load_font("cinzel", 30)

    cdraw.line([(360, 78), (PAGE_W - 360, 78)], fill=(245, 190, 70, 220), width=3)
    draw_wrapped_text(cdraw, "A GRANDE HISTÓRIA DA LUZ", 100, 96, PAGE_W - 200, f_series, fill=(240, 246, 255), align="center", shadow=True)
    cdraw.line([(480, 152), (PAGE_W - 480, 152)], fill=(245, 190, 70, 180), width=2)
    next_y = draw_wrapped_text(cdraw, vol["title"], 70, 174, PAGE_W - 140, f_title, fill=(255, 224, 115), align="center", shadow=True, line_spacing=1.18)
    draw_wrapped_text(cdraw, vol["subtitle"], 110, next_y + 14, PAGE_W - 220, f_sub, fill=(255, 255, 255), align="center", shadow=True)

    cov_rgba = draw_rounded_panel(cov_rgba, (200, PAGE_H - 235, PAGE_W - 200, PAGE_H - 70), (12, 22, 48, 225), (245, 190, 70, 235), border_width=3, radius=24)
    cdraw = ImageDraw.Draw(cov_rgba)
    draw_wrapped_text(cdraw, f"VOLUME {vnum}  •  A BÍBLIA ILUSTRADA PARA PEQUENOS EXPLORADORES", 220, PAGE_H - 208, PAGE_W - 440, f_tag, fill=(254, 240, 138), align="center")
    draw_wrapped_text(cdraw, AUTHOR_UPPER, 220, PAGE_H - 142, PAGE_W - 440, f_author, fill=(255, 255, 255), align="center")
    cov_path = os.path.join(ilus_dir, f"vol{vnum}_capa_oficial_aventura.png")
    cov_rgba.convert("RGB").save(cov_path, quality=95)
    shutil.copy2(cov_path, os.path.join(BRAIN_DIR, f"vol{vnum}_capa_oficial_aventura.png"))

    f_h1 = load_font("cinzel", 48)
    f_h2 = load_font("cinzel", 35)
    f_body = load_font("nunito", 32)
    f_italic = load_font("nunito_italic", 30)
    f_box_title = load_font("atkinson_bold", 26)
    f_box_body = load_font("atkinson", 24)
    f_ref = load_font("atkinson_bold", 24)

    pages = []
    hero_im = Image.open(hero_dst).convert("RGB")

    # PÁGINA 01: CAPA OFICIAL
    pages.append((f"vol{vnum}_p01_capa.png", cov_rgba.convert("RGB")))

    # PÁGINA 02: FOLHA DE ROSTO E GUIA DE LEITURA
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    p2.paste(crop_and_resize(hero_im, PAGE_W - 180, 680), (90, 75))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([90, 75, PAGE_W - 90, 755], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d2, vol["title"], 90, 785, PAGE_W - 180, f_h1, fill=(146, 64, 14), align="center")
    draw_wrapped_text(d2, f"Volume {vnum}  •  Autor: {AUTHOR_NAME} (Edição Independente)", 100, 852, PAGE_W - 200, f_ref, fill=(30, 58, 138), align="center")
    draw_wrapped_text(d2, vol["intro_text"], 110, 910, PAGE_W - 220, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p2 = draw_rounded_panel(p2, (95, 1395, PAGE_W - 95, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "COMO LER ESTE LIVRO EM FAMÍLIA (DUPLA CAMADA 4–10 ANOS):", 135, 1425, PAGE_W - 270, f_box_title, fill=(146, 64, 14))
    guia_txt = (
        "• Cada um dos 6 capítulos conta com 3 páginas completas (Páginas 04 a 21).\n"
        "• Na 1ª página do capítulo, contemple a grande ilustração 3D e o resumo narrativo.\n"
        "• Na 2ª página, escolha entre a Camada Semente (4–6 anos) ou os Diálogos da Camada Explorador (6–10 anos).\n"
        "• Na 3ª página, descubra segredos históricos e arqueológicos e converse em família!"
    )
    draw_wrapped_text(d2, guia_txt, 135, 1480, PAGE_W - 270, f_box_body, fill=(68, 64, 60), line_spacing=1.42)
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 2, f"FOLHA DE ROSTO E GUIA DE LEITURA  •  VOLUME {vnum}", dark_mode=False)
    pages.append((f"vol{vnum}_p02_folha_rosto.png", p2_rgb))

    # PÁGINA 03: MAPA HISTÓRICO E SUMÁRIO DOS 6 CAPÍTULOS
    p3_map = Image.new("RGBA", (PAGE_W, PAGE_H), (12, 20, 40, 255))
    p3_map.paste(crop_and_resize(base_im, PAGE_W - 140, 580), (70, 70))
    dm = ImageDraw.Draw(p3_map)
    dm.rectangle([70, 70, PAGE_W - 70, 650], outline=(245, 190, 70), width=4)
    draw_wrapped_text(dm, vol["map_title"], 90, 680, PAGE_W - 180, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(dm, f"Roteiro e Direção Editorial: {AUTHOR_NAME}  |  {vol['biblical_range']}", 90, 735, PAGE_W - 180, f_ref, fill=(186, 230, 253), align="center")
    p3_map = draw_rounded_panel(p3_map, (85, 795, PAGE_W - 85, 1885), (30, 41, 59, 240), (245, 190, 70, 220), border_width=3, radius=24)
    dm = ImageDraw.Draw(p3_map)
    sum_items = []
    for idx, ch in enumerate(vol["chapters"]):
        p_ini = 4 + idx * 3
        p_fim = p_ini + 2
        sum_items.append(f"• CAPÍTULO {ch['num']} — {ch['title']} (Págs. {p_ini:02d} a {p_fim:02d}):\n  {ch['ref']} — {ch['seed_4_6'][:135]}...")
    draw_wrapped_text(dm, "\n\n".join(sum_items), 120, 830, PAGE_W - 240, f_box_body, fill=(248, 250, 252), line_spacing=1.32)
    p3_map_rgb = p3_map.convert("RGB")
    draw_page_footer(p3_map_rgb, 3, f"SUMÁRIO VISUAL E MAPA HISTÓRICO  •  VOLUME {vnum}", dark_mode=True)
    pages.append((f"vol{vnum}_p03_mapa_sumario.png", p3_map_rgb))

    # PÁGINAS 04 A 21: OS 6 CAPÍTULOS (3 PÁGINAS CADA)
    for idx, ch in enumerate(vol["chapters"]):
        start_p = 4 + idx * 3
        art_im = resolve_source_image(ch["art_source"], ilus_dir, hero_dst)
        ch_pages = make_3page_chapter(vnum, vol["title"], ch, art_im, start_p)
        pages.append((f"vol{vnum}_p{start_p:02d}_cap{ch['num']}_abertura.png", ch_pages[0]))
        pages.append((f"vol{vnum}_p{start_p+1:02d}_cap{ch['num']}_camadas.png", ch_pages[1]))
        pages.append((f"vol{vnum}_p{start_p+2:02d}_cap{ch['num']}_descobertas.png", ch_pages[2]))

    # PÁGINA 22: ARQUEOLOGIA E GLOSSÁRIO DO VOLUME
    p22 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, f"PEQUENA GRANDE DESCOBERTA  •  ARQUEOLOGIA DO VOLUME {vnum}", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")
    p22 = draw_rounded_panel(p22, (80, 145, PAGE_W - 80, 965), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, vol["archaeology_section_title"], 120, 175, PAGE_W - 240, f_box_title, fill=(146, 64, 14))
    draw_wrapped_text(d22, vol["archaeology_full"], 120, 230, PAGE_W - 240, f_body, fill=(41, 37, 36), line_spacing=1.34)

    p22 = draw_rounded_panel(p22, (80, 1005, PAGE_W - 80, 1885), (224, 242, 254, 255), (2, 132, 199, 255), border_width=3, radius=24)
    d22 = ImageDraw.Draw(p22)
    draw_wrapped_text(d22, f"2. PEQUENO GLOSSÁRIO DO EXPLORADOR (VOLUME {vnum})", 120, 1035, PAGE_W - 240, f_box_title, fill=(7, 89, 133))
    draw_wrapped_text(d22, vol["glossary_full"], 120, 1090, PAGE_W - 240, f_body, fill=(28, 25, 23), line_spacing=1.38)
    p22_rgb = p22.convert("RGB")
    draw_page_footer(p22_rgb, 22, f"VOLUME {vnum}  •  ARQUEOLOGIA E GLOSSÁRIO DO EXPLORADOR", dark_mode=False)
    pages.append((f"vol{vnum}_p22_arqueologia_glossario.png", p22_rgb))

    # PÁGINA 23: BÍBLIA DE PERSONAGENS E RECONSTRUÇÃO HISTÓRICA
    p23 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, f"BÍBLIA DE PERSONAGENS  •  VOLUME {vnum} ({AUTHOR_UPPER})", 90, 75, PAGE_W - 180, f_h2, fill=(30, 58, 138), align="center")
    char_dir = os.path.join(BASE_DIR, "04-Biblia-de-Personagens")
    if vnum >= 6:
        sheet_file = os.path.join(char_dir, "char_sheet_jesus_historico.jpg")
    elif vnum == 4:
        sheet_file = os.path.join(char_dir, "char_sheet_abraao_sara_jose.jpg")
    else:
        sheet_file = os.path.join(char_dir, "char_sheet_moises_miriam.jpg")
    if not os.path.exists(sheet_file):
        sheet_file = os.path.join(char_dir, "char_sheet_jesus_historico.jpg")
    sheet_im = Image.open(sheet_file).convert("RGB").resize((1400, 788), Image.Resampling.LANCZOS)
    p23.paste(sheet_im, (100, 145))
    d23.rectangle([100, 145, 1500, 933], outline=(180, 83, 9), width=4)

    p23 = draw_rounded_panel(p23, (85, 975, PAGE_W - 85, 1885), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=24)
    d23 = ImageDraw.Draw(p23)
    draw_wrapped_text(d23, f"DIRETRIZES DE RECONSTRUÇÃO HISTÓRICA — VOLUME {vnum}", 125, 1005, PAGE_W - 250, f_box_title, fill=(146, 64, 14))
    draw_wrapped_text(d23, f"Direção Editorial e Autoral: {AUTHOR_NAME}\n\n" + vol["char_notes"], 125, 1060, PAGE_W - 250, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p23_rgb = p23.convert("RGB")
    draw_page_footer(p23_rgb, 23, f"VOLUME {vnum}  •  BÍBLIA DE PERSONAGENS E RECONSTRUÇÃO HISTÓRICA", dark_mode=False)
    pages.append((f"vol{vnum}_p23_biblia_personagens.png", p23_rgb))

    # PÁGINA 24: CONTRACAPA OFICIAL DO VOLUME
    p24 = crop_and_resize(hero_im, PAGE_W, PAGE_H).convert("RGBA")
    p24 = draw_rounded_panel(p24, (110, 110, PAGE_W - 110, PAGE_H - 120), (8, 15, 38, 232), (245, 190, 70, 235), border_width=4, radius=32)
    d24 = ImageDraw.Draw(p24)
    draw_wrapped_text(d24, vol["title"], 150, 165, PAGE_W - 300, f_h1, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, f"Volume {vnum}  •  A Grande História da Luz", 160, 240, PAGE_W - 320, f_italic, fill=(186, 230, 253), align="center")
    d24.line([(320, 300), (PAGE_W - 320, 300)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(d24, vol["back_cover_synopsis"], 165, 340, PAGE_W - 330, f_body, fill=(248, 250, 252), line_spacing=1.38)
    d24.line([(320, 1695), (PAGE_W - 320, 1695)], fill=(245, 190, 70, 180), width=2)
    draw_wrapped_text(d24, f"AUTOR: {AUTHOR_UPPER}", 160, 1725, PAGE_W - 320, f_h2, fill=(253, 224, 71), align="center")
    draw_wrapped_text(d24, f"Edição Autônoma Independente  •  Volume {vnum} (24 Páginas Ilustradas)", 160, 1785, PAGE_W - 320, f_ref, fill=(186, 230, 253), align="center")
    p24_rgb = p24.convert("RGB")
    draw_page_footer(p24_rgb, 24, f"CONTRACAPA OFICIAL  •  VOLUME {vnum}: {vol['title']}", dark_mode=True)
    pages.append((f"vol{vnum}_p24_contracapa.png", p24_rgb))

    saved = []
    for fname, im in pages:
        fp = os.path.join(p_dir, fname)
        im.save(fp, quality=94)
        saved.append(fp)

    shutil.copy2(os.path.join(p_dir, f"vol{vnum}_p01_capa.png"), os.path.join(BRAIN_DIR, f"vol{vnum}_p01_capa.png"))

    # Exportar PDF HD (Hotmart - 200 DPI)
    pdf_hd = os.path.join(BASE_DIR, f"12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol{vnum}_Piloto_HD.pdf")
    pil_ims = [Image.open(p).convert("RGB") for p in saved]
    pil_ims[0].save(pdf_hd, "PDF", resolution=200.0, save_all=True, append_images=pil_ims[1:], title=f"A Grande História da Luz - Vol. {vnum}: {vol['title'].title()}", author=AUTHOR_NAME)

    # Exportar PDF Print 300 DPI com sangria (KDP Print)
    pdf_print = os.path.join(BASE_DIR, f"13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol{vnum}_Print_300DPI_Bleed.pdf")
    print_ims = [crop_and_resize(im, 2438, 3075) for im in pil_ims]
    print_ims[0].save(pdf_print, "PDF", resolution=300.0, save_all=True, append_images=print_ims[1:], title=f"A Grande História da Luz - Vol. {vnum} (Print 300 DPI Bleed)", author=AUTHOR_NAME)

    # Exportar EPUB 3 Fixed-Layout (Amazon KDP)
    epub_path = os.path.join(BASE_DIR, f"11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol{vnum}_FixedLayout_KDP.epub")
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
    <h1>A Grande História da Luz — Volume {vnum} ({AUTHOR_NAME})</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — {vol['title'].title()}</a></li>
      <li><a href="page_02.xhtml">Folha de Rosto e Guia de Leitura</a></li>
      <li><a href="page_03.xhtml">Mapa Histórico e Sumário</a></li>
      <li><a href="page_04.xhtml">Capítulo 1 — {vol['chapters'][0]['title'].title()}</a></li>
      <li><a href="page_07.xhtml">Capítulo 2 — {vol['chapters'][1]['title'].title()}</a></li>
      <li><a href="page_10.xhtml">Capítulo 3 — {vol['chapters'][2]['title'].title()}</a></li>
      <li><a href="page_13.xhtml">Capítulo 4 — {vol['chapters'][3]['title'].title()}</a></li>
      <li><a href="page_16.xhtml">Capítulo 5 — {vol['chapters'][4]['title'].title()}</a></li>
      <li><a href="page_19.xhtml">Capítulo 6 — {vol['chapters'][5]['title'].title()}</a></li>
      <li><a href="page_22.xhtml">Arqueologia e Glossário</a></li>
      <li><a href="page_23.xhtml">Bíblia de Personagens</a></li>
      <li><a href="page_24.xhtml">Contracapa Oficial</a></li>
    </ol>
  </nav>
</body>
</html>'''
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-vol{vnum}-2026</dc:identifier>
    <dc:title>{vol['title'].title()} — {vol['subtitle']} (A Grande História da Luz - Vol. {vnum})</dc:title>
    <dc:language>pt-BR</dc:language>
    <dc:creator>{AUTHOR_NAME}</dc:creator>
    <meta property="dcterms:modified">2026-11-14T10:00:00Z</meta>
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
    print(f"   Volume {vnum} concluído e exportado (EPUB 3 + PDF HD + PDF 300 DPI)!")
    return saved

def build_master_omnibus_240_pages(vol4_10_paths_by_vol):
    print("-> Gerando Edição Integral Unificada (Volumes 1 a 10 — 240 Páginas Ilustradas de Gênesis ao Apocalipse)...")
    v1_dir = os.path.join(BASE_DIR, "09-Diagramacao/paginas_piloto")
    v1_files = [
        "piloto_p01_capa.png", "piloto_p02_apresentacao.png", "piloto_p03_mapa_sumario.png",
        "piloto_p03_abismo.png", "piloto_p04_fiat_lux_esq.png", "piloto_p05_fiat_lux_dir.png",
        "piloto_p06_ceu_mar_terra.png", "piloto_p07_estrelas_aves.png", "piloto_p08_animais_jardim.png",
        "piloto_p09_humanidade_sopro.png", "piloto_p10_nomes_cuidadores.png", "piloto_p11_descanso_luz.png",
        "piloto_p13_cap2_jardim_eden.png", "piloto_p14_cap2_dialogos.png", "piloto_p14_cap3_escolha_jardim.png",
        "piloto_p16_cap3_dialogos.png", "piloto_p15_cap4_caim_abel.png", "piloto_p18_cap4_dialogos.png",
        "piloto_p16_cap5_arca_noe.png", "piloto_p20_cap5_dialogos.png", "piloto_p17_cap6_torre_babel.png",
        "piloto_p22_cap6_dialogos.png", "piloto_p12_descobertas_e_personagens.png", "piloto_p24_contracapa.png"
    ]
    all_240 = [os.path.join(v1_dir, f) for f in v1_files]

    v2_dir = os.path.join(FUT_DIR, "Volume-2-As-Estrelas-da-Promessa/paginas_piloto")
    v2_files = sorted([os.path.join(v2_dir, f) for f in os.listdir(v2_dir) if f.startswith("vol2_p") and f.endswith(".png")])
    all_240.extend(v2_files)

    v3_dir = os.path.join(FUT_DIR, "Volume-3-O-Caminho-da-Liberdade/paginas_piloto")
    v3_order = [
        "vol3_p01_capa.png", "vol3_p02_folha_rosto.png", "vol3_p03_mapa_sumario.png",
        "vol3_p02_cesto_nilo.png", "vol3_p05_cap1_camadas.png", "vol3_p06_cap1_descobertas.png",
        "vol3_p03_sarca_luz.png", "vol3_p08_cap2_camadas.png", "vol3_p09_cap2_descobertas.png",
        "vol3_p04_noite_liberdade.png", "vol3_p11_cap3_camadas.png", "vol3_p12_cap3_descobertas.png",
        "vol3_p05_travessia_mar.png", "vol3_p14_cap4_camadas.png", "vol3_p15_cap4_descobertas.png",
        "vol3_p06_pao_do_ceu_sinai.png", "vol3_p17_cap5_camadas.png", "vol3_p18_cap5_descobertas.png",
        "vol3_p07_terra_prometida.png", "vol3_p20_cap6_camadas.png", "vol3_p21_cap6_descobertas.png",
        "vol3_p22_arqueologia_glossario.png", "vol3_p08_descobertas_e_personagens.png", "vol3_p24_contracapa.png"
    ]
    all_240.extend([os.path.join(v3_dir, f) for f in v3_order])

    for vnum in range(4, 11):
        all_240.extend(vol4_10_paths_by_vol[vnum])

    print(f"   Total de páginas reunidas na Edição Integral: {len(all_240)} páginas.")
    omnibus_pdf = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Colecao_Completa_Vol1_a_10_240Paginas_HD.pdf")
    # Redimensionar imagens para 1200x1500 no PDF unificado de 240 páginas para manter arquivo ágil para download na Hotmart/GitHub (<95MB)
    omni_ims = [Image.open(p).convert("RGB").resize((1200, 1500), Image.Resampling.LANCZOS) for p in all_240]
    omni_ims[0].save(
        omnibus_pdf,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=omni_ims[1:],
        title="A Grande História da Luz — Coleção Completa (Volumes 1 a 10 - 240 Páginas)",
        author=AUTHOR_NAME
    )
    print(f"   PDF Edição Integral (240 páginas) salvo: {omnibus_pdf}")

    omnibus_epub = os.path.join(BASE_DIR, "11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Colecao_Completa_Vol1_a_10_240Paginas_KDP.epub")
    with zipfile.ZipFile(omnibus_epub, "w") as zf:
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
        for idx, p_path in enumerate(all_240, start=1):
            img_name = f"page_{idx:03d}.jpg"
            xhtml_name = f"page_{idx:03d}.xhtml"
            jpg_temp = os.path.join(BASE_DIR, f"09-Diagramacao/_tmp_omni_{idx:03d}.jpg")
            Image.open(p_path).convert("RGB").resize((1200, 1500), Image.Resampling.LANCZOS).save(jpg_temp, "JPEG", quality=86)
            zf.write(jpg_temp, f"OEBPS/images/{img_name}")
            os.remove(jpg_temp)
            prop = ' properties="cover-image"' if idx == 1 else ''
            manifest_items.append(f'    <item id="img{idx:03d}" href="images/{img_name}" media-type="image/jpeg"{prop}/>')
            manifest_items.append(f'    <item id="page{idx:03d}" href="{xhtml_name}" media-type="application/xhtml+xml"/>')
            spread_prop = "page-spread-right" if idx == 1 or idx % 2 == 1 else "page-spread-left"
            spine_items.append(f'    <itemref idref="page{idx:03d}" properties="{spread_prop}"/>')
            xhtml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head>
  <title>Página {idx}</title>
  <meta name="viewport" content="width=1200, height=1500"/>
  <style type="text/css">
    html, body {{ margin: 0; padding: 0; width: 1200px; height: 1500px; overflow: hidden; background-color: #0b132b; }}
    img {{ width: 1200px; height: 1500px; display: block; }}
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
<head><title>Sumário da Coleção Completa</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>A Grande História da Luz — Coleção Completa Vol. 1 a 10 ({AUTHOR_NAME})</h1>
    <ol>
      <li><a href="page_001.xhtml">Volume 1 — Faça-se a Luz (Gênesis 1–11)</a></li>
      <li><a href="page_025.xhtml">Volume 2 — As Estrelas da Promessa (Gênesis 12–50)</a></li>
      <li><a href="page_049.xhtml">Volume 3 — O Caminho da Liberdade (Êxodo a Deuteronômio)</a></li>
      <li><a href="page_073.xhtml">Volume 4 — Coragem para Mudar o Mundo (Josué, Juízes, Rute e Davi)</a></li>
      <li><a href="page_097.xhtml">Volume 5 — Vozes de Sabedoria e Esperança (Salmos, Provérbios e Profetas)</a></li>
      <li><a href="page_121.xhtml">Volume 6 — Uma Luz Nasce no Mundo (A Infância e o Chamado de Jesus)</a></li>
      <li><a href="page_145.xhtml">Volume 7 — As Histórias que Jesus Contou (Parábolas e Sermão do Monte)</a></li>
      <li><a href="page_169.xhtml">Volume 8 — Quando o Amor Faz Milagres (Curas, Encontros e Compaixão)</a></li>
      <li><a href="page_193.xhtml">Volume 9 — O Amor Mais Forte que o Medo (A Cruz, a Páscoa e a Vida Nova)</a></li>
      <li><a href="page_217.xhtml">Volume 10 — A Luz Continua (Atos, Cartas e a Nova Criação)</a></li>
    </ol>
  </nav>
</body>
</html>'''
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-omnibus-vol1-10-2026</dc:identifier>
    <dc:title>A Grande História da Luz — Coleção Completa Ilustrada (Volumes 1 a 10 - 240 Páginas)</dc:title>
    <dc:language>pt-BR</dc:language>
    <dc:creator>{AUTHOR_NAME}</dc:creator>
    <meta property="dcterms:modified">2026-11-14T10:30:00Z</meta>
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:orientation">portrait</meta>
    <meta property="rendition:spread">landscape</meta>
    <meta name="fixed-layout" content="true"/>
    <meta name="original-resolution" content="1200x1500"/>
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
    print(f"   EPUB 3 Edição Integral (240 páginas) salvo: {omnibus_epub}")

if __name__ == "__main__":
    paths_by_vol = {}
    for vol in ALL_VOLS_4_10:
        paths_by_vol[vol["num"]] = build_single_volume(vol)
    build_master_omnibus_240_pages(paths_by_vol)
    print("TODOS OS 10 VOLUMES (240 PÁGINAS) CONCLUÍDOS COM SUCESSO!")
