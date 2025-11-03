- show mac address-table : voir la table de commutation  
    
- création d’un vlan:   
    
  enable  
  configure terminal  
  vlan 10  
  name “direction”  
  exit  
    
- assigner interface (port) à un vlan:  
    
  configure terminal  
  interface fa0/1                    ou interface range 1-8  
  switchport mode access  
  switchport access vlan 10  
  exit  
    
- configuration de la sécurité des ports, adresse MAC statique:  
  enable  
  configure terminal  
  interface fastEthernet 0/18  
  switchport mode access  
  switchport port-security  
  switchport port-security mac-address AdresseMac  
  end  
    
- configuration de la sécurité des ports, adresse MAC dynamique:  
    
  enable  
  configure terminal  
  interface fa0/5  
  switchport mode access  
  switchport port-security  
  end  
    
- configuration de la sécurité des ports,adresse MAC rémanente:  
    
  enable  
  configure terminal  
  interface fa0/5  
  switchport mode access   
  switchport-security  
  switchport security maximum 10  
  switchport port-security mac address sticky  
  end  
    
- interface peut être remplacé par interface range si c’est plusieurs ports avec par exemple interface range fastEthernet 0/1-5  
    
- affichage des paramètres de sécurité des ports du commutateur ou de l’interface que l’on souhaite:  
    
  show port-security \[ici mettre: interface id\_interface\]  
    
- désactiver les ports non utilisés:  
    
  configure terminal  
  interface (ou interface range)  
  shutdown

- configuration d’un switch en mode VTP serveur:  
    
  vtp domain \[MonReseau\]  
  vtp mode server  
  vtp password \[mot de pass\]  
    
- vérifier les vlans:  
    
  show vlan brief  
    
- Attribuer un nom d’hôte au switch:  
    
  hostname \[nom switch\]  
    
- Assigner une adresse IP au VLAN 1 permet d’accéder au commutateur via SSH ou Telnet et de le gérer sans avoir à être physiquement connecté à celui-ci.

- attribuer une IP au VLAN 1 pour pouvoir se connecter à distance:  
    
  configure terminal  
  interface vlan 1  
  ip address 192.168.1.100 255.255.255.0  
  no shutdown  
    
- activer une interface:  
    
  no shutdown 

- vérifier que l’interface spécifique est bien activée ‘si ping pc ne fonctionne pas):  
    
  show interfaces FastEthernet0/1 status  
    
- vérifier l’état des interfaces:  
  show ip interface brief  
    
- vérifier le statut de toutes les interfaces:  
    
  show interfaces status  
    
- enregistrer les modifications:  
    
  write memory

- consulter la table des adresses MAC:  
    
  show mac address-table  
    
- pour voir uniquement les entrées associées à un port spécifique:  
    
  show mac address-table interface FastEthernet0/1  
    
- 

  