#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera a pasta `ebook/` (no repositório, em ~/Desktop/ebook e em ~/Downloads/ebook)
usando streams JPEG nativos (/DCTDecode) para que cada volume de 24 páginas tenha
apenas ~1,3 MB a ~1,7 MB, as Partes 1 e 2 (120 páginas) tenham ~6,5 MB, e a
Edição Integral de 240 páginas tenha ~12 MB — abrindo instantaneamente no celular,
no navegador, no GitHub e no Google Drive.
"""

import os
import io
import shutil
import zipfile
from PIL import Image

BASE_DIR = "/home/ubuntu-desktop-bootstrap-ubuntu-/.gemini/antigravity-cli/scratch/A-Grande-Historia-da-Luz"
EBOOK_REPO_DIR = os.path.join(BASE_DIR, "ebook")
EBOOK_DESKTOP_DIR = os.path.expanduser("~/Desktop/ebook")
EBOOK_DOWNLOADS_DIR = os.path.expanduser("~/Downloads/ebook")

for sub in ("Volumes-Individuais-PDF-Leve", "Volumes-Individuais-EPUB-Kindle", "Edicao-Integral-240-Paginas"):
    os.makedirs(os.path.join(EBOOK_REPO_DIR, sub), exist_ok=True)

VOL_SLUGS = {
    1: "Vol01_Faca_se_a_Luz",
    2: "Vol02_As_Estrelas_da_Promessa",
    3: "Vol03_O_Caminho_da_Liberdade",
    4: "Vol04_Coragem_para_Mudar_o_Mundo",
    5: "Vol05_Vozes_de_Sabedoria_e_Esperanca",
    6: "Vol06_Uma_Luz_Nasce_no_Mundo",
    7: "Vol07_As_Historias_que_Jesus_Contou",
    8: "Vol08_Quando_o_Amor_Faz_Milagres",
    9: "Vol09_O_Amor_Mais_Forte_que_o_Medo",
    10: "Vol10_A_Luz_Continua",
}

def extract_24_pages_from_epub(vnum):
    epub_path = os.path.join(BASE_DIR, f"11-Exportacoes-Kindle/A_Grande_Historia_da_Luz_Vol{vnum}_FixedLayout_KDP.epub")
    pil_images = []
    with zipfile.ZipFile(epub_path, "r") as zf:
        img_names = sorted([
            n for n in zf.namelist()
            if n.startswith("OEBPS/images/page_") and (n.endswith(".jpg") or n.endswith(".jpeg") or n.endswith(".png"))
        ])
        assert len(img_names) == 24, f"Volume {vnum} EPUB tem {len(img_names)} imagens em vez de 24"
        for name in img_names:
            data = zf.read(name)
            im = Image.open(io.BytesIO(data)).convert("RGB")
            pil_images.append(im)
    return pil_images

def save_dct_pdf(pil_images, out_pdf, target_w=880, target_h=1100, quality=65):
    """
    Gera um arquivo PDF 1.4 enxuto embutindo cada página diretamente como stream JPEG (/DCTDecode),
    evitando que o Pillow infle as imagens.
    """
    page_w_pt = 576  # 8 inches * 72 pt
    page_h_pt = 720  # 10 inches * 72 pt

    jpeg_streams = []
    for im in pil_images:
        resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format="JPEG", quality=quality, optimize=True, progressive=False)
        resized.close()
        jpeg_streams.append(buf.getvalue())

    n_pages = len(jpeg_streams)
    # Obj 1: Catalog
    # Obj 2: Pages
    # For each page i (0..n-1):
    #   Obj (3 + 3*i): Page
    #   Obj (4 + 3*i): Content stream
    #   Obj (5 + 3*i): Image XObject

    objects = {}
    objects[1] = b"<< /Type /Catalog /Pages 2 0 R >>"

    kids_refs = " ".join([f"{3 + 3*i} 0 R" for i in range(n_pages)])
    objects[2] = f"<< /Type /Pages /Kids [ {kids_refs} ] /Count {n_pages} >>".encode("ascii")

    for i, jpg_bytes in enumerate(jpeg_streams):
        page_obj_id = 3 + 3 * i
        content_obj_id = 4 + 3 * i
        img_obj_id = 5 + 3 * i

        content_bytes = f"q {page_w_pt} 0 0 {page_h_pt} 0 0 cm /Im{i} Do Q".encode("ascii")
        objects[content_obj_id] = (
            f"<< /Length {len(content_bytes)} >>\nstream\n".encode("ascii")
            + content_bytes
            + b"\nendstream"
        )

        objects[img_obj_id] = (
            f"<< /Type /XObject /Subtype /Image /Width {target_w} /Height {target_h} "
            f"/ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(jpg_bytes)} >>\nstream\n".encode("ascii")
            + jpg_bytes
            + b"\nendstream"
        )

        objects[page_obj_id] = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {page_w_pt} {page_h_pt}] "
            f"/Resources << /XObject << /Im{i} {img_obj_id} 0 R >> >> "
            f"/Contents {content_obj_id} 0 R >>".encode("ascii")
        )

    total_objs = 2 + 3 * n_pages
    out = io.BytesIO()
    out.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = {}
    for obj_id in range(1, total_objs + 1):
        offsets[obj_id] = out.tell()
        out.write(f"{obj_id} 0 obj\n".encode("ascii"))
        out.write(objects[obj_id])
        out.write(b"\nendobj\n")

    xref_pos = out.tell()
    out.write(f"xref\n0 {total_objs + 1}\n".encode("ascii"))
    out.write(b"0000000000 65535 f \n")
    for obj_id in range(1, total_objs + 1):
        out.write(f"{offsets[obj_id]:010d} 00000 n \n".encode("ascii"))

    out.write(
        f"trailer\n<< /Size {total_objs + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode("ascii")
    )

    with open(out_pdf, "wb") as f:
        f.write(out.getvalue())

    sz_mb = os.path.getsize(out_pdf) / (1024 * 1024)
    print(f"   [OK] {os.path.basename(out_pdf)} ({sz_mb:.2f} MB)")

def save_light_epub(pil_images, out_epub, title, vol_id, target_w=880, target_h=1100, quality=65):
    with zipfile.ZipFile(out_epub, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""", compress_type=zipfile.ZIP_DEFLATED)

        manifest = []
        spine = []
        for idx, im in enumerate(pil_images, start=1):
            resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            resized.save(buf, format="JPEG", quality=quality, optimize=True)
            resized.close()
            img_name = f"images/page_{idx:03d}.jpg"
            zf.writestr(f"OEBPS/{img_name}", buf.getvalue(), compress_type=zipfile.ZIP_DEFLATED)
            props = ' properties="cover-image"' if idx == 1 else ''
            manifest.append(f'    <item id="img_{idx:03d}" href="{img_name}" media-type="image/jpeg"{props}/>')

            xhtml_name = f"page_{idx:03d}.xhtml"
            xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <title>{title} - Pagina {idx}</title>
  <meta name="viewport" content="width={target_w}, height={target_h}"/>
  <style type="text/css">
    html, body {{ margin:0; padding:0; width:{target_w}px; height:{target_h}px; overflow:hidden; background:#0b132b; }}
    img {{ width:{target_w}px; height:{target_h}px; display:block; }}
  </style>
</head>
<body>
  <img src="{img_name}" alt="Pagina {idx}"/>
</body>
</html>"""
            zf.writestr(f"OEBPS/{xhtml_name}", xhtml, compress_type=zipfile.ZIP_DEFLATED)
            manifest.append(f'    <item id="p_{idx:03d}" href="{xhtml_name}" media-type="application/xhtml+xml"/>')
            spread = ' properties="page-spread-right"' if idx == 1 else (' properties="page-spread-left"' if idx % 2 == 0 else ' properties="page-spread-right"')
            spine.append(f'    <itemref idref="p_{idx:03d}"{spread}/>')

        nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head><meta charset="UTF-8"/><title>Sumario</title></head>
<body><nav epub:type="toc" id="toc"><h1>{title}</h1><ol><li><a href="page_001.xhtml">Capa</a></li></ol></nav></body>
</html>"""
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        manifest.append('    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>')

        opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId" xml:lang="pt-BR" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:a-grande-historia-da-luz-leve-{vol_id}</dc:identifier>
    <dc:title>{title}</dc:title>
    <dc:creator>Fábio Motta e Silva</dc:creator>
    <dc:publisher>Fábio Motta e Silva (Publicação Independente)</dc:publisher>
    <dc:language>pt-BR</dc:language>
    <meta property="dcterms:modified">2026-11-14T12:00:00Z</meta>
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:orientation">auto</meta>
    <meta property="rendition:spread">auto</meta>
    <meta name="cover" content="img_001"/>
  </metadata>
  <manifest>
{chr(10).join(manifest)}
  </manifest>
  <spine>
{chr(10).join(spine)}
  </spine>
</package>"""
        zf.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
    sz_mb = os.path.getsize(out_epub) / (1024 * 1024)
    print(f"   [OK] {os.path.basename(out_epub)} ({sz_mb:.2f} MB)")

if __name__ == "__main__":
    all_pages = []
    ot_pages = []
    nt_pages = []

    print("1. Gerando PDFs e EPUBs Superleves por Volume (24 páginas cada, ~1.4 MB)...")
    for vnum in range(1, 11):
        slug = VOL_SLUGS[vnum]
        pages = extract_24_pages_from_epub(vnum)
        all_pages.extend(pages)
        if vnum <= 5:
            ot_pages.extend(pages)
        else:
            nt_pages.extend(pages)

        pdf_out = os.path.join(EBOOK_REPO_DIR, "Volumes-Individuais-PDF-Leve", f"A_Grande_Historia_da_Luz_{slug}_24p_Leve.pdf")
        epub_out = os.path.join(EBOOK_REPO_DIR, "Volumes-Individuais-EPUB-Kindle", f"A_Grande_Historia_da_Luz_{slug}_24p_Kindle_Leve.epub")
        save_dct_pdf(pages, pdf_out, target_w=880, target_h=1100, quality=65)
        save_light_epub(pages, epub_out, f"A Grande História da Luz - Volume {vnum}", f"vol{vnum}", target_w=880, target_h=1100, quality=65)

    print("2. Gerando Edição Integral Superleve (240 páginas) e Partes 1 e 2 (120 páginas cada)...")
    save_dct_pdf(
        ot_pages,
        os.path.join(EBOOK_REPO_DIR, "Edicao-Integral-240-Paginas", "Parte1_Antigo_Testamento_Vol01_a_05_120Paginas_Leve.pdf"),
        target_w=860, target_h=1075, quality=62
    )
    save_dct_pdf(
        nt_pages,
        os.path.join(EBOOK_REPO_DIR, "Edicao-Integral-240-Paginas", "Parte2_Novo_Testamento_Vol06_a_10_120Paginas_Leve.pdf"),
        target_w=860, target_h=1075, quality=62
    )
    save_dct_pdf(
        all_pages,
        os.path.join(EBOOK_REPO_DIR, "Edicao-Integral-240-Paginas", "Colecao_Completa_Vol01_a_10_240Paginas_Leve.pdf"),
        target_w=800, target_h=1000, quality=58
    )
    save_light_epub(
        all_pages,
        os.path.join(EBOOK_REPO_DIR, "Edicao-Integral-240-Paginas", "Colecao_Completa_Vol01_a_10_240Paginas_Kindle_Leve.epub"),
        "A Grande História da Luz - Coleção Completa (Vol. 1 a 10 - 240 Páginas)",
        "omnibus-240p",
        target_w=800, target_h=1000, quality=58
    )

    for im in all_pages:
        im.close()

    # Sincronizar para ~/Desktop/ebook e ~/Downloads/ebook
    for dst in (EBOOK_DESKTOP_DIR, EBOOK_DOWNLOADS_DIR):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(EBOOK_REPO_DIR, dst)
        print(f"Pasta sincronizada em: {dst}")

    print("CONCLUÍDO COM SUCESSO!")
