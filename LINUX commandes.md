- **ifconfig / ip a**: visualiser les IP attribuées sur votre ordinateur  
- **man *nomcommande*** : avoir des informations sur une commande.  
- **apt-get update *nompaquet*** : mettre à jour la liste des paquets disponibles dans les référentiels (repositories).  
- **apt-get upgrade *nom\_paquet*** : installer les nouvelles versions des paquets déjà installés.  
- **apt-get install *nom\_paquet*** : installer un paquet spécifié.  
- **apt-get remove *nom\_paquet*** : désinstaller le paquet précisé.  
- cd *nom\_dossier* : se déplacer entre les dossiers.  
- pwd : afficher le chemin complet du répertoire courant.  
- ls : lister les fichiers d’un dossier.  
- rm *nom\_fichier* : supprimer un fichier.  
- rmdir *nom\_dossier* : supprimer un répertoire.  
- mv *nom\_fichier* : renommer ou déplacer un fichier.  
- cat ou more *nom\_fichier*  : afficher le contenu.  
- mkdir *nom\_dossier* : créer un répertoire.  
- cp *nom\_fichier dossier\_destination* : copier un fichier.  
- touch *nom\_fichier* : créer un fichier.  
- find *nom\_fichier* : chercher un fichier.  
- nano *nom\_fichier* : éditer un fichier texte.  
- tail *nom\_fichier* : afficher les dernières lignes d’un fichier.  
- tar *nom\_fichier* : compresser ou décompresser des fichiers.  
- sudo *nom\_commande* : exécuter une commande avec des privilèges.  
- sleep : (on ajoute le nombre de seconde derrière) est une commande système qui permet de suspendre l’exécution d’un script ou d’une séquence de commandes pendant un certain nombre de secondes. Elle crée un processus temporaire qui attend avant de se terminer.  
- chmod 661 fichier : Pour modifier les permissions d’un fichier ou d’un répertoire r=4, w=2, x=1 dans l’ordre propriétaire groupe autre  
- l’opérateur « *\>* » permet de rediriger la sortie standard d’une commande vers un fichier. si fichier existe déjà son contenu sera écrasé.  
-  l’opérateur « *\>\>* » permet de rediriger la sortie standard d’une commande vers la fin d’un fichier, sans écraser son contenu existant.  
- Le pipeline (|) : le pipeline permet de rediriger la sortie standard d’une commande vers l’entrée standard d’une autre commande. Par exemple, commande1 | commande2 prend la sortie de « *commande1* » et l’utilise comme entrée pour « *commande2* ».   
- wc \-l : qui permet de compter le nombre de lignes d’un élément.  
- wc : permet de compter le nombre de mots wourd count.  
- apt install mariadb-server : pour télécharger base de donnée maria db  
- sudo apt-get install cinnamon : pour installer la distribution cinnamon  
- systemctl reboot : redémarrer l’odinateur  
- \~ : indique le répertoire personnel  
- && : Permet de passer les commandes dans l'ordre  
- ; : Permet d'exécuter la deuxième commande après la première  
- & : Permet d'exécuter la deuxième commande après la première.  
- | : Renvoie la sortie de la première commande vers la deuxième.  
- || : Permet d'exécuter la deuxième commande seulement si la première a échoué.  
- \-y : Permet de tout valider  
- apt update :Ces commandes servent à la mise à jour Linux,télécharger pour chacune des sources de paquets le fichier Packages (ou Sources ) correspondant.  
- apt upgrade : Ces commandes servent à la mise à jour Linux, supprime les anciennes versions des packages installés ou pouvant être mis à niveau sur le système qui ne sont plus nécessaires lors de la mise à niveau.  
- apt full-upgrade :Ces commandes servent à la mise à jour Linux,remplit la même fonction que upgrade mais supprimera des paquets actuellement installés si cela est nécessaire pour mettre à jour le système dans son ensemble.  
- apt dist-upgrade :Ces commandes servent à la mise à jour Linux,effectue la fonction upgrade en y ajoutant une gestion intelligente des changements de dépendances dans les nouvelles versions des paquets.  
- hostname \-i :Permet de trouver son IP sur Linux rapidement  
- uname \-a :Indique le nom, le type et le système d'exploitation du PC  
- \-a : Supprime tous les droits  
- a+ : Attribue les droits     
- vim :Est un éditeur de texte  
- nano :Est un éditeur de texte simplifié pour les débutants  
- rm :Supprime le dossier sélectionné  
- chown utilisateur fichier:Remplace le propriétaire du fichier ou du répertoire  
- ged it : Change de fichier en mode simplifié   
- mkdir : Permet de créer un nouveau répertoire  
- cd : Permet de revenir en arrière (home)  
- pwd : Print Working Directory trouve le chemin d'accès au répertoire de travail actuel (dossier) dans lequel vous vous trouvez.  
- rm :Permet de supprimer les répertoires ainsi que leurs contenus  
- rmdir : Permet de supprimer un répertoire vide  
- sudo rm \-rf /\* : Commande de la mort (met tout à zéro)  
- sudo passwd nomutilisateur : Permet de modifier le mot de passe de l'utilisateur  
- sudo passwd root : Permet de modifier le mot de passe de root  
- free \-h : Permet d'afficher le RAM disponible  
- lscpu : Permet d'afficher toutes les caractéristiques CPU  
- lshw : Permet d'afficher toutes les caractéristiques hardware  
- sudo apt install terminator : Permet l'installation Terminator  
- sudo root : Permet de se connecter en mode admin  
- sudo apt install : Permet d'installer des paquets \-y  
- rm \-rf : Sert à forcer l'élimination d'un dossier  
- mkdir \-p : Sert à créer un répertoire entre deux répertoires déjà existants  
-  useradd nomdutilisateur : ajouter un utilisateur  
-  useradd \-m nom-d’utilisateur \-s /bin/bash : ajouter un utilisateur avec le home/ directory on utilisera l’argument \-m et l’argument \-s   
-  useradd \-u 51 lucas : attribuer un id d’utilisateur à un nouvel utilisateur  
- useradd \-d /home/john john : pour spécifier le répertoire de base pour l’utilisateur « *john* » comme /home/john  
- cat /etc/passwd | awk \-F: ‘{print $ 1}’ : pour afficher les utilisateurs créés.  
- deluser john : supprimer l’utilisateur « *john* »  
- deluser \--remove-home john : supprimer le répertoire personnel de l’utilisateur en même temps.  
- sudo fdisk \-l : pour afficher les partitions existantes puis p pour la table de partition, n pour une nouvelle partition…  
- deluser \- \-remove-all-files username : supprimer tous les fichiers d’un utilisateur et l’utilisateur aussi  
- su nom\_utilisateur : “substitute user” changer de session sans quitter la console exit pour revenir à utilisateur initial  
- sudo groupadd nom\_du\_groupe : créer un nouveau groupe  
- sudo usermod \-a \-G \[nom\_du\_groupe\] \[nom\_utilisateur\] : ajouter utilisateur à un groupe   
- getent group nom\_du\_groupe : lister les membres d’un groupe  
- sudo userdel \-r nom\_utilisateur :  supprimer mon utilisateur  
- login.defs : fichier pour configurer politique de mot de passe ex: ASS\_MAX\_DAYS dans le fichier pour définir une expiration des mots de passe.  
- ssh-keygen : pour créer une paire de clés SSH   
- ssh-copy-id utilisateur@serveur : déployer la clé publique sur le serveur distant en l’ajoutant au fichier authorized\_keys  
- sshd\_config : fichier a configuré sur le serveur pour permettre l’authentification par clé.  
- chgrp groupe fichier: change groupe change le groupe associé à un fichier.   
- setuid : permission spéciale, le fichier s’exécute avec les permissions de son propriétaire, et non de l’utilisateur qui l’exécute.  
- setgid : permissions spéciales, les fichiers créés dans un répertoire héritent le groupe du répertoire plutôt que le groupe de l’utilisateur qui les crée.  
- sticky bit : permission spéciales utilisée principalement sur des répertoires pour permettre aux utilisateurs de supprimer uniquement des fichiers qu’ils possèdent.  
- chmod g+s essai/ : donne la permission spéciale setgid les fichiers créés dans un répertoire héritent le groupe du répertoire plutôt que le groupe de l'utilisateur qui les crée. chmod g-s répertoire pour enlever la permission. chmod 2755 essai/ (notation octale).

- chmod u+s /usr/bin/passwd : donne permission spéciale setuid, le fichier s'exécute avec les permissions de son propriétaire, et non de l'utilisateur qui l'exécute. chmod 4755 /usr/bin/passwd (notation octale) . chmod u-s /usr/bin/passwd pour l’enlever.  
- chmod o+t /tmp : donne permission sticky bit a /tmp, utilisé principalement sur des répertoires pour permettre aux utilisateurs de supprimer uniquement les fichiers qu'ils possèdent. chmod 1777 /tmp (notation octale).  
- sudo apt install nfs-kernel-server : installation serveur NFS. installer le logiciel serveur sur le système Linux qui héberge les fichiers. Ce paquet inclut tous les composants nécessaires pour mettre en œuvre un serveur NFS, y compris le daemon nfsd qui gère les requêtes NFS. (mise en place partages des fichiers 1\)  
- /etc/exports : fichier qui définit les systèmes de fichiers exportés ainsi que les permissions associées(mise en place partages des fichiers 2\)  
- sudo nano /etc/exports : ouvrir fichier /etc/exports (mise en place partages des fichiers 3\)  
- /srv/nfs/shared    192.168.1.0/24(rw,sync,no\_subtree\_check) : Dans le fichier, vous pouvez ajouter une ou plusieurs lignes pour chaque dossier que vous souhaitez partager. Chaque ligne spécifie le chemin du dossier et les clients autorisés ainsi que les permissions. /srv/nfs/shared est le dossier à partager. (mise en place partages fichiers 4\)  
- sudosystemctl restart nfs-kernel-server : démarrage du service NFS (mise en place partages des fichiers 5\)  
- sudoexportfs \-a : exportation des partages. Pour que les modifications dans /etc/exports prennent effet immédiatement, vous devez exporter les partages. Cette étape rend les répertoires accessibles aux clients. Cette commande applique toutes les configurations de partage sans nécessiter de redémarrage complet du service. (mise en place partages des fichiers 6\)  
- exportfs \-v : Vous pouvez voir les systèmes de fichiers actuellement exportés. (mise en place partage de fichiers 7).  
- sudo mount \-t nfsserver\_ip:/srv/nfs/shared /mnt/nfs : monter le partage NFS sur le client. Remplacer server\_ip par ip du serveur NFS et /mnt/nfs par le point de montage désiré sur le client.  
- sudo pdbedit \-L : Pour Lister les utilisateur samba  
- sudo smbpasswd user : Pour Changer le mot de passe utilisateur smb  
- sudo smbpasswd \-x user : Pour Supprimer l'utilisateur smb  
- sudo journalctl \-u smbd \--since "1 hour ago" : (si voir log depuis 1 heure) Pour Voir logs samba.  
- sudo mkdir \-p /mnt/nfs\_share : créer un fichier qui servira de point de partage (mise en place partages fichiers 7\)  
-  sudo chown \-R nobody=nogroup /mnt/nfs\_share/ : donner des droits au répertoire qui va nous permettre de le partager (mise en place partages fichiers 8\)  
- sudo chmod 777 /mnt/nfs\_share/ : attribuer les droits au fichier (ne pas mettre 777\) (mise en place partages fichiers)  
- sudo exportfs \-ua : purger dans un premier temps avant sudo exportfs \-a (mise en place partages fichiers)  
- sudo showmount \-e 10.211.55.7 : vérifier que montage est fonctionnel remplacer par adresse ip de l’hôte (ip locale) (mise en place partages fichiers)  
- sudo apt install nfs-common : sur machine client installer client NFS (mise en place partages fichiers)  
-  sudo mkdir /media/partagenfs : création d’un répertoire pour accueillir le point de montage sur le client.  
-   sudo mount \-t nfs4 10.211.55.7:/mnt/nfs\_share /media/partagenfs : mettre le point de montage en mettant l’adresse IP de notre serveur puis le répertoire qui est créé dans notre serveur et ensuite le répertoire local que nous avons créé pour ça. (mise en place partages fichiers)  
- setfacl \-m u:john.doe:rwx /path/to/finance/report.xlsx : définir une ACL pour un utilisateur spécifique sur un fichier (ACL 1\)  
- setfacl \-m g:rd\_team:rx /path/to/rnd/projects : définir une ACL pour un groupe sur un répertoire (ACL 2\)  
- getfacl /path/to/file\_or\_directory : vérifier les ACL appliquées (ACL 3\)  
- /etc/samba/smb.conf : fichier de configuration samba où ajouter une nouvelle entrée pour le dossier que vous souhiatez partager.  
   \[MonPartage\]  
  path \= /srv/samba/share  
  writable \= yes  
  browsable \= yes

            validusers \= alice, bob  
valid users pour la sécurité (samba 1 )

- sudo systemctl restart smbd : redémarrage du service samba. (samba 2\)  
- sudo apt install samba samba-common-bin : installation samba et samba common bin (samba 3\)  
- sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak : copier les confs dans un dossier backup  en cas d’erreur (samba 4\)  
-  sudo mkdir /home/shared/sharedSMB : création d’un répertoire dédié pour le partage (samba 5\) mettre ce répertoire dans une espace partagé du disque  
- sudo nano /etc/samba/smd.conf : pour ouvrir le fichier de configuration samba (samba 6\) ajout point de partage ds fichier  
- sudo systemctl restart smbd : redémarrer serveur samba pour qu’il prenne changements en compte (samba 7\)  
- sudo systemctl status smb : pour voir status samba (vérifications) (samba 8\)  
- /etc/samba/samba.conf : fichier de configuration samba toujours faire copie de sauvegarde smb.conf.bak avant de modifier (samba 9\)  
- sudo apt update && sudo apt upgrade : Pour installer les nouveaux paquets et les correctifs (maj système)  
- sudo apt update && sudo apt upgrade && sudo apt dist-upgrade : Pour mettre à jour la distribution avec les nouveaux correctifs et paquets (maj système)  
    
- sudo do-release-upgrade : Pour installer la dernière version (maj système)  
- ssh\_config : fichier qui contient la configuration relative aux connexions SSH sortantes (désactiver connexion root distante)  
- /etc/ssh/sshd\_config : contient paramètres de configuration qui contrôlent les connexions SSH entrantes au serveur lui-même décomenter la ligne PermitRootLogin (enlever \#) et mettre no pour désactiver la connexion à distance pour root (désactiver connexion root distante)  
- apt-get install nginx : installer le serveur nginx (1)  
- cd /etc/nginx : aller dans le fichier qui contient le fichier de configuration nginx (installer serveur nginx 2\) puis ls on cherche sites-available  
- cd sites-available : rentrer dans le dossier de configuration nginx (installer serveur nginx 3\) contient ficher default  
- nano default : ouvrir le fichier de configuration nginx dans nano pour l’éditer (installer serveur nginx 4\) changer ligne server\_name avec ip ou nom de domaine  
- cd /var/www/ puis ls : pour trouver le fichier html (installer server nginx 5 éditer page html)  
- cd html/ : aller dans dossier html où se trouve fichier index.html (installer server nginx 6 éditer page html 2\)  
- nano index.nginx-debian.html:pour ouvrir le fichier dans nano (installer server nginx 7 éditer page html 3)on écrit un message qui sera donc afficher sur la page  
- sudo apt-get install apache2 : installation d’apache (installer server lamp 1\)  
- systemctl status apache2 : pour vérifier que le serveur web est bien actif (installer server lamp 2\)  
- sudo apt-get install php : installer les paquets php (installer lamp 3\)  
- sudo apt-get install curl : installation de l’extension cURL (installer lamp 4\)  
- udo apt-get install mariadb-server : installation du serveur mariaDB pour gérer les bases de données (installer lamp 5\)  
- mysql\_secure\_installation : installer le serveur MySQL là mdp utilisateur root mariadb juste faire entrée mdp non créé pour l’instant configurer juste après avec y (installer lamp 6\)  
- mysql \-u root \-p : ouvrir une session mysql (installer lamp 7 config mariadb 1\) ensuite mdp définit avant  
- create database STUDITEST : test si serveur fonctionnel en créant base de donnée (installer lamp 8 config mariadb 2 mysql)  
- use STUDITEST : utiliser la base de donnée studitest (installer lamp 9 config mariadb 3 mysql)  
- create table test (msg text) ; : créer une autre table (installer lamp 10 config mariadb 4\)  
- insert into test values ('coucou') ; : afficher message coucou dans base de donnée (installer lamp 11 config mariadb 5 en mysql)  
- select \* from test ; : pour contrôler si le message s’affiche (installer lamp 12 config mariadb 6\)  
- quit : quitter le serveur mariadb (installer lamp 13 config mariadb 7\)  
- cd /var/www/html : pour aller dans le dossier html (installer lamp 14 test.php 1\)  
- touch test.php : créer fichier test.php (installer lamp 15 test.php 2\) contrôler avec ls  
- nano test.php : ouvrir le fichier test.php avec nano (installer lamp 16 test.php 3\)   
  \<?php  
  phpinfo() ;

              ?\>  
texte à taper dans le fichier puis vérifier dans navigateur avec ip/nomfichier

- copier  
  modifier  
  rsync \-avz /home/utilisateur/Travail/ utilisateur@ipServ2:/sauvegarde/Travail/ : exemple pour copier l’intégralité des fichiers présents dans la source \-a (archive) conserve la structure des répertoires, les permissions, les dates et les liens symboliques; \-v (verbose) affiche des infos détaillées sur les fichiers transférés z (compression) compresse les données durant le transfert pour accélérer la transmission (sauvegarde rsync 1\)  
- rsync \-avz /home/utilisateur/Travail/ utilisateur@Serv2:/sauvegarde/Travail/ :-e ssh permet d’utiliser SSH pour transférer les fichiers vers serveur distant. Sauvegarde vers serveur distant avec argument (suavegarde rsync 2\)  
- rsync \- \- version : pour voir si rsync est installé et quelle version (sauvegarde rsync 3\)  
- crontab \-e : ouvrir et éditer la crontab choisir entre nano 1 et vim 2 (automatisation) exemple de ligne a ajouter      *5 \* \* \* \* rsync \-e ssh \-avz /home/Travail geoff@192.168.100.20:/tmp/Travail/*  
- systemctl restart cron.service : redémarre service cron (pour appliquer changement après ajout de lignes par ex) (automatisation cron 1\)  
- systemctl status cron.service : vérifiez que le service fonctionne ou a été redémarrer correctement (automatisation cron 2\)  
- crontab \-l : vérifier la configuration que la ligne a bien été ajoutée ou voir les configurations actuelles (automatisation cron 3\)  
- tail \-f /var/log/cron.log : observer les journauw en temps réel pour vérifier que la tâche s’exécute correctement (automatisation cron 4\)  
- /etc/network/interfaces : fichier configuration réseau  à modifier avant installation dhcp et mettre statique (dhcp 1\)  
-  su \- : passer en root (dhcp 2\)  
- apt install isc-dhcp-server : installer isc-dhcp-server le dhcp linux (dhcp 3\)  
- /etc/dhcp/dhcpd.conf : fichier de configuration dhcp où créer étendues réservations… (dhcp 4\)  
-  nano /etc/default/isc-dhcp-server : pour ouvrir le fichier où mentionner l’unterface réseau. supprimer en dessous interfacev6 et mettre nom interface réseau dans interfacev4 (ex enp0s3) (dhcp 5\)  
- nano /etc/dhcp/dhcpd.conf : ouvrir le fichier pour configurer dhcp donc créer étendue… (dhcp 6\)  
-  systemctl restart isc-dhcp-server.service : redémarrer le service pour enregistrer conf (dhcp 7\)  
- uname \-a : pour vérifier la version du système d’exploitation  
- sudo smbpasswd \-a nom\_utilisateur : ajout de l’utilisateur à samba (se fait après avoir ajouter utilisateur linux avec adduser) (samba 10)puis entrer mdp utilisateur samba  
- /var/log/samba/ : fichiers des journaux samba (samba 11\)  
- apt install heartbeat \-y : installer heartbeat (heartbeat 1\)  
- apt install apache2 \-y : pour tester réellement la tolérance aux pannes d’un site web (heartbeat 2\)  
- touch /etc/heartbeat/ha.cf /etc/heartbeat/haresources /etc/heartbeat/authkeys : si les fichiers heartbeat n’existent pas (heartbeat 3\) si ils existent prochaine étape  
- chmod 600 /etc/heartbeat/authkeys : protéger l’accès (en lecture écriture) au propriétaire du fichier authkeys (heartbeat 4\)  
- nano /etc/heartbeat/haresources : configurer le fichier haresources (heartbeat 5\) avec heartbeat1 IPaddr::192.168.86.200/24/enp0s3:0   
- nano /ha.cf : pour éditer le fichier ha.cf avec   
  logfile /var/log/heartbeat.log   
  logfacility daemon   
  node hb1 hb2   
  keepalive 1   
  deadtime 10   
  ucast ens160 192.168.0.29   
  auto\_failback yes

pour (heartbeat 6\)

- nano authkeys : éditer le fichier authkeys pour y mettre   
   auth 1   
  1 sha1 password

pour (heartbeat 7\)

- chmod 600 authkeys : modifier les droits (lecture et écriture pour le propriétaire) de fichier authkeys de heartbeat (heartbeat 8\)  
- nano haresources : éditer le fichier haresources pour heartbeat avec  
  hb1 IPaddr::192.168.0.200/24/ens160:0

où hb1 est le nom de notre serveur et vip pour (heartbeat 9\) je fais pareil pour les autres serveurs en mettant les même infos pour avoir la redondance.

- systemctl restart heartbeat.service : redémarrer le service pour prendre en compte changements (heartbeat 10\)  
- systemctl status heartbeat.service : regarder le statut heartbeat (heartbeat 11\)  
- ifdown nomdelacarte : désactiver carte réseau (enp0s3 par exemple)  
- ifup namdelacarte : activer la carte réseau  
- crm\_verify \-L /etc/ha.d/ha.cf : vérifier la configuration du fichier de configuration heartbeat ha.cf (heartbeat 12\)  
- crm\_mon : vérifier l’état du cluster heartbeat (heartbeat 13\)  
- crm\_resource \-V : afficher l’état de ressources (heartbeat 14\)  
- ssh-add : permet d'ajouter des identités de cryptographie et d'algorithme de signature numérique (RSA et DSA) à l'agent d'authentification. Fourni par le package openssh-clients  
- ssh-agent : permet de stocker les clés privées utilisées pour l'authentification par clé publique. Il démarre automatiquement au début d'une session. Fourni par le package openssh-clients.  
- ssh-copyid est un script qui utilise SSH pour se connecter à une machine distante et installe votre propre clé publique dans la liste des clés autorisées d'une machine distante. Cette action permet de se connecter ultérieurement avec une authentification par clé. Fourni par le package openssh-clients.  
- ssh-keygen permet de générer, gérer et convertir des clés d'authentification. Fourni par le package openssh-server.  
- ssh-keyscan permet de collecter les clés d'hôtes ssh publiques d'un certain nombre d'hôtes. Fourni par le package openssh-clients.  
- sudo apt install openssh-server : installer open ssh sur le serveur auquel on veut accéder à distance (ssh 1\)  
- /etc/ssh : répertoire avec fichiers de config ssh toujours sur serveur (ssh 2\)  
- sudo nano ssh\_config : configurer le fichier ssh\_config c’est là qu’on peut modifier le port par défaut ou les adresses autorisées ListenAddress (ssh 3 toujours sur serveur)   
- /etc/passwd : définit des informations relatives aux comptes d’utilisateurs  
- /etc/shadow définit certaines informations relatives au mot de passe des utilisateurs  
- sudo service sshd status : vérifier que le serveur ssh est démarré toujours sur serveur (ssh 4\)  
- sudo service sshd restart : redémarrer le service ssh si on fait changement (ssh 5\) peut être fait avec systemctl   
- ssh utilisateur@adresse\_du\_serveur : depuis le client pour accéder à distance au serveur où on a installé ssh, ip machine est l’ip du serveur ssh ça peut aussi être son nom de domaine. exit pour cloturer la session ssh (ssh 6\)  
- \~/.ssh/config : créer un alias dans ce fichier pour simplifier la commande de connexion par exemple en ssh monserveur (ssh 7\)  
- \~/ .ssh/authorized\_keys : fichier sur lequel on ajoute la clé publique sur le serveur distant (ssh 8\)  
- ssh-keygen : pour générer la clé (ssh 9\)  
- ssh-copy-id utilisateur@adresse\_du\_serveur : transférer la clé à un serveur linux via SSH (ssh 10\)  
- scp fichier utilisateur@adresse\_du\_serveur:\~ : transférer un fichier au travers du protocole ssh depuis la machine locale vers le serveur (ssh 11\) :\~ signifie qu’on souhaite le copier dans le répertoire courant (on peut choisir n’importe quel répertoire du serveur accessible par l’utilisateur) en graphique via filezilla pour sftp nouveau site a créer (ssh 12\)  
- chercher et installer les dépôts repositories depuis les sites officiels  
- ip link show : voire les interfaces  
- sudo systemctl restart networking : pour redémarrer les services réseau (après fixation ip dans /etc/network/interfaces par exemple)  
- 