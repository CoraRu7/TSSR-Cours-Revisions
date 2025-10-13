# Les bases des réseaux IP

## La définition d’un protocole de communication

**Objectif :**  
Comprendre ce qu’est un protocole de communication et se familiariser avec les principaux protocoles réseaux sur Internet, leur rôle, leur fiabilité et leur fonctionnement.

---

### 1️⃣ Définition d’un protocole

- Un **protocole** est un ensemble de règles et de procédures permettant la communication entre plusieurs ordinateurs échangeant des données.  

#### Méthode : Fonctionnement étape par étape

1. **L’envoi postal** → comparaison avec l’envoi de données  
2. **Les informations destinataire et émetteur** → identification des ordinateurs  
3. **Principe sur Internet** → les paquets de données circulent entre machines  
4. **Rôle de l’adresse IP** → identifier de manière unique chaque noeud  
5. **Schéma représentatif :**

```text
[Émetteur] ---paquet--> [Réseau] ---paquet--> [Récepteur]
```

6. **Paramètres définis par les protocoles** → règles de format, d’adresse, de retransmission

---

### 2️⃣ Principaux protocoles réseaux sur Internet

| Protocole | Fonction |
|-----------|---------|
| **TCP/IP** | Communication fiable entre machines |
| **IP** | Identification d’un ordinateur via adresse IP |
| **HTTP** | Transfert de documents hypertextes |
| **FTP** | Transfert de fichiers |

---

### 3️⃣ TCP : Transmission Control Protocol

- Établit une **connexion fiable** entre deux noeuds (client ↔ serveur).  
- Fonctionne sur **la couche 4 du modèle OSI**.  
- Permet **transmission bilatérale de données**.  

#### Procédure de connexion (Three-Way Handshake)

```text
1️⃣ SYN : le client envoie un paquet avec numéro aléatoire
2️⃣ SYN-ACK : le serveur répond avec son propre numéro et incrémente celui du client
3️⃣ ACK : le client confirme la réception du paquet du serveur
```

**Schéma simplifié :**

```text
Client        Serveur
  SYN   ---->
        <----  SYN-ACK
  ACK   ---->
Connexion établie ✅
```

- Chaque noeud doit avoir une **adresse IP** et un **port** pour identifier la connexion.

---

### 4️⃣ Organisation du réseau

- Composants matériels : routeurs, serveurs, postes de travail, périphériques  
- Interfaces : normes et règles pour l’échange d’informations  
- Protocoles : ensembles de règles pour assurer la communication (TCP/IP, HTTP, etc.)

---

### 5️⃣ Nomenclature des protocoles

#### 5.1 Signalisation
- Tous les messages qui comportent les **commandes utiles** du protocole.  
- **In-Band** : signalisation avec les données sur le même canal (HTTP)  
- **Out-of-Band** : signalisation séparée (SIP/SDP/RTP, FTP)

#### 5.2 Maintenance de la connexion
- **Orienté connexion** : établit, maintient et ferme un canal avant envoi (TCP, FTP)  
- **Non orienté connexion** : pas de maintenance (Ethernet, IP, UDP, TFTP)

#### 5.3 Fiabilité
- **Fiable** : reprise sur erreur, accusés de réception, contrôle de flux (TCP)  
- **Non fiable** : aucun mécanisme de fiabilité (Ethernet, IP, UDP, TFTP)

---

### 6️⃣ Modèles de communication

- **TCP/IP** : technologies courantes pour Internet  
- **OSI** : modèle académique de référence, similaire à TCP/IP  

#### Les 4 couches orientées communication

| Couche | Fonction |
|--------|---------|
| Transport | Transmission de données entre applications |
| Réseau | Routage et adressage |
| Liaison | Encapsulation et transfert de trames |
| Physique | Signal physique sur le support |

**Avantages d’un modèle en couches :**

```text
- Facilite le diagnostic et le dépannage
- Permet de modifier un protocole sans tout repenser
- Compatibilité entre différents matériels et constructeurs
```

#### Schéma comparatif OSI / TCP-IP

```text
OSI            TCP/IP
-----          ------
Application    Application
Transport      Transport
Réseau         Internet
Liaison        Accès réseau
Physique       Accès réseau
```

---

### 7️⃣ Notes rapides

- Les protocoles définissent **qui fait quoi, comment et quand**.  
- TCP/IP assure une **communication

## Les caractéristiques des modèles osi, tcp et le principe d’encapsulation

**Objectif :**  
Comprendre les caractéristiques des modèles OSI et TCP/IP, le principe d'encapsulation et la structure des unités de données dans les différentes couches.

---

### 1️⃣ Modèle de référence OSI

- **Créé par :** ISO (Organisation Internationale de Normalisation)  
- **But :** spécifier l'architecture réseau idéale  
- **Organisation :** 7 couches hiérarchiques

| Numéro | Couche        | Fonction principale |
|--------|---------------|------------------|
| 7      | Application   | Interaction avec les applications (navigateur, messagerie…) |
| 6      | Présentation  | Conversion et standardisation des données |
| 5      | Session       | Gestion de la liaison entre systèmes |
| 4      | Transport     | Connexion logique et ajout d'en-têtes transport |
| 3      | Réseau        | Transmission et adressage logique (IP) |
| 2      | Liaison       | Détection d'erreurs, contrôle de flux, adressage physique |
| 1      | Physique      | Conversion en signal physique, support de transmission (DSL, Ethernet, USB…) |

---

### 2️⃣ Modèle TCP/IP

- **Couches :** 4  
- **Rôle :** protocoles utilisés sur Internet, intégrés dans une suite  
- **Correspondance avec OSI :**

| TCP/IP | OSI                  |
|--------|--------------------|
| 4 Application | 7 App + 6 Présentation + 5 Session |
| 3 Transport   | 4 Transport |
| 2 Internet    | 3 Réseau |
| 1 Accès au réseau | 1 Physique + 2 Liaison |

---

### 3️⃣ Principe d’encapsulation

- **Définition :** Inclusion des données d’un protocole dans un autre protocole pour sécuriser et standardiser la transmission  
- **Fonctionnement :**

```text
Machine émettrice :
[Application] -> ajout d'en-têtes
[Transport]   -> ajout segment
[Réseau]      -> encapsulation en paquet
[Liaison]     -> trame
[Physique]    -> signal transmis

Machine réceptrice :
Signal -> trame -> paquet -> segment -> message
Décapsulation couche par couche
```

- Chaque couche ajoute un **en-tête (Header)** contenant des informations utiles pour le routage, le contrôle, la sécurité ou la livraison des données.

---

### 4️⃣ Unités de données par couche (OSI)

| Couche        | Nom de l'unité de données |
|---------------|--------------------------|
| Application   | Message                  |
| Transport     | Segment                  |
| Réseau        | Paquet                   |
| Liaison       | Trame                    |
| Physique      | Signal                   |

---

### 5️⃣ Structure d’un datagramme IP (IPv4)

- **Couches concernées :** Réseau (3) et Transport (4)  
- **Longueur d’en-tête IP :** 20 octets  
- **Champs principaux :**

| Champ              | Description |
|-------------------|-------------|
| Version            | IPv4 ou IPv6 |
| Header Length      | Longueur de l’en-tête (20 octets par défaut) |
| Type of Service    | Priorité du paquet (peu utilisé) |
| Total Length       | Nombre total d’octets du datagramme (16 bits) |
| Identification (ID)| Numéro unique pour identifier les fragments |
| Flags              | Autorisation de fragmenter le paquet |
| Fragment Offset    | Ordre des fragments |
| TTL (Time to Live) | Durée de vie du paquet pour éviter le looping |
| Protocol           | TCP ou UDP (couche 4) |
| Checksum           | Vérification de l’intégrité de l’en-tête |
| Source / Destination IP | Adresses IP source et destination |

- **Fragmentation :** nécessaire si la trame de la couche 2 est plus petite que le datagramme IP  
- **Encapsulation/décapsulation :** chaque couche lit et retire son en-tête à la réception

---

### 6️⃣ Schémas ASCII

#### Encapsulation

```text
Message (Application)
   ↓
Segment (Transport)
   ↓
Paquet (Réseau)
   ↓
Trame (Liaison)
   ↓
Signal (Physique)
```

#### Décapsulation (réception)

```text
Signal (Physique)
   ↓
Trame (Liaison)
   ↓
Paquet (Réseau)
   ↓
Segment (Transport)
   ↓
Message (Application)
```

---

### 7️⃣ Notes rapides

- **Encapsulation** : sécurise et standardise la transmission  
- **Décapsulation** : lecture et retrait des en-têtes pour récupérer le message  
- TCP/IP = modèle pratique sur Internet, 4 couches  
- OSI = modèle théorique, 7 couches, utile pour le diagnostic et l’apprentissage  
- Chaque couche ajoute un en-tête (Header) → changement d’appellation des données selon la couche

---

## Le rôle de couche d’accès réseau et la liaison de données


**Objectif :**  
Comprendre le rôle des couches Accès Réseau (couche 1) et Liaison de données (couche 2) du modèle TCP/IP et OSI, les technologies physiques, les protocoles et les sous-couches.

---

### 1️⃣ Couche Accès Réseau (couche 1)

- Correspond aux **couches Physique et Liaison de données** du modèle OSI  
- **Unité utilisée :** bit ou train de bits continu (trame)  
- **Fonctions principales :**  
  - Conversion bits ↔ signaux physiques  
  - Contrôle d’erreur  
  - Contrôle de flux (asservissement du débit émetteur → récepteur)

#### 1.1 Fonctionnement

- Fournit un accès au réseau physique  
- Décrit les caractéristiques physiques de la communication (câblage, signaux)  
- Conversion des bits en signaux électriques, optiques ou électromagnétiques  
- Principalement réalisé par des circuits électroniques spécialisés  

#### 1.2 Technologies de transmission

| Type de support       | Exemple / Fonctionnement                       | Débit / Distance |
|----------------------|-----------------------------------------------|----------------|
| Signaux électriques  | Variation de tension sur conducteurs cuivre   | Selon câble |
| Fibres optiques      | Variation d’intensité lumineuse              | Jusqu’à 10 000 km, 1 GHz |
| Ondes électromagnétiques | Faisceaux satellite, hertzien, WiFi, Bluetooth, Zigbee | 1 Mb/s → 300 Mb/s selon fréquence et distance |

#### 1.3 Câbles cuivre (RJ45)

- **Paires torsadées :** réduction du bruit électromagnétique  
- **Types :**  
  - STP (Shielded Twisted Pair) : blindé, débit jusqu’à 1 Gb/s  
  - UTP (Unshielded Twisted Pair) : non blindé, débit jusqu’à 10 Gb/s, catégories 3 à 7  
- **Normes de câblage :** T568A (résidentiel), T568B (professionnel)  
- **Câbles droits / croisés :**  
  - Droit : relie PC → switch/hub  
  - Croisé : relie switch → switch ou PC → PC (rare aujourd’hui)

#### 1.4 Fibre optique

- Fil en verre ou plastique très fin, guide d’onde pour la lumière  
- Structure : **cœur** + **gaine** + **revêtement**  
- Types : monomode (longue distance), multimode (courte distance)  
- Avantages : bande passante élevée, faible atténuation  

#### 1.5 Ondes électromagnétiques

| Type             | Fréquences / Exemple                       | Portée / Débit |
|-----------------|-------------------------------------------|----------------|
| Satellite        | Géostationnaire, 36 000 km                | 140 Mb/s |
| Hertzien (WiFi)  | ISM 2,4 GHz, 5 GHz, 5,7 GHz               | 200 m à 50 km, 1 → 300 Mb/s |

```text
Exemple cheminement ondes EM :
Satellite/AP --> Antenne --> PC / Device
```

---

### 2️⃣ Couche Liaison de données (couche 2)

- **Rôle :** transport des paquets sur la couche physique, tramage, contrôle d’erreurs et flux  
- **Protocoles principaux :**  
  - **PPP** : connexion point-to-point via modem  
  - **IEEE802.3 / IEEE802.11b** : Ethernet filaire ou WiFi  
- **Sous-couches :**  
  - **LLC (Logical Link Control)** : contrôle de liaison logique, fiabilise MAC via contrôle d’erreurs et flux  
  - **MAC (Medium Access Control)** : accès au médium, insertion adresses MAC source/destination

#### 2.1 Protocoles Ethernet et WiFi

| Protocole       | Topologie            | Mode d’accès au médium             | Débit |
|-----------------|-------------------|----------------------------------|-------|
| Ethernet        | Bus / Maillage     | CSMA/CD (écoute + collision)     | 10 Mb/s → 10 Gb/s |
| WiFi 802.11     | Infrastructure / Ad-Hoc | CSMA/CA                        | 1 → 2 Mb/s |

- **WiFi Infrastructure :** point d’accès centralise les communications (BSSID)  
- **WiFi Ad-Hoc :** communication directe entre postes (SSID)

---

### 3️⃣ Complément IEEE

- **IEEE (Institute of Electrical and Electronics Engineers)** : normalisation internationale, plus de 1200 normes  
- **Normes réseau :** IEEE 802 (LAN/MAN), définissant couche Physique et Liaison de données  
- **Rôle :** contrôle de flux, fiabilité MAC, standardisation internationale  

```text
Couches OSI / TCP-IP : Physique + Liaison de données
|----------------------|
| Liaison de données   | <-- LLC + MAC
| Accès réseau / Physique | <-- câbles, fibre, ondes EM
|----------------------|
```

---

### 4️⃣ Notes rapides

- Couche Accès réseau = couche 1 TCP/IP = Physique OSI  
- Couche Liaison de données = couche 2 TCP/IP = Liaison OSI  
- LLC = fiabilise la transmission  
- MAC = accès au médium + adresses physiques  
- Ethernet = protocole filaire standard IEEE 802.3  
- WiFi = protocole sans fil IEEE 802.11, CSMA/CA, modes Infrastructure / Ad-Hoc

---

## Le découpage d’un réseau IPv4


**Objectif :**  
Connaître les bases d’IPv4, les adresses publiques/privées, le rôle du NAT, les masques/CIDR et les méthodes pour découper un réseau en sous-réseaux (fixes ou équitables).

---

### 1️⃣ Qu’est-ce que IPv4 ?

- **IPv4** = Internet Protocol version 4 (adresse codée sur **32 bits**).  
- Présentation : 4 octets décimaux séparés par des points, ex. `193.63.52.87`.  
- **Chaque interface réseau** (PC, imprimante, routeur, smartphone...) possède une adresse IP.  
- Attribution : manuelle (admin) ou automatique via **DHCP**.  
- Certaines adresses sont **réservées** (ex. `127.0.0.0/8` pour loopback, `0.0.0.0` route par défaut).

#### 1.1 Adresses publiques vs privées
- **Privées** (non routables sur Internet) :  
  - Classe A : `10.0.0.0/8`  
  - Classe B : `172.16.0.0/12` (`172.16.0.0` → `172.31.255.255`)  
  - Classe C : `192.168.0.0/16` (`192.168.0.0` → `192.168.255.255`)  
- **NAT** (Network Address Translation) : traduit/adapte adresses privées → publiques.  
  - **NAT statique** : 1:1 (IP publique fixe ↔ IP privée).  
  - **NAT dynamique / PAT** : plusieurs machines partagent une IP publique via translation de ports.

---

### 2️⃣ Masque de sous-réseau et CIDR

- Le **masque** sépare la partie réseau de la partie hôte. Même forme qu’une IP (4 octets).  
- **CIDR** : notation `/n` = nombre de bits à 1 dans le masque (ex. `/19` = 19 bits à 1).  
- Exemple : `255.255.224.0` → binaire `11111111.11111111.11100000.00000000` → `/19`.

#### 2.1 Formules utiles
- Bits hôtes = `32 - n`  
- Total d’adresses = `2^(32 - n)`  
- Hôtes utilisables = `2^(32 - n) - 2` (réseau + broadcast exclus)

---

### 3️⃣ Table de référence rapide (masques courants)

| CIDR | Masque décimal         | Bits hôtes | Total adresses | Hôtes utilisables |
|------|-------------------------|------------|----------------|-------------------|
| /30  | 255.255.255.252         | 2          | 4              | 2                 |
| /29  | 255.255.255.248         | 3          | 8              | 6                 |
| /28  | 255.255.255.240         | 4          | 16             | 14                |
| /27  | 255.255.255.224         | 5          | 32             | 30                |
| /26  | 255.255.255.192         | 6          | 64             | 62                |
| /25  | 255.255.255.128         | 7          | 128            | 126               |
| /24  | 255.255.255.0           | 8          | 256            | 254               |
| /23  | 255.255.254.0           | 9          | 512            | 510               |
| /20  | 255.255.240.0           | 12         | 4096           | 4094              |

---

### 4️⃣ Méthode pas-à-pas : déterminer NetID / Broadcast / plage d’hôtes (méthode binaire)

**Exemple donné :** `172.20.56.128 /23`

1. Écrire IP et masque en binaire :  
   - IP : `172.20.56.128` → `10101100.00010100.00111000.10000000`  
   - Masque `/23` → `255.255.254.0` → `11111111.11111111.11111110.00000000`

2. **NetID** = appliquer un ET bit à bit entre IP et masque → mettre les bits host à `0` :  
   - NetID binaire → `10101100.00010100.00111000.00000000` → `172.20.56.0`

3. **Broadcast** = mettre tous les bits host à `1` :  
   - Broadcast → `172.20.57.255`

4. **Plage d’hôtes** : première = NetID + 1 → `172.20.56.1` ; dernière = Broadcast - 1 → `172.20.57.254`

✅ Pour `/23` : bits host = `9` → hôtes = `2^9 - 2 = 510`.

---

### 5️⃣ Méthode « nombre magique » (pratique pour octet significatif)

- Le **nombre magique** = `256 - valeur_octet_significatif` (où l’octet significatif est le premier octet du masque < 255).  
- Exemple `/20` → masque `255.255.240.0` → octet significatif = `240` → nombre magique = `256 - 240 = 16`.  
- Les sous-réseaux se découpent en **multiples** de 16 dans l’octet correspondant.

---

### 6️⃣ Découpage complet (exemple pas-à-pas fourni dans le cours)

**Cas :** réseau `192.168.180.0 /20` — on veut 3 sous-réseaux : 320 techniciens, 140 commerciaux, 15 directeurs.

**Étape 0 :** `/20` → masque `255.255.240.0`, nombre d’adresses possibles `2^12 = 4096` → hôtes utilisables `4094` → suffisant.

**Étape 1 :** Trouver NetID de départ (nombre magique = `256 - 240 = 16`)  
- Trouver multiple de 16 ≤ 180 → 16 × 11 = 176 (16×12=192 >180) → **NetID = 192.168.176.0**  
- Le bloc `/20` couvre de `192.168.176.0` jusqu’à `192.168.191.255`.

**Étape 2 : réseau Techniciens (320 hôtes)**  
- Besoin ≈ 320 → chercher puissance : `2^9 = 512 → 512 - 2 = 510` suffice → bits host = 9 → CIDR = `32 - 9 = /23` → masque `255.255.254.0`.  
- Taille bloc (octet significatif) = `256 - 254 = 2` → réseaux incréments de 2 sur l’octet 3.  
- En partant de `192.168.176.0` : NetID = `192.168.176.0`  
- Broadcast = next multiple − 1 → next multiple = 178 → broadcast = `192.168.177.255`  
- Hôtes : `192.168.176.1` → `192.168.177.254` (510 hôtes utilisables)

**Étape 3 : réseau Commerciaux (140 hôtes)**  
- Besoin ≈ 140 → `2^8 = 256 - 2 = 254` → suffisant → CIDR `/24` (255.255.255.0).  
- Suivant le bloc précédent : commence au `192.168.178.0` (puisque le bloc techniciens a fini sur .177.255).  
- NetID = `192.168.178.0` ; Broadcast = `192.168.178.255` ; Hôtes = `192.168.178.1` → `192.168.178.254` (254 hôtes utilisables)

**Étape 4 : réseau Directeurs (15 hôtes)**  
- Besoin ≈ 15 → `2^5 = 32 - 2 = 30` → CIDR `/27` (255.255.255.224).  
- Commence à `192.168.179.0` (bloc suivant).  
- NetID = `192.168.179.0` ; Broadcast = `192.168.179.31` ; Hôtes = `192.168.179.1` → `192.168.179.30` (30 hôtes utilisables)

> ✅ Résumé résultats :
> - Techniciens : `192.168.176.0/23` → hôtes `.1` → `.177.254`  
> - Commerciaux : `192.168.178.0/24` → hôtes `.1` → `.178.254`  
> - Directeurs : `192.168.179.0/27` → hôtes `.1` → `.179.30`

---

### 7️⃣ Découper équitablement (ex. diviser /24 en 2,4,8 sous-réseaux)

**But :** découper `192.168.1.0/24` en N sous-réseaux égaux.

- N = 2 → besoin `2^1` → emprunter 1 bit aux hôtes → nouveau masque = `/25` (255.255.255.128).  
  - Sous-réseaux :  
    - `192.168.1.0/25` → broadcast `192.168.1.127` → hôtes `.1` → `.126` (126 hôtes)  
    - `192.168.1.128/25` → broadcast `192.168.1.255` → hôtes `.129` → `.254` (126 hôtes)

- N = 4 → emprunter 2 bits → `/26` (64 adresses, 62 hôtes chacun)  
- N = 8 → emprunter 3 bits → `/27` (32 adresses, 30 hôtes chacun)  

**Méthode :**
1. Déterminer la puissance `p` telle que `2^p = N`.  
2. Nouveau préfixe = `original_prefix + p`.  
3. Calculer sous-réseaux en incréments du nombre magique (sur l’octet significatif).

---

### 8️⃣ Astuces & vérifications

- **Vérifier en binaire** quand tu débutes → c’est infaillible.  
- **Nombre magique** = rapide pour octet significatif.  
- Toujours retirer 2 adresses (NetID & Broadcast) pour les hôtes utilisables.  
- Pour trouver le **next network** : NetID_next = NetID + taille_bloc (ex. /23 taille 2 dans l’octet 3 → NetID + 2 sur l’octet 3).  
- Si tu as une suite d’adresses à allouer, avance toujours à la **NetID suivante** après le broadcast précédent.

---

### 9️⃣ Commandes utiles (vérification locale)

```bash
# Linux : voir interfaces et adresses
ip a

# Windows : voir interfaces et adresses
ipconfig /all

# Vérifier reachabilité
ping <IP>

# Tracer le chemin (Linux)
traceroute <IP>

# Tracer le chemin (Windows)
tracert <IP>
```

---

### 10️⃣ Remarques finales

- Plusieurs méthodes existent (binaire, nombre magique, table de puissances) → choisis celle que tu préfères.  
- En entreprise, on documente toujours les sous-réseaux créés (NetID, Mask, Broadcast, plage hôtes, rôle).  
- Le découpage doit prendre en compte extension future (prévoir marge) et contraintes NAT/PAT si accès Internet centralisé.

---

## Les fondamentaux d’IPv6


**Objectif :**  
Comprendre les fondamentaux de l’IPv6, son adressage, les en-têtes, l’absence de broadcast, le protocole Neighbor Discovery, et les types d’adresses.

---

### 1️⃣ Contexte et définition

- **IPv6** = Internet Protocol version 6, couche 3 OSI, protocole sans connexion.  
- Né pour pallier le manque d’adresses IPv4 et améliorer la sécurité, la configuration automatique et l’agrégation des routes.  
- Normalisé par l’IETF (RFC 8200, juillet 2017).  
- **Adresse IPv6** : 128 bits → espace d’adressage immense (~3.4×10^38 adresses).  
- Sous-réseau standard = 64 bits pour le préfixe réseau.  
- Transition IPv4 ↔ IPv6 : double pile, tunnels, traducteurs d’adresses.  

---

### 2️⃣ Notation IPv6

- **Format** : 8 groupes de 16 bits (4 hexadécimaux) séparés par `:`  
  Exemple : `2001:0db8:0000:85a3:0000:0000:ac1f:8001`  
- **Simplification** :  
  - Suppression des zéros de tête dans un groupe : `0db8` → `db8`  
  - Remplacement des suites de groupes nuls contigus par `::` (une seule fois par adresse)  
  Exemple : `2001:db8:0:85a3::ac1f:8001`

---

### 3️⃣ Historique et principes

- IPv6 conçu pour résoudre :  
  - Limitation des 4 milliards d’adresses IPv4  
  - Simplification du routage et agrégation d’itinéraires  
  - Multidiffusion native et sécurisation (IPsec)  
- Chaque appareil connecté reçoit une adresse globale et une adresse locale automatiquement.  
- Plus besoin de NAT pour Internet, protocole autoconfigurable.  

---

### 4️⃣ Préfixe réseau et identifiant d’interface

- IPv6 = **préfixe réseau (64 bits)** + **identifiant d’interface (64 bits)**  
- Notation CIDR : `/n` indique la longueur du préfixe réseau.  
  Exemple : `2001:0820:9511::/48` → adresse allant de `2001:0820:9511:0000:0000:0000:0000:0000` à `2001:0820:9511:FFFF:FFFF:FFFF:FFFF:FFFF`.

#### 4.1 Construction de l'identifiant d'interface (EUI-64)

- À partir de l’adresse MAC 48 bits → ajouter `FFFE` au milieu → inverser le 7ᵉ bit (« bit universel/local »).  
- Exemple : MAC `00-13-28-60-C1-4C`  
  - Découpage : `0013:28` + `60:C14C`  
  - Ajouter `FFFE` : `0013:28FF:FE60:C14C`  
  - Inversion du 7ᵉ bit → `0213:28FF:FE60:C14C`  

---

### 5️⃣ Neighbor Discovery (ND)

- Remplace ARP et broadcast en IPv4.  
- Fonctionnalités :  
  - Détection des doublons d’adresses (Duplicate Address Detection)  
  - Découverte de voisins  
  - Résolution d’adresses  
  - Annonce d’adresses lien-local  
- Processus :  
  - **Neighbor Solicitation** : vérifie doublons  
  - **Neighbor Advertisement** : confirme utilisation de l’adresse  

---

### 6️⃣ Format du paquet IPv6

- En-tête fixe : 40 octets  
- **Champs principaux :**

| Champ | Description |
|-------|-------------|
| Version | Version du protocole (6) |
| Classe de trafic | Priorités (8 bits) |
| Identificateur de flux | Paquets traités de la même manière (20 bits) |
| Longueur du payload | Longueur données utiles + extensions (16 bits) |
| Next Header | Protocole couche transport (8 bits) |
| Hop Limit | Limite de sauts avant expiration (8 bits) |
| Source IP | Adresse source (128 bits) |
| Destination IP | Adresse destination (128 bits) |

- Extensions : champs optionnels entre en-tête et payload, sans modifier l’en-tête fixe.  

---

### 7️⃣ Types d’adresses IPv6

1. **Lien-local**  
   - Préfixe : `FE80::/10`  
   - Valide uniquement sur réseau local, utilisé pour ND et auto-configuration.  

2. **Unicast global**  
   - Préfixe : `2000::/3` (souvent `2001::/16` pour clients FAI)  
   - Routable Internet, unique mondialement.  

3. **Multicast**  
   - Préfixe : `FF00::/8`  
   - Communication d’un à plusieurs (diffusion de groupe).  
   - Un appareil peut appartenir à plusieurs groupes multicast.  

4. **Anycast**  
   - Paquets envoyés au membre le plus proche d’un groupe.  
   - Utilisé pour répartition de charge et sécurité.  

---

### 8️⃣ Points clés

- IPv6 simplifie et sécurise l’adressage : plus de NAT, pas de broadcast, ND pour voisins.  
- Format binaire = 128 bits, notation hexadécimale simplifiée.  
- Préfixe 64 bits + identifiant interface 64 bits (souvent EUI-64).  
- Coexistence IPv4/IPv6 via double pile et tunnels.  
- Types d’adresses : lien-local, unicast global, multicast, anycast.  
- En-tête IPv6 plus simple et extensible qu’IPv4.  

---

### 9️⃣ Commandes utiles (vérification locale IPv6)

```bash
# Linux : voir interfaces IPv6
ip -6 addr

# Windows : voir interfaces IPv6
ipconfig /all

# Ping IPv6
ping6 <IP>

# Traceroute IPv6
traceroute6 <IP>   # Linux
tracert -6 <IP>    # Windows
```

---

## Les topologies physiques et logique des réseaux


**Objectif :**  
Comprendre les topologies physiques et logiques des réseaux, leurs caractéristiques, avantages/inconvénients et cas d’usage.

---

### 1️⃣ Contexte

- Les réseaux informatiques sont omniprésents.  
- Une **topologie** = configuration physique ou logique des éléments du réseau.  
- Détermine comment les appareils, câbles, commutateurs et routeurs sont interconnectés.  
- Objectifs : optimiser la performance, la fiabilité, la maintenance et la résilience du réseau.

---

### 2️⃣ Topologies physiques

#### 2.1 Topologie en bus

- Tous les périphériques connectés à un **câble unique**.  
- Terminaisons aux extrémités pour éviter les réflexions.  
- Simple et économique, mais bande passante partagée.  
- Défaillance du câble = interruption du réseau.

```
PC1 ---+--- PC2 ---+--- PC3 ---+--- PC4
       |           |           |
     [Terminaison]           [Terminaison]
```

---

#### 2.2 Topologie en anneau

- Périphériques connectés en **boucle fermée**.  
- Données circulent dans un sens, chaque périphérique relaie les paquets.  
- Evite collisions, performances constantes.  
- Panne d’un périphérique = arrêt de tout l’anneau.

```
PC1 ---> PC2 ---> PC3 ---> PC4
 ^                           |
 |---------------------------|
```

---

#### 2.3 Topologie en étoile

- Tous les périphériques connectés à un **point central** (hub/switch/routeur).  
- Facile à configurer et dépanner.  
- Défaillance d’un périphérique = impact limité.  
- Défaillance du central = réseau entier paralysé.  
- Nécessite plus de câbles.

```
       PC1
        |
PC2 ----SW---- PC3
        |
       PC4
```

---

#### 2.4 Topologie maillée (Mesh)

- Chaque périphérique connecté à **tous les autres**.  
- Redondance élevée, résiliente aux pannes.  
- Coûteuse en câblage et matériel.  
- Utilisée dans réseaux critiques et centres de données.

```
PC1 --- PC2
 | \   / |
 |  PC3  |
 | /   \ |
PC4 --- PC5
```

---

### 3️⃣ Topologies logiques

- Définissent **le chemin des données**, pas la disposition physique.  
- Types courants :  
  - **Point à point** : liaison directe entre deux nœuds.  
  - **Diffusion (broadcast)** : données envoyées à tous les appareils.  
- Indépendantes de la topologie physique.  

---

### 4️⃣ Types de réseaux selon la zone géographique

| Type | Zone couverte | Exemple d’usage |
|------|---------------|----------------|
| PAN (Personal Area Network) | Quelques mètres | Montre connectée, smartphone, casque Bluetooth |
| LAN (Local Area Network) | Bâtiment, maison, campus | Bureau, école, maison connectée |
| MAN (Metropolitan Area Network) | Ville ou région urbaine | Campus universitaire, réseau FAI urbain |
| WAN (Wide Area Network) | Région, pays ou monde | Internet, interconnexion de sites distants |

---

### 5️⃣ Conclusion

- **Physique** : détermine les connexions et la résilience matérielle.  
- **Logique** : détermine comment les données circulent et affecte performances/sécurité.  
- **Topologies courantes aujourd’hui** :  
  - **Étoile** : réseaux domestiques et entreprises classiques.  
  - **Maillée** : réseaux critiques avec redondance et haute disponibilité.  
- Connaître ces topologies permet de concevoir, gérer et dépanner efficacement les réseaux.

---

## Les équipements d’interconnexion


### Objectif
```text
Comprendre le rôle et le fonctionnement des équipements d’interconnexion (**switch**, **routeur**, **point d’accès Wi-Fi**, **portail captif**) ; savoir configurer **VLANs**, **trunks**, **routage statique et dynamique**, sécuriser une liaison Wi-Fi, accéder à l’interface web d’un AP (http://<ip_passerelle>) et vérifier la connectivité.
```

---

### Contexte
```text
L’efficacité d’un réseau repose sur la qualité et la gestion des équipements d’interconnexion : **commutateurs**, **routeurs**, **points d’accès** et **passerelles**. Cette fiche fournit les notions théoriques, les commandes Cisco pratiques et des procédures pas-à-pas utilisables dans Cisco Packet Tracer ou sur du matériel réel.
```

---

### 1. Commutateurs (Switch)

#### Définition
```text
Dispositif matériel permettant d’acheminer des trames au sein d’un LAN en s’appuyant sur les **adresses MAC**. Les switchs améliorent l’efficacité réseau en n’envoyant les trames qu’aux ports concernés.
```

#### Fonctionnement
```text
- **Table de commutation** : association dynamique port ↔ adresse MAC.
- Acheminement des trames vers le port correct uniquement.
- Réduction du trafic inutile sur le réseau.
```

#### Ports principaux
```text
- **Console** : configuration et maintenance.
- **Ethernet** : connexion aux périphériques (10/100/1000 Mb/s).
- **SFP / SFP+** : modules fibre optique pour liaisons montantes.
- **PoE / PoE+** : alimentation via câble Ethernet (15 W PoE, 30 W PoE+).
```

#### Commandes de base (Cisco)
```bash
enable
configure terminal
vlan 10
name Secrétariat
interface fa0/1
switchport access vlan 10
exit
```

---

### 2. VLANs & Trunks

#### VLAN
```text
- Segment logique d’un réseau local.
- Isolation du trafic entre services différents (ex : **Secrétariat = VLAN 10**, **Informatique = VLAN 20**).
- Les VLANs différents ne communiquent pas sans **routage inter-VLAN**.
```

#### Ports Trunk
```text
- Transportent plusieurs VLAN sur un même lien.
- Standard utilisé : **802.1Q**.
```

#### Exemple de configuration VLAN sur switch
```bash
# Switch Secrétariat
enable
configure terminal
vlan 10
name Secrétariat
interface fa0/1
switchport access vlan 10
interface fa0/2
switchport access vlan 10
interface fa0/3
switchport access vlan 10
exit

# Switch Informatique
enable
configure terminal
vlan 20
name Informatique
interface fa0/2
switchport access vlan 20
interface fa0/3
switchport access vlan 20
interface fa0/4
switchport access vlan 20
exit
```

---

### 3. Spanning Tree Protocol (STP)
```text
- Évite les boucles dans un réseau Ethernet.
- Élection d’un **commutateur racine**.
- Blocage des ports redondants.
- Recalcule automatique de la topologie en cas de changement.
```

---

### 4. Routage

#### Routage statique
```text
- Définition : routes configurées **manuellement**.
```

#### Exemple
```bash
# Routeur 0
enable
configure terminal
ip route 192.168.1.0 255.255.255.0 20.0.0.2

# Routeur 1
enable
configure terminal
ip route 10.0.0.0 255.0.0.0 20.0.0.1
```

#### Routage dynamique (RIP)
```bash
# Routeur 0
enable
configure terminal
router rip
version 2
network 10.0.0.0
network 20.0.0.0
exit

# Routeur 3
enable
configure terminal
router rip
version 2
network 20.0.0.0
network 30.0.0.0
exit

# Routeur 1
enable
configure terminal
router rip
version 2
network 192.168.1.0
network 30.0.0.0
exit
```

```text
- Vérification : **show ip route**
```

---

### 5. Points d’accès Wi-Fi (AP)

#### Fonction
```text
- Émission du signal radio.
- Diffusion du **SSID**.
- Authentification via mot de passe / clé (**WPA2/WPA3**).
- Attribution d’IP via DHCP.
```

#### Sécurité
```text
- **WEP** : obsolète.
- **WPA / WPA2 / WPA3** : recommandations actuelles.
```

#### Configuration (Cisco Packet Tracer)
```text
1. Connecter l’AP au switch.
2. Définir **SSID** et mot de passe Wi-Fi.
3. Depuis un appareil client :
   - Aller sur Wireless → SSID.
   - Entrer le mot de passe.
   - Vérifier la connectivité avec **ping <IP>**.
```

#### Accès via interface web
```text
Ouvrir un navigateur sur : http://<ip_passerelle> pour configurer **SSID** et sécurité.
```

---

### 6. Portail Captif
```text
- Redirection vers une page web pour authentification avant accès au réseau.
- Utilisé dans les hôtels, cafés, réseaux publics.
- Permet d’accepter les conditions d’utilisation ou de se connecter via identifiants.
```

---

### 7. Schémas / Illustrations
```text
- Switch + table MAC + ports Ethernet/SFP/PoE.
- VLAN et port trunk entre deux switches.
- Routeurs interconnectant plusieurs réseaux.
- Point d’accès Wi-Fi connecté au switch et aux clients.
- Portail captif exemple.
```

---

### 8. Exercices pratiques Cisco Packet Tracer
```text
1. Créer 2 VLANs sur 2 switches et tester ping intra/inter VLAN.
2. Configurer routage statique et tester communication inter-réseaux.
3. Configurer RIP sur 3 routeurs et tester ping inter-réseaux.
4. Ajouter AP, configurer SSID et mot de passe, tester ping avec un PC et une tablette.
5. Mettre en place un portail captif et tester authentification.
```

---

### 9. Commandes utiles résumé
```bash
# Switch
enable
configure terminal
vlan <num>
name <nom>
interface fa0/x
switchport access vlan <num>
exit

# Routeur statique
ip route <réseau> <masque> <prochain_saut>

# Routeur dynamique RIP
router rip
version 2
network <réseau>

# Test de communication
ping <IP>
```

---

## Fiche de révision – Sous-réseaux IPv4

**Objectif :**  
Comprendre comment calculer et utiliser les sous-réseaux IPv4, déterminer le masque en fonction du nombre d’hôtes et identifier les adresses réseau, broadcast et utilisables.

---

### 1️⃣ Concepts clés

- **Adresse IP** : identifie un appareil sur un réseau.  
- **Masque de sous-réseau** : détermine quelles parties de l’IP correspondent au réseau et aux hôtes.  
- **CIDR (/n)** : notation indiquant le nombre de bits réseau dans le masque.  
- **Sous-réseautage (subnetting)** : découper un réseau en plusieurs sous-réseaux plus petits.  
- **Formules importantes** :  

```text
Total d’adresses = 2^(32 - n)
Hôtes utilisables = 2^(32 - n) - 2
```

---

### 2️⃣ Calculer le masque à partir du nombre d’hôtes

1. Ajouter 2 à ton nombre d’hôtes désiré (réseau + broadcast).  
2. Trouver la puissance de 2 supérieure ou égale à ce total.  
3. Masque CIDR = 32 - (nombre de bits hôtes).  
4. Masque décimal = convertis les bits 1 en 255 et les 0 en 256 - taille du bloc.

**Exemple :**  

```text
Nombre d’hôtes voulus = 2
Total avec réseau + broadcast = 4
2 bits hôtes → Masque /30 → 255.255.255.252
```

---

### 3️⃣ Tableau des masques IPv4

| CIDR | Masque décimal | Bits hôtes | Total adresses | Hôtes utilisables | Taille bloc |
|------|----------------|------------|----------------|------------------|------------|
| /30  | 255.255.255.252 | 2  | 4   | 2   | 4  |
| /29  | 255.255.255.248 | 3  | 8   | 6   | 8  |
| /28  | 255.255.255.240 | 4  | 16  | 14  | 16 |
| /27  | 255.255.255.224 | 5  | 32  | 30  | 32 |
| /26  | 255.255.255.192 | 6  | 64  | 62  | 64 |
| /25  | 255.255.255.128 | 7  | 128 | 126 | 128|
| /24  | 255.255.255.0   | 8  | 256 | 254 | 256|

> 💡 Astuce : les réseaux plus grands ont plus d’hôtes, les réseaux plus petits sont plus sûrs pour les liens point-à-point (/30, /29).

---

#### 4️⃣ Exemple pratique avec IP

```text
IP : 10.0.0.1/30
Adresse réseau : 10.0.0.0
Hôtes utilisables : 10.0.0.1 et 10.0.0.2
Broadcast : 10.0.0.3
```

---

#### 5️⃣ Schéma visuel simplifié

```text
10.0.0.0/30: [Network] [Host1] [Host2] [Broadcast]
10.0.0.0        10.0.0.1   10.0.0.2   10.0.0.3
```

---

### 6️⃣ Commandes utiles 

```bash
#### Afficher les interfaces et IP sur Linux
ip a

#### Vérifier le masque et la passerelle sur Windows
ipconfig

#### Ping pour tester connectivité
ping 10.0.0.2
```


---

### 8️⃣ Notes rapides

- Masque **grand (/30, /29)** → moins d’hôtes, idéal pour les liens point-à-point.  
- Masque **petit (/24, /16)** → plus d’hôtes, adapté pour LAN plus grands.  
- Toujours vérifier que le nombre d’hôtes nécessaires rentre dans le masque choisi.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Fiche visuelle – Supports physiques et transmission des données

**Objectif :**  
Identifier et comparer les différents supports physiques de transmission : cuivre, fibre, ondes.

---

### 1️⃣ Câbles à paires torsadées (Cuivre)

**Type de câble :**
| Type | Nom complet | Blindage | Débit max | Longueur max | Utilisation |
|------|--------------|-----------|------------|---------------|--------------|
| 🟢 UTP | Unshielded Twisted Pair | ❌ Non blindé | 10 Gb/s | 100 m | Réseaux locaux |
| 🟡 STP | Shielded Twisted Pair | ✅ Blindé | 1 Gb/s | 100 m | Milieu parasité |
| 🔵 FTP | Foiled Twisted Pair | 🔶 Semi-blindé | 1 Gb/s | 100 m | Usage mixte |

**Normes RJ45 :**
| Norme | Utilisation | Description |
|--------|--------------|-------------|
| T568A | Résidentiel | Standard ancien |
| T568B | Professionnel | Le plus courant |

**Schéma simplifié (paires torsadées) :**
```text
[1]----[2]
  ↘  ↗
   ↘↗    => torsade = réduction du bruit EM
  ↗  ↘
[3]----[6]
```

**Câblage :**
```text
Droit : PC → Switch
Croisé : Switch → Switch (ancien)
```

---

### 2️⃣ Fibre optique

**Principe :**
Transmission de lumière à travers un cœur de verre ou plastique.

**Structure :**
```text
+-----------------------------+
|  Revêtement protecteur      |
|    +---------------------+  |
|    | Gaine optique       |  |
|    |   +-------------+   |  |
|    |   | Coeur       |   |  |
|    |   +-------------+   |  |
|    +---------------------+  |
+-----------------------------+
```

| Type | Bande passante | Distance | Description |
|-------|----------------|-----------|--------------|
| 🟢 Monomode | Très élevée (1 GHz) | Jusqu’à 10 000 km | Transmission longue distance |
| 🔵 Multimode | Moyenne | Jusqu’à 2 km | Réseaux internes / campus |

---

### 3️⃣ Ondes électromagnétiques

**Principe :** Transmission de signaux radio via l’air (WiFi, Bluetooth, satellite...).

| Type | Bande de fréquence | Débit | Portée | Exemple |
|-------|--------------------|--------|---------|----------|
| 🛰 Satellite | 40 GHz – 400 MHz | 140 Mb/s | 36 000 km | Liaisons longues distances |
| 📡 Hertzien (WiFi, Wimax) | 2.4 / 5 / 5.7 GHz | 1 → 300 Mb/s | 200 m → 50 km | Réseaux locaux / urbains |
| 🔊 Bluetooth / Zigbee | 2.4 GHz | < 5 Mb/s | 10–100 m | Objets connectés |

**Représentation simplifiée :**
```text
Couleur (longueur d’onde) : 
Rouge ─ Orange ─ Jaune ─ Vert ─ Bleu ─ Violet ─ (invisible : infrarouge, UV)

 ↑ Fréquence
 ↓ Longueur d’onde
```

---

### 4️⃣ Comparatif global des supports

| Support | Transmission | Bande passante | Portée | Avantages | Inconvénients |
|----------|---------------|----------------|---------|-------------|----------------|
| 🟢 Cuivre | Électrique | Moyenne | Courte (100 m) | Peu coûteux, simple | Sensible au bruit |
| 🔵 Fibre | Optique | Élevée | Très longue | Haut débit, fiable | Coût + fragilité |
| 🛰 Ondes | Radio / Micro-onde | Variable | Moyenne à longue | Sans fil, flexible | Parasites, sécurité |

---

### 5️⃣ Notes rapides

- 🌐 Couche physique = transmission des bits  
- 🧭 Support = cuivre / fibre / onde  
- ⚙️ Dépend du type de médium (liaison filaire ou sans fil)  
- 🧩 Normes principales : IEEE 802.3 (Ethernet), IEEE 802.11 (WiFi)  
- 💡 Fibre = meilleure qualité et distance, mais plus coûteuse  

-------------------------------------------------------------------------------------------------------



