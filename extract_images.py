import os
import re
import base64
from pathlib import Path

def safe_write_bytes(path, data_bytes):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(data_bytes)

def sanitize_ref(ref):
    cleaned = re.sub(r'[^A-Za-z0-9_-]', '_', ref)
    if len(cleaned) > 40:
        cleaned = cleaned[:40]
    if cleaned.strip('_') == '':
        return None
    return cleaned

def fix_base64(b64_text):
    # retire les espaces/newlines
    s = re.sub(r'\s+', '', b64_text)
    # retire tout ce qui n'est pas base64 (= A-Z a-z 0-9 + / =)
    s = re.sub(r'[^A-Za-z0-9+/=]', '', s)
    # ajoute le padding '=' si nécessaire
    rem = len(s) % 4
    if rem == 1:
        # improbable, essayer d'enlever 1 char final puis pad
        s = s[:-1]
        rem = len(s) % 4
    if rem != 0:
        s += '=' * (4 - rem)
    return s

def extract_images_from_md(md_path, images_dir):
    try:
        text = Path(md_path).read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ Impossible de lire {md_path}: {e}")
        return

    os.makedirs(images_dir, exist_ok=True)

    # Cherche [ref]: data:image/...;base64, suivi de base64 même multi-lignes
    # capture jusqu'à la prochaine ligne commençant par [xxx]: ou jusqu'à la fin
    pattern = re.compile(
        r'^\s*\[(?P<ref>[^\]]+)\]:\s*<?\s*data:image/(?P<type>png|jpg|jpeg|gif);base64,(?P<b64>.*?)(?=\n\s*\[|\Z)',
        re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    matches = list(pattern.finditer(text))
    if not matches:
        print(f"✅ Aucun base64 trouvé dans {md_path}")
        return

    fallback_counter = 1
    md_stem = Path(md_path).stem

    for m in matches:
        raw_ref = (m.group("ref") or "").strip()
        img_type = (m.group("type") or "png").lower()
        if img_type == "jpeg":
            img_type = "jpg"
        b64_raw = m.group("b64") or ""

        # sanitize ref, fallback si nécessaire
        safe_ref = sanitize_ref(raw_ref)
        if not safe_ref:
            safe_ref = f"{md_stem}_auto{fallback_counter}"
            fallback_counter += 1

        img_filename = f"{md_stem}__{safe_ref}.{img_type}"
        img_path = os.path.join(images_dir, img_filename)

        # tenter de réparer et décoder le base64
        b64_clean = fix_base64(b64_raw)
        try:
            try:
                img_bytes = base64.b64decode(b64_clean, validate=True)
            except Exception:
                img_bytes = base64.b64decode(b64_clean)
        except Exception as e:
            print(f"❌ Échec extraction pour ref '{raw_ref}' dans {md_path} : {e}")
            # on passe à la suivante sans arrêter tout
            continue

        # écrire si n'existe pas
        if not os.path.exists(img_path):
            try:
                safe_write_bytes(img_path, img_bytes)
                print(f"📦 Image extraite : {img_path}")
            except Exception as e:
                print(f"❌ Impossible d'écrire {img_path} : {e}")
                continue
        else:
            print(f"⚠️ Image déjà existante : {img_path}")

        # Remplacements dans le markdown :
        rel_path = os.path.relpath(img_path, Path(md_path).parent).replace(os.sep, "/")
        # ![][ref]
        text = re.sub(r'!\[\]\[' + re.escape(raw_ref) + r'\]', f'![]({rel_path})', text)
        # ![alt][ref]
        text = re.sub(r'!\[([^\]]*)\]\[' + re.escape(raw_ref) + r'\]', r'![\1](' + rel_path + r')', text)

        # supprimer la référence base64 (le bloc entier capturé)
        start, end = m.span()
        text = text[:start] + "\n" + text[end:]

    # sauvegarder
    try:
        Path(md_path).write_text(text, encoding="utf-8")
        print(f"✏️ Markdown mis à jour : {md_path}\n")
    except Exception as e:
        print(f"❌ Impossible d'écrire {md_path} : {e}")

def main():
    blocks = ["Bloc1", "Bloc2"]
    root = Path.cwd()
    for block in blocks:
        bp = root / block
        if not bp.exists():
            print(f"ℹ️ Dossier absent : {block} (ignoré)")
            continue
        images_dir = bp / "images"
        md_files = sorted([p for p in bp.iterdir() if p.suffix.lower() == ".md"])
        for md in md_files:
            extract_images_from_md(str(md), str(images_dir))

if __name__ == "__main__":
    main()
