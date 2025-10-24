import os
import re
import base64
from pathlib import Path

def safe_write_bytes(path, data_bytes):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data_bytes)

def extract_images_from_md(md_path, images_dir):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    os.makedirs(images_dir, exist_ok=True)

    # Pattern robuste :
    # - capture [refname]: optional < then data:image/type;base64, then base64 (allows newlines/spaces)
    # - accepte png|jpg|jpeg|gif
    pattern = re.compile(
        r'^\s*\[(?P<ref>[^\]]+)\]:\s*<?\s*data:image/(?P<type>png|jpg|jpeg|gif);base64,(?P<b64>[A-Za-z0-9+/=\s]+?)>?\s*$',
        re.MULTILINE | re.IGNORECASE
    )

    matches = list(pattern.finditer(content))
    if not matches:
        print(f"✅ Aucun base64 trouvé dans {md_path}")
        return

    for m in matches:
        ref_name = m.group("ref").strip()
        img_type = m.group("type").lower()
        if img_type == "jpeg":
            img_type = "jpg"
        b64_text = m.group("b64")
        # cleanup whitespace/newlines in base64
        b64_clean = re.sub(r'\s+', '', b64_text)

        # compose unique filename: prefix with md base name to avoid collisions
        base_md = Path(md_path).stem
        img_filename = f"{base_md}__{ref_name}.{img_type}"
        img_path = os.path.join(images_dir, img_filename)

        # write file if not exists
        if not os.path.exists(img_path):
            try:
                img_bytes = base64.b64decode(b64_clean, validate=True)
            except Exception as e:
                # si validate échoue, essayer sans validation
                img_bytes = base64.b64decode(b64_clean)
            safe_write_bytes(img_path, img_bytes)
            print(f"📦 Image extraite : {img_path}")
        else:
            print(f"⚠️ Image déjà existante, ignorée : {img_path}")

        # replacement: remplacer toutes les occurrences ![][ref_name] et ![alt][ref_name]
        rel_path = os.path.relpath(img_path, Path(md_path).parent).replace(os.sep, "/")
        # 1) ![][ref]
        content = re.sub(r'!\[\]\[' + re.escape(ref_name) + r'\]', f'![]({rel_path})', content)
        # 2) ![alt text][ref]
        content = re.sub(r'!\[([^\]]*)\]\[' + re.escape(ref_name) + r'\]', r'![\1](' + rel_path + r')', content)

        # remove the reference line (the base64 line)
        content = content[:m.start()] + content[m.end():]

    # write updated markdown back
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✏️ Markdown mis à jour : {md_path}\n")

def main():
    blocks = ["Bloc1", "Bloc2"]
    root = Path.cwd()
    for block in blocks:
        block_path = root / block
        if not block_path.exists() or not block_path.is_dir():
            print(f"ℹ️ Dossier absent : {block} (ignoré)")
            continue
        images_dir = block_path / "images"
        md_files = [p for p in block_path.iterdir() if p.suffix.lower() == ".md"]
        for md_file in md_files:
            extract_images_from_md(str(md_file), str(images_dir))

if __name__ == "__main__":
    main()
