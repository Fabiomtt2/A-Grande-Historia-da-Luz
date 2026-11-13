#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e de Ilustração — Volume 3 (eBook 3): O Caminho da Liberdade
Subtítulo: O príncipe do Nilo e a travessia do deserto
Autor: Fabio (Publicação Independente / Autônoma)
Organiza as ilustrações 3D originais em alta definição, gera a Capa Oficial do Volume 3
(seguindo o padrão da Capa 2 Aventura Infantil escolhida por Fabio),
as 8 páginas completas do Volume 3 (Capa, Capítulos 1 a 6 e Página de Descobertas + Bíblia de Personagens),
e exporta PDF HD, PDF de Impressão 300 DPI com sangria e EPUB 3 Fixed-Layout (Amazon KDP).
"""

import os
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
BRAIN_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/brain/026b6e7b-1190-4ec1-b3f4-789abc0233f8"
FONT_DIR = os.path.join(BASE_DIR, "03-Identidade-Visual/fonts")
VOL3_DIR = os.path.join(BASE_DIR, "15-Volumes-Futuros/Volume-3-O-Caminho-da-Liberdade")

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
    p_str = f"PÁGINA {page_num:02d}"
    bbox = draw.textbbox((0, 0), p_str, font=f_foot)
    draw.text((PAGE_W - 90 - (bbox[2] - bbox[0]), PAGE_H - 62), p_str, font=f_foot, fill=color)

def prepare_vol3_assets():
    print("-> Copiando e preparando ilustrações 3D originais do Volume 3...")
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
            print(f"   Ativo copiado: {os.path.basename(dst_path)}")

    # Diagramar a Capa Oficial do Volume 3 (Estilo Capa 2 Aventura Infantil + Autor Fabio)
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
    draw_wrapped_text(cdraw, "FABIO", 240, PAGE_H - 142, PAGE_W - 480, f_author, fill=(255, 255, 255), align="center")
    cov_path = os.path.join(ilus_dir, "vol3_capa_oficial_aventura.png")
    cov_rgba.convert("RGB").save(cov_path, quality=95)
    shutil.copy2(cov_path, os.path.join(BRAIN_DIR, "vol3_capa_oficial_aventura.png"))

def build_vol3_pages_and_exports():
    prepare_vol3_assets()
    f_h2 = load_font("cinzel", 36)
    f_body = load_font("nunito", 33)
    f_box_title = load_font("atkinson_bold", 27)
    f_box_body = load_font("atkinson", 25)
    f_ref = load_font("atkinson_bold", 24)

    pages = []
    ilus_dir = os.path.join(VOL3_DIR, "ilustracoes")
    p_dir = os.path.join(VOL3_DIR, "paginas_piloto")

    # Pág. 1: Capa Oficial Volume 3
    p1 = Image.open(os.path.join(ilus_dir, "vol3_capa_oficial_aventura.png")).convert("RGB")
    pages.append(("vol3_p01_capa.png", p1))

    # Pág. 2: Capítulo 1 — O Pequeno Barco de Papiro no Grande Rio
    p2 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    cesto_im = Image.open(os.path.join(ilus_dir, "vol3_cap1_cesto_nilo.jpg")).convert("RGB")
    p2.paste(crop_and_resize(cesto_im, PAGE_W - 140, 1020), (70, 70))
    d2 = ImageDraw.Draw(p2)
    d2.rectangle([70, 70, PAGE_W - 70, 1090], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d2, "CAPÍTULO 1  •  O PEQUENO BARCO DE PAPIRO NO RIO NILO", 90, 1125, PAGE_W - 180, f_h2, fill=(146, 64, 14))
    draw_wrapped_text(d2, "Base Bíblica: Êxodo 1:8–2:10  |  Autor: Fabio", 90, 1180, PAGE_W - 180, f_ref, fill=(30, 58, 138))
    t2 = (
        "No Egito antigo, às margens do grande rio Nilo, nasceu um bebê que corria perigo por causa de um decreto cruel do Faraó. Sua mãe, Joquebede, colheu hastes de papiro, trançou um cesto bem firme e o calafetou com betume e piche.\n\n"
        "— Fique de olho nele, Miriam — sussurrou a mãe. — A Luz do Criador vai guardar o seu irmãozinho!\n"
        "— Não vou tirar os olhos dele nem por um segundo, mamãe! — prometeu Miriam entre os juncos.\n"
        "Quando a filha do Faraó abriu o cesto, sentiu compaixão do bebê, acolheu-o e deu-lhe o nome de Moisés ('tirado das águas')!"
    )
    draw_wrapped_text(d2, t2, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p2 = draw_rounded_panel(p2, (90, 1755, PAGE_W - 90, 1890), (254, 243, 199, 255), (217, 119, 6, 255), border_width=2, radius=18)
    d2 = ImageDraw.Draw(p2)
    draw_wrapped_text(d2, "» PEQUENA GRANDE DESCOBERTA: No antigo Egito, a planta do papiro servia tanto para fabricar rolos de escrita quanto pequenos barcos impermeabilizados com betume!", 120, 1780, PAGE_W - 240, f_box_body, fill=(146, 64, 14))
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 8, "VOLUME 3  •  CAPÍTULO 1: O CESTO NO NILO", dark_mode=False)
    pages.append(("vol3_p02_cesto_nilo.png", p2_rgb))

    # Pág. 3: Capítulo 2 — O Arbusto que Brilhava Sem Queimar
    p3 = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    sarca_im = Image.open(os.path.join(ilus_dir, "vol3_cap2_sarca_luz.jpg")).convert("RGB")
    p3.paste(crop_and_resize(sarca_im, PAGE_W - 140, 1020), (70, 70))
    d3 = ImageDraw.Draw(p3)
    d3.rectangle([70, 70, PAGE_W - 70, 1090], outline=(245, 190, 70), width=4)
    draw_wrapped_text(d3, "CAPÍTULO 2  •  O ARBUSTO QUE BRILHAVA SEM QUEIMAR", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d3, "Base Bíblica: Êxodo 3:1–4:15 (A Sarça Ardente de Luz)", 90, 1180, PAGE_W - 180, f_ref, fill=(186, 230, 253))
    t3 = (
        "Cuidando de ovelhas no monte Horebe, Moisés viu uma maravilha: um arbusto do deserto brilhava com chamas douradas e azuis da Presença Divina, mas nenhuma folha se queimava!\n\n"
        "— Moisés! Moisés! Tire as sandálias dos pés, porque este lugar é sagrado. Eu vi o sofrimento do meu povo no Egito e estou enviando você para libertá-los!\n"
        "— Mas quem sou eu? — perguntou Moisés, com medo. — Eu tenho dificuldade para falar!\n"
        "— Eu estarei com você! — respondeu a Luz. — E o seu irmão Arão irá ao seu lado para ajudá-lo!"
    )
    draw_wrapped_text(d3, t3, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.35)
    p3 = draw_rounded_panel(p3, (90, 1755, PAGE_W - 90, 1890), (30, 41, 59, 240), (56, 189, 248, 220), border_width=2, radius=18)
    d3 = ImageDraw.Draw(p3)
    draw_wrapped_text(d3, "» O QUE VOCÊ FARIA? Moisés achava que não falava bem, mas descobriu que não estava sozinho. Quem ajuda você quando você sente vergonha ou medo?", 120, 1780, PAGE_W - 240, f_box_body, fill=(253, 224, 71))
    p3_rgb = p3.convert("RGB")
    draw_page_footer(p3_rgb, 18, "VOLUME 3  •  CAPÍTULO 2: A SARÇA DE LUZ", dark_mode=True)
    pages.append(("vol3_p03_sarca_luz.png", p3_rgb))

    # Pág. 4: Capítulo 3 — O Coração Duro como Pedra e a Noite da Liberdade
    p4_cap3 = Image.new("RGBA", (PAGE_W, PAGE_H), (12, 19, 38, 255))
    noite_im = Image.open(os.path.join(ilus_dir, "vol3_cap3_noite_liberdade.jpg")).convert("RGB")
    p4_cap3.paste(crop_and_resize(noite_im, PAGE_W - 140, 1020), (70, 70))
    d4_c3 = ImageDraw.Draw(p4_cap3)
    d4_c3.rectangle([70, 70, PAGE_W - 70, 1090], outline=(245, 190, 70), width=4)
    draw_wrapped_text(d4_c3, "CAPÍTULO 3  •  A NOITE DA ESPERANÇA E DA LIBERDADE", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d4_c3, "Base Bíblica: Êxodo 7–12 (Os Sinais no Egito e a Primeira Páscoa)", 90, 1180, PAGE_W - 180, f_ref, fill=(186, 230, 253))
    t_c3 = (
        "Moisés e Arão pediram muitas vezes ao Faraó que deixasse o povo ir, mas o rei endureceu o coração diante dos grandes sinais na natureza. Até que chegou a noite decisiva da libertação!\n\n"
        "Reunidas em suas casas de tijolos de barro, com as sandálias nos pés e o cajado na mão, as famílias repartiram o pão sem fermento sob o arco luminoso de proteção do Criador. Antes do amanhecer, as portas da liberdade finalmente se abriram!"
    )
    draw_wrapped_text(d4_c3, t_c3, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.35)
    p4_cap3 = draw_rounded_panel(p4_cap3, (90, 1755, PAGE_W - 90, 1890), (30, 41, 59, 240), (245, 190, 70, 220), border_width=2, radius=18)
    d4_c3 = ImageDraw.Draw(p4_cap3)
    draw_wrapped_text(d4_c3, "» PEQUENA GRANDE DESCOBERTA: A palavra 'Páscoa' vem do hebraico 'Pesach' ('passar por cima / proteger') e lembra a noite em que as famílias saíram rumo à liberdade!", 120, 1780, PAGE_W - 240, f_box_body, fill=(254, 240, 138))
    p4_cap3_rgb = p4_cap3.convert("RGB")
    draw_page_footer(p4_cap3_rgb, 28, "VOLUME 3  •  CAPÍTULO 3: A NOITE DA LIBERDADE", dark_mode=True)
    pages.append(("vol3_p04_noite_liberdade.png", p4_cap3_rgb))

    # Pág. 5: Capítulo 4 — Quando o Vento Abriu um Caminho no Mar
    p5 = Image.new("RGBA", (PAGE_W, PAGE_H), (10, 18, 42, 255))
    mar_im = Image.open(os.path.join(ilus_dir, "vol3_cap4_travessia_mar.jpg")).convert("RGB")
    p5.paste(crop_and_resize(mar_im, PAGE_W - 140, 1020), (70, 70))
    d5 = ImageDraw.Draw(p5)
    d5.rectangle([70, 70, PAGE_W - 70, 1090], outline=(56, 189, 248), width=4)
    draw_wrapped_text(d5, "CAPÍTULO 4  •  UM CAMINHO NO MEIO DO MAR", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d5, "Base Bíblica: Êxodo 14:13–31; 15:20–21 (A Travessia e a Canção de Miriam)", 90, 1180, PAGE_W - 180, f_ref, fill=(125, 211, 252))
    t4 = (
        "Diante das águas profundas do mar, o povo sentiu medo ao ouvir os carros do Faraó se aproximando. Mas Moisés disse com firmeza:\n"
        "— Não tenham medo! Fiquem firmes e vejam o livramento que o Senhor fará hoje!\n\n"
        "Guiado pela Coluna de Luz, um vento fortíssimo soprou a noite inteira, abrindo duas muralhas de água cristalina e revelando um caminho seco no meio do mar! Na outra margem, Miriam pegou seu tamborim e liderou a dança da liberdade."
    )
    draw_wrapped_text(d5, t4, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.35)
    p5 = draw_rounded_panel(p5, (90, 1755, PAGE_W - 90, 1890), (20, 45, 76, 240), (245, 190, 70, 220), border_width=2, radius=18)
    d5 = ImageDraw.Draw(p5)
    draw_wrapped_text(d5, "» CONVERSE COMIGO: Qual música ou canção deixa a sua família mais alegre quando vocês vencem um dia difícil?", 120, 1785, PAGE_W - 240, f_box_body, fill=(254, 240, 138))
    p5_rgb = p5.convert("RGB")
    draw_page_footer(p5_rgb, 38, "VOLUME 3  •  CAPÍTULO 4: A TRAVESSIA DO MAR", dark_mode=True)
    pages.append(("vol3_p05_travessia_mar.png", p5_rgb))

    # Pág. 6: Capítulo 5 — O Pão do Céu, a Água da Rocha e a Montanha da Luz
    p6 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    sinai_im = Image.open(os.path.join(ilus_dir, "vol3_cap5_pao_do_ceu_sinai.jpg")).convert("RGB")
    p6.paste(crop_and_resize(sinai_im, PAGE_W - 140, 1020), (70, 70))
    d6 = ImageDraw.Draw(p6)
    d6.rectangle([70, 70, PAGE_W - 70, 1090], outline=(180, 83, 9), width=4)
    draw_wrapped_text(d6, "CAPÍTULO 5  •  O PÃO DO CÉU E A MONTANHA DA LUZ", 90, 1125, PAGE_W - 180, f_h2, fill=(146, 64, 14))
    draw_wrapped_text(d6, "Base Bíblica: Êxodo 16–20 (O Maná, a Água da Rocha e as Dez Palavras no Sinai)", 90, 1180, PAGE_W - 180, f_ref, fill=(30, 58, 138))
    t6 = (
        "No deserto, a Presença Divina nunca deixou faltar cuidado: a cada manhã, o chão amanhecia coberto pelo maná — floquinhos brancos doces como mel — e da rocha seca brotou água fresca para matar a sede das crianças e dos rebanhos!\n\n"
        "Ao pé do monte Sinai coroado de luz dourada e safira, o povo recebeu as Dez Palavras da Vida: leis de amor para honrar a Deus, respeitar os pais, dizer a verdade e proteger o próximo."
    )
    draw_wrapped_text(d6, t6, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p6 = draw_rounded_panel(p6, (90, 1755, PAGE_W - 90, 1890), (254, 243, 199, 255), (217, 119, 6, 255), border_width=2, radius=18)
    d6 = ImageDraw.Draw(p6)
    draw_wrapped_text(d6, "» VOCÊ PERCEBEU? As Dez Palavras de Êxodo 20 não foram dadas para prender o povo, mas para ensinar um povo recém-liberto a viver em paz e justiça!", 120, 1780, PAGE_W - 240, f_box_body, fill=(146, 64, 14))
    p6_rgb = p6.convert("RGB")
    draw_page_footer(p6_rgb, 48, "VOLUME 3  •  CAPÍTULO 5: O PÃO DO CÉU E O SINAI", dark_mode=False)
    pages.append(("vol3_p06_pao_do_ceu_sinai.png", p6_rgb))

    # Pág. 7: Capítulo 6 — O Horizonte da Terra Prometida
    p7 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    nebo_im = Image.open(os.path.join(ilus_dir, "vol3_cap6_terra_prometida.jpg")).convert("RGB")
    p7.paste(crop_and_resize(nebo_im, PAGE_W - 140, 1020), (70, 70))
    d7 = ImageDraw.Draw(p7)
    d7.rectangle([70, 70, PAGE_W - 70, 1090], outline=(101, 163, 13), width=4)
    draw_wrapped_text(d7, "CAPÍTULO 6  •  O HORIZONTE DA TERRA PROMETIDA", 90, 1125, PAGE_W - 180, f_h2, fill=(63, 98, 18))
    draw_wrapped_text(d7, "Base Bíblica: Números 13–14; Deuteronômio 31 e 34 (Moisés e Josué no Monte Nebo)", 90, 1180, PAGE_W - 180, f_ref, fill=(180, 83, 9))
    t7 = (
        "Depois de quarenta anos de aprendizado pelo deserto, Moisés subiu ao topo do monte Nebo ao lado do jovem Josué. Lá de cima, sob um arco luminoso de esperança, contemplou o vale do rio Jordão e os olivais verdejantes da Terra Prometida.\n\n"
        "— Seja forte e corajoso, Josué! — abençoou Moisés com o coração em paz. — A Luz do Senhor irá adiante de vocês, e Ele jamais os deixará!"
    )
    draw_wrapped_text(d7, t7, 90, 1235, PAGE_W - 180, f_body, fill=(41, 37, 36), line_spacing=1.35)
    p7 = draw_rounded_panel(p7, (90, 1755, PAGE_W - 90, 1890), (236, 252, 203, 255), (101, 163, 13, 255), border_width=2, radius=18)
    d7 = ImageDraw.Draw(p7)
    draw_wrapped_text(d7, "» O QUE VOCÊ FARIA? Moisés passou a missão adiante encorajando Josué. Como você pode encorajar um amigo que está começando um novo desafio?", 120, 1780, PAGE_W - 240, f_box_body, fill=(54, 83, 20))
    p7_rgb = p7.convert("RGB")
    draw_page_footer(p7_rgb, 58, "VOLUME 3  •  CAPÍTULO 6: O HORIZONTE DA PROMESSA", dark_mode=False)
    pages.append(("vol3_p07_terra_prometida.png", p7_rgb))

    # Pág. 8: Pequena Grande Descoberta + Bíblia de Personagens do Volume 3 (Moisés e Miriam)
    p8 = Image.new("RGBA", (PAGE_W, PAGE_H), (253, 251, 247, 255))
    d8 = ImageDraw.Draw(p8)
    draw_wrapped_text(d8, "PEQUENA GRANDE DESCOBERTA  •  VOLUME 3", 90, 75, PAGE_W - 180, f_h2, fill=(146, 64, 14), align="center")
    p8 = draw_rounded_panel(p8, (80, 150, PAGE_W - 80, 620), (254, 243, 199, 255), (217, 119, 6, 255), border_width=3, radius=22)
    d8 = ImageDraw.Draw(p8)
    draw_wrapped_text(d8, "1. ARQUEOLOGIA DO EGITO E DO DESERTO DO SINAI", 120, 178, PAGE_W - 240, f_box_title, fill=(146, 64, 14))
    arq_txt = (
        "• Tijolos de Barro e Palha: Escavações arqueológicas no Delta do Nilo (como em Pi-Ramessés) mostram que os antigos armazéns egípcios eram erguidos com milhões de tijolos de lama do Nilo misturada com palha picada e secos ao sol, exatamente como descreve Êxodo 5!\n"
        "• O Tamborim de Miriam (Tof): Na antiguidade do Oriente Próximo, o 'tof' era um instrumento circular de madeira esticado com pele de animal, tocado pelas mulheres em celebrações de vitória e gratidão.\n"
        "• O Tabernáculo Portátil: A tenda sagrada do deserto usava madeira de acácia (árvore típica do Sinai), linho trançado e cobres polidos."
    )
    draw_wrapped_text(d8, arq_txt, 120, 232, PAGE_W - 240, f_box_body, fill=(41, 37, 36), line_spacing=1.38)

    draw_wrapped_text(d8, "2. BÍBLIA DE PERSONAGENS DO VOLUME 3: MIRIAM E MOISÉS", 90, 660, PAGE_W - 180, f_box_title, fill=(30, 58, 138))
    sheet_mm = Image.open(os.path.join(BASE_DIR, "04-Biblia-de-Personagens/char_sheet_moises_miriam.jpg")).convert("RGB").resize((1360, 765), Image.Resampling.LANCZOS)
    p8.paste(sheet_mm, (120, 715))
    d8.rectangle([120, 715, 1480, 1480], outline=(180, 83, 9), width=3)
    leg_mm = (
        "Reconstrução Histórica Levantina (Volume 3 — Autor: Fabio): À esquerda, a jovem Miriam com túnica de linho cru bordada em azul-turquesa egípcio e seu tamborim de madeira (tof). À direita, Moisés no monte Horebe/Sinai, com pele morena-oliva marcada pelo sol do deserto, túnica de lã tecida, manto terracota, sandálias de couro e cajado de pastor em madeira de acácia."
    )
    draw_wrapped_text(d8, leg_mm, 120, 1510, PAGE_W - 240, f_box_body, fill=(28, 25, 23), line_spacing=1.38)
    p8_rgb = p8.convert("RGB")
    draw_page_footer(p8_rgb, 64, "VOLUME 3  •  ARQUEOLOGIA E BÍBLIA DE PERSONAGENS", dark_mode=False)
    pages.append(("vol3_p08_descobertas_e_personagens.png", p8_rgb))

    saved = []
    for fname, im in pages:
        fp = os.path.join(p_dir, fname)
        im.save(fp, quality=95)
        saved.append(fp)
        shutil.copy2(fp, os.path.join(BRAIN_DIR, fname))
        print(f"   Página Volume 3 salva: {fname}")

    # Manter compatibilidade com o nome vol3_p04_travessia_mar.png caso referenciado
    shutil.copy2(os.path.join(p_dir, "vol3_p05_travessia_mar.png"), os.path.join(p_dir, "vol3_p04_travessia_mar.png"))
    shutil.copy2(os.path.join(p_dir, "vol3_p05_travessia_mar.png"), os.path.join(BRAIN_DIR, "vol3_p04_travessia_mar.png"))

    # 1. Exportar PDF HD do Volume 3 (Hotmart / Tablet)
    pdf_v3 = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol3_Piloto_HD.pdf")
    pil_ims = [Image.open(p).convert("RGB") for p in saved]
    pil_ims[0].save(pdf_v3, "PDF", resolution=200.0, save_all=True, append_images=pil_ims[1:], title="A Grande História da Luz - Vol. 3: O Caminho da Liberdade", author="Fabio")
    print(f"   Volume 3 PDF HD gerado: {pdf_v3}")

    # 2. Exportar PDF de Impressão 300 DPI com sangria do Volume 3
    print_pdf_v3 = os.path.join(BASE_DIR, "13-Edicao-Impressa/A_Grande_Historia_da_Luz_Vol3_Print_300DPI_Bleed.pdf")
    print_ims = [crop_and_resize(im, 2438, 3075) for im in pil_ims]
    print_ims[0].save(print_pdf_v3, "PDF", resolution=300.0, save_all=True, append_images=print_ims[1:], title="A Grande História da Luz - Vol. 3 (Print 300 DPI Bleed)", author="Fabio")
    print(f"   Volume 3 PDF Print 300 DPI gerado: {print_pdf_v3}")

    # 3. Exportar EPUB 3 Fixed-Layout (Amazon KDP) do Volume 3
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

        nav_xhtml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head><title>Sumário</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>A Grande História da Luz — Volume 3: O Caminho da Liberdade</h1>
    <ol>
      <li><a href="page_01.xhtml">Capa — O Caminho da Liberdade</a></li>
      <li><a href="page_02.xhtml">Capítulo 1 — O Pequeno Barco de Papiro no Nilo</a></li>
      <li><a href="page_03.xhtml">Capítulo 2 — O Arbusto que Brilhava Sem Queimar</a></li>
      <li><a href="page_04.xhtml">Capítulo 3 — A Noite da Esperança e da Liberdade</a></li>
      <li><a href="page_05.xhtml">Capítulo 4 — Um Caminho no Meio do Mar</a></li>
      <li><a href="page_06.xhtml">Capítulo 5 — O Pão do Céu e a Montanha da Luz</a></li>
      <li><a href="page_07.xhtml">Capítulo 6 — O Horizonte da Terra Prometida</a></li>
      <li><a href="page_08.xhtml">Arqueologia e Bíblia de Personagens (Miriam e Moisés)</a></li>
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
    <dc:creator>Fabio</dc:creator>
    <meta property="dcterms:modified">2026-11-13T16:45:00Z</meta>
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
    print(f"   Volume 3 EPUB 3 Fixed-Layout KDP gerado: {epub_v3}")

if __name__ == "__main__":
    build_vol3_pages_and_exports()
    print("VOLUME 3 CONCLUÍDO COM SUCESSO!")
