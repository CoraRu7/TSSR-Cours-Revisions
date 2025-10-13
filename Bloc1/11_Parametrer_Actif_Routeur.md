# Paramétrer un actif de type Routeur


## Les composants d’un routeur



### 🎯 Objectif
Comprendre la structure, le rôle et le fonctionnement d’un routeur, ainsi que ses interfaces, ses composants matériels et les différents types de routeurs existants.

---

### 🧠 Concepts clés

- Un **routeur** est un périphérique réseau chargé de **transférer des paquets de données** entre différents réseaux.
- Il détermine le **meilleur chemin** pour le trafic réseau.
- Possède plusieurs **interfaces et ports** pour les connexions LAN, WAN ou de gestion.
- Joue un rôle essentiel dans la **sécurité, la connectivité et la distribution des ressources**.

---

### ⚙️ Présentation d’un routeur

#### 📝 Définition
Un routeur est un appareil qui achemine des paquets de données entre les réseaux.  
Exemple : lorsqu’un utilisateur saisit `www.google.com`, la requête traverse plusieurs routeurs avant d’atteindre le serveur de Google.

#### 💡 Complément
Un routeur dispose de plusieurs interfaces pour se connecter à différents hôtes et réseaux.

---

### 🧩 Composants matériels d’un routeur

| Composant | Rôle |
|------------|------|
| **Alimentation électrique** | Fournit l’énergie nécessaire au fonctionnement du routeur |
| **Ventilateur** | Refroidit les composants internes |
| **Cartes d’interface WAN (WIC / HWIC)** | Connectent le routeur aux réseaux WAN |
| **RAM (SDRAM)** | Stocke la configuration active et les tables de routage |
| **NVRAM & Flash** | Contiennent le code de démarrage (ROMMON) et la configuration sauvegardée |
| **CPU** | Exécute les processus du système d’exploitation du routeur |
| **Module AIM** | Délègue certaines fonctions au processeur secondaire (ex : cryptage) |

🔧 Un technicien réseau doit connaître l’emplacement et le rôle de ces composants dans le matériel Cisco.

---

### 🔌 Interfaces et ports d’un routeur

#### Principaux types d’interfaces :

| Interface | Description |
|------------|-------------|
| **Console (RJ45 / USB mini-B)** | Configuration initiale via CLI |
| **USB-0 / USB-1** | Extension de stockage (mémoire flash) |
| **Gigabit Ethernet (GE0/0, GE0/1)** | Connexions LAN ou interconnexion entre routeurs |
| **Port AUX (RJ45)** | Accès distant (anciennement pour modems) |
| **Emplacements eHWIC** | Modules WAN (série, DSL, sans fil, etc.) |
| **CompactFlash (CF0, CF1)** | Stockage additionnel et démarrage du système |

#### 🧭 Regroupement des connexions
- **Ports de gestion (violet)** : console et AUX — servent à la configuration, pas au trafic utilisateur.  
- **Interfaces en bande (orange)** : LAN et WAN — transportent le trafic réseau.  

---

### 🧮 Fonctions d’un routeur

| Fonction | Description |
|-----------|--------------|
| **Acheminement des paquets** | Oriente les données vers la bonne destination |
| **Attribution d’adresses IP (DHCP)** | Fournit automatiquement une adresse IP aux hôtes |
| **Pare-feu intégré** | Protège contre le trafic non autorisé |
| **Partage de ressources** | Permet le partage d’imprimantes, fichiers et périphériques sur le réseau |

---

### 🧭 Commandes de diagnostic : `traceroute` / `tracert`

#### 🎓 Principe
La commande **`traceroute`** (ou `tracert` sous Windows) permet d’analyser le **chemin emprunté par les paquets IP** entre un hôte source et une destination.

- Utilise le champ **TTL (Time To Live)** pour identifier chaque routeur intermédiaire.  
- Chaque saut (routeur) renvoie un message **ICMP** lorsqu’un paquet expire.  
- Le résultat affiche la **liste ordonnée** des routeurs traversés et le **temps de réponse**.  

💡 Très utile pour **détecter les points de défaillance** dans un réseau.

---

### 🛰️ Différentes utilisations d’un routeur

- Acheminer les données vers la **destination correcte**
- Servir de **tampon entre le modem et le réseau local**
- **Sécuriser** la communication et bloquer les menaces
- **Partager les informations** avec d’autres routeurs ou réseaux

---

### 🧱 Types de routeurs

| Type | Description |
|------|--------------|
| **Routeur filaire** | Connexion par câble Ethernet, souvent avec NAT, SPI et DHCP. Idéal pour petits réseaux. |
| **Routeur sans fil** | Transmet les données via signaux radio (Wi-Fi), emploie WPA et filtrage MAC. |
| **Routeur virtuel** | Logiciel utilisant le protocole VRRP pour redondance et bascule automatique. |
| **Routeur Core (principal)** | Routeur central d’un réseau, très haute capacité, supporte plusieurs interfaces télécom. |
| **Routeur de bordure (Edge)** | Placé à la limite du réseau, connecté au FAI, utilise le protocole BGP. |

---

### 🧾 Commandes / Notes utiles

```bash
# Afficher la table de routage
show ip route

# Vérifier les interfaces actives
show ip interface brief

# Lancer un traceroute (Cisco)
traceroute [adresse IP]

# Lancer un tracert (Windows)
tracert [adresse IP]
```
Liens utiles
RFC 1812 Requirements for IP routers
---

## Paramétrer un routeur et un switch sous packet tracer



### 🎯 Objectif

Apprendre à configurer un switch et un routeur dans Cisco Packet Tracer : accès CLI, hostname, VLANs, affectation des ports, trunk, sécurisation des ports, router-on-a-stick (sous-interfaces 802.1Q), routes statiques, tests (ping/traceroute), vérifications et sauvegarde.

---

### 📚 Contexte

Les switches et les routeurs sont les piliers de toute infrastructure réseau. Un switch connecte plusieurs périphériques dans un réseau local et, grâce aux VLANs, segmente le réseau pour renforcer la sécurité et l’efficacité. Le routeur connecte plusieurs réseaux entre eux et achemine les données selon les chemins définis. La configuration précise et sécurisée est indispensable pour garantir une communication fluide entre les différents segments.

---

### 1 — Configuration d’un SWITCH sous Packet Tracer

#### 1.1 Accès au switch via le CLI

Le CLI (« Command-Line Interface ») permet de configurer les équipements Cisco.

##### Modes

* `Switch>` : mode utilisateur limité (lecture seule)
* `Switch#` : mode privilégié (`enable`)
* `Switch(config)#` : mode configuration globale (`configure terminal`)

##### Méthode

```bash
enable
configure terminal
```


##### Exemple

```bash
Switch> enable
Switch# configure terminal
Switch(config)#

```


*Remarque :* le prompt indique le niveau d’accès.

---

#### 1.2 Nommer le switch (hostname)

Le `hostname` identifie l’équipement et facilite sa gestion.

##### Commande

```bash
hostname <nom_du_switch>
```

##### Exemple

```bash
Switch(config)# hostname SwitchSalle1
SwitchSalle1(config)#
```

*Conseil :* adopter une convention de nommage claire (ex : site-fonction-emplacement).

---

#### 1.3 Configuration des VLANs

##### Rappel

Les VLANs segmentent un réseau physique en réseaux logiques (ID 1–4095), isolant les groupes d’utilisateurs ou périphériques.

##### Méthode — création et nommage

```bash
vlan <ID>
name <nom_vlan>
```

##### Exemple

```bash
Switch(config)# vlan 10
Switch(config-vlan)# name Vente
Switch(config)# vlan 20
Switch(config-vlan)# name RH
```

---

#### 1.4 Affectation des ports aux VLANs (mode access)

##### Méthode

```bash
interface range fa0/1 - 10
switchport mode access
switchport access vlan 10
exit

```

##### Exemple

```bash
Switch(config)# interface range fa0/1 - 10
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# exit
```

*Remarque :* les ports en access ne communiquent pas entre VLANs sans routage inter-VLAN.

---

#### 1.5 Mode trunk

Pour faire transiter plusieurs VLANs sur un port entre switch et routeur :

##### Exemple trunk

```bash
interface FastEthernet0/3
switchport mode trunk
switchport trunk allowed vlan 10,20
exit
```

##### Vérification

```bash
show interfaces trunk
show running-config
```

---

#### 1.6 Sécurisation des ports (Port Security)

##### Rappel

Port-security restreint les périphériques autorisés par adresse MAC sur un port.

##### Méthode

```bash
interface fa0/1
switchport mode access
switchport port-security
switchport port-security maximum <nombre>
switchport port-security mac-address sticky
switchport port-security violation {shutdown | restrict | protect}
exit
```

##### Exemple concret

```bash
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation restrict
Switch(config-if)# exit
```

##### Vérification

```bash
show port-security interface fa0/1
```

---

#### 1.7 Vérifications et sauvegarde

##### Vérifier les VLANs

```bash
show vlan brief
```

##### Voir la configuration courante

```bash
show running-config
```

##### Sauvegarder

```bash
copy running-config startup-config
```

##### Vérifier la config de démarrage

```bash
show startup-config
```

---

### 2 — Configuration d’un ROUTEUR sous Packet Tracer

#### 2.1 Connexion et modes

* `Router>` : mode utilisateur limité
* `Router#` : mode privilégié
* `Router(config)#` : mode configuration globale

##### Accès

```bash
enable
configure terminal

```

---

#### 2.2 Nommer le routeur

##### Commande

```bash
hostname <nom_du_routeur>
```

##### Exemple

```bash
Router(config)# hostname Routeur-Salle1
Routeur-Salle1(config)#
```

*Conseil :* noms uniques et descriptifs.

---

#### 2.3 Configuration des interfaces

##### Interface physique

```bash
interface gigabitEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```

##### Router-on-a-stick (sous-interfaces 802.1Q)

```bash
interface gigabitEthernet0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
exit

interface gigabitEthernet0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
exit

interface gigabitEthernet0/0
no shutdown
exit

```

##### Vérification

```bash
show ip interface brief

```

---

#### 2.4 Configuration des routes

##### Ajouter une route statique

```bash
ip route <destination> <masque> <passerelle>
```

##### Exemple

```bash
ip route 192.168.2.0 255.255.255.0 192.168.1.2
```

##### Supprimer une route

```bash
no ip route 192.168.2.0 255.255.255.0 192.168.1.2
```

##### Route par défaut

```bash
ip route 0.0.0.0 0.0.0.0 <passerelle>
```

##### Vérification

```bash
show ip route
```

---

### 3 — Tests de connectivité et débogage

#### 3.1 Commandes de test

* `ping <adresse>` : test ICMP
* `traceroute <adresse>` (Cisco) / `tracert <adresse>` (Windows) : voir le chemin des paquets

##### Exemple

```bash
ping 192.168.1.1
traceroute 8.8.8.8
```

#### 3.2 Vérifications supplémentaires

* `show ip interface brief`
* `show ip route`
* `show running-config`
* Vérifier `no shutdown`, adresses IP, masques, gateway, VLAN, port-security.

---

### 4 — Exemple complet : topologie PC VLAN10 ↔ PC VLAN20

#### Switch

```bash
enable
configure terminal
hostname SW-Lab

vlan 10
name Vente
vlan 20
name RH

interface range fa0/1 - 10
switchport mode access
switchport access vlan 10
exit

interface range fa0/11 - 20
switchport mode access
switchport access vlan 20
exit

interface fa0/3
switchport mode trunk
switchport trunk allowed vlan 10,20
exit

copy running-config startup-config

```

#### Routeur (router-on-a-stick)

```bash
enable
configure terminal
hostname R1

interface gigabitEthernet0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
exit

interface gigabitEthernet0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
exit

interface gigabitEthernet0/0
no shutdown
exit

copy running-config startup-config
```

#### PC (Packet Tracer → Desktop → IP Configuration)

* PC VLAN10 : IP `192.168.10.10`, Mask `255.255.255.0`, Gateway `192.168.10.1`
* PC VLAN20 : IP `192.168.20.20`, Mask `255.255.255.0`, Gateway `192.168.20.1`

#### Tests

```bash
! Sur le switch
show vlan brief
show interfaces trunk

! Sur le routeur
show ip interface brief
show ip route

! Depuis PC1
ping 192.168.20.20
traceroute 192.168.20.20
```

---

### 5 — Commandes récapitulatives

#### Modes

```bash
enable
configure terminal
exit
```

#### VLAN & ports (switch)

```bash
vlan <ID>
name <nom>
interface range fa0/x - y
switchport mode access
switchport access vlan <ID>
interface <port_trunk>
switchport mode trunk
switchport trunk allowed vlan <liste>
```

#### Port-security

```bash
switchport port-security
switchport port-security maximum <n>
switchport port-security mac-address sticky
switchport port-security violation {shutdown|restrict|protect}
show port-security
```

#### Routeur (interfaces & routes)

```bash
interface gigabitEthernet0/0
no shutdown
interface gigabitEthernet0/0.10
encapsulation dot1Q 10
ip address <IP> <MASK>
exit
ip route <dest> <mask> <next-hop>
show ip interface brief
show ip route
```

#### Sauvegarde & vérification

```bash
show running-config
show startup-config
copy running-config startup-config
show vlan brief
show interfaces trunk
```

---

### 6 — Bonnes pratiques & conseils

* Utilise une **convention de nommage cohérente** (ex : `Site-Rôle-N°`)
* **Évite VLAN 1** pour le trafic de production
* Documente toujours ports, VLANs, adresses IP et plan d’adressage
* Active la **port-security** sur les ports exposés
* Sauvegarde après validation : `copy running-config startup-config`
* Teste avec `ping` puis `traceroute`
* Pour réseaux larges, utilise des protocoles de routage dynamiques (OSPF/EIGRP) plutôt que trop de routes statiques

---

## Le routage statique sous packet tracer
## Lire une table de routage
## Mettre en œuvre un protocole de routage
