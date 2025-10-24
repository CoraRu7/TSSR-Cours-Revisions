import os
import re
import base64

# Fonction pour extraire les images d'un fichier markdown
def extract_images_from_md(md_path, images_dir):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pour trouver les images encodées en base64
    pattern = r'!\[.*?\]\(data:image/(png|jpeg|jpg|gif);base64,(.*?)\)'
    matches = re.findall(pattern, content, re.DOTALL)

    if not matches:
        print(f"✅ Aucun base64 trouvé dans {md_path}")
        return

    # Crée le dossier images si nécessaire
    os.makedirs(images_dir, exist_ok=True)

    for i, (img_type, b64_data) in enumerate(matches, start=1):
        # Normaliser jpg/jpeg
        if img_type.lower() == "jpeg":
            img_type = "jpg"

        # Nom unique de l'image
        base_name = os.path.splitext(os.path.basename(md_path))[0]
        img_filename = f"{base_name}_{i}.{img_type}"
        img_path = os.path.join(images_dir, img_filename)

        # Évite les doublons
        if not os.path.exists(img_path):
            with open(img_path, "wb") as img_file:
                img_file.write(base64.b64decode(b64_data))
            print(f"📦 Image extraite : {img_path}")

        # Remplace le lien dans le markdown
        content = content.replace(
            f"data:image/{img_type};base64,{b64_data}",
            f"{os.path.relpath(img_path, os.path.dirname(md_path)).replace(os.sep, '/')}"
        )

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

