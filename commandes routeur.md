**Routage statique:**

- configuration de l’adresse IP sur une interface du routeur:  
  enable  
  configure terminal  
  interface gigabitEthernet 0/0/0  
  ip address 10.0.0.254 255.0.0.0  
  no shutdown  
  exit  
    
- création d’une route:  
  ip  route  192.168.1.0  255.255.255.0  20.0.0.2  
  ou    
  ip route IP-réseau-destination masque-réseau-destination IP-prochain-saut  
    
- pour voir la table de routage:  
  show ip route

**Routage dynamique:**

- paramétrer le protocole de routage RIP sur le routeur:  
  enable   
  configure terminal   
  router rip   
  version 2   
  network 192.168.1.0   
  network 30.0.0.0   
  exit

Les réseaux spécifiés sont ceux auxquels il est connecté puis show ip route pour vérifier

**Commandes de base IOS Cisco:**

- Afficher la version IOS et les caractéristiques du routeur : show version  
- Affiche la configuration en cours: show running-config  
- Lister les interfaces avec leur état et adresse IP: show ip interface brief  
- définir un nom pour le routeur: hostname \[nom\]  
- définir un mot de passe pour accéder au mode enable (mdp stocké en clair) : enable password \[motdepasse\]  
- définir mot d passe pour mode enable chiffré : enable secret \[mot de passe\]  
- définir un message d’avertissment “message of the day: banner motd \# \[message\]\#  
- sélectionner l’interface: interface GigabitEthernet0/0  
- Attribuer une adresse IP: ip address \[IP\] \[masque\]  
- activer l’interface: no shutdown  
- sauvegarder la configuration: copy running-config startup-config  
- pour conigurer les lignes: line vty 0 4  \[ex: utilisé avec SSH\]  
- voire la table de routage: show ip route  Attention sortir du mode config/privilèges  
- attribuer une ip : ip address \[IP\] \[masque\]  
- pour attribuer un domaine a la place de l’ip dans une connexion distante : ip domain-name \[nomdedomaine.com\]  
- vérifier les routes ospf: show ip route ospf

**Exemple de configuration d’une interface avec une adresse IP:**  
enable  
configure terminal  
interface GigabitEthernet0/0  
ip address 192.168.1.1 255.255.255.0  
no shutdown  
exit  
**Restreindre l’accès aux lignes de commande (console):**

enable  
configure terminal  
line console 0  
password \[mot de passe\]  
login  
exit

**Configuration d’un accès distant (Telnet/SSH) sécurisé:**

enable   
configure terminal  
line vty 0 4  
password \[mot de passe\]  
login  
exit  
**Sécuriser l’accès distant via SSH:**

enable  
configure terminal  
hostname \[nom routeur\]  
ip domain-name example.com  
crypto key generate rsa  
line vty 0 4  
transport input ssh  
password sshaccess  
login  
exit

**configuration HSRP (Cisco):**

enable  
configure terminal  
interface GigabitEthernet0/1  
standby 1 ip 192.168.1.254           c’est IP virtuelle du groupe HSRP  
standby 1 priority 110                     c’est la priorité  
standby 1 preempt                         active le basculement automatique

**Création ACL standard (filtrage basé sur l’IP source):**

config terminal  
access-list 10 permit 192.168.1.0 0.0.0.255  
interface GigabitEthernet0/1  
ip access-group 10 in

ici autorise tout le réseau 192.168.1.0 (attention masque de sous réseau inversé)

**Création d’une ACL étendue (Filtrage par protocole, IP source et destination):**

Router(config)\# access-list 101 deny tcp any host 192.168.1.100 eq 23

Router(config)\# access-list 101 permit ip any any

Router(config)\# interface GigabitEthernet0/1

Router(config-if)\# ip access-group 101 in

ici Deny tcp any host 192.168.1.100 eq 23 → **Bloque Telnet** vers l’IP **192.168.1.100**

Permit ip any any → **Autorise tout le reste**

