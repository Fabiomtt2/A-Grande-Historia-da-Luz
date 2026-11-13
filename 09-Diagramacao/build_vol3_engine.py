#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor Editorial e de Ilustração — Volume 3 (eBook 3): O Caminho da Liberdade
Subtítulo: O príncipe do Nilo e a travessia do deserto
Autor: Fabio (Publicação Independente / Autônoma)
Gera as ilustrações em alta definição, a Capa Oficial do Volume 3 (seguindo o padrão da Capa 2 Aventura Infantil escolhida por Fabio),
as 8 páginas do Piloto Ilustrado do Volume 3, o PDF HD e o EPUB 3 Fixed-Layout.
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

def render_vol3_illustrations():
    os.makedirs(os.path.join(VOL3_DIR, "ilustracoes"), exist_ok=True)
    os.makedirs(os.path.join(VOL3_DIR, "paginas_piloto"), exist_ok=True)

    aventura_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_2_aventura_base.jpg")).convert("RGB")
    cosmica_base = Image.open(os.path.join(BASE_DIR, "03-Identidade-Visual/capa_conceito_1_cosmica_base.jpg")).convert("RGB")
    abismo_base = Image.open(os.path.join(BASE_DIR, "08-Ilustracoes-Originais/vol1_cap1_cena1_misterio_abismo.jpg")).convert("RGB")

    # 1. Capa Volume 3 (Estilo Capa 2 Aventura Infantil — Crianças levantinas sob o arco de luz e águas abertas)
    cov_base = crop_and_resize(aventura_base, PAGE_W, PAGE_H)
    # Ajuste de atmosfera quente dourada do Egito/Sinai
    cov_base = ImageEnhance.Color(cov_base).enhance(1.12)
    cov_rgba = cov_base.convert("RGBA")
    grad = Image.new("RGBA", (PAGE_W, PAGE_H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grad)
    for y in range(540):
        alpha = int(195 * (1 - y / 540.0) ** 1.35)
        gdraw.line([(0, y), (PAGE_W, y)], fill=(12, 24, 52, alpha))
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
    cov_path = os.path.join(VOL3_DIR, "ilustracoes/vol3_capa_oficial_aventura.png")
    cov_rgba.convert("RGB").save(cov_path, quality=95)
    shutil.copy2(cov_path, os.path.join(BRAIN_DIR, "vol3_capa_oficial_aventura.png"))

    # 2. Ilustração Cap. 1: O Pequeno Barco de Papiro no Rio Nilo (1600x1200)
    nilo = Image.new("RGBA", (1600, 1200), (12, 28, 58, 255))
    # Fundo de alvorada dourada sobre as águas do Nilo
    n_bg = crop_and_resize(cosmica_base.crop((0, int(cosmica_base.height * 0.45), cosmica_base.width, cosmica_base.height)), 1600, 1200)
    nilo.paste(n_bg, (0, 0))
    ndraw = ImageDraw.Draw(nilo)
    # Desenhar silhuetas ricas de juncos de papiro às margens e o cesto iluminado pela fita dourada
    random.seed(101)
    for x in list(range(30, 420, 22)) + list(range(1180, 1570, 22)):
        h_reed = random.randint(380, 720)
        lean = random.randint(-35, 35)
        ndraw.line([(x, 1200), (x + lean, 1200 - h_reed)], fill=(20, 83, 45, 230), width=7)
        # Coroa de papiro no topo
        tx, ty = x + lean, 1200 - h_reed
        for a in range(-40, 45, 16):
            rad = math.radians(a - 90)
            ndraw.line([(tx, ty), (tx + int(math.cos(rad)*55), ty + int(math.sin(rad)*55))], fill=(34, 139, 74, 210), width=3)
    # Cesto de papiro flutuando no centro com halo de luz protetora (Fiat Lux)
    glow = Image.new("RGBA", (1600, 1200), (0, 0, 0, 0))
    gld = ImageDraw.Draw(glow)
    for r in range(260, 10, -10):
        gld.ellipse([800 - r, 860 - int(r*0.6), 800 + r, 860 + int(r*0.6)], fill=(255, 215, 90, int(85 * (1 - r/260.0)**2)))
    gld.rounded_rectangle([690, 810, 910, 915], radius=45, fill=(146, 64, 14, 255), outline=(253, 224, 71, 255), width=4)
    gld.arc([700, 735, 830, 880], start=180, end=360, fill=(180, 83, 9, 255), width=14)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=2))
    nilo = Image.alpha_composite(nilo, glow)
    nilo.convert("RGB").save(os.path.join(VOL3_DIR, "ilustracoes/vol3_cap1_cesto_nilo.png"), quality=95)

    # 3. Ilustração Cap. 2: A Sarça que Brilhava Sem Queimar (1600x1200)
    sarca = crop_and_resize(abismo_base, 1600, 1200).convert("RGBA")
    s_ov = Image.new("RGBA", (1600, 1200), (0, 0, 0, 0))
    sd = ImageDraw.Draw(s_ov)
    # Colina rochosa do Horebe
    sd.polygon([(0, 1200), (0, 920), (450, 780), (950, 740), (1600, 890), (1600, 1200)], fill=(45, 30, 22, 245))
    # Explosão de luz dourada e safira na sarça (sem queimar os ramos verdes-esmeralda)
    bx, by = 800, 560
    for r in range(420, 15, -12):
        col = (255, 210, 75, int(110 * (1 - r/420.0)**2)) if r % 24 == 0 else (56, 189, 248, int(75 * (1 - r/420.0)**2))
        sd.ellipse([bx - r, by - r, bx + r, by + r], fill=col)
    s_ov = s_ov.filter(ImageFilter.GaussianBlur(radius=10))
    sarca = Image.alpha_composite(sarca, s_ov)
    sd2 = ImageDraw.Draw(sarca)
    # Galhos vivos da acácia/sarça brilhando no centro da luz
    random.seed(202)
    for i in range(-5, 6):
        angle = math.radians(-90 + i * 14)
        ex = bx + int(math.cos(angle) * 230)
        ey = by + int(math.sin(angle) * 230)
        sd2.line([(bx, by + 180), (ex, ey)], fill=(254, 240, 138, 240), width=6)
        sd2.ellipse([ex - 14, ey - 14, ex + 14, ey + 14], fill=(16, 185, 129, 255), outline=(253, 224, 71, 255), width=2)
    sarca.convert("RGB").save(os.path.join(VOL3_DIR, "ilustracoes/vol3_cap2_sarca_luz.png"), quality=95)

    # 4. Ilustração Cap. 4: A Travessia do Mar Aberto pelo Vento e pela Coluna de Luz (1600x1200)
    mar = Image.new("RGBA", (1600, 1200), (10, 20, 48, 255))
    m_bg = crop_and_resize(cosmica_base, 1600, 1200)
    mar.paste(m_bg, (0, 0))
    m_ov = Image.new("RGBA", (1600, 1200), (0, 0, 0, 0))
    md = ImageDraw.Draw(m_ov)
    # Duas muralhas monumentais de água azul-turquesa nas laterais e caminho seco dourado no centro
    md.polygon([(0, 220), (580, 460), (460, 1200), (0, 1200)], fill=(14, 116, 144, 215))
    md.polygon([(1600, 220), (1020, 460), (1140, 1200), (1600, 1200)], fill=(14, 116, 144, 215))
    md.polygon([(460, 1200), (580, 460), (1020, 460), (1140, 1200)], fill=(217, 160, 91, 235))
    # Coluna de Luz Dourada no horizonte guiando o caminho
    for r in range(180, 10, -10):
        md.rectangle([800 - r, 40, 800 + r, 520], fill=(255, 230, 130, int(90 * (1 - r/180.0)**2)))
    m_ov = m_ov.filter(ImageFilter.GaussianBlur(radius=12))
    mar = Image.alpha_composite(mar, m_ov)
    mar.convert("RGB").save(os.path.join(VOL3_DIR, "ilustracoes/vol3_cap4_travessia_mar.png"), quality=95)

def build_vol3_pilot():
    render_vol3_illustrations()
    f_h1 = load_font("cinzel", 50)
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
    cesto_im = Image.open(os.path.join(ilus_dir, "vol3_cap1_cesto_nilo.png")).convert("RGB")
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
    draw_wrapped_text(d2, "★ PEQUENA GRANDE DESCOBERTA: No antigo Egito, a planta do papiro servia tanto para fabricar rolos de escrita quanto pequenos barcos impermeabilizados com betume!", 120, 1780, PAGE_W - 240, f_box_body, fill=(146, 64, 14))
    p2_rgb = p2.convert("RGB")
    draw_page_footer(p2_rgb, 8, "VOLUME 3  •  CAPÍTULO 1: O CESTO NO NILO", dark_mode=False)
    pages.append(("vol3_p02_cesto_nilo.png", p2_rgb))

    # Pág. 3: Capítulo 2 — O Arbusto que Brilhava Sem Queimar
    p3 = Image.new("RGBA", (PAGE_W, PAGE_H), (15, 23, 42, 255))
    sarca_im = Image.open(os.path.join(ilus_dir, "vol3_cap2_sarca_luz.png")).convert("RGB")
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

    # Pág. 4: Capítulo 4 — Quando o Vento Abriu um Caminho no Mar
    p4 = Image.new("RGBA", (PAGE_W, PAGE_H), (10, 18, 42, 255))
    mar_im = Image.open(os.path.join(ilus_dir, "vol3_cap4_travessia_mar.png")).convert("RGB")
    p4.paste(crop_and_resize(mar_im, PAGE_W - 140, 1020), (70, 70))
    d4 = ImageDraw.Draw(p4)
    d4.rectangle([70, 70, PAGE_W - 70, 1090], outline=(56, 189, 248), width=4)
    draw_wrapped_text(d4, "CAPÍTULO 4  •  UM CAMINHO NO MEIO DO MAR", 90, 1125, PAGE_W - 180, f_h2, fill=(253, 224, 71))
    draw_wrapped_text(d4, "Base Bíblica: Êxodo 14:13–31; 15:20–21 (A Travessia e a Canção de Miriam)", 90, 1180, PAGE_W - 180, f_ref, fill=(125, 211, 252))
    t4 = (
        "Diante das águas profundas do mar, o povo sentiu medo ao ouvir os carros do Faraó se aproximando. Mas Moisés disse com firmeza:\n"
        "— Não tenham medo! Fiquem firmes e vejam o livramento que o Senhor fará hoje!\n\n"
        "Guiado pela Coluna de Luz, um vento fortíssimo soprou a noite inteira, abrindo duas muralhas de água cristalina e revelando um caminho seco no meio do mar! Na outra margem, Miriam pegou seu tamborim e liderou a dança da liberdade."
    )
    draw_wrapped_text(d4, t4, 90, 1235, PAGE_W - 180, f_body, fill=(248, 250, 252), line_spacing=1.35)
    p4 = draw_rounded_panel(p4, (90, 1755, PAGE_W - 90, 1890), (20, 45, 76, 240), (245, 190, 70, 220), border_width=2, radius=18)
    d4 = ImageDraw.Draw(p4)
    draw_wrapped_text(d4, "★ CONVERSE COMIGO: Qual música ou canção deixa a sua família mais alegre quando vocês vencem um dia difícil?", 120, 1785, PAGE_W - 240, f_box_body, fill=(254, 240, 138))
    p4_rgb = p4.convert("RGB")
    draw_page_footer(p4_rgb, 36, "VOLUME 3  •  CAPÍTULO 4: A TRAVESSIA DO MAR", dark_mode=True)
    pages.append(("vol3_p04_travessia_mar.png", p4_rgb))

    saved = []
    for fname, im in pages:
        fp = os.path.join(p_dir, fname)
        im.save(fp, quality=95)
        saved.append(fp)
        shutil.copy2(fp, os.path.join(BRAIN_DIR, fname))

    # Exportar PDF HD do Piloto do Volume 3
    pdf_v3 = os.path.join(BASE_DIR, "12-Exportacoes-Hotmart/A_Grande_Historia_da_Luz_Vol3_Piloto_HD.pdf")
    pil_ims = [Image.open(p).convert("RGB") for p in saved]
    pil_ims[0].save(pdf_v3, "PDF", resolution=200.0, save_all=True, append_images=pil_ims[1:], title="A Grande História da Luz - Vol. 3: O Caminho da Liberdade", author="Fabio")
    print(f"   Volume 3 Piloto PDF gerado: {pdf_v3}")

if __name__ == "__main__":
    build_vol3_pilot()
    print("VOLUME 3 CONCLUÍDO COM SUCESSO!")
