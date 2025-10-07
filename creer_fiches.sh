#!/bin/bash

# Créer les dossiers principaux
mkdir -p Bloc1 Bloc2 Fiches Commandes_Windows Commandes_Linux Protocoles templates

# Créer le modèle de fiche
cat <<EOT > templates/modele_fiche.md
# Titre de la fiche

## Objectif
Décrire l’objectif de la fiche.

## Concepts clés
- Concept 1
- Concept 2

## Commandes / Notes
- Commande 1
- Commande 2

## Liens / Références
- [Lien utile](#)
EOT

# --- Bloc 1 ---
declare -a bloc1=("Bases_Gestion_Incidents" "Prendre_en_main_GLPI" "Gerer_Incidents_Problemes" "Exploiter_Serveurs_Windows" "Installer_Config_Domaine_AD" "Exploiter_Domaine_AD" "Exploiter_Serveurs_Linux" "Bases_Reseaux_IP" "Parametrer_Telephonie_IP" "Connectivite_Filaire_Sans_Fil" "Parametrer_Actif_Routeur" "Superviser_Reseau" "Exploitation_Quotidienne_Reseau_IP" "Projets_Fil_Rouge_Bloc1")

for f in "${bloc1[@]}"; do
  touch "Bloc1/$f.md"
  ln -s "../Bloc1/$f.md" "Fiches/$f.md"
done

# --- Bloc 2 ---
declare -a bloc2=("Bases_Serveurs_Virtualises" "Hyperviseur_Type1" "Introduction_Programmation" "Automatiser_Taches_Scripts" "Bases_Securisation_Acces_Internet" "Intervenir_Autocommutateur_IP" "Configurer_VLANs" "Maintenir_Acces_Reseau_Distants" "Detection_Prevention_Intrusion" "Sauvegarder_Restaurer_Infrastructure" "Configurer_Services_Deployement_Terminaux" "Projets_Fil_Rouge_Bloc2")

for f in "${bloc2[@]}"; do
  touch "Bloc2/$f.md"
  ln -s "../Bloc2/$f.md" "Fiches/$f.md"
done

# Onglets spéciaux
touch Commandes_Windows/Commandes.md
touch Commandes_Linux/Commandes.md
touch Protocoles/Protocoles.md

echo "Toutes les fiches et liens ont été créés avec succès !"
