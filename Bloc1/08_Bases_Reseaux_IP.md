# Les bases des réseaux IP

## La définition d’un protocole de communication
## Les caractéristiques des modèles osi, tcp et le principe d’encapsulation
## Le rôle de couche d’accès réseau et la liaison de données
## Le découpage d’un réseau IPv4
## Les fondamentaux d’IPv6
## Les topologies physiques et logique des réseaux
## Les équipements d’interconnexion
# Fiche de révision – Sous-réseaux IPv4

**Objectif :**  
Comprendre comment calculer et utiliser les sous-réseaux IPv4, déterminer le masque en fonction du nombre d’hôtes et identifier les adresses réseau, broadcast et utilisables.

---

## 1️⃣ Concepts clés

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

## 2️⃣ Calculer le masque à partir du nombre d’hôtes

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

## 3️⃣ Tableau des masques IPv4

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

## 4️⃣ Exemple pratique avec IP

```text
IP : 10.0.0.1/30
Adresse réseau : 10.0.0.0
Hôtes utilisables : 10.0.0.1 et 10.0.0.2
Broadcast : 10.0.0.3
```

---

## 5️⃣ Schéma visuel simplifié

```text
10.0.0.0/30: [Network] [Host1] [Host2] [Broadcast]
10.0.0.0        10.0.0.1   10.0.0.2   10.0.0.3
```

---

## 6️⃣ Commandes utiles (colorées sur GitHub)

```bash
# Afficher les interfaces et IP sur Linux
ip a

# Vérifier le masque et la passerelle sur Windows
ipconfig

# Ping pour tester connectivité
ping 10.0.0.2
```

---

## 7️⃣ Ajouter des images ou schémas

```markdown
![Schéma sous-réseau](images/sous_reseau.png)
```
- Mets le fichier `sous_reseau.png` dans un sous-dossier `images/` de ton projet.  

---

## 8️⃣ Notes rapides

- Masque **grand (/30, /29)** → moins d’hôtes, idéal pour les liens point-à-point.  
- Masque **petit (/24, /16)** → plus d’hôtes, adapté pour LAN plus grands.  
- Toujours vérifier que le nombre d’hôtes nécessaires rentre dans le masque choisi.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

