import os
import re
import base64

def extract_images_from_md(md_path, images_dir):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Crée le dossier images si nécessaire
    os.makedirs(images_dir, exist_ok=True)

    # Regex pour trouver les références base64 [imageX]: data:image/type;base64,...
    pattern = r'^\s*\[(.*?)\]:\s*data:image/(png|jpeg|jpg|gif);base64,(.*)$'
    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)

    if not matches:
        print(f"✅ Aucun base64 trouvé dans {md_path}")
        return

    for ref_name, img_type, b64_data in matches:
        img_type = "jpg" if img_type.lower() == "jpeg" else img_type.lower()
        img_filename = f"{ref_name}.{img_type}"
        img_path = os.path.join(images_dir, img_filename)

        # Évite les doublons
        if not os.path.exists(img_path):
            with open(img_path, "wb") as img_file:
                img_file.write(base64.b64decode(b64_data))
            print(f"📦 Image extraite : {img_path}")

        # Remplace toutes les occurrences ![][imageX] par ![](images/...)
        content = re.sub(r'!\[\]\[' + re.escape(ref_name) + r'\]', 
                         f'![]({os.path.relpath(img_path, os.path.dirname(md_path)).replace(os.sep, "/")})',
                         content)

        # Supprime la référence base64 du Markdown
        content = re.sub(r'^\s*\[' + re.escape(ref_name) + r'\]:\s*data:image/.*$', '', content, flags=re.MULTILINE)

    # Sauvegarde le Markdown mis à jour
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✏️ Markdown mis à jour : {md_path}\n")


# Dossiers à traiter
blocks = ["Bloc1", "Bloc2"]

for block in blocks:
    images_dir = os.path.join(block, "images")
    md_files = [f for f in os.listdir(block) if f.endswith(".md")]
    for md_file in md_files:
        md_path = os.path.join(block, md_file)
        extract_images_from_md(md_path, images_dir)

