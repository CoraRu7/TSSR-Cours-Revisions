#!/usr/bin/env python3
import re
from pathlib import Path
import base64

ROOT = Path.cwd()
BLOCKS = ["Bloc1", "Bloc2"]

def extract_images_from_dot_block(md_text, md_path, images_dir):
    """
    Cherche le bloc <details><summary>.</summary>...</details>
    et extrait toutes les définitions [imageX]: data:image/... 
    Retourne un dict {ref: nom_fichier_extrait}
    """
    image_map = {}
    # chercher le bloc avec summary "."
    dot_block_pattern = re.compile(r"<details>\s*<summary>\s*\.\s*</summary>(.*?)</details>", re.DOTALL | re.IGNORECASE)
    dot_blocks = dot_block_pattern.findall(md_text)
    if not dot_blocks:
        return image_map

    content = dot_blocks[-1]  # on prend le dernier bloc ".", qui contient toutes les images

    # regex pour [imageX]: data:image/png;base64,...
    ref_pattern = re.compile(r"^\s*\[([^\]]+)\]:\s*<data:image/[^;]+;base64,([^>]+)>", re.MULTILINE)
    counter = 1
    for match in ref_pattern.finditer(content):
        ref, b64data = match.group(1), match.group(2)
        # nettoyer b64data
        b64data = b64data.replace("\n", "").replace(" ", "")
        # nom fichier
        suffix = ".png"  # par défaut png
        filename = f"{md_path.stem}__image{counter}{suffix}"
        file_path = images_dir / filename
        if not images_dir.exists():
            images_dir.mkdir(parents=True, exist_ok=True)
        if file_path.exists():
            print(f"⚠️ Image déjà existante : {file_path}")
        else:
            try:
                file_path.write_bytes(base64.b64decode(b64data))
                print(f"📦 Image extraite : {file_path}")
            except Exception as e:
                print(f"❌ Échec extraction pour ref '{ref}' : {e}")
                continue
        image_map[ref] = filename
        counter += 1
    return image_map

def replace_links(md_text, image_map):
    """
    Remplace ![][ref] et ![alt][ref] par ![](chemin/vers/fichier)
    """
    # ![alt][ref]
    pattern2 = re.compile(r'!\[([^\]]*)\]\[([^\]]+)\]')
    for m in list(pattern2.finditer(md_text)):
        alt, ref = m.group(1), m.group(2)
        if ref in image_map:
            replacement = f"![{alt}]({image_map[ref]})"
            md_text = md_text[:m.start()] + replacement + md_text[m.end():]

    # ![][ref]
    pattern1 = re.compile(r'!\[\]\[([^\]]+)\]')
    for m in list(pattern1.finditer(md_text)):
        ref = m.group(1)
        if ref in image_map:
            replacement = f"![]({image_map[ref]})"
            md_text = md_text[:m.start()] + replacement + md_text[m.end():]

    return md_text

def process_md_file(md_path):
    print(f"\n🔹 Traitement : {md_path}")
    md_text = md_path.read_text(encoding="utf-8")
    # déterminer le dossier images
    block = md_path.parent.name
    images_dir = md_path.parent / "images"
    image_map = extract_images_from_dot_block(md_text, md_path, images_dir)
    if image_map:
        md_text = replace_links(md_text, image_map)
        md_path.write_text(md_text, encoding="utf-8")
        print(f"✏️ Mis à jour liens images dans {md_path}")
    else:
        print("✅ Aucun base64 trouvé dans ce fichier")

def main():
    for block in BLOCKS:
        block_path = ROOT / block
        if not block_path.exists():
            continue
        for md_file in sorted(block_path.glob("*.md")):
            process_md_file(md_file)

if __name__ == "__main__":
    main()
