import os
import re
import base64
from pathlib import Path
import sys

def safe_write_bytes(path, data_bytes):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(data_bytes)

def sanitize_ref(ref):
    # conserve lettres, chiffres, _, - ; remplace autres par _
    cleaned = re.sub(r'[^A-Za-z0-9_-]', '_', ref)
    # tronque si trop long
    if len(cleaned) > 40:
        cleaned = cleaned[:40]
    # si vide, renvoyer None pour indiquer fallback
    if cleaned.strip('_') == '':
        return None
    return cleaned

def extract_images_from_md(md_path, images_dir):
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Impossible de lire {md_path}: {e}")
        return

    os.makedirs(images_dir, exist_ok=True)

    # Pattern tolérant : capture [ref]: optional < then data:image/type;base64, then base64 (multiligne possible)
    pattern = re.compile(
        r'^\s*\[(?P<ref>[^\]]+)\]:\s*<?\s*data:image/(?P<type>png|jpg|jpeg|gif);base64,(?P<b64>[A-Za-z0-9+/=\s\r\n\t]+?)>?\s*$',
        re.MULTILINE | re.IGNORECASE
    )

    matches = list(pattern.finditer(content))
    if not matches:
        print(f"✅ Aucun base64 trouvé dans {md_path}")
        return

    fallback_counter = 1
    md_stem = Path(md_path).stem

    for m in matches:
        raw_ref = (m.group("ref") or "").strip()
        img_type = m.group("type").lower()
        if img_type == "jpeg":
            img_type = "jpg"
        b64_text = m.group("b64") or ""
        # nettoie base64 (enlève whitespace/newlines)
        b64_clean = re.sub(r'\s+', '', b64_text)

        # sanitize/ref fallback
        safe_ref = sanitize_ref(raw_ref)
        if not safe_ref:
            safe_ref = f"{md_stem}_auto{fallback_counter}"
            fallback_counter += 1

        # compose filename unique
        img_filename = f"{md_stem}__{safe_ref}.{img_type}"
        img_path = os.path.join(images_dir, img_filename)

        # write image if not exists
        if not os.path.exists(img_path):
            try:
                try:
                    img_bytes = base64.b64decode(b64_clean, validate=True)
                except Exception:
                    img_bytes = base64.b64decode(b64_clean)
                safe_write_bytes(img_path, img_bytes)
                print(f"📦 Image extraite : {img_path}")
            except Exception as e:
                print(f"❌ Échec extraction pour ref '{raw_ref}' dans {md_path} : {e}")
                # skip this image but continue
                continue
        else:
            print(f"⚠️ Image déjà existante : {img_path}")

        # replacement: ![][ref] and ![alt][ref]
        rel_path = os.path.relpath(img_path, Path(md_path).parent).replace(os.sep, "/")
        # 1) ![][ref]
        content = re.sub(r'!\[\]\[' + re.escape(raw_ref) + r'\]', f'![]({rel_path})', content)
        # 2) ![alt][ref]
        content = re.sub(r'!\[([^\]]*)\]\[' + re.escape(raw_ref) + r'\]', r'![\1](' + rel_path + r')', content)

        # remove the reference block (the base64 line)
        # be careful to remove the exact match span
        start, end = m.span()
        # replace with a single newline to avoid merging lines
        content = content[:start] + "\n" + content[end:]

    # write updated markdown back
    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✏️ Markdown mis à jour : {md_path}\n")
    except Exception as e:
        print(f"❌ Impossible d'écrire {md_path} : {e}")

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
