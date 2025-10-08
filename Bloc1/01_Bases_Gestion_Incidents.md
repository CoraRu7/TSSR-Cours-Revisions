# Bases de la gestion d’incidents

## L’organisation d’un centre de services

### Fiche 1 (développée)
#### Objectif
Comprendre le rôle, les fonctions et les bonnes pratiques d’un centre de services pour les utilisateurs et l’entreprise.

#### Concepts clés
- Rôle central du centre de services client dans l’entreprise.
- **Différences détaillées :**
  - **Support client** : apporte assistance et informations sur les produits/services. Peut être physique ou virtuel (e-mail, chat, téléphone). Concerne la résolution de problèmes simples ou spécifiques.
  - **Centre d’appels** : gère un grand volume de demandes via téléphone, e-mails, chat ou réseaux sociaux. Axé sur la communication, le suivi de commandes, télémarketing ou enquêtes. L’interaction est majoritairement distante, peu d’intervention physique.
  - **Service desk** : point de contact unique entre utilisateurs et IT. Gère incidents, demandes de service, accès aux ressources et support réactif. Va au-delà du simple support client en intégrant des processus ITIL et des outils de suivi.
- Gestion des incidents et demandes selon ITIL.
- Contact unique entre utilisateurs et organisation IT.
- Avantages : réduction des coûts, meilleure satisfaction client, suivi des incidents et demandes.

#### Commandes / Notes
- Numéros verts : 0800, 0801, 0803, 0804, 0805 et numéros courts (ex. 116162, 3132).
- Le service desk peut traiter : incidents, demandes de services, communications utilisateurs.
- Meilleures pratiques :
  - Portail libre-service 24/7
  - SLA et priorisation des incidents
  - Reporting et tableaux de bord en temps réel
  - Gestion des connaissances pour FAQ et erreurs connues
- Logiciels : GLPI, ServiceNow, autres systèmes de ticketing

#### Liens / Références
- [ITIL Foundation](https://www.axelos.com/certifications/itil)
- [Exemple GLPI](https://glpi-project.org)

---

### Fiche 2 (initiale)
#### Objectif
Appliquer les pratiques de gestion de centre de services pour optimiser la satisfaction client et la performance opérationnelle.

#### Concepts clés
- Flux opérationnel et automatisation des tickets.
- Gestion des SLA et escalades.
- Gestion de la connaissance : base de données, workflows, erreurs et problèmes connus.
- Libre-service pour l’utilisateur final : diagnostics, demandes de service, processus automatisés.
- Reporting : tableaux de bord, analyse des problèmes, suivi des incidents majeurs.

#### Commandes / Notes
- Utilisation de logiciels de centre de services pour organiser transferts et escalades.
- Surveillance proactive des problèmes pour anticiper pannes et interruptions.
- Création de rapports pour mesurer la performance et optimiser les coûts.
- Communication et suivi client pour fidélisation.

#### Liens / Références
- Documentation interne ITIL
- Tutoriels logiciels de service desk (GLPI, ServiceNow)


## La méthode ITIL

### Fiche 1 – Développée

## Objectif
Comprendre la méthode ITIL pour la gestion des services IT, la gestion des incidents et des problèmes.

## Concepts clés
- ITIL : bonnes pratiques pour services IT.
- Gestion des incidents : restaurer le service rapidement.
- Gestion des problèmes : identifier et traiter la cause des incidents.
- Différence incident / problème.
- 3 phases de gestion des problèmes : Identification, Contrôle, Contrôle d’erreur.
- Solutions de contournement pour incidents connus.

## Détails / Notes
- Gestion des incidents ITIL :
  - Détecter, enregistrer, classer, prioriser, résoudre, clore.
  - Processus réactif, communication et coordination.
- Avantages ITIL :
  - Meilleure allocation des ressources,
  - Réduction des incidents récurrents,
  - Amélioration satisfaction utilisateur.
- Gestion des problèmes :
  - Identification des causes profondes,
  - Documentation des solutions de contournement,
  - Analyse coûts / risques / efficacité des solutions permanentes.
- Solutions de contournement :
  - Réduisent impact incidents si solution complète non disponible,
  - Temporaires ou permanentes.
- Contrôle d’erreur :
  - Suivi erreurs connues,
  - Analyse solutions définitives.

## Commandes / Notes pratiques
- Utiliser logiciel ITSM pour incidents, problèmes, SLA.
- Créer base de connaissances pour solutions et erreurs.
- Mettre en place escalade et priorisation.

### Fiche 2 – Résumée

## Objectif
Identifier rapidement les points essentiels ITIL.

## Concepts clés
- ITIL = gestion des services IT.
- Incident : perturbation service à corriger.
- Problème : cause incidents à analyser et résoudre.
- Solutions de contournement pour incidents connus.

## Commandes / Notes
- Étapes incidents : détecter → prioriser → résoudre → clore.
- Hiérarchiser problèmes selon impact et probabilité.
- Documenter solutions de contournement et erreurs connues.


## L’architecture matérielle des équipements numériques

### Fiche 3 – Détaillée

## Objectif
Comprendre les composants matériels, les technologies et normes, ainsi que les critères de choix d’un équipement numérique pour un usage optimal.

## Concepts clés

### Composants essentiels (détaillés)
- **Boîtier** : protège et organise les composants internes. Assure le flux d’air pour le refroidissement et permet l’accès aux ports externes et à l’alimentation. Formats : tour complète, compacte, tout-en-un.  

- **Alimentation (PSU)** : convertit le courant alternatif (CA) du secteur en courant continu (CC) utilisable par les composants. Fournit les tensions nécessaires (3,3V, 5V, 12V) et alimente cartes, disques et périphériques. La qualité de l’alimentation impacte stabilité et durée de vie des composants.  

- **Carte mère** : circuit principal reliant CPU, RAM, stockage, cartes d’extension et périphériques. Gère la communication via bus et chipset, permet l’installation de périphériques et l’évolution de l’équipement.  

- **Chipset** : contrôleur principal des communications sur la carte mère.  
  - **Northbridge** : liaison rapide entre CPU, RAM et GPU intégré, impacte la vitesse globale du système.  
  - **Southbridge** : gère périphériques lents (disques, USB, audio), communication secondaire mais essentielle pour I/O.  

- **Processeur (CPU)** : exécute les instructions logicielles, calcule les opérations et gère les flux de données.  
  - **Architecture** : x86 (32 bits), x64 (64 bits), détermine la capacité mémoire et la performance.  
  - **Cœurs et threads** : plus de cœurs = meilleur multitâche, Hyper-Threading/SMT = exécution simultanée de plusieurs threads.  
  - **Sockets** : type de connexion CPU-carte mère (PGA, LGA).  

- **Ventilation** : dissipe la chaleur pour maintenir les composants à température optimale. Ventilateurs et radiateurs (Ventirad) évitent la surchauffe, garantissant performance et longévité.  

- **Mémoires** : stockent temporairement ou définitivement les données.  
  - **ROM/BIOS/UEFI** : contient les programmes de démarrage et la configuration du matériel.  
  - **RAM** : mémoire vive pour stocker les données et instructions en cours d’utilisation ; impact direct sur vitesse multitâche. Types : DIP, SIMM, DIMM, SODIMM, SRAM, ECC.  

- **Disques durs** : stockage permanent des données.  
  - **HDD** : mécanique, stockage magnétique, grande capacité, coût faible.  
  - **SSD** : mémoire flash, rapide, durable, impacte temps de démarrage et vitesse d’accès.  
  - **NVMe** : SSD haute performance via bus PCIe, faible latence.  
  - **SSHD** : hybride HDD+SSD, compromis entre capacité et rapidité.  

- **Carte graphique (GPU)** : traite les calculs graphiques et images.  
  - **Intégrée** : partie du CPU ou chipset, adaptée pour bureautique et vidéos simples.  
  - **Dédiée** : GPU + mémoire GDDR séparée, nécessaire pour jeux, rendu 3D, calculs intensifs.  

- **Gestion des périphériques** : outil natif Windows ou logiciel tiers comme AIDA64. Permet de voir tous les composants et périphériques, d’identifier les périphériques non reconnus et d’installer/mettre à jour les pilotes (drivers). Accessible via :  
  - **Windows** : clic droit sur “Démarrer” → “Gestionnaire de périphériques” ou `devmgmt.msc`.  
  - **AIDA64** : analyse complète matériel + pilotes + BIOS/UEFI + sondes (températures, voltage, RPM ventilateurs).  

### Technologies et normes (détaillées)

- **CPU** :  
  - Cache (L1-L3) pour données fréquentes, DVFS (tension/fréquence variable), Hyper-Threading/SMT, Pipeline, préchargement spéculatif, sécurité (DEP/NX, TXT, SGX/SME/SEV), Turbo Boost/Core, virtualisation (VT-x, AMD-V).  

- **Mémoire vive** : HBM (large bande), NVDIMM (persistance + volatilité), RDIMM / LRDIMM (stabilité et capacité).  

- **Stockage** :  
  - HDD : PMR (magnétique perpendiculaire), SMR (pistes superposées).  
  - SSD : NAND Flash, TRIM, Wear Leveling.  
  - NVMe : faible latence et haut débit via PCIe.  

- **GPU** : SLI / Crossfire (multi-GPU), VRS (résolution variable), Tensor Cores / AI, CUDA (NVIDIA) / Stream (AMD).  

- **Connectiques** : USB/USB-C/USB PD, Thunderbolt, HDMI, DisplayPort, SATA, M2, Ethernet, WiFi, Bluetooth, RFID/NFC.  

### Choix d’un équipement

- **Énergie** : composants basse consommation pour réduire coûts et impact énergétique.  
- **Espace** : RAM et stockage adaptés au nombre d’applications et volume de données.  
- **Évolutivité** : compatibilité avec composants futurs pour upgrades.  
- **Puissance de traitement** : processeur plus rapide, plus de cœurs, GPU dédié selon usage.  
- **Pilotes et support** : garantie fabricant et disponibilité mises à jour pilotes.  
- **Budget** : équilibrer performance et coût.  
- **Sécurité** : compatibilité avec politiques sécurité entreprise.  
- **Type d’utilisation** : bureautique, jeux, montage vidéo, IA, serveurs…  
- **Système d’exploitation** : compatibilité avec Windows, Linux, macOS ou OS embarqué.


## L’architecture logicielle des équipements numériques

### Fiche 4 – 

## Objectif
Comprendre les principes logiciels, les couches logicielles, les interactions avec le matériel, les systèmes d’exploitation, et les tendances évolutives de l’architecture logicielle.

## Concepts clés

### Introduction et définition
- **Logiciel** : ensemble d’instructions, de procédés et de règles relatifs au traitement des données.  
- **Types de logiciels :**
  - **Logiciels systèmes** : interagissent directement avec le matériel.  
    - Exemples : Microsoft Windows 11/Serveur 2022, Linux Debian, MacOS.  
  - **Logiciels applicatifs** : interagissent indirectement avec le matériel via le système.  
    - Exemples : Google Chrome, WinRAR, OpenOffice, Filezilla Server.  
- **Licences :**
  - Propriétaire : utilisation payante, contrôle par l’auteur.  
  - Libre / Open Source : utilisation, modification, redistribution autorisées.  
  - Gratuiciel (Freeware) : utilisation gratuite mais propriétaire.  
  - Partagiciel (Shareware) : période d’essai gratuite, puis payant.

### Interactions matériel – logiciel
- **Logiciel système** : OS qui communique directement avec le matériel (CPU, RAM, disques, GPU).  
- **Logiciel applicatif** : application, utilitaire ou pilote qui ajoute des fonctionnalités ou optimise l’utilisation des ressources.  
  - **Application** : ajout de fonctionnalités non natives (ex : bureautique OpenOffice).  
  - **Utilitaire** : analyse, configuration et optimisation du matériel et logiciels.  
  - **Pilote (Driver)** : permet au système d’exploitation de reconnaître un périphérique et d’utiliser toutes ses fonctionnalités.  
- **Logiciels standard** : distribués à grande échelle pour des besoins communs.  
- **Logiciels spécifiques (métiers)** : créés pour répondre à un besoin unique.

### Couches logicielles et fonctionnement
- **Hiérarchie logicielle** : chaque couche fournit des services à la couche supérieure tout en cachant sa complexité.  

```text
┌───────────────────────────────────────────────┐
│ Couche 4 : Logiciels applicatifs / Interface │
│           utilisateur (OpenOffice, Chrome)  │
└───────────────────────────────────────────────┘
                    ▲
                    │ Utilise
                    ▼
┌───────────────────────────────────────────────┐
│ Couche 3 : Intergiciel / Middleware          │
│           (API, librairies, pilotes)        │
└───────────────────────────────────────────────┘
                    ▲
                    │ Communique avec
                    ▼
┌───────────────────────────────────────────────┐
│ Couche 2 : Logiciel système / OS             │
│           (noyau, gestion des ressources)   │
└───────────────────────────────────────────────┘
                    ▲
                    │ Contrôle
                    ▼
┌───────────────────────────────────────────────┐
│ Couche 1 : Matériel / Hardware               │
│           (CPU, RAM, disques, GPU)          │
└───────────────────────────────────────────────┘

