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
 ```
 <!doctype html>
 <html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche — Méthode ITIL (TSSR)</title>
<style>
  :root{
    --bg:#0b0f14;
    --panel:#0f1720;
    --muted:#9aa6b2;
    --blue:#1e90ff;
    --red:#ff4d4f;
    --card:#0c1116;
    --glass: rgba(255,255,255,0.03);
    --mono: "Fira Code", monospace;
  }
  body{
    margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Arial;
    background:var(--bg);color:#e6eef6;padding:24px;line-height:1.45;
  }
  .wrap{max-width:920px;margin:0 auto}
  header{display:flex;gap:14px;align-items:center;margin-bottom:14px}
  .logo{width:56px;height:56px;border-radius:8px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021127}
  h1{font-size:18px;margin:0}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--card),#071016);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--red);margin:10px 0 6px 0}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  ul{margin:6px 0 6px 18px}
  ol{margin:6px 0 6px 18px}
  code,pre{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:6px;border-radius:6px}
  .diagram{width:100%;height:auto;margin:12px 0}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:600}
  .kpis{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}
  .kpis .k{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px;min-width:110px}
  footer{color:var(--muted);font-size:13px;margin-top:14px;text-align:center}
  @media(max-width:720px){.kpis{flex-direction:column}}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">ITIL</div>
      <div>
        <h1>Méthode ITIL — Fiche synthétique</h1>
        <div class="meta">Bloc 1 · Thème : Les bases de la gestion d'incidents · Durée conseillée : 1h</div>
      </div>
    </header>

   <section class="card">
      <h2>Résumé en 2 lignes</h2>
      <p>ITIL (Information Technology Infrastructure Library) est un cadre de bonnes pratiques pour gérer les services IT.  
      La <strong>gestion des incidents</strong> vise la restauration rapide du service ; la <strong>gestion des problèmes</strong> vise à traiter les causes profondes.</p>
    </section>

   <section class="card">
      <h2>I. Gestion des incidents (ITIL)</h2>
      <h3>Définition</h3>
      <p>Processus réactif dont l'objectif principal est de <strong>restaurer le service</strong> le plus rapidement possible après interruption.</p>

  <h3>Activités courantes</h3>
      <ul>
        <li>Détection et enregistrement</li>
        <li>Classification & priorisation (impact × urgence)</li>
        <li>Routage / assignation</li>
        <li>Diagnostic & résolution (N1 → N2 → N3)</li>
        <li>Clôture & documentation</li>
      </ul>

  <h3>Pourquoi l'implémenter ? (avantages)</h3>
      <ul>
        <li>Maintien des SLAs et disponibilité</li>
        <li>Réduction du temps d'arrêt (MTTR)</li>
        <li>Meilleure productivité du personnel</li>
        <li>Amélioration de la satisfaction utilisateur (CSAT)</li>
      </ul>
    </section>

<section class="card">
      <h2>II. Gestion des problèmes (ITIL)</h2>
  <h3>Définition</h3>
      <p>Processus visant à identifier et corriger les causes profondes des incidents pour réduire leur récurrence.</p>

  <h3>Différence Incident vs Problème</h3>
      <table>
        <thead><tr><th>Incident</th><th>Problème</th></tr></thead>
        <tbody>
          <tr><td>Impact immédiat — restaurer le service</td><td>Cause racine — recherche de solution permanente</td></tr>
          <tr><td>Traité par support (N1/N2)</td><td>Analyser (RCA), planifier correction</td></tr>
        </tbody>
      </table>

  <h3>3 phases de la gestion des problèmes</h3>
      <ol>
        <li><strong>Identification</strong> — détecter tendances et incidents récurrents.</li>
        <li><strong>Contrôle des problèmes</strong> — analyser, documenter solutions de contournement (workarounds).</li>
        <li><strong>Contrôle d'erreur</strong> — gérer erreurs connues et planifier résolutions permanentes (change management si nécessaire).</li>
      </ol>
    </section>

<section class="card">
      <h2>III. Processus simplifié (ticket lifecycle)</h2>
      <ol>
        <li>Création</li>
        <li>Classification & priorisation</li>
        <li>Routage</li>
        <li>Diagnostic</li>
        <li>Résolution</li>
        <li>Clôture</li>
        <li>Analyse / RCA si incident majeur</li>
      </ol>

  <!-- simple SVG flow -->
  <svg class="diagram" viewBox="0 0 800 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <style>.s{font:12px sans-serif;fill:#eaf6ff}</style>
        <rect x="8" y="10" width="110" height="60" rx="6" fill="#072136" stroke="#1e90ff"/>
        <text x="63" y="40" text-anchor="middle" class="s">Création</text>
        <rect x="140" y="10" width="140" height="60" rx="6" fill="#07171a" stroke="#1e90ff"/>
        <text x="210" y="40" text-anchor="middle" class="s">Classification / Priorité</text>
        <rect x="300" y="10" width="120" height="60" rx="6" fill="#072136" stroke="#ff4d4f"/>
        <text x="360" y="40" text-anchor="middle" class="s">Routage</text>
        <rect x="440" y="10" width="150" height="60" rx="6" fill="#07171a" stroke="#60b8ff"/>
        <text x="515" y="40" text-anchor="middle" class="s">Diagnostic & Résolution</text>
        <rect x="610" y="10" width="160" height="60" rx="6" fill="#072136" stroke="#2ecc71"/>
        <text x="690" y="40" text-anchor="middle" class="s">Clôture / KB</text>
        <g stroke="#2b3e48" stroke-width="2" fill="none">
          <path d="M118 40 H140" stroke="#7fbfff"/>
          <path d="M280 40 H300" stroke="#7fbfff"/>
          <path d="M420 40 H440" stroke="#7fbfff"/>
          <path d="M590 40 H610" stroke="#7fbfff"/>
        </g>
      </svg>
    </section>

<section class="card">
      <h2>IV. Outils et pratiques</h2>
      <ul>
        <li><strong>Outils tickets :</strong> GLPI, Jira Service Management, ServiceNow — gérer flux, SLA, routage, KB.</li>
        <li><strong>KB / Self-service :</strong> FAQ, diagnostics, formulaires de demande — réduit les tickets simples.</li>
        <li><strong>Automatisation :</strong> réinitialisation de mot de passe, assignation, escalades basées sur règles.</li>
      </ul>

  <h3>Checklist implémentation (rapide)</h3>
      <ul>
        <li>Définir SLA & priorités</li>
        <li>Mettre en place flux de tickets et routage</li>
        <li>Créer KB & portail self-service</li>
        <li>Mesurer KPIs (MTTR, FCR, CSAT)</li>
      </ul>
      <div class="kpis">
        <div class="k"><strong>MTTR</strong><div style="color:var(--muted);font-size:13px">Temps moyen de réparation</div></div>
        <div class="k"><strong>FCR</strong><div style="color:var(--muted);font-size:13px">% résolu au 1er contact</div></div>
        <div class="k"><strong>CSAT</strong><div style="color:var(--muted);font-size:13px">Satisfaction utilisateur</div></div>
      </div>
    </section>
    <section class="card">
      <h2>V. Exemples de procédures courtes</h2>
      <p><strong>Réinitialisation de mot de passe (N1)</strong> :</p>
      <ol>
        <li>Vérifier identité (3 données)</li>
        <li>Vérifier politique (SLA)</li>
        <li>Réinitialiser via AD / outil</li>
        <li>Tester connexion avec l'utilisateur</li>
        <li>Documenter la résolution dans le ticket et KB si utile</li>
      </ol>
    </section>
    <section class="card">
      <h2>VI. Auto-évaluation (Quiz rapide)</h2>
      <details><summary>Q1 — La gestion des incidents ITIL est-elle réactive ?</summary><div style="margin-top:8px">Réponse : <strong>Oui</strong> — objectif : restaurer le service rapidement.</div></details>
      <details><summary>Q2 — Combien de phases pour la gestion des problèmes ?</summary><div style="margin-top:8px">Réponse : <strong>3</strong> — identification, contrôle des problèmes, contrôle d'erreur.</div></details>
      <details><summary>Q3 — Donnez 2 KPI importants</summary><div style="margin-top:8px">Exemples : <strong>MTTR, FCR, CSAT</strong>.</div></details>
    </section>
    <footer>Fiche synthétique — méthode ITIL · Bloc 1 · TSSR — concise pour révision</footer>
  </div>
</body>
</html>

<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche — Architecture logicielle des équipements numériques</title>
<style>
  :root{
    --bg:#0b1116;
    --panel:#0b1720;
    --muted:#9fb0bf;
    --blue:#1e90ff;
    --red:#ff4d4f;
    --card:#071017;
    --glass: rgba(255,255,255,0.03);
    --mono: "Fira Code", monospace;
  }
  body{margin:0;font-family:Inter,system-ui,Arial;color:#e6eef6;background:var(--bg);padding:22px;line-height:1.45}
  .wrap{max-width:980px;margin:0 auto}
  header{display:flex;gap:12px;align-items:center;margin-bottom:12px}
  .logo{width:56px;height:56px;border-radius:8px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021127}
  h1{margin:0;font-size:18px}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--card),#061018);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--red);margin:8px 0}
  p{margin:6px 0}
  ul{margin:6px 0 6px 18px}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  code{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:4px;border-radius:6px}
  .diagram{width:100%;height:auto;margin-top:8px}
  .row{display:flex;gap:12px}
  .col{flex:1}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:600}
  footer{color:var(--muted);font-size:13px;margin-top:12px;text-align:center}
  @media(max-width:820px){.row{flex-direction:column}}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">SW</div>
      <div>
        <h1>Architecture logicielle des équipements numériques — Fiche</h1>
        <div class="meta">Bloc 1 · Concepts clés : couches logicielles, noyau, middleware, applicatif, OSI</div>
      </div>
    </header>
    <section class="card">
      <h2>Résumé rapide</h2>
      <p>Architecture logicielle = organisation en couches qui sépare le matériel, le noyau (OS), le middleware (bibliothèques, API) et la couche applicative. Principe clef : <strong>abstraction</strong> — chaque couche cache la complexité de la couche inférieure.</p>
    </section>
    <div class="row">
      <div class="col">
        <section class="card">
          <h2>1. Définitions essentielles</h2>
          <ul>
            <li><strong>Logiciel système</strong> : logiciel qui interagit directement avec le matériel (ex. noyau, drivers, OS).</li>
            <li><strong>Logiciel applicatif</strong> : programme utilisé par l'utilisateur (ex. navigateur, suite bureautique).</li>
            <li><strong>Middleware</strong> : bibliothèques, APIs, services facilitant la communication entre appli et OS.</li>
            <li><strong>Driver (pilote)</strong> : permet au système d'exploitation d'utiliser un composant matériel.</li>
            <li><strong>Licence</strong> : propriétaire, libre (open-source), freeware, shareware.</li>
          </ul>
        </section>
        <section class="card">
          <h2>2. Les couches logicielles (vue simplifiée)</h2>
          <ol>
            <li><strong>Couche matérielle</strong> — CPU, RAM, périphériques.</li>
            <li><strong>Noyau / OS</strong> — kernel, gestion mémoire, planificateur, drivers.</li>
            <li><strong>Middleware</strong> — bibliothèques, API, runtime, services.</li>
            <li><strong>Applicatif</strong> — GUI/CLI, applications utilisateur.</li>
          </ol>
          <h3>Principe :</h3>
          <p>Abstraction & interfaces : les applications appellent des APIs (middleware) qui appellent le noyau, qui pilote le matériel.</p>
        </section>
        <section class="card">
          <h2>3. Tableau : OSI ↔ appareils & protocoles (mapping)</h2>
          <p>Comprendre quel équipement ou protocole agit à quelle couche aide pour le diagnostic réseau et le choix des outils.</p>
          <table>
            <thead><tr><th>Couche OSI</th><th>Rôle / Exemples de protocoles</th><th>Appareils concernés</th></tr></thead>
            <tbody>
              <tr><td>7 - Application</td><td>HTTP, SMTP, DNS, FTP, SSH — interface utilisateur / services</td><td>Serveurs applicatifs, clients (navigateurs)</td></tr>
              <tr><td>6 - Présentation</td><td>Encodage, chiffrement, SSL/TLS</td><td>Proxy SSL, terminators TLS, appliances</td></tr>
              <tr><td>5 - Session</td><td>Gestion de session (ex. contrôles de session, NetBIOS)</td><td>Serveurs d'applications, load balancers</td></tr>
              <tr><td>4 - Transport</td><td>TCP, UDP — multiplexage ports, contrôle flux</td><td>Pare-feu de couche 4, proxies</td></tr>
              <tr><td>3 - Réseau</td><td>IP, ICMP — routage, addressing</td><td>Routeurs, pare-feu, serveurs DHCP/DNS</td></tr>
              <tr><td>2 - Liaison</td><td>Ethernet (802.3), PPP, VLAN (802.1Q)</td><td>Switches, ponts, cartes réseau (NIC)</td></tr>
              <tr><td>1 - Physique</td><td>Câbles (UTP, fibre), signaux, hubs</td><td>Câblage, hubs, modems, interfaces physiques</td></tr>
            </tbody>
          </table>
          <p><em>Remarque :</em> Dans la pratique, beaucoup de fonctions se chevauchent (ex. NAT = couche 3/4), et les « appliances » modernes opèrent sur plusieurs couches.</p>
        </section>
        <section class="card">
          <h2>4. Interactions Matériel ↔ Logiciel</h2>
          <ul>
            <li><strong>Drivers</strong> : traduisent les appels OS → instructions hardware.</li>
            <li><strong>Firmware / BIOS / UEFI</strong> : logiciel minimal entre matériel et OS (initialisation).</li>
            <li><strong>Virtualisation</strong> : hyperviseur intercale une couche logicielle (hosts, guests).</li>
          </ul>
        </section>
      </div>
      <aside class="col">
        <section class="card">
          <h2>Schéma : Empilement logique (simplifié)</h2>
          <!-- Simple SVG stack -->
          <svg class="diagram" viewBox="0 0 420 380" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <style>.t{font:12px sans-serif;fill:#eaf6ff}</style>
            <rect x="40" y="290" width="340" height="60" rx="6" fill="#07171a" stroke="#1e90ff"/>
            <text x="210" y="320" text-anchor="middle" class="t">Couche Applicative — Apps, GUI (HTTP, SMTP)</text>
            <rect x="60" y="210" width="300" height="60" rx="6" fill="#071017" stroke="#60b8ff"/>
            <text x="210" y="240" text-anchor="middle" class="t">Middleware — APIs, bibliothèques, runtimes</text>
            <rect x="80" y="130" width="260" height="60" rx="6" fill="#07171a" stroke="#ff6b6b"/>
            <text x="210" y="160" text-anchor="middle" class="t">Noyau / OS — kernel, drivers, gestion ressources</text>
            <rect x="100" y="50" width="220" height="60" rx="6" fill="#071017" stroke="#2ecc71"/>
            <text x="210" y="80" text-anchor="middle" class="t">Matériel — CPU, RAM, Disques, NIC</text>
            <!-- arrows -->
            <g stroke="#0a2430" stroke-width="2" fill="none">
              <path d="M210 130 V150" stroke="#7fbfff"/>
              <path d="M210 210 V230" stroke="#7fbfff"/>
              <path d="M210 290 V310" stroke="#7fbfff"/>
            </g>
          </svg>
          <p style="color:var(--muted);font-size:13px;margin-top:8px">Flux : l'appli → appelle l'API → -> OS via syscall → OS commande le matériel.</p>
        </section>
        <section class="card">
          <h2>5. Systèmes d'exploitation & embarqué (bref)</h2>
          <table>
            <thead><tr><th>Type</th><th>Exemples</th><th>Usage</th></tr></thead>
            <tbody>
              <tr><td>Desktop / Serveur</td><td>Windows, Linux, macOS</td><td>PC, serveurs, applications générales</td></tr>
              <tr><td>Embarqué</td><td>RTOS, firmware, Linux embarqué</td><td>IoT, routeurs, systèmes critiques</td></tr>
              <tr><td>Mobile</td><td>Android, iOS</td><td>Smartphones, tablettes</td></tr>
            </tbody>
          </table>
        </section>
        <section class="card">
          <h2>6. Points clés à retenir (examen)</h2>
          <ul>
            <li>4 couches logicielles : Matériel → OS → Middleware → Applicatif.</li>
            <li>Principe d'<strong>abstraction</strong> : facilite développement et portabilité.</li>
            <li>Drivers & firmware lient matériel ↔ OS ; middleware fournit API aux appli.</li>
            <li>Connaître mapping OSI → appareils & protocoles pour dépanner réseaux.</li>
          </ul>
        </section>
        <section class="card">
          <h2>7. Quiz court</h2>
          <details><summary>Q1 — Quel rôle du kernel ?</summary><div style="margin-top:8px">Réponse : gérer la mémoire, les processus, E/S et interfaces hardware.</div></details>
          <details><summary>Q2 — Middleware = ?</summary><div style="margin-top:8px">Réponse : bibliothèques, API, runtimes facilitant l'échange entre appli et OS.</div></details>
          <details><summary>Q3 — À quelle couche OSI correspond le routage ?</summary><div style="margin-top:8px">Réponse : couche 3 (Réseau).</div></details>
        </section>
      </aside>
    </div>
    <footer>Fiche synthétique — Architecture logicielle · Bloc 1 · TSSR</footer>
  </div>
</body>
</html>

<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche — Fondamentaux du câblage réseaux</title>
<style>
  :root{
    --bg:#0b1116;
    --panel:#071018;
    --muted:#9eb0bf;
    --blue:#1e90ff;
    --red:#ff4d4f;
    --card:#0c151a;
    --accent:#60b8ff;
    --mono: "Fira Code", monospace;
  }
  body{
    margin:0;padding:20px;font-family:Inter,system-ui,Arial;color:#e6eef6;background:linear-gradient(180deg,var(--bg),#061018);
    line-height:1.45;
  }
  .wrap{max-width:980px;margin:0 auto}
  header{display:flex;gap:12px;align-items:center;margin-bottom:14px}
  .logo{width:56px;height:56px;border-radius:8px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021127}
  h1{margin:0;font-size:18px}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--card),#071018);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--red);margin:10px 0 6px 0}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  ul{margin:6px 0 6px 18px}
  .diagram{width:100%;height:auto;margin-top:12px}
  .wire{height:14px;border-radius:3px;margin-bottom:4px}
  .pin-row{display:flex;gap:6px;align-items:center;margin-top:6px}
  .pin{width:28px;height:28px;border-radius:4px;display:flex;align-items:center;justify-content:center;font-weight:700;color:#061018}
  .note{color:var(--muted);font-size:13px}
  code{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:4px;border-radius:6px}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:600}
  footer{color:var(--muted);font-size:13px;margin-top:12px;text-align:center}
  @media(max-width:720px){.pin{width:22px;height:22px;font-size:12px}}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">NET</div>
      <div>
        <h1>Fondamentaux du câblage réseaux</h1>
        <div class="meta">Bloc 1 · Thème : câblage · Durée estimée : 1h</div>
      </div>
    </header>
    <section class="card">
      <h2>Résumé</h2>
      <p>Le câblage réseau (RJ45 / Ethernet) comprend plusieurs catégories (Cat5e → Cat8), différents blindages (U/UTP, F/FTP, etc.), et deux types de cordons importants : <strong>droit</strong> (même ordonnancement aux deux extrémités) et <strong>croisé</strong> (certaines paires inversées). Les câbles peuvent être <em>monobrins</em> (rigides, baie) ou <em>multibrins</em> (souples, cordons).</p>
    </section>
    <section class="card">
      <h2>I. Port Ethernet & RJ45</h2>
      <ul>
        <li><strong>Port Ethernet</strong> : prise pour câble RJ45 (8 conducteurs, 4 paires).</li>
        <li><strong>RJ45</strong> désigne le connecteur ; les paires sont torsadées (couples uni/rayé).</li>
        <li><strong>Usage</strong> : box, PC, switch, routeur, console, TV.</li>
      </ul>
    </section>
    <section class="card">
      <h2>II. Catégories (capacité & usage)</h2>
      <table>
        <thead><tr><th>Catégorie</th><th>Débit typique / Usage</th><th>Portée typique</th></tr></thead>
        <tbody>
          <tr><td>Cat5e</td><td>1 Gbps (LAN domestique)</td><td>≤100 m</td></tr>
          <tr><td>Cat6 / 6a</td><td>1 Gbps → 10 Gbps (6a)</td><td>≤100 m (10Gbp court ≈55m pour Cat6)</td></tr>
          <tr><td>Cat7 / 7a</td><td>10 Gbps+ (data centers, blindage avancé)</td><td>courtes liaisons / serveurs</td></tr>
          <tr><td>Cat8</td><td>25/40 Gbps (centre de données)</td><td>très courtes liaisons</td></tr>
        </tbody>
      </table>
      <p class="note">La catégorie est imprimée sur la gaine. Choisir en fonction bande passante et environnement (bruit électromagnétique).</p>
    </section>
    <section class="card">
      <h2>III. Blindages (nomenclature moderne)</h2>
      <table>
        <thead><tr><th>Code</th><th>Signification</th><th>Quand l'utiliser</th></tr></thead>
        <tbody>
          <tr><td>U/UTP</td><td>Pas de blindage (gaine non blindée, paires non blindées)</td><td>Réseau standard en intérieur, peu d'interférences</td></tr>
          <tr><td>F/UTP</td><td>Feuille sur la gaine, paires non blindées</td><td>Protège contre EMI externes</td></tr>
          <tr><td>S/UTP</td><td>Tresse sur la gaine, paires non blindées</td><td>Environnements avec interférences</td></tr>
          <tr><td>U/FTP, F/FTP, S/FTP, SF/FTP</td><td>Blindage par paire + gaine (variantes)</td><td>Installations sensibles / data centers</td></tr>
        </tbody>
      </table>
      <p class="note">SFTP, S/FTP etc. : vérifiez la signification exacte sur la fiche technique (nouvelle nomenclature).</p>
    </section>
    <section class="card">
      <h2>IV. Droits vs Croisés — schéma</h2>
      <p>On montre ici l'ordre des 8 conducteurs, vue face au clip (comme quand on regarde la fiche sertie).</p>
      <!-- legend -->
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <div style="display:flex;align-items:center;gap:6px"><span style="width:18px;height:12px;background:#ff9900;display:inline-block;border-radius:2px"></span><small>Pair 1 (Pins 1/2)</small></div>
        <div style="display:flex;align-items:center;gap:6px"><span style="width:18px;height:12px;background:#0066ff;display:inline-block;border-radius:2px"></span><small>Pair 2 (Pins 3/6)</small></div>
        <div style="display:flex;align-items:center;gap:6px"><span style="width:18px;height:12px;background:#00cc66;display:inline-block;border-radius:2px"></span><small>Pair 3 (Pins 4/5)</small></div>
        <div style="display:flex;align-items:center;gap:6px"><span style="width:18px;height:12px;background:#cccccc;display:inline-block;border-radius:2px"></span><small>Pair 4 (Pins 7/8)</small></div>
      </div>
      <!-- Straight cable diagram -->
      <div style="margin-top:8px">
        <strong>Câble droit (même ordonnancement aux 2 extrémités)</strong>
        <div style="display:flex;gap:18px;align-items:center;margin-top:8px;flex-wrap:wrap">
          <!-- left RJ45 -->
          <div>
            <div class="pin-row">
              <div class="pin" style="background:#ff9900">1</div>
              <div class="pin" style="background:#ffcc99">2</div>
              <div class="pin" style="background:#0066ff;color:#fff">3</div>
              <div class="pin" style="background:#99ccff">4</div>
              <div class="pin" style="background:#00cc66;color:#fff">5</div>
              <div class="pin" style="background:#b3ffd9">6</div>
              <div class="pin" style="background:#cccccc;color:#000">7</div>
              <div class="pin" style="background:#eeeeee;color:#000">8</div>
            </div>
            <div style="text-align:center;margin-top:6px;color:var(--muted)">Extrémité A</div>
          </div>
          <div style="flex:1">
            <div style="height:8px;background:linear-gradient(90deg,#ff9900 12.5%,#ffcc99 12.5% 25%,#0066ff 25% 37.5%,#99ccff 37.5% 50%,#00cc66 50% 62.5%,#b3ffd9 62.5% 75%,#cccccc 75% 87.5%,#eeeeee 87.5% 100%);border-radius:6px"></div>
            <div style="height:8px;background:linear-gradient(90deg,#ff9900 12.5%,#ffcc99 12.5% 25%,#0066ff 25% 37.5%,#99ccff 37.5% 50%,#00cc66 50% 62.5%,#b3ffd9 62.5% 75%,#cccccc 75% 87.5%,#eeeeee 87.5% 100%);border-radius:6px;margin-top:6px"></div>
          </div>
          <!-- right RJ45 -->
          <div>
            <div class="pin-row">
              <div class="pin" style="background:#ff9900">1</div>
              <div class="pin" style="background:#ffcc99">2</div>
              <div class="pin" style="background:#0066ff;color:#fff">3</div>
              <div class="pin" style="background:#99ccff">4</div>
              <div class="pin" style="background:#00cc66;color:#fff">5</div>
              <div class="pin" style="background:#b3ffd9">6</div>
              <div class="pin" style="background:#cccccc;color:#000">7</div>
              <div class="pin" style="background:#eeeeee;color:#000">8</div>
            </div>
            <div style="text-align:center;margin-top:6px;color:var(--muted)">Extrémité B</div>
          </div>
        </div>
      </div>
      <!-- Crossover -->
      <div style="margin-top:18px">
        <strong>Câble croisé (paires 1/2 ↔ 3/6 inversées)</strong>
        <div style="display:flex;gap:18px;align-items:center;margin-top:8px;flex-wrap:wrap">
          <!-- left RJ45 -->
          <div>
            <div class="pin-row">
              <div class="pin" style="background:#ff9900">1</div>
              <div class="pin" style="background:#ffcc99">2</div>
              <div class="pin" style="background:#0066ff;color:#fff">3</div>
              <div class="pin" style="background:#99ccff">4</div>
              <div class="pin" style="background:#00cc66;color:#fff">5</div>
              <div class="pin" style="background:#b3ffd9">6</div>
              <div class="pin" style="background:#cccccc;color:#000">7</div>
              <div class="pin" style="background:#eeeeee;color:#000">8</div>
            </div>
            <div style="text-align:center;margin-top:6px;color:var(--muted)">Extrémité A</div>
          </div>
          <div style="flex:1">
            <!-- show crossing -->
            <svg class="diagram" viewBox="0 0 560 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <!-- wires positions left to right -->
              <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#fff"/></marker></defs>
              <!-- background wires -->
              <rect x="0" y="12" width="560" height="8" fill="#ff9900"/>
              <rect x="0" y="24" width="560" height="8" fill="#ffcc99"/>
              <rect x="0" y="36" width="560" height="8" fill="#0066ff"/>
              <rect x="0" y="48" width="560" height="8" fill="#99ccff"/>
              <rect x="0" y="60" width="560" height="8" fill="#00cc66"/>
              <rect x="0" y="72" width="560" height="8" fill="#b3ffd9"/>
              <!-- crossing lines visual: swap 1-3 -->
              <g stroke="#ffffff" stroke-width="2" fill="none" opacity="0.6">
                <path d="M40 16 C 150 16, 340 40, 520 40" stroke="#ff9900"/>
                <path d="M40 40 C 150 40, 340 16, 520 16" stroke="#0066ff"/>
                <path d="M40 28 C 280 28, 360 28, 520 28" stroke="#ffcc99"/>
              </g>
            </svg>
            <div style="font-size:13px;color:var(--muted);margin-top:6px">Sur un câble croisé classique on échange la paire 1/2 (pins 1 & 2) avec la paire 3/6 (pins 3 & 6).</div>
          </div>
          <!-- right RJ45 (crossed) -->
          <div>
            <div class="pin-row">
              <!-- show swapped positions: pins 1-8 labels remain numeric -->
              <div class="pin" style="background:#0066ff;color:#fff">1</div>
              <div class="pin" style="background:#99ccff">2</div>
              <div class="pin" style="background:#ff9900">3</div>
              <div class="pin" style="background:#99ccff">4</div>
              <div class="pin" style="background:#00cc66;color:#fff">5</div>
              <div class="pin" style="background:#b3ffd9">6</div>
              <div class="pin" style="background:#cccccc;color:#000">7</div>
              <div class="pin" style="background:#eeeeee;color:#000">8</div>
            </div>
            <div style="text-align:center;margin-top:6px;color:var(--muted)">Extrémité B (croisée)</div>
          </div>
        </div>
      </div>
      <p class="note" style="margin-top:10px">Aujourd'hui la plupart des équipements supportent l'auto-MDI/MDIX → les câbles droits suffisent généralement. Utiliser un câble croisé seulement si un équipement ancien l'exige.</p>
    </section>
    <section class="card">
      <h2>V. Monobrins vs Multibrins</h2>
      <table>
        <thead><tr><th>Type</th><th>Caractéristiques</th><th>Usage</th></tr></thead>
        <tbody>
          <tr><td>Monobrin (solid)</td><td>Fil unique rigide, meilleure performance électrique, moins d'atténuation</td><td>Installations fixes (baie → prise murale), câblage structuré</td></tr>
          <tr><td>Multibrins (stranded)</td><td>Fils fins torsadés, très souples, plus résistants au mouvement</td><td>Cordons de raccordement, patchs, rangement flexible</td></tr>
        </tbody>
      </table>
      <p class="note">Monobrin : préférer pour permanence ; multibrins : pour cordons et mobilité.</p>
    </section>
    <section class="card">
      <h2>VI. Bonnes pratiques & checklist</h2>
      <ul>
        <li>Respecter longueur max 100 m pour une liaison cuivre (patch + horizontal + patch).</li>
        <li>Sertissage soigné : pas de torsion excessive des paires au sertissage & tester avec testeur RJ45.</li>
        <li>Étiqueter les câbles et documenter la baie de brassage.</li>
        <li>Choisir blindage adapté (S/FTP) si forte EMI ou proximité de sources électriques).</li>
        <li>Vérifier continuité & performance (wire map, attenuation, NEXT) après installation.</li>
      </ul>
    </section>
    <section class="card">
      <h2>VII. Quiz rapide</h2>
      <details><summary>Q1 — Quel connecteur avec Cat7 ?</summary><div style="margin-top:8px">Réponse : GG45 proposé mais RJ45 reste courant.</div></details>
      <details><summary>Q2 — Quelle paire est croisée sur un câble crossover ?</summary><div style="margin-top:8px">Réponse : 1/2 ↔ 3/6.</div></details>
      <details><summary>Q3 — Monobrin ou multibrins pour patchs ?</summary><div style="margin-top:8px">Réponse : multibrins (souples).</div></details>
    </section>
    <footer>Fiche synthétique — Câblage réseau · Bloc 1 · TSSR — version concise pour révision</footer>
  </div>
</body>
</html>

<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche — Adressage IP</title>
<style>
  :root{
    --bg:#0b1116;
    --card:#0c151a;
    --blue:#1e90ff;
    --red:#ff4d4f;
    --muted:#9eb0bf;
    --mono:"Fira Code", monospace;
  }
  body{
    margin:0;padding:20px;font-family:Inter,system-ui,Arial;color:#e6eef6;background:linear-gradient(180deg,var(--bg),#061018);line-height:1.5
  }
  .wrap{max-width:980px;margin:0 auto}
  header{display:flex;gap:12px;align-items:center;margin-bottom:14px}
  .logo{width:56px;height:56px;border-radius:8px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021127}
  h1{margin:0;font-size:18px}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--card),#071018);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--red);margin:10px 0 6px 0}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  ul{margin:6px 0 6px 18px}
  code{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:4px;border-radius:6px}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:600}
  .diagram{width:100%;height:auto;margin-top:12px}
  footer{color:var(--muted);font-size:13px;margin-top:12px;text-align:center}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="logo">IP</div>
  <div>
    <h1>La base des systèmes d'adressage IP</h1>
    <div class="meta">Bloc 2 · Adressage IP · Durée estimée : 1h</div>
  </div>
</header>

<section class="card">
  <h2>Résumé</h2>
  <p>Une adresse IP identifie de manière unique un appareil sur un réseau. Le protocole <strong>TCP/IP</strong> permet la communication des paquets entre machines. On distingue <strong>IPv4</strong> (32 bits) et <strong>IPv6</strong> (128 bits). Les adresses peuvent être <em>publiques</em> ou <em>privées</em>, <em>statiques</em> ou <em>dynamiques</em>.</p>
</section>

<section class="card">
  <h2>I. Modèles TCP/IP et OSI</h2>
  <p>Le modèle TCP/IP comprend 4 couches :</p>
  <ul>
    <li><strong>Couche réseau/host</strong> : physique + liaison</li>
    <li><strong>Couche Internet</strong> : envoi des paquets</li>
    <li><strong>Couche transport</strong> : TCP (fiable), UDP (rapide)</li>
    <li><strong>Couche application</strong> : interface utilisateur et applications</li>
  </ul>
  <h3>Correspondance avec le modèle OSI (7 couches)</h3>
  <table>
    <thead><tr><th>OSI</th><th>TCP/IP</th></tr></thead>
    <tbody>
      <tr><td>7 - Application</td><td>Application</td></tr>
      <tr><td>6 - Présentation</td><td>Application</td></tr>
      <tr><td>5 - Session</td><td>Application</td></tr>
      <tr><td>4 - Transport</td><td>Transport</td></tr>
      <tr><td>3 - Réseau</td><td>Internet</td></tr>
      <tr><td>2 - Liaison</td><td>Hôte/Réseau</td></tr>
      <tr><td>1 - Physique</td><td>Hôte/Réseau</td></tr>
    </tbody>
  </table>
</section>

<section class="card">
  <h2>II. Conversion binaire ↔ décimal</h2>
  <p>1 octet = 8 bits, valeurs de 2⁷ à 2⁰ :</p>
  <table>
    <thead><tr><th>Binaire</th><th>Décimal</th></tr></thead>
    <tbody>
      <tr><td>00000000</td><td>0</td></tr>
      <tr><td>00000001</td><td>1</td></tr>
      <tr><td>00000010</td><td>2</td></tr>
      <tr><td>00000100</td><td>4</td></tr>
      <tr><td>00001000</td><td>8</td></tr>
      <tr><td>00010000</td><td>16</td></tr>
      <tr><td>00100000</td><td>32</td></tr>
      <tr><td>01000000</td><td>64</td></tr>
      <tr><td>10000000</td><td>128</td></tr>
      <tr><td>11111111</td><td>255</td></tr>
    </tbody>
  </table>
</section>

<section class="card">
  <h2>III. Classes d'adresses IPv4</h2>
  <table>
    <thead><tr><th>Classe</th><th>Plage Décimale</th><th>Masque / Bits</th><th>Usage</th></tr></thead>
    <tbody>
      <tr><td>A</td><td>0.0.0.0 – 127.255.255.255</td><td>/8</td><td>Grand réseau, IP publiques & privées</td></tr>
      <tr><td>B</td><td>128.0.0.0 – 191.255.255.255</td><td>/16</td><td>Moyen réseau</td></tr>
      <tr><td>C</td><td>192.0.0.0 – 223.255.255.255</td><td>/24</td><td>Petit réseau</td></tr>
      <tr><td>D</td><td>224.0.0.0 – 239.255.255.255</td><td>-</td><td>Multicast</td></tr>
      <tr><td>E</td><td>240.0.0.0 – 255.255.255.255</td><td>-</td><td>Expérimental / réservé</td></tr>
    </tbody>
  </table>
  <p class="note">127.0.0.0 = localhost, 0.0.0.0 = route par défaut.</p>
</section>

<section class="card">
  <h2>IV. Adresses privées et publiques</h2>
  <table>
    <thead><tr><th>Classe</th><th>Privée</th><th>Exemples</th></tr></thead>
    <tbody>
      <tr><td>A</td><td>10.0.0.0 – 10.255.255.255</td><td>10.12.0.1</td></tr>
      <tr><td>B</td><td>172.16.0.0 – 172.31.255.255</td><td>172.20.1.1</td></tr>
      <tr><td>C</td><td>192.168.0.0 – 192.168.255.255</td><td>192.168.1.1</td></tr>
    </tbody>
  </table>
  <p>Les adresses publiques sont toutes les autres IP accessibles sur Internet.</p>
</section>

<section class="card">
  <h2>V. Exemple de calcul réseau</h2>
  <p>IP : 192.168.56.128 /24</p>
  <ul>
    <li>Binaire : 11000000.10101000.00111000.10000000</li>
    <li>Masque /24 : 11111111.11111111.11111111.00000000</li>
    <li>NetID : 192.168.56.0</li>
    <li>Broadcast : 192.168.56.255</li>
    <li>Plage hôtes : 192.168.56.1 → 192.168.56.254 (254 hôtes max)</li>
  </ul>
</section>

<section class="card">
  <h2>VI. Schéma des couches OSI / TCP-IP</h2>
  <svg class="diagram" viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg">
    <!-- Couche Application -->
    <rect x="0" y="0" width="350" height="40" fill="#1e90ff"/>
    <text x="175" y="25" text-anchor="middle" fill="#fff" font-size="14">OSI 7 - Application</text>
    <rect x="350" y="0" width="350" height="40" fill="#1e90ff"/>
    <text x="525" y="25" text-anchor="middle" fill="#fff" font-size="14">TCP/IP Application</text>
    <!-- Couche Présentation -->
    <rect x="0" y="40" width="350" height="40" fill="#6495ed"/>
    <text x="175" y="65" text-anchor="middle" fill="#fff" font-size="14">OSI 6 - Présentation</text>
    <rect x="350" y="40" width="350" height="40" fill="#1e90ff"/>
    <text x="525" y="65" text-anchor="middle" fill="#fff" font-size="14">TCP/IP Application</text>
    <!-- Couche Session -->
    <rect x="0" y="80" width="350" height="40" fill="#87cefa"/>
    <text x="175" y="105" text-anchor="middle" fill="#021127" font-size="14">OSI 5 - Session</text>
    <rect x="350" y="80" width="350" height="40" fill="#1e90ff"/>
    <text x="525" y="105" text-anchor="middle" fill="#fff" font-size="14">TCP/IP Application</text>
    <!-- Couche Transport -->
    <rect x="0" y="120" width="350" height="40" fill="#60b8ff"/>
    <text x="175" y="145" text-anchor="middle" fill="#021127" font-size="14">OSI 4 - Transport</text>
    <rect x="350" y="120" width="350" height="40" fill="#60b8ff"/>
    <text x="525" y="145" text-anchor="middle" fill="#021127" font-size="14">TCP/IP Transport</text>
    <!-- Couche Réseau -->
    <rect x="0" y="160" width="350" height="40" fill="#ff9900"/>
    <text x="175" y="185" text-anchor="middle" fill="#021127" font-size="14">OSI 3 - Réseau</text>
    <rect x="350" y="160" width="350" height="40" fill="#ff9900"/>
    <text x="525" y="185" text-anchor="middle" fill="#021127" font-size="14">TCP/IP Internet</text>
    <!-- Couche Liaison -->
    <rect x="0" y="200" width="350" height="40" fill="#00cc66"/>
    <text x="175" y="225" text-anchor="middle" fill="#021127" font-size="14">OSI 2 - Liaison</text>
    <rect x="350" y="200" width="350" height="40" fill="#00cc66"/>
    <text x="525" y="225" text-anchor="middle" fill="#021127" font-size="14">TCP/IP Host/Network</text>
    <!-- Couche Physique -->
    <rect x="0" y="240" width="350" height="40" fill="#009966"/>
    <text x="175" y="265" text-anchor="middle" fill="#fff" font-size="14">OSI 1 - Physique</text>
    <rect x="350" y="240" width="350" height="40" fill="#00cc66"/>
    <text x="525" y="265" text-anchor="middle" fill="#021127" font-size="14">TCP/IP Host/Network</text>
  </svg>
</section>


<section class="card">
  <h2>VII. Quiz rapide</h2>
  <details><summary>Q1 — Classe de 172.17.1.16 ?</summary><div style="margin-top:8px">Réponse : Classe B</div></details>
  <details><summary>Q2 — Adresse privée ou publique 172.17.1.16 ?</summary><div style="margin-top:8px">Réponse : Privée</div></details>
  <details><summary>Q3 — Combien de bits IPv4 ?</summary><div style="margin-top:8px">Réponse : 32 bits</div></details>
  <details><summary>Q4 — Nombre hôtes pour /24 ?</summary><div style="margin-top:8px">Réponse : 254 hôtes</div></details>
</section>

<footer>Fiche synthétique — Adressage IP · Bloc 2 · TSSR — version révision rapide</footer>
</div>
</body>
</html>


<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche — Configuration & sécurisation d'un réseau sans fil (Wi-Fi)</title>
<style>
  :root{
    --bg:#0b1116;
    --card:#0b1720;
    --muted:#9fb0bf;
    --blue:#1e90ff;
    --red:#ff4d4f;
    --accent:#60b8ff;
    --mono: "Fira Code", monospace;
  }
  /* Page layout */
  html,body{height:100%;margin:0;background:var(--bg);color:#e6eef6;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Arial;line-height:1.45}
  .wrap{max-width:1100px;margin:22px auto;padding:18px}
  header{display:flex;gap:14px;align-items:center;margin-bottom:18px}
  .logo{width:64px;height:64px;border-radius:10px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:800;color:#021127}
  h1{margin:0;font-size:20px}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--card),#071018);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:14px;box-shadow:0 8px 30px rgba(0,0,0,0.45)}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--red);margin:8px 0}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  ul{margin:6px 0 6px 18px}
  code,pre{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:6px;border-radius:6px;color:#d7f0ff}
  .diagram{width:100%;height:auto;margin-top:12px;border-radius:8px}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:700}
  .cols{display:grid;grid-template-columns:1fr 360px;gap:16px}
  .kpi{display:flex;gap:10px;flex-wrap:wrap}
  .pill{display:inline-block;padding:6px 10px;border-radius:999px;background:rgba(255,255,255,0.02);color:var(--muted);font-size:13px}
  footer{color:var(--muted);font-size:13px;margin-top:18px;text-align:center}
  /* Print layout for ultra-short A4 */
  @media print {
    body{background:#fff;color:#000}
    .wrap{max-width:780px;margin:0 auto;padding:0}
    .no-print{display:none}
    .print-card{page-break-after:always; padding:18mm}
    .print-recto, .print-verso{width:210mm;height:297mm}
    .small{font-size:12px}
  }
  @media (max-width:980px){
    .cols{grid-template-columns:1fr}
  }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">Wi-Fi</div>
      <div>
        <h1>Configuration & sécurisation d'un réseau sans fil (Wi-Fi)</h1>
        <div class="meta">Bloc 1 · Fiche complète + version imprimable A4 (recto/verso)</div>
      </div>
    </header>
    <!-- MAIN CONTENT -->
    <div class="card">
      <h2>Résumé</h2>
      <p>Le Wi-Fi (IEEE 802.11) permet la connexion sans câble entre appareils. Sécuriser un réseau implique : changer identifiants par défaut, activer un chiffrement fort (WPA2-AES ou WPA3), désactiver WPS, isoler invités, tenir le firmware à jour et surveiller les accès.</p>
      <div style="margin-top:8px">
        <span class="pill">SSID</span><span class="pill">WPA2 / WPA3</span><span class="pill">WPS off</span><span class="pill">Réseau invité</span>
      </div>
    </div>
    <div class="cols">
      <main>
        <section class="card">
          <h2>Concepts & définitions</h2>
          <ul>
            <li><strong>SSID</strong> — nom du réseau (Service Set Identifier).</li>
            <li><strong>BSSID</strong> — adresse MAC de l'AP (identifiant physique).</li>
            <li><strong>Canal</strong> — fréquence utilisée (2.4GHz : canaux 1..13 ; 5GHz : plus de canaux).</li>
            <li><strong>WPS</strong> — mécanisme d'association simplifiée (PIN / bouton) — souvent vulnérable.</li>
            <li><strong>Modes</strong> : Infrastructure (AP central) / Ad-Hoc (peer-to-peer).</li>
          </ul>
        </section>
        <section class="card">
          <h2>Méthode — Connexion client (Windows)</h2>
          <ol>
            <li>Paramètres → Réseau et Internet → Wi-Fi.</li>
            <li>Afficher les réseaux disponibles → choisir SSID → Se connecter.</li>
            <li>Entrer la clé (PSK). Cocher « Se connecter automatiquement » si voulu.</li>
          </ol>
        </section>
        <section class="card">
          <h2>Méthode — Accès & configuration du routeur</h2>
          <ol>
            <li>Ouvrir navigateur → `http://192.168.1.1` (ou IP du routeur).</li>
            <li>Se connecter (changer login/password admin par défaut).</li>
            <li>Section Wi-Fi → modifier : SSID, canal, largeur, mode radio (2.4/5GHz), sécurité (WPA2/WPA3), clé.</li>
            <li>Désactiver WPS ; activer réseau invité isolé ; sauvegarder & redémarrer si demandé.</li>
          </ol>
          <div style="margin-top:8px;color:var(--muted)">Astuce : 2.4GHz → choisir canal 1,6 ou 11 pour limiter chevauchement ; 20 MHz recommandé en 2.4GHz.</div>
        </section>
        <section class="card">
          <h2>Sécurisation — Étapes concrètes (ordre conseillé)</h2>
          <ol>
            <li>Changer les identifiants admin du routeur.</li>
            <li>Mettre à jour le firmware.</li>
            <li>Désactiver WPS (PIN/button).</li>
            <li>Activer WPA2-AES (ou WPA3) et définir un mot de passe fort (PSK).</li>
            <li>Créer réseau invité isolé (VLAN si possible).</li>
            <li>Désactiver administration distante ; limiter gestion à LAN ou câble.</li>
            <li>Filtrage MAC en complément (facultatif) ; limiter portée TX si nécessaire.</li>
            <li>Surveiller logs & appareils connectés.</li>
          </ol>
        </section>
        <section class="card">
          <h2>Commandes utiles — Linux (diagnostic & connexion)</h2>
          <pre><code>

# lister interfaces
ip link show

# scanner réseaux (wlan0)
sudo iwlist wlan0 scan | egrep 'ESSID|Channel|Quality|Encryption'
# ou NetworkManager
nmcli device wifi list

# se connecter via nmcli
nmcli device wifi connect "MonReseau" password "MonMotDePasse"

# état IP et route
ip addr show wlan0
ip route show

# signal
iwconfig wlan0
</code></pre>
        </section>
        <section class="card">
          <h2>Commandes utiles — Windows (PowerShell / cmd)</h2>
          <pre><code># lister adaptateurs
Get-NetAdapter

# lister réseaux (cmd)
netsh wlan show networks mode=bssid

# se connecter (profile présent)
netsh wlan connect name="MonProfile"

# IP / statut
ipconfig /all

# informations interface
netsh wlan show interfaces
</code></pre>
        </section>
        <section class="card">
          <h2>Dépannage rapide</h2>
          <ul>
            <li>Client sans IP → vérifier DHCP (`ip addr` / `ipconfig`).</li>
            <li>Signal faible → changer canal, rapprocher, ajuster antennes.</li>
            <li>Intermittent → test en 2.4 vs 5GHz ; interférences (micro-ondes, Bluetooth).</li>
            <li>Perte d'accès routeur → vérifier IP admin, reset physique si mot de passe perdu.</li>
          </ul>
        </section>
      </main>
      <aside>
        <section class="card">
          <h2>Réseau invité / IoT</h2>
          <ul>
            <li>Isoler IoT & invités dans VLAN séparés.</li>
            <li>Limiter accès LAN, autoriser uniquement Internet si requis.</li>
            <li>Attribuer durée DHCP courte pour invités (lease time).</li>
          </ul>
        </section>
        <section class="card">
          <h2>Paramètres & recommandations</h2>
          <table>
            <thead><tr><th>Réglage</th><th>Recommandation</th></tr></thead>
            <tbody>
              <tr><td>Chiffrement</td><td>WPA2-AES minimum (WPA3 si dispo)</td></tr>
              <tr><td>WPS</td><td>Désactiver</td></tr>
              <tr><td>Canal 2.4GHz</td><td>1 / 6 / 11</td></tr>
              <tr><td>Largeur canal 2.4GHz</td><td>20 MHz</td></tr>
              <tr><td>Mot de passe</td><td>12+ caractères, mix lettres/chiffres/symboles</td></tr>
            </tbody>
          </table>
        </section>
        <section class="card">
          <h2>Checklist sécurité rapide</h2>
          <ul>
            <li>Admin changé ? ✅</li>
            <li>Firmware à jour ? ✅</li>
            <li>WPS désactivé ? ✅</li>
            <li>WPA2/AES ou WPA3 ? ✅</li>
            <li>Réseau invité isolé ? ✅</li>
          </ul>
        </section>
        <section class="card">
          <h2>Mini quiz</h2>
          <details><summary>Q1 — Quelle fréquence utilise le Wi-Fi ?</summary><div style="margin-top:8px">Réponse : 2.4 GHz et 5 GHz (selon norme).</div></details>
          <details><summary>Q2 — Pourquoi désactiver WPS ?</summary><div style="margin-top:8px">Réponse : vulnérable (PIN facile à brute-force).</div></details>
          <details><summary>Q3 — Quel chiffrement éviter ?</summary><div style="margin-top:8px">Réponse : WEP (insecure), WPA-TKIP (obsolète).</div></details>
        </section>
      </aside>
    </div>
    <!-- SVG diagram -->
    <section class="card">
      <h2>Schéma — Architecture Wi-Fi & isolation (AP, clients, guest, LAN)</h2>
      <!-- simplified SVG -->
      <svg class="diagram" viewBox="0 0 900 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma WiFi">
        <!-- AP -->
        <rect x="360" y="20" width="180" height="80" rx="8" fill="#1e90ff"/>
        <text x="450" y="45" fill="#fff" font-size="14" text-anchor="middle">Point d'accès (AP)</text>
        <text x="450" y="64" fill="#eaf6ff" font-size="12" text-anchor="middle">SSID: MonReseau</text>
        <!-- Clients -->
        <rect x="60" y="140" width="120" height="60" rx="8" fill="#60b8ff"/>
        <text x="120" y="170" fill="#021127" font-size="13" text-anchor="middle">PC Client</text>
        <rect x="220" y="140" width="120" height="60" rx="8" fill="#60b8ff"/>
        <text x="280" y="170" fill="#021127" font-size="13" text-anchor="middle">Smartphone</text>
        <rect x="580" y="140" width="120" height="60" rx="8" fill="#60b8ff"/>
        <text x="640" y="170" fill="#021127" font-size="13" text-anchor="middle">Smart TV</text>
        <!-- Radio lines (curves) -->
        <path d="M420 100 Q 420 120 360 140" stroke="#a9e3ff" stroke-width="2" fill="none"/>
        <path d="M540 100 Q 540 120 640 140" stroke="#a9e3ff" stroke-width="2" fill="none"/>
        <path d="M420 100 Q 450 150 300 160" stroke="#a9e3ff" stroke-width="2" fill="none"/>
        <!-- Guest network -->
        <rect x="360" y="220" width="220" height="80" rx="8" fill="#ff6b6b"/>
        <text x="470" y="250" fill="#fff" font-size="13" text-anchor="middle">Réseau invité (Guest)</text>
        <text x="470" y="268" fill="#ffecec" font-size="12" text-anchor="middle">isolation client ↔ LAN</text>
        <!-- LAN / VLAN block -->
        <rect x="60" y="260" width="220" height="80" rx="8" fill="#00cc66"/>
        <text x="170" y="290" fill="#021127" font-size="13" text-anchor="middle">LAN (VLAN 10)</text>
        <text x="170" y="308" fill="#053723" font-size="12" text-anchor="middle">IoT, Serveurs</text>
        <!-- switch / internet -->
        <rect x="720" y="240" width="140" height="80" rx="8" fill="#0c1116" stroke="#60b8ff"/>
        <text x="790" y="270" fill="#60b8ff" font-size="13" text-anchor="middle">Switch / Internet</text>
        <!-- Links -->
        <path d="M450 100 V 220" stroke="#eaf6ff" stroke-width="2"/>
        <path d="M450 300 H 720" stroke="#eaf6ff" stroke-width="2"/>
        <path d="M180 220 H 360" stroke="#eaf6ff" stroke-width="2"/>
      </svg>
    </section>
    <footer class="no-print">
      Fiche générée — Configuration & sécurisation Wi-Fi · Bloc 1 · TSSR — Copie HTML pour VS Code
    </footer>
    <!-- PRINTABLE ULTRA-SHORT A4 (recto/verso) -->
    <div class="print-card no-screen" style="display:none">
      <!-- we'll replicate for browser printing using CSS @media print; but we also include visible print sections below -->
    </div>
    <!-- Visible printable block (so user can preview) -->
    <section class="card no-print">
      <h2>Version ultra-courte (A4 recto / verso) — Aperçu</h2>
      <div style="border:1px dashed rgba(255,255,255,0.04);padding:12px;border-radius:8px;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(0,0,0,0.02))">
        <h3>Recto — Récap technique</h3>
        <ul class="small">
          <li><strong>SSID / BSSID</strong> — nom du réseau / MAC AP</li>
          <li><strong>Canaux</strong> 2.4GHz : 1,6,11 ; 5GHz : 36,40,44... (selon pays)</li>
          <li><strong>Chiffrement</strong> : WPA2-AES (min) ; WPA3 si dispo</li>
          <li><strong>WPS</strong> : désactiver</li>
          <li><strong>Admin</strong> : changer login/mdp par défaut</li>
          <li><strong>Guest</strong> : réseau invité isolé (VLAN)</li>
          <li><strong>Firmware</strong> : maintenir à jour</li>
        </ul>
        <h3>Verso — Procédures courtes</h3>
        <ol class="small">
          <li>Accéder routeur : navigateur → `http://192.168.1.1` → login admin.</li>
          <li>Modifier Admin → Wi-Fi : SSID + WPA2/AES + mot de passe fort.</li>
          <li>Désactiver WPS, désactiver Admin distant.</li>
          <li>Activer réseau invité + isolation; limiter lease DHCP si besoin.</li>
          <li>Tests : `ip addr` / `ipconfig`, `nmcli device wifi list`, tester signal & connexion.</li>
        </ol>
        <div style="margin-top:8px;color:var(--muted);font-size:13px">Imprimer : Fichier → Imprimer → sélectionner orientation portrait, 1 page recto puis verso.</div>
      </div>
    </section>
  </div>
</body>
</html>


<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Les principes de base de la téléphonie IP / SIP — Fiche</title>
<style>
  :root{
    --bg:#081018;
    --panel:#0c1720;
    --muted:#9fb0bf;
    --blue:#1e90ff;
    --green:#00cc66;
    --red:#ff6b6b;
    --mono: "Fira Code", monospace;
  }
  html,body{height:100%;margin:0;background:var(--bg);color:#e6eef6;font-family:Inter,system-ui,Arial;line-height:1.45}
  .wrap{max-width:1100px;margin:20px auto;padding:18px}
  header{display:flex;gap:14px;align-items:center;margin-bottom:14px}
  .logo{width:64px;height:64px;border-radius:10px;background:linear-gradient(135deg,var(--blue),#60b8ff);display:flex;align-items:center;justify-content:center;font-weight:800;color:#021127}
  h1{margin:0;font-size:20px}
  .meta{color:var(--muted);font-size:13px}
  .card{background:linear-gradient(180deg,var(--panel),#071018);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px;box-shadow:0 8px 30px rgba(0,0,0,0.45)}
  h2{color:var(--blue);margin:0 0 8px 0}
  h3{color:var(--green);margin:8px 0}
  p,li{font-size:14px}
  table{width:100%;border-collapse:collapse;margin:10px 0;font-size:14px}
  th,td{padding:8px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  th{color:var(--muted);font-size:13px}
  code,pre{font-family:var(--mono);background:rgba(255,255,255,0.02);padding:8px;border-radius:6px;color:#d7f0ff;display:block;overflow:auto}
  .diagram{width:100%;height:auto;margin-top:12px;border-radius:8px}
  .cols{display:grid;grid-template-columns:1fr 360px;gap:16px}
  details{background:rgba(255,255,255,0.02);padding:8px;border-radius:8px}
  summary{cursor:pointer;color:var(--blue);font-weight:700}
  footer{color:var(--muted);font-size:13px;margin-top:18px;text-align:center}
  @media(max-width:980px){.cols{grid-template-columns:1fr}}
  @media print {
    body{background:#fff;color:#000}
    .no-print{display:none}
    .wrap{max-width:780px;padding:6mm}
  }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">SIP</div>
      <div>
        <h1>Les principes de base de la téléphonie IP / SIP — Fiche</h1>
        <div class="meta">PABX · IPBX · Centrex · SIP · RTP · Codecs · QoS · Sécurité · Commandes</div>
      </div>
    </header>
    <section class="card">
      <h2>Résumé rapide</h2>
      <p>La téléphonie IP (VoIP / ToIP) transporte la voix sous forme de paquets IP. <strong>SIP</strong> gère l'établissement/contrôle de session (signalisation) ; <strong>RTP</strong> transporte le media (voix). Les éléments clés : IPBX (serveur SIP), trunk SIP (liaison opérateur), téléphones IP (IP phone), QoS, PoE et sécurité (TLS/SRTP, firewall).</p>
    </section>
    <div class="cols">
      <main>
        <section class="card">
          <h2>1. Définitions essentielles</h2>
          <ul>
            <li><strong>PABX</strong> : autocommutateur privé traditionnel (circuit switching, lignes analogiques / RNIS).</li>
            <li><strong>IPBX</strong> : PABX sur IP (commutation par paquets). Offre fonctions avancées (CTI, messagerie unifiée, mobilité).</li>
            <li><strong>Centrex</strong> : IPBX hébergé (SaaS) — opérateur fournit le service dans le cloud.</li>
            <li><strong>SIP</strong> (Session Initiation Protocol) : protocole de signalisation (RFC 3261) — ouvre/contrôle/ferme sessions.</li>
            <li><strong>RTP</strong> (Real-time Transport Protocol) : transporte flux audio/vidéo ; associé à RTCP pour métriques.</li>
            <li><strong>Codecs</strong> : G.711 (µ-law / A-law, 64 kbps), G.729 (8 kbps), OPUS (large bande variable), etc.</li>
            <li><strong>Trunk SIP</strong> : canal logique chez un opérateur pour faire sortir/entrer les appels (remplace T0/T2).</li>
            <li><strong>PoE</strong> (Power over Ethernet) : alimente IP phone via switch (IEEE 802.3af/at/bt).</li>
          </ul>
        </section>
        <section class="card">
          <h2>2. Architecture & schémas</h2>
          <h3>PABX vs IPBX vs Centrex (schéma)</h3>
          <!-- Simple SVG comparison -->
          <svg class="diagram" viewBox="0 0 980 240" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <!-- PABX -->
            <rect x="20" y="20" width="280" height="200" rx="8" fill="#15394a" stroke="#1e90ff"/>
            <text x="160" y="48" fill="#1e90ff" font-size="14" text-anchor="middle">PABX (RTC)</text>
            <text x="160" y="68" fill="#cfefff" font-size="12" text-anchor="middle">Lignes analogiques / RNIS</text>
            <rect x="40" y="100" width="80" height="40" rx="6" fill="#1e90ff"/><text x="80" y="125" fill="#021127" font-size="12" text-anchor="middle">Téléphones</text>
            <rect x="160" y="100" width="80" height="40" rx="6" fill="#1e90ff"/><text x="200" y="125" fill="#021127" font-size="12" text-anchor="middle">Trunk RNIS</text>
            <!-- IPBX -->
            <rect x="350" y="20" width="280" height="200" rx="8" fill="#102a16" stroke="#00cc66"/>
            <text x="490" y="48" fill="#00cc66" font-size="14" text-anchor="middle">IPBX (On-prem)</text>
            <text x="490" y="68" fill="#cfefff" font-size="12" text-anchor="middle">SIP, RTP, VoIP</text>
            <rect x="370" y="100" width="80" height="40" rx="6" fill="#00cc66"/><text x="410" y="125" fill="#021127" font-size="12" text-anchor="middle">IP Phones</text>
            <rect x="490" y="100" width="80" height="40" rx="6" fill="#00cc66"/><text x="530" y="125" fill="#021127" font-size="12" text-anchor="middle">Trunk SIP</text>
            <!-- Centrex -->
            <rect x="680" y="20" width="280" height="200" rx="8" fill="#2b163a" stroke="#ff6b6b"/>
            <text x="820" y="48" fill="#ff6b6b" font-size="14" text-anchor="middle">Centrex (Cloud)</text>
            <text x="820" y="68" fill="#cfefff" font-size="12" text-anchor="middle">IPBX hébergé — SaaS</text>
            <rect x="700" y="100" width="80" height="40" rx="6" fill="#ff6b6b"/><text x="740" y="125" fill="#021127" font-size="12" text-anchor="middle">IP Phones</text>
            <rect x="820" y="100" width="80" height="40" rx="6" fill="#ff6b6b"/><text x="860" y="125" fill="#021127" font-size="12" text-anchor="middle">Opérateur Cloud</text>
            <!-- Arrows / Internet -->
            <path d="M240 120 H 350" stroke="#9fb0bf" stroke-width="2" marker-end="url(#arrow)"/>
            <path d="M630 120 H 680" stroke="#9fb0bf" stroke-width="2" marker-end="url(#arrow)"/>
            <defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#9fb0bf"/></marker></defs>
          </svg>
        </section>
        <section class="card">
          <h2>3. SIP : principes et messages</h2>
          <p>SIP gère la signalisation : <strong>INVITE</strong> (ouvrir session), <strong>100-Trying / 180-Ringing / 200-OK</strong>, <strong>ACK</strong>, <strong>BYE</strong> (terminer). SIP transporte aussi la description des flux media via <strong>SDP</strong> (ports RTP, codecs).</p>
          <h3>Exemple simplifié d'échange SIP (INVITE)</h3>
          <pre><code>        
  Client A -> Proxy/Registrar : INVITE sip:bob@example.com SIP/2.0
Proxy -> Server B : INVITE ...
Server B -> Proxy : 180 Ringing
Server B -> Proxy : 200 OK (SDP with media=RTP  10.0.0.5:40000, codec=PCMU)
Proxy -> Client A : 200 OK
Client A -> Server B : ACK
Media (RTP) flows between A and B on UDP ports announced in SDP
</code></pre>
          <p><strong>Remarque :</strong> SIP use généralement le port 5060 (UDP/TCP) pour non-chiffré, 5061 pour TLS. Les flux RTP utilisent des ports dynamiques (ex. 10000-20000).</p>
        </section>
        <section class="card">
          <h2>4. RTP & codecs</h2>
          <ul>
            <li><strong>RTP</strong> : transport média (UDP). Paquets contiennent payload codec (PCM, G.729...).</li>
            <li><strong>RTCP</strong> : statistique (jitter, packet loss, MOS).</li>
            <li><strong>Codecs</strong> : G.711 (µ/A-law) → qualité téléphonique, 64 kbps ; G.729 → compression 8 kbps (licence) ; OPUS → large bande, adaptatif.</li>
            <li><strong>NAT/Firewall</strong> : NAT traverse nécessaire pour RTP (STUN/TURN/ICE). ALG SIP dans routeur peut créer des problèmes.</li>
          </ul>
        </section>
        <section class="card">
          <h2>5. Ports & plages courantes</h2>
          <table>
            <thead><tr><th>Service</th><th>Port / Proto</th><th>Remarque</th></tr></thead>
            <tbody>
              <tr><td>SIP non sécurisé</td><td>5060 UDP / TCP</td><td>signalisation</td></tr>
              <tr><td>SIP TLS</td><td>5061 TCP/TLS</td><td>signalisation chiffrée</td></tr>
              <tr><td>RTP (media)</td><td>10000–20000 UDP (exemple)</td><td>configurable sur IPBX</td></tr>
              <tr><td>RTCP</td><td>ports RTP+1 UDP</td><td>statistiques</td></tr>
              <tr><td>Web (UI)</td><td>80/443 TCP</td><td>gestion IPBX</td></tr>
            </tbody>
          </table>
        </section>
        <section class="card">
          <h2>6. Exemples de configuration & commandes utiles</h2>
          <h3>Asterisk (exemples)</h3>
          <p>Pour chan_sip (ancien) — fichier `/etc/asterisk/sip.conf` :</p>
          <pre><code>[general]
context=public
allowguest=no
srvlookup=yes
udpbindaddr=0.0.0.0
tcpenable=yes

[1001]
type=peer
host=dynamic
secret=MonSecretFort
context=internal
disallow=all
allow=ulaw,alaw
</code></pre>
          <p>Pour pjsip (nouveau) — fichier `pjsip.conf` :</p>
          <pre><code>[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0

[endpoint-1001]
type=endpoint
aors=1001
auth=auth1001
context=internal
allow=ulaw,alaw

[aors]
type=aor
max_contacts=1

[auth1001]
type=auth
auth_type=userpass
password=MonSecret
username=1001
</code></pre>
          <h3>Commandes Asterisk (CLI)</h3>
          <pre><code>asterisk -rvv
sip show peers          # chan_sip
pjsip show endpoints    # pjsip
core show channels
rtp set debug on        # debug RTP packets
sip set debug on        # debug SIP messages
</code></pre>
          <h3>Linux / réseau</h3>
          <pre><code>

# capture SIP / RTP
sudo tcpdump -n -s0 -A udp port 5060 or portrange 10000-20000

# vérifier NAT / iptables (ex)
sudo iptables -L -n
# tester latence/jitter
ping 8.8.8.8
# test SIP (sipsak, sipcli)
sipsak -v -s sip:1001@pbx.example.com
</code></pre>
        </section>
        <section class="card">
          <h2>7. QoS, VLAN & PoE (bonnes pratiques réseau)</h2>
          <ul>
            <li><strong>QoS</strong> : marquer DSCP (EF 46) pour RTP ; prioriser dans switch & routeur pour éviter jitter.</li>
            <li><strong>Voice VLAN</strong> : séparer ToIP (VLAN 10) du data (VLAN 20) pour performance et sécurité.</li>
            <li><strong>PoE</strong> : utiliser switch PoE (802.3af/at) pour alimenter IP phones.</li>
          </ul>
          <p>Exemples de configuration (Cisco IOS) — marquage DSCP :</p>
          <pre><code>class-map match-any VOICE
 match ip dscp ef

policy-map QOS
 class VOICE
  priority percent 70
 class class-default
  fair-queue
</code></pre>
        </section>
        <section class="card">
          <h2>8. Sécurité SIP / VoIP</h2>
          <ul>
            <li><strong>TLS</strong> pour chiffrer signalisation SIP (port 5061).</li>
            <li><strong>SRTP</strong> pour chiffrer média (RTP) — évite écoute passive.</li>
            <li><strong>Firewall</strong> : n'ouvrir que ports nécessaires, utiliser SBC (Session Border Controller) pour protéger IPBX et NAT traversal.</li>
            <li><strong>Fail2ban / rate limiting</strong> : bloquer bruteforce SIP (ex. registration attempts).</li>
            <li><strong>NAT</strong> : préférer STUN/TURN/ICE pour clients derrière NAT ; attention aux SIP ALGs des routeurs.</li>
          </ul>
          <p>Exemple de règles iptables simplifiées (protection basique)</p>
          <pre><code># autoriser SIP + RTP (exemple)
iptables -A INPUT -p udp --dport 5060 -j ACCEPT
iptables -A INPUT -p tcp --dport 5061 -j ACCEPT
iptables -A INPUT -p udp --dport 10000:20000 -j ACCEPT
# bloquer scans / rate limit
iptables -A INPUT -p udp --dport 5060 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
</code></pre>
        </section>
        <section class="card">
          <h2>9. Déploiement & checklist</h2>
          <ol>
            <li>Planifier VLANs & QoS → définir DSCP / prioritisation.</li>
            <li>Choisir IPBX on-prem ou Centrex selon coût / fonctionnalités.</li>
            <li>Configurer trunk SIP chez opérateur (auth, IP/username, codecs acceptés, NAT settings).</li>
            <li>Configurer IP phones : provisioning automatique (HTTP/HTTPS), PoE, VLAN voice tag.</li>
            <li>Activer TLS/SRTP si exigences RGPD/confidentialité.</li>
            <li>Tester : appels internes, appels externes, qualité (MOS), montée en charge.</li>
            <li>Moniteur : RTCP stats, logs, alertes de sécurité.</li>
          </ol>
        </section>
      </main>
      <aside>
        <section class="card">
          <h2>Mini-glossaire</h2>
          <ul>
            <li><strong>SIP</strong> : signalisation (INVITE, ACK, BYE).</li>
            <li><strong>SDP</strong> : échange d'offres/paramètres média (ports, codecs).</li>
            <li><strong>RTP / RTCP</strong> : transport média / métriques.</li>
            <li><strong>Trunk SIP</strong> : canal opérateur pour appels PSTN via IP.</li>
            <li><strong>SBC</strong> : Session Border Controller (sécurité & NAT).</li>
          </ul>
        </section>
        <section class="card">
          <h2>Exemples rapides (trunk SIP)</h2>
          <p>Paramètres typiques à fournir à l'opérateur :</p>
          <ul>
            <li>Adresse SIP trunk : sip.opérateur.tld</li>
            <li>Auth : username / password (ou IP auth)</li>
            <li>Codecs supportés : PCMU (G.711), opus, G.729 (si licence)</li>
            <li>RTP port range : ex. 10000-20000</li>
            <li>DTMF : RFC2833 (out-of-band) ou SIP INFO</li>
          </ul>
        </section>
        <section class="card">
          <h2>Mini-quiz</h2>
          <details><summary>Q1 — Quel port SIP non sécurisé ?</summary><div style="margin-top:8px">Réponse : 5060 (UDP/TCP).</div></details>
          <details><summary>Q2 — RTP = ?</summary><div style="margin-top:8px">Réponse : transport du média (voix, via UDP).</div></details>
          <details><summary>Q3 — PoE utile pour IP Phones ?</summary><div style="margin-top:8px">Réponse : Oui (802.3af/at).</div></details>
        </section>
      </aside>
    </div>
    <!-- SIP vs RTP diagram -->
    <section class="card">
      <h2>Schéma : SIP (signalisation) vs RTP (media)</h2>
      <svg class="diagram" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <!-- Clients -->
        <rect x="40" y="20" width="160" height="60" rx="8" fill="#60b8ff"/><text x="120" y="55" fill="#021127" font-size="13" text-anchor="middle">IP Phone A</text>
        <rect x="680" y="20" width="160" height="60" rx="8" fill="#60b8ff"/><text x="760" y="55" fill="#021127" font-size="13" text-anchor="middle">IP Phone B</text>
        <!-- IPBX -->
        <rect x="360" y="20" width="180" height="80" rx="8" fill="#102a16"/><text x="450" y="54" fill="#00cc66" font-size="14" text-anchor="middle">IPBX (SIP Server)</text>
        <!-- SIP signaling arrows -->
        <path d="M200 50 H 360" stroke="#ffd57f" stroke-width="3" marker-end="url(#arr)"/><text x="280" y="40" fill="#ffd57f" font-size="12" text-anchor="middle">SIP INVITE / 200 OK (5060)</text>
        <path d="M540 50 H 680" stroke="#ffd57f" stroke-width="3" marker-end="url(#arr)"/>
        <!-- RTP flows (media) -->
        <path d="M200 140 C400 100 500 100 700 140" stroke="#a9e3ff" stroke-width="3" fill="none" marker-end="url(#arr)"/>
        <text x="450" y="130" fill="#a9e3ff" font-size="12" text-anchor="middle">RTP Media (UDP ports e.g. 10000-20000)</text>
        <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#dfefff"/></marker></defs>
        <!-- legends -->
        <rect x="40" y="180" width="240" height="64" rx="8" fill="#071017" stroke="#60b8ff"/>
        <text x="160" y="200" fill="#60b8ff" font-size="13" text-anchor="middle">SIGNALISATION — SIP (INVITE, 200 OK, ACK)</text>
        <text x="160" y="216" fill="#9fb0bf" font-size="12" text-anchor="middle">port 5060 / 5061(TLS)</text>
        <rect x="420" y="180" width="360" height="64" rx="8" fill="#071017" stroke="#a9e3ff"/>
        <text x="600" y="200" fill="#a9e3ff" font-size="13" text-anchor="middle">MEDIA — RTP / RTCP (voice)</text>
        <text x="600" y="216" fill="#9fb0bf" font-size="12" text-anchor="middle">ports dynamiques (configurables)</text>
      </svg>
    </section>
    <section class="card no-print">
      <h2>Version ultra-courte (A4 recto/verso) — Aperçu</h2>
      <div style="border-radius:8px;padding:12px;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(0,0,0,0.02))">
        <h3>Recto — Récap technique</h3>
        <ul>
          <li><strong>SIP</strong> = signalisation (5060/5061)</li>
          <li><strong>RTP</strong> = média (UDP ports 10k-20k)</li>
          <li><strong>Codecs</strong> : G.711 (64kbps), G.729 (8kbps), OPUS</li>
          <li><strong>PoE</strong> pour IP phones ; VLAN voice + QoS DSCP EF</li>
          <li><strong>Sécurité</strong> : TLS + SRTP ; SBC en front office</li>
        </ul>
        <h3>Verso — Procédures courtes</h3>
        <ol>
          <li>Plan VLAN & QoS → voice VLAN, DSCP EF.</li>
          <li>Configurer IPBX : endpoints, auth, RTP range, codecs.</li>
          <li>Configurer trunk SIP chez opérateur (auth, codecs, NAT).</li>
          <li>Provisioning téléphones (HTTP/HTTPS), activer PoE, tester appels internes & externes.</li>
          <li>Activer TLS/SRTP et monitoring RTCP/MOS.</li>
        </ol>
      </div>
    </section>
    <footer class="no-print">
      Fiche générée — Téléphonie IP / SIP · 
    </footer>
  </div>
</body>
</html>


<html lang="fr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Fiche courte — E-mail & visioconf (Gmail / Meet / Thunderbird / Chat)</title>
<style>
  :root{
    --bg:#071221; --panel:#0b1720; --muted:#9fb0bf; --blue:#1e90ff; --accent:#60b8ff; --mono: "Fira Code", monospace;
  }
  html,body{height:100%;margin:0;background:var(--bg);color:#e6eef6;font-family:Inter,system-ui,Segoe UI,Arial;}
  .wrap{max-width:900px;margin:18px auto;padding:16px}
  .card{background:linear-gradient(180deg,var(--panel),#071018);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);margin-bottom:12px}
  h1{margin:0 0 6px 0;color:var(--blue);font-size:18px}
  h2{margin:8px 0;color:var(--accent);font-size:15px}
  p,li{font-size:14px;margin:6px 0}
  ul{margin:6px 0 6px 18px}
  pre{background:rgba(255,255,255,0.02);padding:8px;border-radius:6px;font-family:var(--mono);overflow:auto}
  table{width:100%;border-collapse:collapse;margin-top:6px}
  th,td{padding:6px;border-bottom:1px dashed rgba(255,255,255,0.03);text-align:left}
  .muted{color:var(--muted);font-size:13px}
  .small{font-size:13px;color:var(--muted)}
  .k{display:flex;gap:8px;flex-wrap:wrap}
  .pill{background:rgba(255,255,255,0.02);padding:6px 10px;border-radius:999px;color:var(--muted);font-size:13px}
  svg{width:100%;height:auto;border-radius:6px;margin-top:8px}
  @media print{
    body{background:#fff;color:#000}
    .no-print{display:none}
    .wrap{max-width:210mm;padding:8mm}
  }
</style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Fiche courte — Communication par e-mail & visioconférence</h1>
      <div class="muted">Synthèse rapide • Procédures essentielles • Règles de rédaction</div>
    </div>
    <section class="card">
      <h2>Essentiel (1 phrase)</h2>
      <p>Le courriel sert à transmettre des informations formelles et conservables ; le chat/visioconf (Google Meet, Slack, Teams) sert aux échanges instantanés et à la collaboration en direct.</p>
    </section>
    <section class="card">
      <h2>Créer un compte Gmail — étapes rapides</h2>
      <ol>
        <li>Aller sur <strong>accounts.google.com</strong> → « Créer un compte ». Choisir un identifiant simple (prenom.nom).</li>
        <li>Renseigner nom, date de naissance, téléphone (récupération) → accepter CGU.</li>
        <li>Configurer validation 2FA (recommandé) : SMS ou application d'authentification.</li>
      </ol>
      <p class="small">Astuce : activer la récupération (téléphone / e-mail secondaire) pour retrouver l'accès facilement.</p>
    </section>
    <section class="card">
      <h2>Rédiger un e-mail — structure & règles</h2>
      <ul>
        <li><strong>Objet</strong> court et précis (ex : « RDV projet — 24/10 14h »).</li>
        <li>Salutation brève (« Bonjour Mme X, »), 1 à 3 paragraphes clairs, formule de politesse ("Cordialement").</li>
        <li>Eviter MAJUSCULES, émoticônes abusives ; relire l'orthographe.</li>
        <li>Utiliser <strong>À</strong> pour destinataires principaux, <strong>Cc</strong> pour info, <strong>Cci</strong> pour copie cachée.</li>
      </ul>
      <p class="small">Quand joindre un fichier ? si ≤ 25 Mo en PJ, sinon générer un lien Drive/WeTransfer et expliciter dans le message.</p>
    </section>
    <section class="card">
      <h2>Pièces jointes — bonnes pratiques</h2>
      <ol>
        <li>Compresser si plusieurs fichiers (.zip) ; nommer clairement (Projet_Nom_date.pdf).</li>
        <li>Pour gros fichiers → Google Drive / Dropbox / WeTransfer → partager lien et droits (lecture ou téléchargement).</li>
        <li>Attention aux données sensibles : chiffrer ou demander communication sécurisée.</li>
      </ol>
    </section>
    <section class="card">
      <h2>Créer une réunion (Google Agenda → Meet)</h2>
      <ol>
        <li>Ouvrir Google Agenda → Nouveau évènement → ajouter titre/date/heure.</li>
        <li>Cliquer « Ajouter une visioconférence Google Meet » → copier le lien.</li>
        <li>Ajouter invités (emails) → envoyer l'invitation. Joindre l'ordre du jour en description.</li>
      </ol>
      <p class="small">Pendant la réunion : partage d'écran pour demo, chat pour liens/documents, enregistrer si accord des participants.</p>
    </section>
    <section class="card">
      <h2>Thunderbird — config rapide (IMAP recommandé)</h2>
      <ul>
        <li>Installer Thunderbird → Fichier → Nouveau → Compte Courriel.</li>
        <li>Saisir e-mail/mdp → laisser détection automatique → choisir <strong>IMAP</strong> (garder messages sur serveur).</li>
        <li>Synchroniser dossiers / exporter contacts si besoin.</li>
      </ul>
      <p class="small">POP3 télécharge et retire du serveur (pas recommandé si multi-appareils).</p>
    </section>
    <section class="card">
      <h2>Chat & visioconf — choix rapides</h2>
      <table>
        <thead><tr><th>Usage</th><th>Outil recommandé</th></tr></thead>
        <tbody>
          <tr><td>Chat pro, canaux, intégrations</td><td>Slack / Microsoft Teams</td></tr>
          <tr><td>Visioconf simple intégrée (agenda)</td><td>Google Meet</td></tr>
          <tr><td>Salle de conférence / e-learning</td><td>BigBlueButton / Zoom</td></tr>
        </tbody>
      </table>
      <p class="small">Règle : pour info officielle → envoyer e-mail ; pour discussion rapide → chat ; pour décision collective → visioconf + compte rendu.</p>
    </section>
    <section class="card">
      <h2>Raccourcis & petites commandes utiles</h2>
      <ul>
        <li>Gmail : <code>c</code> (composer), <code>/</code> (rechercher), <code>r</code> (répondre), <code>f</code> (transférer). Activez les raccourcis dans Paramètres.</li>
        <li>Thunderbird : <code>Ctrl+N</code> (nouveau message), <code>Ctrl+Shift+M</code> (envoyer/recevoir).</li>
        <li>Meet : partager écran → bouton « Présenter maintenant » ; couper micro/caméra depuis l'interface.</li>
      </ul>
    </section>
    <section class="card">
      <h2>Bonnes pratiques résumé (checklist)</h2>
      <div class="k">
        <div class="pill">Objet précis</div>
        <div class="pill">PJ ≤ 25Mo ou lien</div>
        <div class="pill">IMAP pour multi-appareils</div>
        <div class="pill">2FA activé</div>
        <div class="pill">Relire avant envoi</div>
      </div>
    </section>
    <section class="card">
      <h2>Mini-schéma : flux communication</h2>
      <svg viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="schéma mail chat visio">
        <rect x="30" y="20" width="220" height="80" rx="8" fill="#1e90ff"/>
        <text x="140" y="55" fill="#021127" font-size="13" text-anchor="middle">E-mail (Gmail/IMAP)</text>
        <rect x="340" y="20" width="220" height="80" rx="8" fill="#60b8ff"/>
        <text x="450" y="55" fill="#021127" font-size="13" text-anchor="middle">Chat (Slack/Teams)</text>
        <rect x="650" y="20" width="220" height="80" rx="8" fill="#00cc66"/>
        <text x="760" y="55" fill="#021127" font-size="13" text-anchor="middle">Visioconf (Meet)</text>
        <path d="M250 60 H 340" stroke="#dfefff" stroke-width="2" marker-end="url(#arr)"/>
        <path d="M560 60 H 650" stroke="#dfefff" stroke-width="2" marker-end="url(#arr)"/>
        <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#dfefff"/></marker></defs>
        <text x="140" y="115" fill="#9fb0bf" font-size="12" text-anchor="middle">Conserver trace / formel</text>
        <text x="450" y="115" fill="#9fb0bf" font-size="12" text-anchor="middle">Rapide, informel, intégré</text>
        <text x="760" y="115" fill="#9fb0bf" font-size="12" text-anchor="middle">Réunion / démonstration</text>
      </svg>
    </section>
    <section class="card">
      <h2>Ultra-court pour l'examen (1 page)</h2>
      <p class="small"><strong>À retenir :</strong> E-mail = trace & formel (objet, salutation, PJ ≤25Mo, signature). Chat = conversation rapide. Meet = visioconf + partage d'écran. Thunderbird : IMAP si multi-appareils. Sécurité : 2FA, attention aux PJ sensibles.</p>
    </section>
  </div>
</body>
</html>

<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Collaborer avec les apps Google</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
    h1, h2, h3 { color: #1a73e8; }
    ul { margin: 5px 0 15px 20px; }
    li { margin-bottom: 5px; }
    table { border-collapse: collapse; margin-bottom: 20px; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    th { background-color: #f2f2f2; }
    .procedure { background-color: #eef5ff; padding: 10px; border-left: 4px solid #1a73e8; margin-bottom: 15px; }
</style>
</head>
<body>
<h1>Collaborer avec les apps Google</h1>
<h2>Objectif</h2>
<p>Comprendre et utiliser les applications bureautiques de Google pour créer, partager et collaborer sur des documents (texte, tableur, présentation, formulaire) et gérer les droits d’accès.</p>
<hr>
<h2>Concepts clés</h2>
<h3>I. Applications bureautiques de Google</h3>
<p><strong>Contexte :</strong> Suite bureautique en ligne pour collaborer sur tous types de documents via <strong>Google Drive</strong> (cloud). Partage possible en lecture seule, commentaires ou modification.</p>
<h4>A. Google Drive</h4>
<ul>
    <li>Stockage en ligne : 15 Go gratuits.</li>
    <li>Créer, importer, organiser, dupliquer, déplacer, supprimer documents.</li>
    <li>Navigation : <strong>Mon Drive</strong>, <strong>Partagés avec moi</strong>, <strong>Récents</strong>, <strong>Suivis</strong>, <strong>Corbeille</strong>.</li>
</ul>
<div class="procedure">  
    <strong>Exemple d’action :</strong> <br>

    Pour supprimer un fichier : sélectionner le fichier (cocher la case), puis cliquer sur l'icône 
    <strong>Corbeille</strong> en haut. 
</div>
<h4>B. Google Docs</h4>
<ul>
    <li>Traitement de texte avec styles, en-têtes/pieds, insertion d’images et liens.</li>
    <li>Plan et table des matières pour navigation rapide.</li>
    <li>Vérification orthographique et dictionnaire personnel.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Pour appliquer un style : <em>Menu Format > Style de paragraphes > Choisir ou créer un style</em>.
</div>
<h4>C. Google Sheets</h4>
<ul>
    <li>Tableur pour créer des feuilles avec formules, fonctions et mise en forme.</li>
    <li>Tri et filtres pour afficher les données souhaitées.</li>
    <li>Fonctions courantes : SUM, AVERAGE, COUNT, MAX, MIN.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Ajouter une nouvelle feuille : cliquer sur le bouton 
    <strong>+</strong> en bas à gauche.
</div>
<h4>D. Google Slides</h4>
<ul>
    <li>Création de présentations animées (diaporama).</li>
    <li>Thèmes et mises en page préconfigurés ou personnalisables.</li>
    <li>Insertion de médias : images, vidéos, audio, tableaux Sheets.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Pour insérer une image : <em>Menu Insertion > Image > Choisir l’emplacement</em>.
</div>
<h4>E. Google Forms</h4>
<ul>
    <li>Création de formulaires, sondages et quiz.</li>
    <li>Types de questions : courte, paragraphe, choix multiples, cases à cocher, liste déroulante, échelle linéaire, grille, date/heure.</li>
    <li>Sections conditionnelles selon réponses précédentes.</li>
    <li>Analyse des réponses via graphiques ou export vers Sheets.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Pour créer un quiz : cliquer sur Nouveau > Google Forms, renommer le formulaire, ajouter des questions et sélectionner le type (choix multiples, cases à cocher, etc.).        
</div>
<h4>F. Google Agenda</h4>
<ul>
    <li>Création et partage de calendriers/plannings.</li>
    <li>Modes d’affichage : jour, semaine, mois, année, planning.</li>
    <li>Paramétrage : créer plusieurs agendas et les partager avec collaborateurs.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Pour ajouter un événement : cliquer sur 
    <strong>Créer</strong> , remplir titre, description, lieu et choisir l’agenda concerné.
</div>
<hr>
<h3>II. Travail collaboratif</h3>
<h4>A. Avantages</h4>
<ul>
    <li>Collaboration simultanée sur documents.</li>
    <li>Communication facilitée, gain de temps et réduction des déplacements.</li>
    <li>Accès aux documents depuis n’importe quel poste connecté.</li>
</ul>
<h4>B. Partage des documents</h4>
<ul>
    <li>Par défaut, un document est non partagé.</li>
    <li>Partage par mail ou lien.</li>
    <li>Possibilité de partager un dossier entier.</li>
</ul>
<div class="procedure">
    <strong>Exemple :</strong> <br>

    Pour partager un document : 
    <em> Clic droit > Partager > Entrer adresse mail ou copier lien de partage
    </em>.
</div>
<h4>C. Niveaux d’autorisations</h4>
<ul>
    <li><strong>Modification</strong> : droit de modifier et commenter.</li>
    <li><strong>Commentaires</strong> : droit de commenter seulement.</li>
    <li><strong>Lecture seule</strong> : consultation uniquement.</li>
</ul>
<h4>D. Gestion des commentaires</h4>
<ul>
    <li>Menu : <em>Insertion > Commentaires</em>.</li>
    <li>Suggestions pour corrections orthographiques ou révisions.</li>
</ul>

<h4>E. Utilisation sur smartphone/tablette</h4>
<ul>
    <li>Consultation via navigateur web.</li>
    <li>Pour modification, utiliser les applications Google dédiées.</li>
</ul>

<hr>

<h3>III. Essentiel</h3>
<ul>
    <li>Collaboration en temps réel, avec droits adaptés.</li>
    <li>Protection des documents via options de partage (lecture, commentaires, modification).</li>
</ul>

<hr>

<h2>Commandes / Notes pratiques</h2>
<ul>
    <li><strong>Créer un document :</strong> Nouveau > Choisir l’application</li>
    <li><strong>Partager un document :</strong> Clic droit > Partager > Obtenir le lien</li>
    <li><strong>Appliquer un style dans Docs :</strong> Format > Style de paragraphes</li>
    <li><strong>Ajouter une feuille dans Sheets :</strong> bouton + en bas à gauche</li>
    <li><strong>Insérer médias dans Slides :</strong> Insertion > Image/Vidéo/Audio</li>
    <li><strong>Exporter réponses Forms vers Sheets :</strong> Onglet Réponses > Feuille de calcul</li>
</ul>

<hr>

<h2>Exercices & Auto-évaluation</h2>

<h4>1. Identifier l’outil adapté :</h4>
<ul>
    <li>Mettre en page du texte → Google Docs</li>
    <li>Créer un tableau → Google Sheets</li>
    <li>Présentation dynamique → Google Slides</li>
    <li>Formulaire/sondage → Google Forms</li>
</ul>

<h4>2. Catégoriser les niveaux d’autorisation :</h4>
<table>
    <tr>
        <th>Action</th>
        <th>Autorisation</th>
    </tr>
    <tr>
        <td>Lire seulement</td>
        <td>Lecture seule</td>
    </tr>
    <tr>
        <td>Donner son avis</td>
        <td>Commentaires</td>
    </tr>
    <tr>
        <td>Modifier directement</td>
        <td>Modification</td>
    </tr>
</table>

<h4>3. Questions rapides :</h4>
<ul>
    <li>Travail collaboratif en temps réel → Vrai</li>
    <li>Proposer des corrections orthographiques → Suggestions</li>
    <li>Modifier sur smartphone → Applis à télécharger</li>
</ul>

</body>
</html>

<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Bonnes pratiques de sécurité</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background-color: #1e1e1e; color: #eee; }
    h1, h2, h3 { color: #3498db; margin-top: 1em; }
    h1 { font-size: 2em; }
    h2 { font-size: 1.5em; }
    h3 { font-size: 1.2em; }
    ul { margin-left: 20px; }
    .procedure { 
        background-color: #2c3e50; 
        border-left: 4px solid #e74c3c; 
        padding: 10px; 
        margin: 10px 0; 
        color: #eee; 
    }
    .important { font-weight: bold; color: #e74c3c; }
    .tip { font-style: italic; color: #16a085; }
    a { color: #3498db; text-decoration: underline; }
</style>
</head>
<body>

<h1>Bonnes pratiques de sécurité</h1>

<h2>I. Gestion des mots de passe</h2>
<p>Un mot de passe doit être :</p>
<ul>
    <li>Composé d'au moins 12 caractères</li>
    <li>Inclure majuscules, minuscules, chiffres et caractères spéciaux</li>
    <li>Ne pas figurer dans un dictionnaire</li>
</ul>

<div class="procedure">
    <strong class="important">Bons gestes :</strong><br>
    - Ne laissez jamais les mots de passe par défaut.<br>
    - Définissez des règles de composition.<br>
    - Ne stockez pas vos mots de passe dans des fichiers ou post-its.<br>
    - Ne pré-enregistrez pas les mots de passe dans le navigateur.<br>
    <span class="tip">Astuce :</span> Utilisez un gestionnaire de mots de passe pour les sauvegarder en sécurité.
</div>

<h2>II. Mise à jour des logiciels</h2>
<p>Pour corriger les failles de sécurité, il est essentiel de mettre à jour :</p>
<ul>
    <li>Le système d'exploitation</li>
    <li>Les logiciels et applications</li>
</ul>

<div class="procedure">
    <strong class="important">Bons gestes :</strong><br>
    - Mettre en place des mises à jour automatiques si possible.<br>
    - Télécharger uniquement sur le site officiel de l’éditeur.<br>
    - Suivre la politique de mises à jour de l'entreprise.
</div>

<h2>III. Utilisateurs et administrateurs</h2>
<p>Différents niveaux d’accès :</p>
<ul>
    <li><strong>Utilisateur :</strong> accès limité à l’usage quotidien</li>
    <li><strong>Administrateur :</strong> accès complet au système</li>
</ul>

<div class="procedure">
    <strong class="important">Bons gestes :</strong><br>
    - Réserver les comptes Administrateur au service informatique.<br>
    - Supprimer les comptes anonymes ou génériques.<br>
    - Nommer les comptes de manière identifiable.
</div>

<h2>IV. Sauvegardes régulières</h2>
<div class="procedure">
    - Sauvegarder les données importantes sur un serveur distinct.<br>
    - Placer les sauvegardes dans un lieu différent.<br>
    - <strong class="important">Cloud :</strong> pratique mais attention aux risques de confidentialité et d'indisponibilité.
</div>

<h2>V. Vigilance et sécurité</h2>
<div class="procedure">
    <strong class="important">Wi-Fi :</strong> privilégier la connexion filaire, créer un réseau invité, donner un identifiant unique.<br>
    <strong class="important">Smartphone / tablette :</strong> installer uniquement des apps officielles, mettre code PIN, sauvegarder régulièrement, ne pas pré-enregistrer les mots de passe.
</div>

<h2>VI. Utilisation prudente de la messagerie</h2>
<div class="procedure">
    - Ne jamais divulguer les informations personnelles via mail.<br>
    - Vérifier l’adresse de l’expéditeur.<br>
    - Ne pas cliquer sur les liens suspects.<br>
    - Scanner les pièces jointes avant ouverture.<br>
    <strong class="important">Phishing :</strong> e-mails frauduleux pour obtenir vos données.<br>
    <strong class="important">SimSwap :</strong> vol de carte SIM pour accéder à vos comptes.<br>
    <strong class="important">Vishing :</strong> phishing vocal pour soutirer des informations.
</div>

<h2>VII. Téléchargement et vigilance</h2>
<div class="procedure">
    - Télécharger uniquement depuis le site officiel de l’éditeur.<br>
    - Vérifier le nom et le format des fichiers.<br>
    - Scanner les fichiers téléchargés avec un antivirus.<br>
    <strong class="important">Ransomware :</strong> bloque l'accès au système jusqu'au paiement d'une rançon.<br>
    <strong class="important">Cheval de Troie :</strong> malware déguisé en logiciel légitime.
</div>

<h2>VIII. Usage et identité numérique</h2>
<div class="procedure">
    - Séparer usage professionnel et personnel.<br>
    - Ne pas héberger de données professionnelles sur des supports personnels.<br>
    - Rester vigilant avant de cliquer sur des liens sponsorisés.<br>
    - Vérifier la présence du cadenas et du https sur les sites sécurisés.<br>
    - Ne pas publier toutes vos informations personnelles sur les réseaux sociaux.
</div>

<h2>IX. Auto-évaluation</h2>
<div class="procedure">
    <strong class="important">Quiz :</strong><br>
    1. Une cyberattaque se produit toutes les : <strong>39 secondes</strong>.<br>
    2. Le mot de passe "Ordinateur22!" est : <strong>faux</strong>, il contient un mot du dictionnaire.<br>
    3. Mail suspect : <strong>vérifier l'adresse avant de cliquer</strong>.<br>
    4. Stagiaire : <strong>ne pas créer un compte générique</strong>.<br>
    5. Télécharger un logiciel : <strong>chercher le site officiel de l’éditeur</strong>.
</div>

</body>
</html>

