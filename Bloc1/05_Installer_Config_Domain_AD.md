# Installer et configurer un domaine ActiveDirectory

<details>
<summary>
COURS COMPLETS
</summary>

<details>
<summary>

**L’installation de l’Active Directory:**
</summary>

Dans la compétence précédente, nous avons pu voir que **Active Directory** (AD) est un ensemble structuré de données, mais également une unité de services qui rassemble les utilisateurs aux ressources du réseau afin qu'ils puissent accomplir leur fonction.

La base de données, aussi appelée répertoire, détient toutes les informations indispensables sur notre cadre informatique.

Dans cette compétence, nous allons voir pas à pas comment installer **Server Active Directory** et découvrir les outils disponibles pour l'administrer.

(vidéo) Découvrez l’installation de l’Active Directory  
Pour commencer dans le gestionnaire de serveurs nous allons cliquer sur “gérer” ensuite sur ajouter des rôles et fonctionnalités” sur la page qui s’affiche on clique sur “suivant” concernant la sélection du type d’installation, nous laisserons par défaut l’installation basée sur un rôle ou une fonctionnalité et cliquer sur “suivant” pour la sélection du serveur on laissera égalemnt par défaut et nous allons directement aller sur “suivant” pour le rôle des serveurs nous allons cliquer sur “service AD DS puis sur “ajouter des fonctionnalités” et “suivant”. Pour la sélection des fonctionnalités on ne touchera pas on ira directement cliquer sur “suivant” Puis “suivant” jusqu’à confirmer les sélections d’installation en cliquant sur “installer” et par la suite l’ordinateur va redémarrer en cliquant sur fermer. Dans le gestionnaire de serveur sur la gauche nous pouvons voir que l’active directory a bien été installé.  
**Installation pas à pas de l'Active Directory:**

### ***Méthode***

###     **Découvrez l'installation de l'Active Directory**

**Étape 1** : allez dans « ***Gestionnaire de serveur*** » \> « ***Tableau de bord*** ».

![](images/05_Installer_Config_Domain_AD__image1.png)

Ici se trouve l'assistant d'ajout de rôles et de fonctionnalités. Il faut lire les informations avant de commencer l'installation. Puis, cliquez sur « ***Suivant*** ».

### ***Exemple***

###     **Assistant d'installation**

**![](images/05_Installer_Config_Domain_AD__image2.png)**

### ***Méthode***

**Étape 2** : choisissez le type d'installation, puis cliquez sur « ***Suivant*** ».

![][image3]

**Étape 3** : sélectionnez le serveur sur lequel seront installés les rôles et les fonctionnalités pour **Active Directory**. Cliquez sur « ***Suivant*** » une fois terminé.

![][image4]

**Étape 4** : choisissez les rôles à installer (« ***Service AD DS*** ») et cliquez sur « ***Ajouter des fonctionnalités*** ».

![][image5]

![][image6]

### ***Complément***

Il est impossible d'installer les **Services AD DS** tant que les services de rôles ou les fonctionnalités qui sont listés ne sont pas installés.

### ***Méthode***

Après avoir cliqué sur « ***Ajouter des fonctionnalités*** », on peut observer que le **Service AD DS** est bien coché. Vous pouvez alors continuer en allant sur « ***Suivant*** ».

### ***Exemple***

###    **Sélection des rôles des serveurs**

**![][image7]**

### ***Méthode***

À ce stade de l'installation d'Active Directory, il faut laisser les fonctionnalités cochées par défaut ; il ne faut rien modifier. Continuez sur « ***Suivant*** ».

### ***Exemple***

###     **Sélection des fonctionnalités**

**![][image8]**

### ***Méthode***

Dans les services de domaine Active Directory, toutes les informations à connaître sont stipulées. Pour commencer l'installation, cliquez sur « ***Suivant*** ».

### ***Exemple***

###     **Services AD DS**

**![][image9]**

### ***Méthode***

**Étape 5** : cliquez sur « ***Installer*** » pour confirmer les sélections d'installation, et AD DS sera appliqué.

![][image10]

**Étape 6** : une fois l'installation réussie, cliquez sur « ***Fermer*** » sans interrompre les tâches qui sont en cours d'exécution.

![][image11]

![][image12]

### ***Complément***

Après l'installation, on peut retrouver les services de domaine de l'Active Directory dans le « ***Gestionnaire de serveur*** ».

Si l'on fait le parcours « ***Gestionnaire de serveur*** » \> « ***Tableau de bord*** » \> « ***Outils*** », on peut voir apparaître les différents outils qui vont permettre d'administrer l'AD.

![][image13]
</details>

<details>
<summary>

**La configuration de l’Active Directory:**
</summary>

**L’importance de bien paramétrer l’AD:**

Indivisible de Windows, on a pu voir, dans la compétence précédente, quel rôle joue l'**Active Directory**. Il sert comme on pourrait dire d'annuaire, il fonctionne comme un système qui gère et stocke toutes les informations que peut posséder un réseau.

Afin que l'**AD DS** puisse agir correctement, il faut mettre en place des contrôleurs de domaine.

À quoi sert un **contrôleur de domaine** ?

C'est un type de serveur qui va se servir des données stockées dans l'Active Directory, et qui va permettre d'identifier et d'inspecter les usagers qui vont se connecter au réseau informatique.

Si on compare l'Active Directory à un contrôleur de domaine, on peut alors en déduire que l'AD DS est un domaine, et le contrôleur de domaine exécute celui-ci.

Le contrôleur de domaine participe à la coordination et la protection des données.

Derrière chaque intrusion se cache un déploiement Active Directory (AD) fragile. AD est devenu une cible privilégiée des attaquants qui souhaitent utiliser des vulnérabilités et des erreurs de configuration connues pour élever les privilèges et faciliter les mouvements latéraux.

Malgré tout, en raison des erreurs de configuration qui s'accumulent à mesure que la complexité du domaine augmente, la plupart des entreprises ont du mal à sécuriser Active Directory. Par conséquent, l'équipe de sécurité ne peut pas trouver et corriger les vulnérabilités avant qu'elles ne deviennent des problèmes affectant l'entreprise.

Ainsi, Active Directory vous aide à organiser les utilisateurs, les ordinateurs, etc. de votre entreprise. Votre administrateur utilise AD pour organiser l'ensemble de la hiérarchie de votre entreprise, quels ordinateurs appartiennent à quel réseau, à quoi ressemble votre photo de profil ou quels utilisateurs peuvent accéder à la salle de stockage.

Vous l'aurez compris, Active Directory est le noyau principal de l'infrastructure informatique de chaque entreprise dans le monde, et la première couche pour construire la sécurité, la conformité, l'automatisation pour les utilisateurs et les ordinateurs. Pour créer la bonne infrastructure, il n'est pas nécessaire d'être un assistant, mais il est important de connaître quelques petites astuces pour éviter les problèmes de configuration et de sécurité.

**Configuration de l’Active Directory:**

Après avoir vu l'installation de l'Active Directory, nous allons voir maintenant comment procéder à la configuration d'AD DS et mettre en place un contrôleur de domaine, afin que celui-ci soit fonctionnel en tout temps.

**Étape 1 :** allez dans « ***Gestionnaire de serveur*** » → « ***Tableau de bord*** » → Cliquez sur le drapeau et triangle jaune, comme sur la capture, puis cliquez de nouveau sur « ***Promouvoir ce serveur en contrôleur de domaine*** ».

![][image14]

**Étape 2 :** pour commencer la configuration de déploiement, cliquez sur « ***Ajouter une nouvelle forêt*** » puis nommez votre domaine racine. Dans notre cas, ce sera **STUDI.SRV**.

Poursuivez avec « ***Suivant*** ».

![][image15]

**Étape 3 :** dans les options de contrôleur de domaine, il faut mettre en place un mot de passe, par sécurité, si on a besoin de restaurer notre serveur.

Cliquez ensuite sur « ***Suivant*** ».

![][image16]

Dans la sélection du niveau fonctionnel, on laissera par défaut. Le niveau fonctionnel sert à déterminer les limites des fonctionnalités si une version antérieure de Windows était installée.

**Étape 4 :** ici, dans l'étape « ***Options DNS*** », il est demandé de créer une délégation DNS, mais il ne faudra rien modifier. Continuez la configuration en allant sur « ***Suivant*** ».

![][image17]

**Étape 5 :** Dans l'onglet « ***Options supplémentaires*** », si le nom **NetBIOS** attribué au domaine est correct, il vous suffit de cliquer sur « ***Suivant*** ». Dans le cas contraire, il est tout à fait possible de le modifier.

![][image18]

**Étape 6 :** Dans la continuité de l'**Assistant Configuration des services de domaine Active Directory**, cette étape concerne les chemins d'accès. Il faut spécifier l'emplacement de la base de données de l'Active Directory. Ici, laissez par défaut et poursuivez la configuration.

![][image19]

**Étape 7 :** la partie « ***Examiner les options*** » concerne tout ce qui a été configuré précédemment. Une vérification des sélections est conseillée avant de continuer la configuration. Cliquez sur « ***Suivant*** » une fois terminé.

![][image20]

**Étape 8 :** Dans le passage de « ***Vérification de la configuration requise*** », certaines icônes peuvent faire penser à des anomalies, mais il ne faut pas y prêter attention. Les modifications se feront plus tard. Cliquez sur « ***Installer*** ».

![][image21]

Cliquez sur « ***Installer*** » : le serveur va redémarrer.

**Étape 9 :** après le redémarrage du serveur, entrez les identifiants.

![][image22]

On pourra observer ici et dans la vidéo qu'il apparaît **STUDI\\Administrateur** et non plus **Administration** avant la configuration. Donc, on peut en déduire que le domaine a bien été configuré.

Si l'on se rend dans le « ***Gestionnaire de serveur*** » → « ***Serveur local*** », on verra le nom du domaine qui a été créé.

![][image23]

(vidéo) configuration active directory

Dans gestionnaire de serveur on clique sur le drapeau en haut à droite ensuite sur “promouvoir ce serveur en contrôleur de domaine”. Dans la configuration de déploiement on clique sur “ajouter une nouvelle forêt” puis spécifier un nom de domaine et cliquer sur “suivant”. Dans les options du contrôleur de domaine on va créer un mot de passe pour le mode de restauration en cas de problèmes pour les services d’annuaires et cliquer sur “suivant”. Sur la fenêtre option DNS nous allons tout laisser par défaut et cliquer sur “suivant”, ici dans les options supplémentaires nous allons vérifier le nom du NetBIOS et le modifier si nécessaire et cliquer sur “suivant”. Concernant les chemins d’accès nous allons le laisser par défaut et cliquer sur “suivant”. Dans l’examination des options on va vérifier nos sélections et cliquer sur “suivant”. On va attendre la vérification de la configuration, si les vérifications ont donné satisfaction, on peut cliquer sur “installer”, L’ordinateur va redémarrer, on clique sur “fermer” et encore une fois sur “fermer”, l’ordinateur redémarre. Après le redémarrage de notre serveur, on peut constater que notre domaine a bien été appliqué mais afin de vérifier que l’AD DS a bien été configuré, nous allons rentrer dans le gestionnaire de serveur, pour ce faire on rentre notre mot de passe et cliquer sur “entré”, notre gestionnaire de serveur va s’ouvrir et onv oit à gauche l’AD DS donc la configuration du domaine a bien été appliquée car on voit le nom de domainequ’on a configuré.

**Bonnes pratiques:**

Lorsque vous envisagez de créer une infrastructure Active Directory, il est bon de connaître quelques conseils pour éviter les problèmes de sécurité et de configuration :

* **Renommer l'administrateur de domaine.** Le premier utilisateur utilisé pour lancer une attaque est l'administrateur ; votre première étape consiste donc à changer le nom d'administrateur de domaine par défaut. Utilisez un nom complètement différent des normes, comme AdminContosoAD.  
* **Mot de passe fort pour l'administrateur de domaine.** Sécurité, sûreté, sécurité \! L'administrateur du domaine doit avoir un mot de passe fort et les informations d'identification doivent être réservées.  
* **Informations d'identification dédiées pour l'informatique.** L'une des premières règles consiste à séparer les informations d'identification par défaut de la direction pour empêcher une escalade de la sécurité en cas d'attaque externe.  
* **Attribuer la bonne autorisation.** Si vous avez plusieurs administrateurs dans votre infrastructure, il est fondamental d'attribuer la bonne autorisation et les bonnes informations d'identification pour chaque utilisateur. Personne ne doit être au-dessus des administrateurs de domaine pour éviter la possibilité de changer le schéma AD ou de modifier le modèle de forêt.  
* **Configurer GPO.** Configurer les stratégies de groupe par utilisateurs et ordinateurs, cela permet une granularité parfaite. N'oubliez pas d'éviter trop d'objets de stratégie de groupe, mais également de regrouper de nombreux paramètres dans un seul objet de stratégie de groupe. N'utilisez pas l'objet « stratégie de groupe » en tant que stratégie de domaine par défaut \!  
* **Mot de passe fort pour les utilisateurs.** L'administrateur de domaine, mais aussi tous les utilisateurs doivent répondre aux exigences de complexité du mot de passe. Si vous utilisez Windows 10, une idée consiste à configurer Windows Hello Entreprise pour simplifier la méthode d'authentification, sans réduire la sécurité.  
* **Activer la corbeille.** La corbeille a été introduite dans Windows Server 2008 R2 et constitue le moyen idéal pour restaurer un élément en quelques secondes, sans avoir à exécuter AD Restore.  
* **Au moins deux contrôleurs de domaine.** Peu importe si votre infrastructure n'est pas une entreprise, vous devez avoir deux contrôleurs de domaine pour éviter les pannes critiques.  
* **Supprimer les éléments obsolètes.** N'oubliez pas de nettoyer votre infrastructure d'utilisateurs et d'ordinateurs là où ils ne sont plus présents ou nécessaires. Ceci afin d'éviter des problèmes ou des problèmes de sécurité.  
* **Un contrôleur de domaine n'est pas un ordinateur.** N'installez rien à l'intérieur d'un contrôleur de domaine \! Pas de logiciel, pas d'applications tierces, pas de rôles, rien \!  
* **Règle de convention de nommage.** Définissez une convention de nommage avant de créer votre infrastructure, utilisateurs, clients, serveurs, appareils et ressources (groupes, partages, etc.). Cela vous aidera à simplifier la gestion et l'évolutivité.  
* **Patcher vos contrôleurs de domaine.** Les attaquants exploitent rapidement les vulnérabilités connues, ce qui signifie que vous devez toujours maintenir votre machine à jour. Planifiez le bon moment pour installer les mises à jour Windows.  
* **Audit.** Déployez une solution d'audit pour savoir qui effectue les modifications. Ce n'est pas une exigence du RGPD, mais un moyen d'éviter les problèmes de sécurité.
</details>

<details>
<summary>

**L’intégration des postes au domaine Active Directory:**
</summary>

**Intégration d’un poste client:**

### ***Contexte***

Nous savons que l'Active Directory est défini comme une base de données intégrant un regroupement de services favorisant la mise en relation entre les utilisateurs et les ressources de réseau, c'est-à-dire un assemblage de matériels connectés entre eux par le biais d'un réseau qui permet aux utilisateurs de réaliser leurs objectifs.

La principale mission de l'Active Directory est d'authentifier et d'identifier un poste sur Windows.

Dans les cours qui ont précédé, nous avons pu voir comment se déroulait la configuration de l'Active Directory, ainsi que la définition d'un DNS et d'un annuaire informatique.

Ces compétences vont nous aider dans ce cours, car il faut savoir que, quand nous sommes sur un poste client, il est nécessaire de faire apparaître toutes les propriétés liées au système.

### ***Méthode***

###    **Découvrir l'intégration d'un poste client au domaine Active Directory**

Dans la compétence précédente, nous avons pu voir la configuration de l'Active Directory. Maintenant, nous allons voir, pas à pas, comment intégrer des postes de travail dans un domaine AD.

* **Étape 1 :**

Dans l'explorateur de Windows, effectuez un clic-droit sur « *Ce PC* », puis cliquez sur « *Propriétés* ».

![][image24]

Il est également possible d'afficher les propriétés du système en passant par le « *Panneau de configuration* », en cliquant ensuite sur « *Système et sécurité* » et « *Système* ».

* **Étape 2 :** cliquez sur « *Protection du système* » ou bien « *Paramètres système avancés* ».

![](images/05_Installer_Config_Domain_AD__image25.png)

* **Étape 3 :** apparaît ensuite une fenêtre, dans laquelle il faut cliquer sur l'onglet « *Nom de l'ordinateur* » et « *Modifier* ».

![][image26]

Cette fenêtre du panneau de configuration va nous permettre de procéder à la modification du nom du poste de travail.

* **Étape 4 :** dans la partie « *Membre d'un* », cliquez sur « *Domaine* », puis saisissez le nom du domaine Microsoft. Ici, ce sera **SRV.STUDI**, et validez en cliquant sur « *OK* ».

![][image27]

Il faut noter que tous les postes d'ordinateurs sont intégrés dans un groupe de travail.

* **Étape 5 :** une nouvelle fenêtre va s'ouvrir, il s'agit de la modification du nom ou du domaine de l'ordinateur. Dans cette étape, rentrez les paramètres du compte qui sont « *SRV\\dam* » et le mot de passe de la session, puis cliquez sur « *OK* » pour valider.

![][image28]

Si les étapes ont été correctement respectées, une nouvelle fenêtre avec un message s'affiche, en indiquant : « ***Bienvenue dans le domaine SRV.STUDI*** » (ou le nom que vous aurez choisi).

![][image29]

| Modification du nom ou du domaine de l'ordinateur |
| :---: |

*   
  **Étape 6 :** pour finaliser l'intégration d'un poste client dans Active Directory, il est nécessaire de procéder au redémarrage de l'ordinateur.

Cliquez sur « *Redémarrer maintenant* » pour poursuivre.

![][image30]

* **Étape 7 :** une fois l'ordinateur redémarré, on peut constater que l'écran indique le domaine de connexion qui a bien été configuré.

![][image31]

### (vidéo) Samba Active Directory

Samba AD est un équivalent open source à microsoft active directory ils ont les mêmes fonctionnalités à part que Samba AD ne dispose pas de frais de license. La première version de Samba a vue le jour en 1992\. Samba se nomme ainsi due au protocole de communication et de partage de fichiers qu’il utilise. Il utilise le protocole SMB (Server Message Block) qui sert à échanger des fichiers sur les réseaux de tous les systèmes d’exploitation qui incluent la gestion centralisée de l’indentification et d’autentification en mode domaine active directory, ainsi que la gestion centralisée des groupes, les droits d’accès aux fichiers et répertoires mais aussi de partager des fichiers selon la version du protocole Microsoft SMB ainsi que le partage d’imprimantes. Samba va ainsi évoluer en 4 versions, la quatrième version est celle qui devient un active directory en 2005 avec les spécifications de Microsoft. En 2012 Samba 4 a totalement été réécris avec 3 composants majeurs. Le premier composant est l’atcive directory, le deuxième le partage de fichiers SMBD (SaMBa Daeman) et le troisième le mapping utilisateur winbindd. La version de Samba 4 a évoluée et est devenue un logiciel à part entière avec la fonctionnalité de contrôleur de domaine Active Directory. Il inclut dans ses fonctionnalités les services DNS, LDAP, Kerberos, RPC et Samba 3 avec la gestion des GPO(group policy object). L’évolution et les mises à jour de Samba AD permettent de nouvelles fonctionnalités. Parmis ces nouvelles fonctionnalités, les plus pertinantes sont la possibilité d’exporter les GPO à partir d’un domaine dans un fichier XML pour obtenir des backups des GPO.Ensuite, il permet grâce à une nouvelle commande de pouvoir sauvegarder en mode hors ligne en toute sécurité. Samba AD supporte python 2 et python 3\. Il permet également de voir le numéro d’identification d’évènements de Windows ainsi que le nom d’utilisateur.   
Pour résumer, la version de Samba qui a pu fusionner avec Active Directory est Samba 4\. Il utilise le protocole SMB d’où son nom pour permettre le partage de fichiers et d’imprimantes par le réseau. L’évolution de Samba AD lui a permis de pouvoir monter en popularité avec le système d’exploitation (OS) de Linux. Il a inclut dans ses fonctionnalités plusieurs serviuces tels que les srvices DNS et la gestion des GPO.  
**Bonnes pratiques de configuration des machines virtuelles sous AD:**

Il y a quelques règles à retenir lors de la création d'un contrôleur de domaine dans une machine virtuelle :

* **Prise en charge des contrôleurs de domaine virtualisés.** À partir de Windows Server 2012, lorsqu'une nouvelle fonctionnalité appelée VM Generation-ID est ajoutée, l'installation de contrôleurs de domaine en tant que machines virtuelles est prise en charge.  
* **Doit-on utiliser un DC physique ?** Cela dépend de l'infrastructure, mais, pour la plupart des entreprises, la réponse est non. Il est important de configurer l'opération de démarrage pour qu'elle démarre toujours dans les 0 secondes.  
* **Ne virtualisez pas les points de contrôle** : les points de contrôle DC sont désormais pris en charge, mais il est préférable d'éviter cela.  
* **Désactiver la synchronisation de l'heure** : les contrôleurs de domaine veulent qu'ils soient au sommet de la hiérarchie de l'heure locale et quittent le service de synchronisation de l'heure de l'hôte. Cela entraînera le remplacement forcé de toute autre source définie par le service de temps Windows, ce qui peut causer des problèmes.  
* **Ne mettez pas le contrôleur de domaine dans un état enregistré.** Lorsqu'une machine virtuelle est restaurée à partir d'un état enregistré ou est restaurée vers un point de contrôle, la seule garantie que son horloge est réglée est de synchroniser l'heure du service. Cependant, comme vous le savez d'après ce qui précède, vous ne pouvez pas activer cette fonctionnalité sur un contrôleur de domaine virtualisé. Si son horloge est trop obsolète, il se peut qu'il ne se répare jamais automatiquement.  
* **Ne convertissez pas les contrôleurs de domaine**, que vous soyez un contrôleur de domaine physique ou un contrôleur de domaine virtuel, la conversion est erronée et n'est pas prise en charge. Si vous souhaitez migrer de VMware vers Hyper-V, vous devez réinstaller le contrôleur de domaine à partir de zéro ; si vous avez un DC physique, il en va de même.  
* **Conversion de type mise à niveau sur place** : la mise à niveau sur place n'est pas prise en charge. Par conséquent, si vous installez une nouvelle version de Windows Server, prévoyez de déployer de nouveaux ordinateurs, ajoutez-les à la forêt AD, déplacez les rôles FSMO et rétrogradez le contrôleur de domaine le plus ancien. Il n'y a pas d'autre moyen \!  
* **Les réplicas ne doivent pas être utilisées dans la plupart des cas.** Si vous disposez d'un site distant de reprise après sinistre, il peut être préférable de configurer un autre contrôleur de domaine et d'utiliser un système de réplication AD.  
</details>

<details>
<summary>

  **L’identification des objets de l’annuaire:**
</summary>

  ### ***Contexte***

Qu'est-ce qu'un ADSI Edit ?

ADSI Edit ou Active Directory Services Interfaces Editor est un éditeur d'annuaires de Microsoft qui peut régir la modification ainsi que l'affichage des attributs des objets dans Active Directory.

Il permet aussi de modifier tous les attributs qu'il est impossible d'étudier à partir des autres consoles d'administration d'annuaires, comme les utilisateurs et ordinateurs Active Directory ou bien les sites ou encore les services.

### **Quels sont les objectifs de ADSI Edit et à qui profitent-ils ?**

Les interfaces ADSI forment comme un groupe, une bibliothèque d'interfaces, et sont basées sur le modèle COM (*Component Object Model*, procédé de composants logiciels créé par Microsoft en 1994). Celles-ci servent à parvenir à tous les services d'annuaires qui proviennent de réseaux distincts.

Faisant partie de l'annuaire Active Directory, les propriétés de l'ADSI sont présentées sous forme d'attributs. Ces attributs sont manœuvrés par les applications ou l'annuaire lui-même.

Il n'est pas sans savoir que ADSI est appliqué dans le domaine de l'informatique. Les services ADSI peuvent être utilisés dans le cadre de la gestion des ressources présente dans un service d'annuaire et, ceci, dans n'importe quel réseau qui retient la ressource.

Comme indiqué plus haut dans la partie contexte, l'ADSI peut être manipulée par les administrateurs afin de pouvoir gérer diverses tâches, comme gérer les imprimantes, ajouter, modifier ou supprimer des utilisateurs et / ou groupes.

Les interfaces de services peuvent également servir aux éditeurs de logiciels autonomes qui leur permettront d'activer l'annuaire directement depuis leurs applications.

L'annuaire sert aussi à effectuer des recherches de services pour les clients.

(vidéo) Comment fonctionne Active Directory et quelle est sa structure

Le principal service Active Directory est Active Directory Domain Services (AD DS) qui fait lui-même parti du système d’exploitation Windows Server. Ces serveurs qui exécutent AD DS constituent des contrôlleurs de domaine. En général, les entreprises ont plusieurs contrôlleurs de domaines chacun possédant un exemplaire de l’annuaire pour l’ensemble du domaine. Les variations apportées au répertoire sur l’un des contrôleur de domaine sont copiés sur les autres contrôleurs de domaine afin qu’ils restent tous à jour. Un serveur de répertoire global est un contrôleur de domaine qui enregistre une copie intégrale de tous les objets de son répertoire de domaine  et des copies intermédiaires des objets de tous les autres domaines de la forêt. Par conséquent, les utilisateurs et les applications peuvent trouver des objets dans n’importe quel domaine de leur forêt. Les postes de travail, les appareils portables et les autres périphériques basés sur Windows autre que Windows Server peuvent être intégré à l’environnement Active Directory. Cependant ils n’exécutent pas AD DS. AD DS repose sur divers protocoles et normes définis notamment le protocole LDAP (Lightweight Directory Access Protocol), le protocole Keberos et le DNS (Domain Name System). Il est essentiel de préciser qu’Active Directory n’est accessible que pour les environnements sur site de Microsoft. Les environnements Microsoft dans le cloud emploient Azure Active Directoryqui a la même fonctionnalité que son homologue local. Bien que AD  et Azure AD soient deux outils différents, ils peuvent fonctionner ensemble si votre entreprise possède un environnement informatique à la fois local et dans le cloud. AD fournit 3 niveaux principaux: Domaine, Arbre et Forêt. Un domaine est un groupe dans lequel les différents utilisateurs AD, ordinateurs et objets sont liés. Plusieurs domaines peuvent être combinés pour former un arbre et la combinaison des arbres forme une forêt. N’oubliez pas qu’un domaine représente une étendue administrative. Les objets spécifiques au domaine sont stockés dans une base de donnée et peuvent être gérés de manière centralisée. La forêt est une zone sûre, les objets de différentes forêts ne peuvent pas s’affecter à moins que les administrateurs de chaque forêt établissent une relation de confiance entre eux. 

**Identification des objets de l'annuaire:**

### ***Méthode***

###     **Découvrez l'identification des objets de l'annuaire**

Dans ce cours, toujours dans le chapitre de l'Active Directory, nous allons voir comment utiliser l'outil ADSI Edit dans le serveur Windows 2019\.

**Étape 1** : Rendez-vous dans « ***Gestionnaire de serveur*** » puis « ***Outils*** ».

Cherchez ensuite « ***Modification ADSI*** » et cliquez dessus.

![][image32]

L'éditeur ADSI :

![][image33]

**Étape 2** : Afin de pouvoir commencer à créer une connexion vers les services, faites un clic droit sur « ***Modification ADSI*** » puis cliquez sur « ***Connexion*** ».

![][image34]

**Étape 3** : Après avoir cliqué sur « ***Connexion*** », une nouvelle fenêtre s'ouvre avec le menu des « ***Paramètres de connexion*** ».

À cette étape, il faut rentrer le nom de domaine et laisser par défaut ce qui est déjà coché. Cliquer ensuite sur « ***OK*** » pour continuer la manipulation.

![][image35]

On peut constater ensuite que la connexion a bien été créée et établie.

Connexion établie :

![][image36]

**Étape 4** : Cliquez sur « ***SRV.STUDI*** », dans la partition présente dans le volet situé à gauche. Vous accédez à un déroulé, dont l'éditeur ADSI affiche tous les groupes et comptes d'utilisateurs. Ici, il est possible de modifier, supprimer, renommer ou encore déplacer tous les dossiers des postes de travail, des groupes et comptes utilisateurs.

![][image37]

Dans « ***CN=Users*** » apparaissent toutes les sessions que nous avons créées précédemment dans notre Active Directory.

Sessions créées dans Active Directory :

![][image38]

**Étape 5** : Si on fait un clic droit sur une session, comme « ***CN=DAM*** » par exemple, il est possible de procéder à une nouvelle connexion, de réinitialiser le mot de passe ou encore d'actualiser.

Mais ici, on va continuer en allant dans « ***Propriétés*** ».

![][image39]

Dans cet onglet apparaissent tous les détails de l'éditeur d'attributs.

Quelques soient les propriétés, elles sont modifiables.

Éditeurs d'attributs :

![][image40]

### ***Complément***

Pour retrouver un attribut qui n'est pas dans la liste, il suffit de cliquer sur « ***Filtrer*** » et ensuite de décocher l'option « ***Afficher uniquement les attributs qui ont des valeurs*** ».

### ***Méthode***

Dans cette étape, on va procéder à une modification pour observer comment fonctionne l'ADSI Edit.

Dans le cas de la démonstration du cours, vous allez modifier le nom de la session encadrée en rouge : « ***displayName DAM*** »

### ***Exemple***

###     **Modification de la session displayName DAM**

**![][image41]**

### ***Méthode***

**Étape 6** : Cliquez sur « ***Modifier*** », entrez de nouveau le nom, cliquez sur « ***OK*** » et enfin sur « ***Appliquer*** ».

![][image42]

**Étape 7** : Maintenant, on va vérifier si la modification du nom a bien été prise en compte.

Allez dans « ***Centre d'administration Active Directory*** », cherchez ensuite l'utilisateur qui vient d'être modifié, faites un clic droit et allez sur « ***Propriétés*** ».

![][image43]

Cette fenêtre affiche tous les détails de la session.

Vous pouvez constater que le **Nom complet** a été bien modifié.

Modification du nom prise en compte :

![][image44]
</details>

<details>
<summary>

**La création et l’organisation des unités organisationnelles, utilisateurs et groupes:**
</summary>

**Unité d’organisation dans l’Active Directory:**

### ***Contexte***

Après avoir vu dans les compétences précédentes « *L'intégration des postes au domaine Active Directory* » et « *L'identification des objets de l'annuaire* », nous allons poursuivre avec la création et l'organisation des unités organisationnelles, utilisateurs et groupes.

Nous allons voir, pas à pas, comment créer l'organisation des unités organisationnelles des utilisateurs et groupes.

### ***Méthode***

###     **Découvrez l'unité d'organisation dans l'Active Directory**

Nous allons voir, dans un premier temps, la définition de l'unité d'organisation, puis, dans les autres parties, nous verrons comment créer l'organisation des unités organisationnelles des utilisateurs et groupes.

### **Qu'est-ce que l'unité d'organisation ?**

L'**Unité d'Organisation** ou bien **Organizational Unit (OU)** en anglais, est considérée comme un groupe dans l'Active Directory. Cet espace d'exécution va amplifier l'organisation de chaque objet présent dans l'Active Directory. Le rôle d'une unité d'organisation va permettre de décharger les tâches administratives ainsi que les droits sur les objets.

Par le biais de cette unité, un administrateur pourra ajuster des paramètres à une section d'utilisateurs bien définie ou bien affecter des autorisations de compte.

### ***Attention***

Une unité d'organisation peut rassembler une ou plusieurs sous unités d'organisation, mais chacun des attributs de l'unité d'organisation peut caractériser une entité unique.

**Création d’une unité d’organisation:**

### **Découvrez la création d'une unité d'organisation**

**Étape 1 :** Tout d'abord, allez dans le menu « ***Gestionnaire de serveur*** », cliquez sur « ***Outils*** ». Ouvrez l'onglet « ***Utilisateurs et ordinateurs Active Directory*** ».

![][image45]

**Étape 2 :** Ici, on va créer une unité organisationnelle.

Dans « ***Utilisateurs et ordinateurs Active Directory*** », accédez au nom du serveur, faites un clic droit, allez ensuite dans « ***Nouveau*** » et enfin cliquez sur « ***Unité d'organisation*** ».

![][image46]

**Étape 3 :** Dans la fenêtre qui s'affiche, choisissez et entrez un **Nom** de votre unité d'organisation. Une fois terminé, cliquez sur « ***OK*** » pour poursuivre.

![][image47]

### ***Complément***

Il est déconseillé de décocher « ***Protéger le conteneur contre une suppression accidentelle*** », car, si on supprime un fichier ou un dossier, il sera impossible de le récupérer.

**Création d’un utilisateur dans l’unité organisationnelle (UO):**

### **Découvrez la création d'un utilisateur dans l'unité d'organisation**

**Étape 4 :** Maintenant, vous pouvez créer un utilisateur.

Allez dans « ***Nouveau*** » puis cliquez sur « ***Utilisateur*** ».

![][image48]

### ***Complément***

À cette étape, il est déjà possible de déplacer une session créée auparavant.

### ***Méthode***

**Étape 5 :** À ce stade de manœuvre, on passe à la création d'un utilisateur.

Entrez les données demandées et poursuivez en cliquant sur « ***Suivant*** ».

![][image49]

### ***Complément***

Pour chaque ajout d'utilisateur, il faudra répéter la même procédure.

Si on observe bien, on peut constater que l'utilisateur « ***dami*** » pourra ouvrir une session de deux manières. Soit avec l'adresse email ou bien par le biais de l'authentification de Windows (antérieur à Windows 2000).

### ***Méthode***

**Étape 6 :** Après avoir cliqué sur « ***Suivant*** », saisissez le mot de passe de cet utilisateur, puis continuez.

![][image50]

### ***Complément***

Il est possible de choisir une option parmi les quatre proposées, concernant le mot de passe. Dans le cas de la démonstration, on ne cochera rien.

### ***Méthode***

Après avoir mis en place un mot de passe, un résumé des informations entrées précédemment pour la création de l'utilisateur s'affiche.

Cliquez sur « ***Terminer*** » et l'utilisateur sera créé.

Création de l'utilisateur terminée.

![][image51]

**Création d’un groupe dans l’unité organisationnelle:**

### 

Maintenant que l'utilisateur a été créé, nous passons à la création d'un groupe.

**Étape 7 :** Pour créer un groupe, faites un clic-droit, allez dans « ***Nouveau*** » et continuez sur « ***Groupe*** ».

![][image52]

**Étape 8 :** Entrez le nom du groupe que vous souhaitez mettre en place.

Laissez les options par défaut dans « ***Étendue du groupe*** », puis cliquez sur « ***OK*** ».

![][image53]

### ***Conseil***

Il est conseillé de laisser coché « ***Globale*** » car cette option va permettre au membre du groupe de pouvoir ajouter d'autres groupes ou d'autres comptes qui viennent seulement du domaine dans lequel le groupe aura été déterminé.

### ***Méthode***

###     **Création du groupe terminée**

**![][image54]**

Dans le groupe informatique qui a été formé, il sera possible d'y ajouter plusieurs utilisateurs. Il est également possible de déplacer les utilisateurs d'un groupe vers un autre, de les supprimer d'un groupe.

(vidéo) La création et l’organisation des unités organisationnelle

Dans gestionnaire de serveur aller sur “outil” puis “utilisateurs et ordinateurs Active Directory”. Pour créer une unité d’organisation faire un clic droit sur notre nom de domaine aller sur “nouveau” puis “Unité d’organisation” entrez le nom de l’unité et cliquer sur “ok”. L’UO qui vient d’être créée apparaît dans l’arborescence du nom de domaine. Si vous souhaitez créer des utilisateurs ou groupe dans l’unité d’organisation, aller dans l’unité d’organisation faire un clic droit puis “nouveau” puis “groupe”, entrez le nom de groupe puis cliquer sur “ok”. Le groupe qui vient d’être créé apparaît bien dans l’uo, même schéma pour créer un utilisateur faire un clic droit puis nouveau puis utilisateur, entrez les données de l’utilisateur suivant créez un mot de passe puis suivant puis terminer. Lutilisateur qui vient d’être créé apparaît dans l’uo.
</details>

<details>
<summary>

**Configurer les stratégies de groupe: GPO:**
</summary>

 ***Contexte***

Dans un environnement professionnel, les entreprises doivent gérer efficacement les configurations de leurs systèmes informatiques afin d'assurer la sécurité, la productivité et la conformité aux politiques internes. Pour y parvenir, les administrateurs systèmes utilisent les stratégies de groupe (GPO), un outil centralisé permettant de contrôler et automatiser divers paramètres sur les postes clients et serveurs. Ce cours vous prépare à utiliser cet outil en simulant des situations réelles de gestion informatique, afin de vous rendre opérationnel dans des fonctions d'administration réseau ou de support technique.

**Introduction aux Stratégies de groupes GPO:**

**Définition et utilité des GPO:**

### ***Définition***

Une stratégie de groupe (ou GPO \- Group Policy Object) est un ensemble de règles permettant de gérer et de configurer, de manière centralisée, les paramètres d’ordinateurs et d’utilisateurs dans un environnement Windows. Elle agit comme un outil d'administration pour automatiser les tâches répétitives, standardiser les paramètres et sécuriser les postes de travail ainsi que les comptes utilisateurs.

### ***Fondamental***

Les GPO sont essentielles à la gestion centralisée d’un parc informatique. Elles permettent de définir des configurations qui sont appliquées automatiquement aux ressources (ordinateurs ou utilisateurs) d’un réseau Active Directory, réduisant ainsi le besoin d’interventions manuelles. Ces stratégies offrent aux administrateurs une grande souplesse pour contrôler les paramètres critiques de l’infrastructure, garantissant à la fois cohérence et conformité.

Les stratégies de groupe peuvent être utilisées pour diverses finalités, telles que :

* Renforcer la sécurité du réseau (ex. : forcer l'utilisation de mots de passe complexes).  
* Standardiser les configurations sur tous les postes (ex. : définir des configurations réseau ou des restrictions d'accès).  
* Automatiser le déploiement d’applications ou la configuration de nouveaux postes.

### ***Exemple***

Une entreprise souhaitant interdire l'accès au gestionnaire de tâches pour certains utilisateurs. Une stratégie de groupe peut être créée pour désactiver cette fonction, et elle sera automatiquement appliquée à tous les utilisateurs concernés. Ainsi, l’administrateur n’a pas besoin de configurer cette restriction poste par poste.

### ***Conseil***

Il est préférable de centraliser toutes les règles et configurations critiques dans des GPO bien structurées pour éviter des erreurs ou des oublis. De plus, il est recommandé de tester les stratégies sur un groupe restreint avant de les appliquer au reste du réseau.

**Principe de fonctionnement des GPO:**

### ***Définition***

Les stratégies de groupe (GPO) sont appliquées selon différents emplacements et suivent une hiérarchie stricte dans leur mise en œuvre. Cette organisation permet de structurer l’application des configurations sur les utilisateurs et les ordinateurs d’un réseau Windows. La connaissance des types de GPO, de la hiérarchie et de l’ordre de priorité permet une gestion efficace.

Les GPO peuvent être définies à différents niveaux d’application, ce qui influe sur leur portée et leur priorité. Ces niveaux sont conçus pour répondre aux besoins variés des infrastructures informatiques.

* GPO locales : les stratégies locales sont définies sur un ordinateur et s’appliquent uniquement à ce dernier. Elles sont utiles dans des environnements isolés ou pour des configurations spécifiques à un poste. Toutefois, elles ne permettent pas de gestion centralisée, ce qui limite leur utilisation dans les grandes entreprises. Elles sont également prioritaires uniquement en l’absence d’autres GPO provenant d’un domaine.  
* GPO de domaine : les stratégies de domaine sont créées sur un contrôleur de domaine. Elles sont diffusées à l’ensemble des objets (utilisateurs, ordinateurs) du domaine. Cela permet aux administrateurs d’automatiser et de centraliser les configurations sur tous les postes intégrés au domaine Active Directory.  
* GPO liées à une Unité d’Organisation (OU) : les unités d’organisation regroupent des objets logiques tels que des utilisateurs et des ordinateurs. Une GPO liée à une OU s’applique uniquement aux objets de cette OU et de ses sous-OU. Ce mécanisme permet une gestion ciblée et granulaire des configurations.  
* GPO liées à un site : un site représente une zone géographique définie dans Active Directory. Les GPO associées à un site s’appliquent à tous les objets se trouvant dans cette zone, quelle que soit leur appartenance à un domaine particulier. Ce type de GPO est souvent utilisé pour gérer des paramètres spécifiques à des sites distants.  
* Hiérarchie d’application des GPO : site, Domaine, Unité d’Organisation (OU) : l’application des GPO suit une hiérarchie bien définie pour gérer les priorités entre les différents niveaux. Cette hiérarchie permet d’éviter les conflits et de structurer l’application des stratégies.

L’ordre d’application est le suivant :

* GPO locale : appliquée en premier sur l’ordinateur.  
* GPO de site : appliquée ensuite, en fonction de l’emplacement géographique de l’objet dans le réseau.  
* GPO de domaine : appliquée après la stratégie de site. Elle affecte tous les objets du domaine.  
* GPO d’Unités d’Organisation : appliquée en dernier et a la priorité la plus élevée, sauf si des exceptions sont configurées.

### ***Exemple***

Si une stratégie locale autorise l’accès au Panneau de configuration et qu’une stratégie de domaine le bloque, la stratégie de domaine s’appliquera à condition que l’ordinateur soit membre du domaine.

### ***Fondamental***

La hiérarchie d'application garantit qu’une stratégie plus spécifique (comme une GPO liée à une OU) ait priorité sur une stratégie plus générale (comme une GPO de domaine). Cela permet une flexibilité importante dans la gestion des configurations.

Lorsqu’un même paramètre est configuré différemment dans plusieurs GPO, un conflit peut survenir. L’ordre de priorité, basé sur la hiérarchie, résout ce conflit en appliquant la règle provenant du niveau le plus précis. Cependant, certaines options permettent de modifier ce comportement.

* Option « *Enforce* » (Forcer) : une GPO marquée « *Enforce* » prend le dessus sur les stratégies définies à des niveaux inférieurs dans la hiérarchie, même si celles-ci sont plus spécifiques. Cette option est souvent utilisée pour imposer des règles de sécurité critiques.  
* Option « *Block Inheritance* » (Bloquer l’héritage) : une unité d’organisation peut bloquer l’application des GPO héritées des niveaux supérieurs. Cette option permet de personnaliser les configurations pour certains services ou départements sans être affectée par les stratégies générales du domaine. Cependant, une GPO marquée « *Enforce* » reste applicable même en cas de blocage de l’héritage.

### ***Exemple***

Supposons qu’une GPO de domaine impose une politique de mot de passe complexe, tandis qu’une GPO locale permet des mots de passe simples. Étant donné la hiérarchie, la politique de mot de passe complexe s'appliquera automatiquement aux ordinateurs membres du domaine, même si la stratégie locale définit des règles moins strictes.

### ***Conseil***

Pour éviter les conflits, il est recommandé de planifier soigneusement la structure des GPO en tenant compte de la hiérarchie. Testez les stratégies sur un groupe restreint d’ordinateurs avant de les appliquer à l’ensemble du parc informatique. De plus, documentez toutes les stratégies mises en place pour faciliter leur gestion et leur maintenance.

**Outils de gestion des GPO:**

Pour créer, configurer, appliquer et surveiller les stratégies de groupe (GPO), les administrateurs Windows disposent de plusieurs outils spécialisés. Ces outils permettent de gérer efficacement les différentes configurations au sein d'un environnement Active Directory, garantissant ainsi la sécurité et la cohérence des systèmes.

### ***Fondamental***

La Console de Gestion des Stratégies de Groupe (GPMC, en anglais Group Policy Management Console) est l’outil principal pour la gestion centralisée des GPO. Elle offre une interface qui permet de créer, modifier, et lier les stratégies de groupe à différents niveaux hiérarchiques dans Active Directory.

![][image55]

Avec la GPMC, un administrateur peut :

* Créer, modifier ou supprimer des stratégies de groupe (Gérer les stratégies de groupe).  
* Lier les stratégies à des sites, domaines ou unités d’organisation (UO).  
* Configurer des paramètres avancés, comme les filtres de sécurité ou les filtres WMI (Windows Management Instrumentation).  
* Exporter et importer des stratégies pour faciliter leur sauvegarde et réutilisation.  
* Consulter l’ordre d’application des stratégies via la fonctionnalité « *Ordre de traitement* ».  
* Diagnostiquer les conflits entre GPO en utilisant les rapports fournis par l’outil.

En français, la GPMC est disponible sous le nom « *Gestion des stratégies de groupe* ». Cet outil se trouve dans la section "Outils d’administration" du menu Démarrer ou via la commande gpmc.msc.

### ***Exemple***

Supposons qu'un administrateur veuille empêcher les utilisateurs d'un service de modifier leurs paramètres réseau. Avec la GPMC, il peut créer une nouvelle GPO, configurer cette restriction, et la lier à l’Unité d’Organisation (UO) correspondante. Cette stratégie s'appliquera automatiquement aux ordinateurs de cette UO.

### **Utilisation de la console Active Directory Users and Computers (ADUC)**

**![][image56]**

La console Utilisateurs et ordinateurs Active Directory (en anglais Active Directory Users and Computers, ou ADUC) est un autre outil essentiel. Elle permet de gérer les objets du réseau, comme les utilisateurs, les groupes, les ordinateurs et les unités d’organisation.

Bien que cette console ne permette pas directement de modifier les stratégies de groupe, elle est utilisée pour :

* Organiser les objets dans des unités d’organisation pour structurer l’application des GPO.  
* Vérifier les liens entre les UO et les GPO associées.  
* Modifier les permissions sur les objets, ce qui peut influencer l’application des stratégies (par exemple, en modifiant les appartenances à des groupes de sécurité).

La console ADUC est accessible via la commande dsa.msc ou en lançant « *Utilisateurs et ordinateurs Active Directory* » depuis les Outils d'administration.

### ***Fondamental***

La GPMC et la console ADUC travaillent de manière complémentaire :

* La GPMC est utilisée pour la gestion des stratégies de groupe proprement dite.  
* La console ADUC permet d’organiser les objets Active Directory et de vérifier les permissions et structures hiérarchiques.

### ***Fondamental***

###     **Outils complémentaires pour la gestion et le suivi des GPO**

Outil gpupdate (ou « *Actualisation des stratégies de groupe* ») :

En français, cet outil est disponible via la commande gpupdate. Il permet d’actualiser les stratégies de groupe immédiatement, sans attendre le prochain cycle de mise à jour automatique.

Les options principales incluent :

gpupdate /force : force l’actualisation de toutes les stratégies, y compris celles non modifiées.

![][image57]

gpupdate /target:user ou gpupdate /target:computer : actualise uniquement les stratégies utilisateur ou ordinateur.

Outil gpresult (ou « *Résultat des stratégies de groupe* »)

L’outil gpresult fournit un rapport détaillé sur les stratégies appliquées à un utilisateur ou un ordinateur. Cet outil est utile pour diagnostiquer les problèmes liés à l'application des GPO.

Exemples de commandes :

gpresult /r : génère un résumé des stratégies appliquées.

![][image58]

gpresult /h rapport.html : génère un rapport détaillé au format HTML.

Visualiseur d'événements (Event Viewer)

Le Visualiseur d’événements permet de consulter les journaux d’application des stratégies de groupe. Les erreurs ou avertissements liés à l'application des GPO y sont enregistrés, ce qui facilite le dépannage. il se trouve via :

En français : « *Observateur d’événements* » dans les Outils d'administration.

* Commande : eventvwr.msc,  
* Dans les journaux, les événements liés aux stratégies de groupe se trouvent dans « *Applications et services → Microsoft → Windows → Group Policy* ».

### ***Conseil***

Il est recommandé d’utiliser les commandes gpupdate et gpresult après chaque modification importante de stratégie pour vérifier leur application. La consultation régulière des journaux d’événements peut également prévenir les problèmes en identifiant rapidement les erreurs.

### ***Exemple***

Un administrateur modifie une GPO pour renforcer les paramètres de sécurité. Pour vérifier que cette modification est bien appliquée, il utilise la commande gpupdate /force pour forcer l’actualisation des stratégies, suivie de gpresult /r pour obtenir un rapport sur les stratégies effectivement appliquées au poste de test.

**Structure, Application et Gestion des GPO:**

**Types de paramètres des GPO:**

### ***Définition***

Dans un environnement Windows, les paramètres des stratégies de groupe (GPO) se distinguent en deux grandes catégories : les paramètres appliqués aux utilisateurs et ceux appliqués aux ordinateurs. Cette distinction permet d’adapter la configuration en fonction des besoins spécifiques des systèmes et des utilisateurs.

Une stratégie de groupe (GPO) est une règle ou une directive définie par un administrateur pour automatiser et centraliser la gestion des paramètres des systèmes et des utilisateurs au sein d'un réseau.

Paramètres pour les utilisateurs vs. paramètres pour les ordinateurs :

Paramètres utilisateurs : ces paramètres s’appliquent au moment de la connexion de l’utilisateur. Ils permettent, par exemple, de configurer le bureau (fonds d’écran, menu Démarrer), de définir les accès aux dossiers réseau ou de restreindre les applications disponibles.

### ***Exemple***

Modifier le fond d’écran via :

Configuration utilisateur → Modèles d’administration → Bureau → Papier peint du Bureau.

Limiter l'accès à des options système via :

Configuration utilisateur → Modèles d’administration → Menu Démarrer et barre des tâches.

Paramètres ordinateurs : ces paramètres s’appliquent au démarrage de l’ordinateur. Ils permettent de configurer des éléments comme la sécurité, les services Windows ou les paramètres réseau, indépendamment de l’utilisateur connecté.

### ***Exemple***

Paramètres ordinateurs :

Activer le pare-feu Windows via :

Configuration ordinateur → Paramètres Windows → Paramètres de sécurité → Pare-feu Windows avec fonctions avancées de sécurité.

Définir les mises à jour automatiques via :

Configuration ordinateur → Modèles d’administration → Composants Windows → Windows Update.

### ***Rappel***

Les paramètres utilisateurs suivent l’utilisateur quel que soit le poste sur lequel il se connecte, tandis que les paramètres ordinateurs restent fixes pour une machine, quel que soit l’utilisateur.

Voici les principales catégories de paramètres que vous rencontrerez dans les GPO :

Paramètres de sécurité : ils permettent de renforcer la sécurité du système en imposant des règles comme la complexité des mots de passe ou la désactivation des ports USB.

### ***Exemple***

Pour interdire l’utilisation des clés USB, vous pouvez aller dans :

Configuration ordinateur → Paramètres Windows → Paramètres de sécurité → Stratégies locales → Options de sécurité → Accès aux périphériques : refuser l'accès de stockage amovible.

### ***Rappel***

Configuration système : ces paramètres permettent de gérer les services Windows, la configuration réseau et les ressources du système.

### ***Exemple***

Vous pouvez désactiver les mises à jour automatiques en configurant :

Configuration ordinateur → Modèles d’administration → Composants Windows → Windows Update → Configurer les mises à jour automatiques.

### ***Rappel***

Modèles d’administration : ces paramètres permettent de gérer l'interface utilisateur (bureau, menu Démarrer, barre des tâches), ainsi que les fonctionnalités des applications Microsoft (comme Office).

### ***Complément***

Les Modèles d’administration sont des fichiers .ADMX ou .ADML qui définissent les paramètres disponibles. Vous pouvez personnaliser ou importer des modèles supplémentaires si nécessaire.

### ***Attention***

Une mauvaise configuration des paramètres peut entraîner des restrictions trop strictes ou des incompatibilités. Il est conseillé de tester les stratégies sur un groupe d’utilisateurs ou de machines avant de les déployer sur l'ensemble du réseau.

### ***Complément***

Windows permet d’ajouter des filtres pour affiner l’application des GPO :

* Filtrage par groupes de sécurité : limite l’application d’une stratégie à certains groupes d’utilisateurs ou d’ordinateurs.  
* Filtrage WMI (Windows Management Instrumentation) : permet d’appliquer une stratégie en fonction de critères précis, comme la version de Windows ou les ressources matérielles d’un poste.  
* Boucle de rappel (loopback) : utilisé pour forcer l’application de paramètres utilisateurs en fonction de la machine utilisée.

### ***Méthode***

Pour configurer un filtre WMI :

* Ouvrez la Console de gestion des stratégies de groupe (GPMC).  
* Sélectionnez la GPO concernée, puis allez dans l’onglet Portée.  
* Cliquez sur Filtrage WMI, puis ajoutez un filtre en fonction de vos besoins

**Paramètres d’application des GPO:**

L’application des stratégies de groupe (GPO) repose sur des mécanismes de filtrage et un cycle de traitement précis. Ces outils permettent d’adapter l’application des stratégies en fonction des besoins de l’organisation.

Le filtrage permet de définir quels utilisateurs, ordinateurs ou groupes sont concernés par une stratégie donnée.

### ***Définition***

Le filtrage d’une stratégie de groupe est une règle permettant de restreindre ou de cibler l’application d’une GPO pour certains utilisateurs ou ordinateurs uniquement.

### **Filtrage par groupes de sécurité**

Le filtrage par groupes de sécurité permet de limiter l’application d’une stratégie aux utilisateurs ou ordinateurs faisant partie de groupes Active Directory spécifiques.

### ***Méthode***

Pour configurer le filtrage par groupes de sécurité :

* Ouvrez la Console de gestion des stratégies de groupe (GPMC).  
* Sélectionnez la stratégie concernée.  
* Accédez à l’onglet Délégation.  
* Cliquez sur Ajouter et sélectionnez le groupe de sécurité concerné.  
* Accordez les autorisations d’application en cochant la case Appliquer la stratégie de groupe.

### ***Exemple***

Vous pouvez empêcher l'accès au panneau de configuration uniquement pour les utilisateurs du groupe « *Stagiaires* » en configurant un filtre sur cette GPO.

### **Ciblage par boucle de rappel (loopback)**

Le ciblage par boucle de rappel permet d'appliquer des paramètres utilisateurs en fonction de l'ordinateur sur lequel ils se connectent. Cela permet d'appliquer un profil standardisé sur des postes spécifiques, indépendamment des paramètres habituels des utilisateurs.

Deux modes sont disponibles :

* Fusion : les paramètres utilisateurs spécifiques à l’ordinateur complètent ceux déjà définis pour l’utilisateur,  
* Remplacement : les paramètres utilisateurs spécifiques à l’ordinateur remplacent complètement ceux de l’utilisateur.

### ***Méthode***

Pour activer le mode de traitement en boucle de rappel :

* Accédez à la GPO dans GPMC.  
* Naviguez jusqu’à : configuration ordinateur → Modèles d’administration → Système → Stratégie de groupe.  
* Activez Mode de traitement de la boucle de rappel de stratégie de groupe utilisateur et choisissez le mode souhaité.

### ***Exemple***

Vous pouvez utiliser le mode Remplacement pour les ordinateurs d’une salle de réunion afin de limiter l’accès à certains fichiers ou logiciels, quel que soit l’utilisateur connecté.

### **Cycle de traitement des GPO**

Les stratégies de groupe sont appliquées à des moments précis afin d’assurer la cohérence et la sécurité des configurations système.

### ***Rappel***

L’ordre d’application des stratégies est le suivant :

* Local (stratégies définies directement sur le poste)  
* Site (stratégies définies au niveau du site Active Directory)  
* Domaine (stratégies définies pour l’ensemble du domaine)  
* Unité d’organisation (OU) (stratégies définies pour des unités spécifiques)

Les stratégies définies à un niveau inférieur peuvent écraser celles héritées d’un niveau supérieur, en fonction des priorités et des options de gestion d’héritage (ex. : enforcer ou Bloquer l’héritage).

### ***Fondamental***

###     **Déroulement de l’application des GPO**

Les GPO sont appliquées à trois moments clés :

* Au démarrage de l’ordinateur : les paramètres de configuration de l’ordinateur sont appliqués lors du démarrage du système,  
* À la connexion de l’utilisateur : les paramètres utilisateurs sont appliqués au moment où l’utilisateur se connecte,  
* En arrière-plan : les stratégies sont réappliquées automatiquement toutes les 90 minutes par défaut (5 minutes pour les contrôleurs de domaine).

### ***Méthode***

Vous pouvez forcer l’application immédiate des stratégies en exécutant la commande suivante :

* Cliquez sur Démarrer et ouvrez l’Invite de commandes en mode administrateur.  
* Tapez la commande suivante dans le CMD : gpupdate /force.  
* Appuyez sur Entrée.

### ***Fondamental***

###     **Scénarios de rafraîchissement et de mise à jour**

Les stratégies peuvent nécessiter un redémarrage ou une reconnexion pour que certaines modifications soient prises en compte, notamment celles affectant la sécurité ou les services système.

### ***Conseil***

Pour limiter les perturbations, planifiez les modifications importantes en dehors des heures de travail ou pendant les périodes de maintenance.

### ***Méthode***

Pour vérifier les stratégies appliquées sur un poste :

* Ouvrez l’invite de commandes en mode administrateur,  
* Tapez la commande suivante : gpresult /r,  
* Consultez les résultats affichés pour analyser les GPO appliquées.

**Création et gestion des GPO:**

(vidéo) Création d’une GPO

Dans cette vidéo, nous allons voir comment créer une stratégie de groupe GPO dans windows server et la configurer selon les besoins d’une organisation. 

Nous allons commencer par accéder à la console de gestion des stratégies de groupe GPMC. On cherche dans la barre windows démarrer “gestion des stratégies de groupe”. Une fois dans gestion des stratégies de groupe, dans l’arborescence, on va développer notre domaine puis faire un clic droit sur l’unité d’organisation qui nous intéresse. Ici nous avons créé une unité d’organisation “comptabilité” qui possède deux utilisateurs sur laquelle nous allons appliquer notre GPO. Nous allons faire clic droit puis “créer un objet GPO dans ce domaine, et le lier ici…” cet objet de GPO on l’appelle “Restriction du Panneau de configuration” puis faire “ok”. Une fois que nous avons créé notre GPO nous allons pouvoir l’éditer en faisant un clic droit dessus puis “modifier”, nous sommes maintenant dans l’éditeur de gestion de stratégie de groupe. Nous voulons appliquer notre stratégie de groupe à des utilisateurs, nous nous rendons donc dans “utilisateurs”, il s’agit d’un “modèle d’administration” qui concerne le panneau de configuration donc “panneau de configuration” et nous voulons “interdire l’accès au panneau de configuration” donc on double clic dessus puis on va cocher “activé” et faire “appliquer” puis “ok”. Maintenant on peut fermer cette interface puis dans “comptabilité”, on double clic sur la restriction de panneau de configuration pour vérifier sa configuration donc dans l’onglet “paramètres” (on ferme le message indicatif) on se rend compte qu’il y a la stratégie “interdire l’accès au panneau de configuration et à l’application paramètres du PC” qui est activée. 

La gestion des stratégies de groupe (GPO) est un aspect essentiel de l'administration des réseaux Windows. Elle comprend la création de nouvelles stratégies, leur assignation aux bonnes unités d’organisation (OU) et la gestion des priorités et de l’héritage.

### ***Méthode***

Créer une stratégie de groupe permet de définir les paramètres souhaités pour un ensemble d’ordinateurs ou d’utilisateurs.

Pour créer une nouvelle GPO dans la console GPMC :

* Ouvrez la Console de gestion des stratégies de groupe (GPMC).  
* Faites un clic droit sur le domaine ou l’OU où vous souhaitez créer la stratégie.  
* Sélectionnez Créer une stratégie de groupe dans ce domaine et la lier ici.  
* Donnez un nom à la stratégie (ex. : « *Politique Sécurité mot de passe* »).  
* Une fois la stratégie créée, faites un clic droit dessus et sélectionnez Modifier.  
* Configurez les paramètres souhaités dans les sections Configuration ordinateur et/ou Configuration utilisateur.

### ***Exemple***

Vous pouvez créer une GPO qui impose un mot de passe complexe en accédant à :

Configuration ordinateur → Paramètres Windows → Paramètres de sécurité → Stratégies de compte → Stratégie de mots de passe.

Pour appliquer efficacement une stratégie de groupe, elle doit être liée à un niveau précis de l’Active Directory, tel qu’un site, un domaine ou une unité d’organisation (OU).

### ***Méthode***

Pour assigner une GPO à une OU spécifique :

* Dans la console GPMC, sélectionnez l’OU souhaitée.  
* Faites un clic droit sur l’OU et choisissez Lier une stratégie de groupe existante.  
* Sélectionnez la stratégie de groupe que vous souhaitez lier et cliquez sur OK.

### ***Conseil***

Liez les GPO aux OUs de manière organisée afin de limiter les risques de conflits ou d'erreurs de configuration.

### ***Rappel***

Les GPO peuvent être liées à différents niveaux de l’Active Directory : site, domaine ou unité d’organisation (OU). Ces niveaux définissent le périmètre d'application des stratégies.

L'ordre d'application des stratégies suit la hiérarchie Active Directory :

* Local  
* Site  
* Domaine  
* Unité d’organisation (OU)

Les stratégies liées à un niveau inférieur (par exemple, une OU) peuvent remplacer celles héritées des niveaux supérieurs (site ou domaine).

### ***Méthode***

Pour vérifier où une stratégie est liée :

* Dans GPMC, sélectionnez la stratégie concernée.  
* Consultez l’onglet Liaisons pour voir les niveaux auxquels elle est appliquée.

### ***Exemple***

Une GPO liée au site Europe s’applique à toutes les unités d’organisation sous ce site, sauf si une autre stratégie dans une OU remplace les paramètres.

Lorsqu'une stratégie est héritée d’un niveau supérieur (ex. : domaine), elle peut être remplacée par une stratégie définie au niveau inférieur (ex. : OU). La gestion des priorités permet de définir quel paramètre s’applique en cas de conflit.

### ***Définition***

L’option Enforcer (Appliquer de manière forcée) empêche les stratégies définies à un niveau supérieur d’être remplacées par des stratégies d’un niveau inférieur.

L’option Bloquer l’héritage (Block Inheritance) empêche une OU de recevoir les stratégies héritées des niveaux supérieurs.

### ***Méthode***

Pour utiliser l’option Enforcer :

* Sélectionnez la GPO dans GPMC.  
* Faites un clic droit sur la liaison de la stratégie et sélectionnez Appliquer de manière forcée (Enforce).

Pour bloquer l’héritage sur une OU :

* Faites un clic droit sur l’OU concernée,  
* Sélectionnez Bloquer l’héritage.

### ***Attention***

L’utilisation excessive de l’option Enforcer ou du Blocage de l’héritage peut entraîner des conflits de stratégies difficiles à diagnostiquer. Utilisez ces options uniquement lorsque cela est nécessaire.

En cas de stratégies conflictuelles (par exemple, deux GPO imposant des paramètres de mot de passe différents), Windows applique celle qui a la priorité la plus élevée ou celle définie au niveau le plus bas (OU).

### ***Méthode***

Pour gérer la priorité des stratégies liées :

* Accédez à l’OU ou au domaine concerné dans GPMC.  
* Cliquez sur Liaisons de stratégies de groupe.  
* Réorganisez les stratégies en les déplaçant vers le haut ou le bas de la liste.

### ***Conseil***

Donnez des noms explicites aux GPO (par exemple, « *Politique Sécurité \- Mots de passe* ») pour faciliter la gestion et le suivi des priorités.

**Dépannage et vérification des GPO:**

(vidéo)

Application d’une GPO

La GPO que nous avons créé précédemment est maintena t applicable à nos ordinateurs windows. Elle va s’appliquer sur tous les utilisateurs qui sont présents dans l’OU comptabilité dans laquelle nous avons mis la GPO. Pour vérifier les utilisateurs présents dans l’OU comptabilité, on clique sur la gpo puis sur “utilisateurs et ordinateurs active directory” un fois qu’on a cliqué dessus, on rentre dans l’OU “comptabilité” et on voit que nos deux utilisateurs présents sont john doe et carl doe nous allons donc nous rendre sur l’utilisateur john doe. Une fois sur l’utilisateur nous allons pouvoir ouvrir le cmd, dans ce cmd nous allons faire la commande “gpupdate /force”, cette commande permet d’appliquer immédiatemment les stratégies sans attendre le cycle automatique qui se fait toutes les 90min. Les stratégies ont bien été mise à jour. Nous pouvons vérifier leur résultat en tapant la commande “gpresult /r” et ici nous aurons toutes les informations qui auront été appliquées. On voit sous la parite “Objets Stratégie de groupe appliquées” la stratégie “Restriction du Panneau de configuration”. On peut fermer le cmd et vérifier si on a toujours accès au panneau de configuration en cliquant dessus on a un message “cette opération a été annulé en raison de restrictions sur cet ordinateur. Contactez votre administrateur système” voilà, à partir de maintenant les utilisateurs de l’OU “comptabilité” ne pourront plus accèder au panneau de configuration.

Pour garantir le bon fonctionnement des stratégies de groupe (GPO), il est indispensable de savoir les actualiser, les diagnostiquer et résoudre les problèmes courants liés à leur application. Les outils gpupdate et gpresult sont utilisés directement sur les ordinateurs clients Windows, et non sur le serveur Active Directory.

L’outil gpupdate permet d’actualiser manuellement les stratégies de groupe sur un ordinateur client Windows. Cette actualisation ne se fait pas depuis le serveur Active Directory, mais directement sur les machines où les stratégies doivent être appliquées.

### ***Définition***

La commande gpupdate force l'application des stratégies de groupe définies sur le poste client Windows, sans attendre le cycle automatique d’actualisation (90 minutes par défaut).

### ***Méthode***

Pour actualiser les stratégies de groupe sur un poste client Windows :

* Connectez-vous à l’ordinateur client.  
* Cliquez sur Démarrer, tapez Invite de commandes et ouvrez-la en mode administrateur.  
* Saisissez la commande suivante : gpupdate /force  
* Appuyez sur Entrée.

Une fois l’actualisation terminée, un message de confirmation apparaît.

### ***Conseil***

Utilisez l’option /force pour réappliquer tous les paramètres, même ceux qui n’ont pas été modifiés. Cela peut être utile après des changements importants ou lors de tests.

### ***Exemple***

Si vous venez de modifier une stratégie pour bloquer l’accès au panneau de configuration, utilisez la commande gpupdate /force sur un poste client pour vérifier l’application immédiate de cette stratégie.

L’outil gpresult permet d’obtenir un rapport détaillé des stratégies appliquées sur un ordinateur client. Ce rapport indique les GPO actives, les paramètres appliqués et les éventuels conflits.

### ***Définition***

La commande gpresult affiche les stratégies de groupe appliquées sur un poste client Windows, tant pour l’ordinateur que pour l’utilisateur connecté. Cela permet de vérifier les paramètres actifs et de diagnostiquer les problèmes.

### ***Méthode***

Pour consulter les stratégies appliquées sur un poste client Windows :

* Connectez-vous à l’ordinateur client,  
* Ouvrez l’Invite de commandes en mode administrateur,  
* Saisissez la commande suivante : gpresult /r,  
* Appuyez sur Entrée.

**Analysez les résultats affichés, qui indiquent :**

* Les GPO appliquées à l’ordinateur et à l’utilisateur  
* Les paramètres hérités ou bloqués  
* Les erreurs éventuelles

### ***Exemple***

Si un utilisateur ne voit pas les restrictions prévues par une stratégie (par exemple, l’interdiction d’installer des logiciels), vous pouvez exécuter gpresult /r sur le poste client pour vérifier si la stratégie est bien appliquée.

### ***Méthode***

Pour une meilleure lisibilité, il est possible de générer un rapport détaillé en format HTML.

Pour générer un rapport HTML :

* Sur le poste client, ouvrez l’Invite de commandes en mode administrateur.  
* Tapez la commande suivante : gpresult /h C:\\rapport\_GPO.html.  
* Ouvrez le fichier rapport\_GPO.html avec un navigateur web pour visualiser le rapport complet.

Les rapports générés par gpupdate et gpresult permettent d’identifier rapidement les causes de problèmes courants liés aux stratégies de groupe.

Les problèmes les plus fréquents incluent les GPO non appliquées, souvent causées par un mauvais filtrage, comme un groupe de sécurité mal configuré ou un héritage bloqué. Un autre problème courant est le conflit entre stratégies, où deux GPO définissent des paramètres contradictoires. Dans ce cas, c’est la stratégie ayant la priorité la plus élevée ou celle définie au niveau le plus bas (par exemple, une unité d’organisation) qui s’applique.

### ***Méthode***

Pour résoudre un problème de stratégie non appliquée :

* Vérifiez la liaison de la stratégie dans GPMC au niveau du site, domaine ou unité d'organisation.  
* Assurez-vous que les filtres (groupes de sécurité, héritage) permettent l’application de la stratégie.  
* Exécutez gpresult /r sur le poste client pour vérifier si la GPO est listée parmi celles appliquées.  
* Si nécessaire, modifiez les priorités ou utilisez les options Enforce ou Bloquer l’héritage.

### ***Attention***

Certains paramètres, comme ceux relatifs aux services système ou à la sécurité, nécessitent un redémarrage de l’ordinateur client pour être pris en compte.

### ***Exemple***

Un utilisateur voit toujours le panneau de configuration, bien qu’une stratégie interdit son accès. En consultant le rapport de gpresult, vous découvrez qu'une autre GPO appliquée sur une unité d'organisation supérieure a la priorité et remplace la restriction.

**Essentiel:**

Les stratégies de groupe (GPO) sont un outil incontournable pour les administrateurs systèmes, permettant de gérer de manière centralisée les configurations des utilisateurs et des ordinateurs dans un environnement Windows. Elles sont utilisées pour automatiser l'application de paramètres essentiels, tels que les politiques de sécurité, les restrictions d’accès, la configuration réseau ou encore les paramètres des applications.

L’application des GPO suit une hiérarchie stricte : les stratégies locales sont appliquées en premier, suivies de celles liées au site Active Directory, au domaine et enfin aux unités d’organisation (OU). Les administrateurs peuvent également ajuster les priorités et les exceptions grâce aux options comme Enforce ou Bloquer l’héritage, afin de résoudre les éventuels conflits entre stratégies.

La gestion efficace des GPO permet non seulement de sécuriser les infrastructures informatiques, mais aussi de faciliter la maintenance et la standardisation des postes de travail. De plus, les outils d’administration comme la Console de gestion des stratégies de groupe (GPMC), ainsi que les commandes gpupdate et gpresult, offrent des moyens pratiques pour créer, actualiser et diagnostiquer les stratégies appliquées.

La maîtrise des GPO est donc essentielle pour tout professionnel travaillant dans la gestion de réseaux ou le support technique, car elle garantit une administration fiable, sécurisée et évolutive des systèmes.
</details>

<details>
<summary>

**Sauvegarder et restaurer un annuaire ActiveDirectory:**
</summary>

### ***Contexte***

L'un des outils les plus importants et les plus utiles dont nous disposons en tant qu'administrateurs dans un environnement serveur est sans conteste l'Active Directory, car à partir de là, nous avons un contrôle total sur les différents éléments de l'architecture de l'organisation, qu'il s'agisse d'utilisateurs, d'ordinateurs, d'imprimantes, etc.

Bien que les services Active Directory soient conçus avec une redondance élevée (si vous avez déployé plusieurs contrôleurs de domaine dans votre entreprise), un administrateur AD doit développer et mettre en œuvre une politique de sauvegarde Active Directory claire.

Parmi les avantages de créer une copie de sauvegarde de l'Active Directory, en voici quelques-uns :

* Diminuer les difficultés avec l'un des objets de l'infrastructure organisationnelle,  
* Éviter les tâches administratives supplémentaires,  
* Détenir chaque information à jour,  
* Prévenir les erreurs dans la gestion des serveurs.

Dans cette première partie du cours, nous aborderons la sauvegarde d'un annuaire Active Directory exécuté sur Windows Server 2019\.

(vidéo) Un annuaire Active Directory

Active Directory est un service d’annuaire qui stocke des informations sur les objets d’un réseau. Il fournit une authentification, une autorisation et une identification centralisée. AD est le service d’annuaire le plus utilisé dans le monde. L’AD a été introduit en 1998 avec la version 4.0 de Windows NT 4.0 server. L’objectif principal de ce service d’annuaire est de stocker et d’organiser les données relatives aux objets sur les serveurs et les postes de travail du réseau à travers une organisation. 

L’objet peut être n’importe quoi d’un compte d’utilisateur au compte d’ordinateur jusqu’à une imprimante ou un partage de fichiers. Les objets sont organisés en conteneurs appelés Unité d’Organisation (OU). C’est ainsi que Microsoft organise les données dans les services d’annuaire.On parle alors de schéma hiérarchique. Un annuaire Active Directory est implémenté sous la forme d’une base de données hiérarchiques stockées sur un ou plusieurs serveurs physiques. Le sommet de cette hiérarchie est le domaine racine de la forêt qui contient tous les autres domaines de la forêt. Le domaine racine de la forêt contient deux domaines enfants spéciaux: Le domaine “Maître de Schéma” qui héberge le rôle de “maître de schéma” et le rôle de “maître de nommage de domaines. 

Il y a aussi le rôle de “maître des opérations à l’échelle de la forêt” qui héberge les rôles de “maître des opérations pour la réplication interdomaines” et les changements de mots de passes. 

Le terme “domaine” fait référence à une frontière administrative dans une forêt Active Directory. Chaque domaine possède ses propres stratégies de sécurité, ces données de configuration et ses comptes d’utilisateurs, mais contrairement aux objets de stratégies de groupe GPO locaux, les GPO de domaines s’appliquent à tous les ordinateurs et utilisateurs de ce domaine. 

L’AD stocke des informations sur tous les objets de votre réseau, notamment les utilisateurs, les groupes et les ordinateurs. Il gèrent aussi la sécurité de ces objets et fournit divers autres services de gestion de ces objets tel que la réplication entre différents sites de votre organisation. 

Les annuaires actifs sont ceux utilisés par les entreprises pour assurer le suivi des personnes travaillant sur leur système ainsi que des appareils qu’elles utilisent. Un annuaire actif peut être utilisé par une entreprise pour gérer toutes ses ressources informatiques y compris les ordinateurs de bureau, les ordinateurs portables, les serveurs, les imprimantes et les licenses de logiciels. Il permet également aux entreprises de controller qui accède à ces ressources et quand. L’AD est un service d’annuaire qui complète certains services du système d’exploitation de réseau permettant aux clients et aux services de s’identifier les uns les autres. Ainsi il peut controler et gérer les stations de travail et les serveurs de façon centralisée.

### **Comment installer un serveur de sauvegarde sur Windows Server 2019:**

Dans cette première partie, nous allons découvrir comment installer un serveur de sauvegarde dans l'annuaire Active Directory.

**Étape 1 :** pour commencer, il faut installer un serveur de sauvegarde. Dans le « *Gestionnaire de serveur* », cliquez sur « ***Gérer*** » puis « ***Ajouter des rôles et fonctionnalités*** ».

![][image59]

**Étape 2 :** une fois que vous vous trouvez dans « *Assistant Ajout de rôles et de fonctionnalités* », avant de commencer, nous avons un récapitulatif des fonctionnalités de l'assistant.

Cliquez sur « ***Suivant*** » pour continuer l'installation.

![][image60]

**Étape 3 :** dans cette partie, il faut sélectionner le type d'installation. Dans notre démonstration, ce sera la première option : « ***Installation basée sur un rôle ou une fonctionnalité*** ».

Cliquez ensuite sur « ***Suivant*** » pour poursuivre.

![][image61]

**Étape 4 :** à l'étape de la sélection du serveur, il faut choisir l'option : « ***Sélectionner un serveur du pool de serveurs*** », sauf si vous souhaitez procéder sur un autre serveur, mais dans le cas du cours, ce n'est pas le cas. Cliquez ensuite sur « ***Suivant*** ».

![][image62]

**Étape 5 :** maintenant arrive l'étape de la sélection des rôles de serveurs. Ici, nous laisserons par défaut.

Cliquez directement sur « ***Suivant*** ».

![][image63]

**Étape 6 :** toujours dans l'assistant, cette étape consiste à sélectionner une ou plusieurs fonctionnalités à installer dans le serveur sélectionné précédemment. Il faut donc chercher dans la liste « ***Sauvegarde Windows Server*** » et cliquer sur « ***Suivant*** ».

![][image64]

**Étape 7 :** pour pouvoir installer les rôles, services de rôles ou fonctionnalités sur le serveur, confirmez en cliquant sur « ***Installer*** », et l'installation débutera.

![](images/05_Installer_Config_Domain_AD__image65.png)

### ***Remarque***

Vous pouvez constater la progression de l'installation du serveur de sauvegarde. Il est possible de fermer l'assistant sans interrompre les tâches en cours.

### ***Exemple*****Progression de l'installation**

**![](images/05_Installer_Config_Domain_AD__image66.png)**

**![][image67]**

### ***Méthode***

**Étape 8 :** nous allons vérifier si notre serveur de sauvegarde a bien été installé.

Pour cela, rendez-vous dans la barre de recherche et écrivez « *CMD* » puis cliquez sur « ***Invite de commandes*** ».

![][image68]

**Étape 9 :** une fois entré dans **l'Invite de commandes**, tapez la commande suivante : « ***wbadmin*** »

On peut voir apparaître une liste de commandes de sauvegarde prises en charge, comme « ***START BACKUP*** » par exemple.

![][image69]

  **Création d'une sauvegarde d'un annuaire Active Directory:**

### **Comment créer la sauvegarde d'un annuaire Active Directory**

Dans cette deuxième partie, nous allons voir comment créer la sauvegarde d'un annuaire Active Directory.

Nous allons sauvegarder l'intégralité du serveur sur un lecteur réseau. C'est-à-dire que nous allons créer un répertoire de sauvegarde qui sera partagé ensuite sur notre serveur AD puis, pour finir, nous monterons un lecteur réseau.

### **Création d'un nouveau répertoire**

#### ***Méthode***

**Étape 1 :** pour commencer, ouvrez l'**Explorateur de fichiers** puis cliquez ensuite deux fois sur « ***Disque local (C:)*** ».

![][image70]

***Étape 2 :*** pour créer le nouveau répertoire que l'on nommera « ***Sauvegarde*** », faites un clic-droit sur « ***Nouveau*** » puis « ***Dossier*** » et nommez-le.

![][image71]

![][image72]

### **Partage du dossier Sauvegarde et attribution des droits**

#### ***Méthode***

**Étape 3 :** après la création du dossier, nous allons passer au partage de fichiers. Faites alors un clic-droit sur le dossier « ***Sauvegarde*** », sélectionnez ensuite « ***Accorder l'accès à*** » et enfin cliquez sur « ***Des personnes spécifiques*** ».

![][image73]

**Étape 4 :** à présent, nous allons sélectionner les utilisateurs qui auront accès au dossier partagé. Dans le cas de la démonstration, nous allons choisir « ***Tout le monde*** » et cliquer sur « ***Partager*** ».

![](images/05_Installer_Config_Domain_AD__image74.png)

![][image75]

**Étape 5 :** dans la capture ci-dessous, on peut constater que le dossier « ***Sauvegarde*** » a bien été partagé. Cliquez sur « ***Terminé*** ».

![](images/05_Installer_Config_Domain_AD__image76.png)

### **Mappage d'un lecteur de réseau à partir de l'explorateur de fichiers**

#### ***Définition***

Le mappage d'un lecteur réseau consiste à configurer à distance un dossier sur un PC afin qu'il puisse partager des fichiers ou des dossiers via un réseau LAN ou local.

#### ***Méthode***

**Étape 6 :** pour mapper un lecteur de réseau, il faut se rendre dans l'**Explorateur de fichiers** et pour l'ouvrir, nous utiliserons l'IP **127.0.0.1**.

Le dossier **Sauvegarde** remonte bien sur le réseau. Ensuite, faites un clic-droit sur le dossier « ***Sauvegarde*** » puis sélectionnez « ***Connecter un lecteur réseau*** ».

![][image77]

![][image78]

**Étape 7 :** pour connecter un lecteur réseau, il faut spécifier dans quel dossier réseau nous souhaitons nous connecter. Dans ce cas pratique, on laissera par défaut, mais il est possible de changer.

Cliquez sur « ***Terminer*** » pour achever le processus.

![][image79]

#### ***Complément***

Le dossier mappé sera bien le dossier « ***Sauvegarde*** ».

#### ***Méthode***

Pour voir si le lecteur réseau a bien été mappé, il faut retourner dans l'Explorateur de fichiers. Le lecteur « ***Sauvegarde*** » apparaît bien sur « ***Ce PC*** ».

#### ***Exemple*****Lecteur réseau mappé**

**![][image80]**

#### ***Complément***

Nous allons procéder à la sauvegarde avec « ***CMD*** ».

### **Création de la sauvegarde**

#### ***Méthode***

**Étape 8 :** maintenant que le lecteur est bien créé et configuré, nous allons pouvoir lancer la création d'une sauvegarde complète de notre serveur depuis l'invite de commandes.

Dans l'**Invite de commandes**, tapez la commande suivante :

**Wbadmin start backup \-backuptarget:\\\\127.0.0.1\\sauvegarde \-include:C: \-systemstate \-vssFull**

**![][image81]**

#### ***Complément***

Dans ce cas pratique, nous allons créer une sauvegarde à l'aide de l'utilitaire de console Wbadmin. Il faut savoir que la création de la sauvegarde se fait aussi depuis le gestionnaire de serveur.

**Étape 9 :** après avoir tapé la commande précédente, le serveur nous demande si l'on souhaite démarrer l'opération de sauvegarde. Nous allons taper **(O)** pour oui, puis taper sur la touche « ***Entrée*** ».

Le serveur va ensuite démarrer la sauvegarde et faire des copies.

![][image82]

![](images/05_Installer_Config_Domain_AD__image83.png)

**Suppression d'un objet d'Active Directory:**

Malgré les nombreuses précautions et contrôles qui sont pris pour les éviter, des suppressions ou des modifications accidentelles peuvent toujours se produire. Selon le type de modification apportée, cela peut affecter un seul utilisateur, par exemple en empêchant l'utilisateur de se connecter ou d'accéder à un fichier, ou cela peut affecter un contrôleur de domaine (DC) et affecter de nombreux, voire tous les utilisateurs.

Ces types d'incidents perturbent souvent des processus commerciaux importants. Cependant, des modifications non autorisées, même minimes, peuvent nuire à la productivité de votre organisation. S'ils ne sont pas corrigés, ces changements involontaires peuvent paralyser l'ensemble de votre organisation.

Nous allons montrer comment supprimer un objet de l'AD et nous verrons également comment le restaurer.

Après avoir supprimé un objet dans Active Directory (un utilisateur, un groupe, un ordinateur ou une unité d'organisation), vous pouvez le restaurer.

Pour commencer, avant de restaurer un annuaire Active Directory, nous allons déjà supprimer un objet de l'Active Directory.

### ***Méthode***

###     **Découvrez comment supprimer un objet d'un annuaire Active Directory**

**Étape 1** : rendez-vous dans le « ***Gestionnaire de serveur*** », allez ensuite sur « ***Outils*** » puis cliquez sur « ***Utilisateurs et ordinateurs Active Directory*** ».

![](images/05_Installer_Config_Domain_AD__image84.png)

**Étape 2** : sélectionnez le dossier à supprimer, faites un clic droit puis cliquez sur « ***Supprimer*** ». Un message apparaît ensuite, demandant si vous êtes sûr de vouloir supprimer l'objet. Cliquez sur « ***Oui*** ».

![][image85]

![][image86]

**Étape 3** : si tout se passe bien, l'objet ou le dossier disparaîtra de l'arborescence dans le volet de gauche.

Cependant, nous pouvons également avoir un léger contretemps si, lors de sa création, nous laissons cochée l'option par défaut : « ***Protéger l'objet des suppressions accidentelles*** ». Dans ce cas, un avertissement comme celui de la fenêtre suivante apparaîtra, nous informant que nous n'avons pas les privilèges suffisants ou que l'objet est protégé.

Pour arriver à supprimer cet objet, nous devons donc désactiver cette configuration contre les suppressions accidentelles.

![][image87]

**Étape 4** : pour désactiver la configuration, toujours dans « ***Utilisateurs et ordinateurs Active Directory*** », allez dans l'onglet « ***Affichage*** » puis cliquez sur « ***Fonctionnalités avancées*** ».

![][image88]

**Étape 5** : faites un clic droit sur le dossier (objet) que vous souhaitez supprimer puis cliquez sur « ***Propriétés*** ».

![][image89]

**Étape 6** : dans cette étape, nous allons accéder aux propriétés du dossier.

Allez dans l'onglet « ***Objet*** » puis décochez l'option « ***Protéger l'objet des suppressions accidentelles*** ». Cliquez ensuite sur « ***Appliquer*** » et enfin « ***OK*** ».

![][image90]

![](images/05_Installer_Config_Domain_AD__image91.png)

**Étape 7** : désormais, il sera possible de supprimer l'objet sans encombre.

Faites de nouveau un clic droit sur le dossier « ***SMOG*** », puis cliquez sur « ***Supprimer*** ».

Encore une fois, le message pour valider la suppression du dossier des services de domaine Active Directory s'affiche. Cliquez sur « ***Oui*** ».

![](images/05_Installer_Config_Domain_AD__image92.png)

![](images/05_Installer_Config_Domain_AD__image93.png)

Le dossier SMOG a bien disparu. Cela signifie donc que la désactivation contre la protection de suppression accidentelle a bien fonctionné.

### ***Exemple***

###     **Dossier SMOG supprimé de l'Active Directory**

**![](images/05_Installer_Config_Domain_AD__image94.png)**

(vidéo) Contrôleur de domaine

Un contrôleur de domaine Active Directory est le centre de votre réseau. Il est chargé de fournir un service d’authentification et d’autorisation pour tous les utilisateurs qui se connectent au réseau. Un contrôleur de domaine stocke des informations sur tous les utilisateurs, comptes informatiques et autres objets d’un domaine. Cela permet à un personnel administratif de créer une base de données de comptes centralisée qui peut être utilisée par diverses applications à travers le réseau. Ces comptes sont également répliqués entre plusieurs contrôleurs de domaine afin de les rendre résistants aux pannes et aux éventuelles attaques de sécurité. Il a traduit également les informations entre l’ordinateur et le contrôleur de domaine. De cette façon, il peut être répliqué sur de nombreux ordinateurs. Si un contrôleur de domaine est hors ligne, tous les comptes d’utilisateurs sont innactifs jusqu’à ce que le serveur soit remis en ligne. Ce ne sont pas seulement les comptes d’utilisateurs qui sont affectés par un contrôleur de domaine hors ligne, mais aussi les comptes de messagerie et d’autres objets dans Active Directory. Il existe trois types de contrôleurs de domaine:

- contrôleur de domaine primaire: Le PDC est le premier contrôleur de domaine créé dans une forêt, il conserve tous les mots de passe des comptes. Tous les autres contrôleurs de domaines obtiennent des informations sur les mots de passe auprès de PDC. Le PDC est chargé d’authentifier les demandes de connexion des utilisateurs et de fournir un accès aux ressources tel que les partages de fichiers et les imprimantes. Si vous avez plus d’un domaine dans la forêt vous aurez également un PDC pour chaque domaine.  
- Contrôleur de domaine en lecture seul: c’est-à-dire le RODC qui fournit des copies en lecture seule des informations de la base de données Active Directory sur un segment de réseau avec des utilisateurs et des ordinateurs relativement peu fiables. Les RODC sont déployés dans les endroits éloignés tel que les succursalles ou des sites où les risques de sécurité peuvent être plus élevés que dans les sièges sociaux. Un RODC ne stocke pas les mots de passe des utilisateurs et n’effectue pas d’authentifications. En revanche, il se met en cache dans sa base de données locale des copies des modifications de mots de passe provenant des contrôleurs de domaine inscriptibles, ce qui permet au client de s’authentifier auprès du RODC même s’il ne dispose pas d’informations d’identification valides attribuées localement sur le périphérique.   
- Niveau fonctionnel ici, la version d’ActiveDirectory fonctionne sur un contrôleur de domaine qui détermine les fonctionnalités disponnibles dans la forêt. Il existe deux niveaux qui peuvent être définis sur chaque contrôleur de domaine. Le contrôleur de domaine active directory constitue l’active directory de votre entreprise et en assure la cohérence. Ce service fournit un accès au répertoire qui prend en charge les différents types d’informations contenues dans l’active directory. 

**Restauration d'un objet d'Active Directory**

Avant de procéder à la restauration de l'objet de l'AD, il faut d'abord passer par quelques étapes.

### ***Méthode***

Découvrez comment restaurer un objet dans l'annuaire « *Active Directory* ».

### **Redémarrage du serveur**

#### ***Méthode***

**Étape 1** : pour redémarrer le serveur avant de procéder à la restauration du dossier, allez sur « ***Démarrer*** », cliquez sur le menu d'arrêt et cliquez sur « ***Redémarrer*** ».

![](images/05_Installer_Config_Domain_AD__image95.png)

**Étape 2** : après avoir cliqué sur « ***Redémarrer*** », tapez sur la touche « ***F8*** » pour accéder au menu d' « ***Options de démarrage avancées*** ». Cherchez ensuite l'option « ***Mode de réparation des services d'annuaire*** » puis tapez sur la touche « ***Entrée*** » du clavier.

![][image96]

**Étape 3** : entrez en vous connectant en tant qu'administrateur "LOCAL" de la machine (attention : ce n'est pas le compte administrateur du domaine), afin de pouvoir accéder à la session pour paramétrer les configurations et terminer la restauration.

![][image97]

Comme vous pouvez le constater, l'interface est différente, l'environnement charge en « ***Mode sans échec*** ».

#### ***Exemple***

####     **Redémarrage serveur en « Mode sans échec »**

**![][image98]**

#### ***Méthode***

**Étape 4** : dans cette étape, rendez-vous sur la barre de Windows, faites un clic droit sur « ***Démarrer*** » puis allez sur « ***Windows PowerShell (admin)*** ».

![][image99]

**Étape 5** : une fois dans le PowerShell en tant qu'administrateur, exécutez la commande « ***wbadmin*** » pour vérifier quelle option sélectionner pour la restauration.

![][image100]

**Étape 6** : pour la démonstration, nous allons utiliser la commande « ***wbadmin GET VERSIONS*** » qui permet d'afficher la liste détaillée des sauvegardes effectuées et que l'on peut restaurer.

Dans le cadre rouge, vous pouvez observer que le serveur a fait une sauvegarde qui date du **15/10/2021 à 18 : 52\.** On peut voir également que la sauvegarde a été localisée en **127.0.0.1** en sauvegarde.

![](images/05_Installer_Config_Domain_AD__image101.png)

Pour pouvoir restaurer le dossier ou l'objet supprimé précédemment, il faut procéder à la restauration de la sauvegarde de l'état du système.

### **Restauration de la sauvegarde de l'état du système**

#### ***Méthode***

**Étape 7** : tapez la commande suivante :

1

wbadmin START SYSTEMSTATERECOVERY \-version:10/15/2021-16 : 52

Avec cette commande, le serveur de restauration va vous demander si vous souhaitez démarrer l'opération de récupération de l'état du système.

Vous avez deux options : **(O)** pour **oui** et **(N)** pour **non.**

Tapez **(O)** pour **oui** et appuyez sur la touche « ***Entrée*** » du clavier.

**Étape 8** : après avoir accepté de démarrer l'opération de récupération du système dans l'étape précédente, il nous est proposé de continuer avec la restauration de sauvegarde.

Tapez la lettre **(O)** pour valider et appuyez sur la touche « ***Entrée*** » du clavier pour confirmer.

![][image102]

![][image103]

**Étape 9** : toujours sur Windows PowerShell, on nous explique que pour la récupération de l'état du système, il est nécessaire de redémarrer le serveur pour terminer l'opération de récupération.

Tapez de nouveau **(O)** et appuyez sur la touche « ***Entrée*** » pour continuer.

![][image104]

**Étape 10** : le serveur va commencer à récupérer l'état du système, il va ainsi traiter les fichiers pour tout restaurer.

Pour que la restauration de l'état du système soit complète, un redémarrage de l'ordinateur est nécessaire. Tapez sur **O** pour accepter le redémarrage.

![][image105]

Après le démarrage, Windows Server va se lancer. Patientez quelques instants pour pouvoir entrer dans la session du compte Administrateur du serveur.

#### ***Exemple***

####     **Redémarrage de l'ordinateur en cours**

**![][image106]**

#### ***Méthode***

**Étape 11** : à présent, vous pouvez entrer dans la session de l'administrateur. Entrez le mot de passe pour pouvoir accéder à l'interface de Windows Server 2019\.

![][image107]

Une fois dans le serveur, une fenêtre de CMD s'ouvre avec un message vous informant que l'opération de récupération de l'état du système s'est bien déroulée.

Pour continuer, appuyez sur la touche « ***Entrée*** ».

#### ***Exemple***

####     **Récupération de l'état du système exécutée avec succès**

**![][image108]**

### **Vérification de la restauration du dossier SMOG supprimé**

#### ***Méthode***

**Étape 12** : pour terminer, nous allons vérifier si le dossier ou l'objet supprimé a bien été restauré.

Pour ce faire, rendez-vous dans « ***Gestionnaire de serveur*** » → « ***Outils*** », puis cliquez sur « ***Utilisateurs et ordinateurs Active Directory*** ».

![][image109]

Le dossier **SMOG** apparaît bien, il a été restauré.

#### ***Exemple***

####     **Restauration de l'objet terminée**

**![][image110]**
</det
ksYpifk6Nkv/AbWoJE8MFYuyAAAAAElFTkSuQmCC>


[J5soHWzembOiljrgL4Pfz+sRTS8siqeztqfyWHvol2eef/26288dHYPAv1iMgoyK/nF+fVYc75PLfp+efiNAv/LoTf/fOvSW+ioMDaOC6XHe9f6GwdHFlaFsn5oh0pf3WwbwyUz90XCbimhJiY+iowyR7vhMxe46wvr3MXlnQOeUCrxnXjIi3K74xXoGRaXV5JTVFJS0V7XNja2ITqX8f+PKzeooXmloOFpMRzPJxiMPKUiGh0TiPWIp3H2tobezSOFHpZDGBiYHwosh+/y95fDcyAiv1ROT3y7LApihtLS0hL9HdhOd+4fM0D0oaTn91m3ZScHE5idlHlwr5JIl6bWJnoqSpIzczOftBEJQuCWdvH5vxtAva3WRHOtHBg+gfQWQlMv0UZJqJ7eXpmb7wm/Zff3BFT9OgD+X7I5P8mHUjYvADpUdzzKZxJCQUFZIOMPD3u79P9t6EUlB4WEYrC+0iOSqpqf9/dkBuFt/v+bh7YenRBDcb7z/5ytXiJmO3LaVycayUA//q7chZx86+dY1Pxz5TlBceVU2Cf/5350cPKHd+bnYfenBDsvMfjBQHhVA8YqsKW6ahZvfm33GxPkGBcRDCGqHZwZqh6dyznYIKBSKzs7Ohw8fcrnciYmJjY0NiDwzEY82NpaZmRkfHx8aGkq6aP5205iYGFJBsiUBGJoeFik3Off8ramBz6iCnaphZjvFghFUPf5g++ErCfTI/z5HDa9eutbW1SaVS6qpKsIRIJCLTQv66gBwCgNVY5jCUuZ2sDul9v2L3/++Y+7uzh77MwHgw9p4c+tf4+/8tbIDMj08lj8rh3NPmsLu7u7W1tbm5eXx8fBgeNzIyQqbl8uXLyCEAWM1jOdxD5XDrOdkmh7ubnPo2udzbROvDeGw495EWkvlx[[[[[[GH1dXVZWVlZA3UCt9DpoVMTnt7
[feliLIZFLPLwiq9dmK0KO/PJyfv+QYGep3Dt3Hc1jkrvyQ0taw+PIBJuQwUodr85Na2mNvfnnkq5Mefim59QsVD48e+/phDVErXT4GNvvy6weVBB2fdBCU0ccr4Ezo2Np6YdGo2ADLMDknjx2KKhsXm0HBnHrhYitRYHUVxaLmFYwztbrFkgdXD+0/METX0XpTPE7uP5naXRBWThaZ7HZRU9hVuRl5mmfijkZeO3Pwwv3sYYbZ1Sso6ND+zz77Yv/Bs2WgRzytJB5RAb/61XwFejQ5doQfEbfT2USN1ZdpvvNKa6Pege0Vp08yNrYlJQ43Z2U1MlTns0Z1ScVLkRV2q0ZcYFnarVmagH1F+XFmfqyW+WTgfktExzB0k/rOkIcAgCA7b2AONyxVvHGErGxsVGr1e5PxN2apWpRjpEXJxdmrbKiKS2fq2n+Rna0ZvHJmqVY7zBoBO8dWgzrpJb5hZqw0HBrzdJiP2vN0iD/oLhOyVSey2n/YaEeVRPzpmQbzKnsIJdLV88kjXPnBwtDbiVMCObCaxdRk4JYER/gVohae4eT5YkBAcXWXcN7h8YNamIjVWsyb3KGs6McDKpmYDafPNrVQBBtG6BmKQAA2NihxyGHWD92w[[[[[[[[nt9/g[nt9/g[nt9/gxM5VitF
[nt9/gMOziVbLNTy7oaIFezvl/R0jo+PhS37PZT1OT7XvjnaOcMzF+qF9A3TRkmcpOWyPmlfW5X2S6O+rPGfI10hblo+288RbXt8fMg7Rsn3G1GdNP/85PqPOYf8Ns/37kJHHIb9ntoULw0Nphyb/p533L37C9fQPl6slW2ND+MW/W7Qk+pfD+Usin8vJk4cmppBTVoXRqWlMz83DKr+MKp/jw6W9EbZHpzWJiQnaD7jTenuIfLLlR07Po6WdqTyW/T0szi9ckLDtrQ0hVKuqZB2jRUs/EtmH2isfE[[[[[[EFQtChahBBCCDEIihZFixBCCCE
[/qtf5qOjBYv51e9VV29NvM7kSnQ+alQhUWB59646+A7/ytWqnbsa09N1MplvvABLXd0NevpfcWllVl5xF51J7WeWVta0tvvd8bHeO0sSZ6QjHc/sIj2YvtH8OIQe/zzmvDSFI4LvO7sHfEFYZGulk50ZASK8N7//X/FxyQVZKXduPZ9dD06vF46FCoUfql5kcVVffMjm6vVy33e3Y/0+ZmgbYZFDAABBNiaHubm5LS0tqy/Ptoy139F4+1t7eQUmpqSTMJxOj09LjHPZt9/HP2S4vycenH
[image57]: <data:image/png;base64qKT59u3rx51qxZ5cyYrW2IglS2eV5XljrWXX+M+alXwcETlLCM279/P4U0qVevHrugW0RNnM3T0B1mleaa8ZCDgN9+fLlMWPGSBfieZfyMA9FaKuvOyyy7j7wBGa8uGKlYoW+YWK6N9fMU9dFdHmF93bbbbf11lvHe2K7/f4GTCpfY4rPzjxiV/[[[[[[//RRx9tyYg/pPpEo4lEIpH4HGL/
[0jaINqlFka6uIUxsnmphUS7HbsVJNPH27VtHGutTGmPbQlP+EwJeXA0TVdRd4jIiJiYmL0RLdvyAI7UdEh1IgLhj0BPWglRsR+nUYKd5CVcuZCywFtkT7WqlWratWqol9Mopvk6BAzBA8fQxtt27GAXOCk1NRUz0ICFzEK0S5curVWr1oU6oS1yBYAYDlLnYQaslp6ejvEQnrVHAB0eOXINrkoMACnWDJkyJBFixYxW6VKFbZjBKc4WjQIAYatTuOZxc5jx46FhoZWKP5p1jp16qSnp8OIl4bxmIe[[[[[[Bcjk5OdevX5cP/0RZzIops1ej9u
[+i1L+VcUFcWnQqAlS6D1W/NoDnZe2tD3cHndMouOUj0kIWm9ZxOAln614yXPoIRok4BrASy6Z/iH9ygf98/fpfNXrl7DzVtPlq97n96jeqc6vL4pUqfqzSe7s0d/fT21trfL7UXD6j+pPmQyMLQVO09FYR3VVBQ2tfeJaubEuLzLY2URtrYaZNkgrKkNNM5/3GTHsUGdDOQrovA6PTmCgq5mm6O8PO2goH6cn39Z3hUM81wzVFgc5xXezz+WShSQ+CpNkNb6QrMRXLinxH6lK/G+6Cv9HQvULg485M63Aj0bo4jc0XZ3G7q5o+NdjkosYmVaulQcSYS2KH8uAbxKVkUVJSQX1jN5MLGwy1FdvpkgVp0y4ypp1kCbJnnOTP2SmWXj/O2KgW1djhCT[[[[[[[v2N8[v2N8[v2N8[v2N8[v2N80
[v2N8uOuMAAAu/n0jrvJvK9f+LA1WJfqOZfyqGWAhrE52mdXWTQr+67sbaMSiUQikf1PJ+muSubQ5Qdopl2YLWOkBPoRXTaIc1tf9VtdN805/JZG9HdfJJDHLFzdMC3ood7fqkUp/l6uURR0Vy77EVq44Sql4/tTXyo8KH0bceW11T8LLZBekNxie6RyYD0SHRztJyaNGeCklPozfPGgNnuLxZ1/Yhrt815md8j5qBJnM2e8+mnv+9qrY2qymoyUyvkOh5vT5Lt/1QQQjfys6JwNVgej6Pmb5OZJX2Qjz0EL/NHsHUUA1uZj9B27dS6mPrttLbi90iWmO0gh/QhpJPk7AVrEmA5j/G02pUNi9Tn9twZ4uVkAnl9QOYMtCiQD+FO/ZqJvUic/NKFpVKlEsqDJtmZqfGmZydR6lSoZE4f6/HfZDfg2M03vD/4j/TAbEOOPCXg9ROHl4lkqC6g+TQJKJSRZqjA7gZF7IuzSBKenqq8TYcfugj2pakeLSz26dEK7VWEK3cQjJd3TTP2VPlCY1vZKk7gP95xRqlqLfIAAM+E0b0M0Fa/w+0Y8JkVM9lSTd8CDyTgEFBfk0jszw6F4pt0LzQCjRZjHDTIrO1nUr1OdFk9ITBGtfZMszE/g4MvhE[[[[[[2dKBFVoLrUZG4FpuPdr1FFP2AYFO
[2oJdhAtEhIj1OjHpRuke1ArhHyK0vobP4Wo8I71bkEaH3bO96/P5Dfld6nhbuyWG/K11PjojirFEKcDWrgg+yumlcfLjDzLZsontcqGlh+UQQYnzfUhkSRdj62b21+fprSpkeMXsmq47IVr7uiJbawWGkqX2Y8ZV9DKuztGfHihItU1daRXXp/x/iexOttq5unJIr+cPGEG5bEcBtq1UG/Wrq9i4vbpkXyFPGGbx/Mo7fbo1krGc+xkH5PkaL4ve54G+NNgvBtvSAAOuC/zUiZbsnN0tVbiEAqxfOZclGfyLFZwPSX1Hk36yp5mLsAXaunbLBlnZ5jN2CoVdDl06P0eRQjkQ77P3YpQyCTNOF5MEVPHfng0xevI4tW3fj6RVCcsFFfvbsfqWNwxQ0k4uLhz59EN27HhIUpwfF4XSTW8aYmTkwivyJFE2Uxxzkk+OMXmUV1ax8vCsLYfc4FDw8R4ypVQYmKMy4y269mhph60iIiIrjcGLTPJTgRyf2y0brGjPBE1QwxaZBoGLbpqMkiJ40c5fptSTe[[[[[[[weOw[weOw[weOwPkZnYfuUX1i
[weOwOavv42Ih7d5m5QCku+fM2Fe6WPzCQG0nVjig3D8jQcjc/jiBhxJjTLfWDCrddTKrx46jnt5Bsj80q5huDDavI65hKhWp4lKm5J2aSzc+ZGZpis6ieNEG97h1z5vEFjWHmypKov0h5mYXKb1CoDlJTX1GbHUnPb3NFIb8mvyCdGJyRsKO7M3q6em5vEfLKS+gdnQTHeQG7mTL3k7ot5S/bRpZFaePF9lqOsm2pPoth8u5Jpa4doFRXC74GzxoYMDw+5gOOSvs5POZT+GTXDQ1dnz6u+fL3TX4KEGGNUV6bBQaUEcDplxuRkyRguCoGRUqJyokBmwvbMaafKof8mZMWF9JIKZGmIAGX4kHck9/4QdBi906VBh8yMiVYdoRHbaVWVDO6tNPZGy/yEDQ6qW2cZQmlnZ/8DbqmkQJlgpNOCw2Ik+gxCGC1rAqH4FYG0oaTNiYqUYsAauY4FEm1qKK3SaUSPHXSBEmpysp34zY3+CCSOtGzuF67g5DVVkjNh0hv7oADhbKMS7PAJ3MhJkbSvHphYtrOsDLYrfzwjg/pamw4b8ZmQ1aDExUozP4CY0wJCEFoFAIBAOG0hoEQ8MSWgRCAQC4bCBhGh933oFcEtohSC3tAz5fpeY/cFITUuDy8mnKnPIEok/HJLQIu4r/8WF1h6Xm620bgsB2PbjEB+XJs0jE3TV5uPj4CcTrVbFDe5F5ZMX74FfhoJFfTwWdIt5dUZZ0pQvmRibYCLfoZ1H85oMVNafiFe67S1QGRpIQUcPo7OrROCU/0gmevVdC1hTn58Pd3f2GIlvUGZ4giDsSfs87ePAgMjIyUF9fD7VajYaGhluOuqYGWiZ6HA0TKhVLh0qrFWjQaNDA03WjaWP7yNm8+aqiJWGiVSlTQqtWQcNQN8weeH44MUVKVDLRGhqY+hk3U6IlY3Woq5sJndGIAVbGsw3+01TVtbKritbevXuhVCr/YtfRzUYmk2HPnj0kWgRBENeLo2hpuNRMcYO9ZfDjMwTRssTm[[[[[[noacCn6NBOtevQPXF86x9M7k6LC
[V4r9/tYdb1YOKka24uoVjNyXRqmDb3/U/23SbRT1G/CIwWGMpKIaDpR2x/rF4AjJJaKS8bW3IW2lHCGsRgMt63Qatd/XKRTwCoI4x4VS5YKiJCKCHnHjiejQewb58HWz+mhpZ6GOsJgGF+sTfxMhJbkl44UWhKJRCKRHEUKLcmJIIWWRpGjb4nMsm7+/HIRz8mpPDktKP7+yukSTEu1+2oDnU701DOIEQ1fXnwkLpevcOG8OaZnL3D6R6EQqMQzN6+MeMuzCRdFnNL9zbk6AgRoFTWOM2D09u69eHolxWUVU5yJZWwFVO3ZtY7Uy1lZNTXFw07xuhv72M4mkT2z1JRMQ8p7yln609I1YBOKkgEKR36LIArcO+VB6HRvMiOk4AlDxKOmfRbgzwm/Mir4EphQGxZKBeHCOraAS9bZXsL2NpX8zfwsf+ND6a7OkS6B1yV8kfy5AyyYWdKmxkjcHaP4PugX56m0p4Hq2iY3qbrclOSvKSeVmuxr4VBqLqB8cZ6S3jd8/b8Dl3KFWALAEAeScmkl/PG+VrIz3NIHckfN1va+4oMk81haTgwY9HqhO95kJfpVzpjGhG5pENfVBea9aboqisnLLGBFcsz9033hxmKcRaWShsKjrCqCvkTb08eMcU/kajEVCzjl9prI/cy5jX60g5rUcEJf3uVfvEplMCC3Twj7VWkhkYQmd3A8MQ85n3x0m+tMDfcRGiets8ZXptPKnq84kICCJY1DUqMlz05TL2oxMO/l07jsUuJS+JpRpq4u+T2zlLQ4w7X3/rSohDTbRpKaijMqibFITIvDMqmZ6wYBvRA6lVfU0dpxgyoDRKpGEhJw5Te/YaLFuG8YjUYEBgQw0WIIBW
[image64]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGrCAYAAAAYfTnLAACAAElEQVR4Xuy9d3Bd2X3nOX9szdbWzszuH/vn7E7Y3amt/cNbHq/tmrVlWZZlS5ZtWZZasqSW1DmQ3SSbbAYQJMEIkARJEIkkcs4555xzzuEhvgfgJbyc8PDZc+8DSKTuZrdAuW3fb9W3SNx74u+ce873xPev/vX/8l848fFZMrNzZWZk+ZiXl/eFLCwslJmfn3/o3S6ld5KboqKi55Se5eTkHHL7eSwoKNgXj/R/6Vlubu5zSs/3/r+4uFimFP/esHbdSGmRwjgY19eahaVU1TfR2tpCY3UZyQnxxCUkkJSeSV5RGbUV5ZRJ7nZscPzMpbi8koryUgoPvfv6cLeMC0vKKCoU9SZXenbY3athLqWlFZSLulck/f3KykLhkczJJisjmfh48W3ExZGQnkN+cQlp8XHy39Lz+PgkcvOOKBeprCQWFlFSItqqvM+rN6J+FZVSVia+ucIC2VM7hOVJJd3UJ1yyhqrR6juY/4jBI6hkQ7VxxCTVCBTlOFqKmu4P6VtGPtHUQK+K7cfMW9xMKGNEpUypo0XSISa0bjRjgb4emit+lvEipFBNrC+1D8JVKzCfmu42ihJfcPnqPay6Om7/w3/gg9P3cvJepfZ9xz7/GLODzCONVEUHUpMahN18d/z7ffi2HrVXH86pPPePzZ7/jsfhjt8uT4I7n0doLLuDGZ+162VH2WNsfKUgZYET/n5+cpgYzAYHstysF9YWFA6wOPysmzO01VbRklxMWVidSntMH2cdE8MessbBsX227vRrmWblbEOassLKSgoZVs6pMWCbm2O6YmZhwHtWyypNCL8JqqJPpoqyiguKWPFIE0/yJt968z0tVBSVk1L3xQbx+8GnNIpvQvJPvtUgZaIL+0OvnnFj6TqfhZm+mksjMA9JI7E0Nu89NoZ4hp7SY7PoKJ1FNWGDp1mBXc/P5qW97vhawxXo0Z4jtJ87yeP/QAaF327eRPAnu50aaz4NTXI4zaMR07JgMpMYlk5eZRWJhHSFyl6GiXZiZuky2TnqWhHlqbxMLZO8KyxXOz5jxJ/YlztK2bVscf+Th9ZGblUFBYS8TSU+LZlxRP84Bgz8GDHR4aIvJZCqamdmx4lhvpf6kizSCitJfuu7SI/t5aPOdTg1avFJbuF4M55JkZ0xCUO4jN4ku+KAEe9BDylHNacl4zCL+MS5lWZrxV8VO+ZStWcc1Tg3S2imczKgBempC/t8H0YCst6k6j5MroG5zCfvy06RO1bV1EbzSxaN3i6esfT9I4+t7PP2roWXiUpgSjAse3kiMDkOoXxASW4bZBuYgSg1BYVYU4nIKUd6uQZ+6Cd6BgQiPikORSA99ZwtC/f3h73EJ3t7BCC4W39r94rAKjblx8L92E4XVnRiYX8SyZQQxmZXIYtsNC09BcZMUWbFZqGSiNT3agshjR+EbmYaGTiPG+hWQFCTANyIAl4r7mWjVws8jFJ06JWoKkhAWFoOc1qHbx0vhow0s32LXLlt7LV67VV1tH+MTE3g5ItEiCMfcEq0TN2fRIjaKTStaHFYOpli5WPq3f4P1c5/D8leGSM5
[image65]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGvCAYAAACD7HvdAACAAElEQVR4Xuy9d3QcR57n2Wf+uJu93b9uZ3fu7u2tuRv39u2NN9s93a2W1E5St9TyakmURFL03oAGJEHvABIEQZAASBCO8B4oeO+99x4FXzDlPYDPRWaBsBQlSqBG3ZM/vO8rVGZkRGTYT0RGRn3ve3/0d/zPf/RX/PFffJ8//9sfu/Q3P+Iv/v4FfvSTl3n5pZd46Sn6+c9/zltvvSV/rj33WC+//LLs5t1335X1zjvv8Oabb/LTn/6UF198cZ37L5Lkx6uvvir7J32X/n/77bd544031rn9xS9+IYfz3nvvyZ+vvfbaqvNSuL/61a/kc7/+9a+X/PzOS0qvl3/BG7/dzK4j7lw8e4pjh/axa9cu9hx0w+vmNc7s+ZzfvvILfvrCT9Zf/w314os/4eWfv8bOk+e4dO4Ur73wAi88wd13QiKtXnzpdc5dPI/b7s94Vf7+BHcbrhf50Q/fYvOuM5zYvoWPXvk5P1nnRtHz0osvis+fvsrnO3exc+dOdu7Yzk63s1xzP8nR3bvFd3Fs1w7e+/UrvPyTJ9QRuZy8zGa3kxmhLP/u9xJ1y+dW9L8ohaWwpD9E9dJ16z0a34Wa3oW0BDWTJZhVmk9zoZKL3Hpv0+1He20ZAT6e6zrwz13n7/3Q741Xfz6aOhlvO9feL75v9LVUtIQixD4d1msbGFlo6tQwOipn+qhvD8ARLLeD27ChHPGzZDAwK3fS2zcN5JH50OC6ipfhiRnjU9RpMJg26Z0TJffi3q4/33f8U//N0n3JlmukmO90rYAzqTy7S1xmhLIbG+7kRk9b9Wjkt15Fa0C7sZQVHezvK2mY3uDJ7a+1CuzCIyRSb3P+ba/ReER4fg7+tDYa+G4mcPKBqYo68ikJPchzucipzIv6VReJwHkuRYK/l3N+krSSMtKYkRMFKbBL9TfkK0nOitSsLlkOPYt3ML4ooaMm5+GeEEEIWHYoWs6SjhmiVlJQo/esIIYSQW43a5LqVuvePu0cSmkxC/ExC7Bw2pUN9uVyPrmH+FYAipepK3HMPgo89Bq9Wy6XBEZk2g3ET9BARIM5
[image66]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGvCAYAAACD7HvdAACAAElEQVR4Xuy9V3BcWX6nqed93dl9mbeN3bd92d1YxcROTIxGK2kUO9JIrW6V1N3qbnWZ7vKOZNEWQYIASZAE4QhLeG8S3ia89yaRyIRHwiR8+kRauG/PvQlUgSCry7Gqq1vnH/ELIM89efy95zvmnvyT1KcZZGTlkpmT/5ly8wsoKPjdKi4uprS0lKKioueunfdTVlamSvk/Pz9f1Xm/L1JhYaEaRklJyTPxKJ9P4z4fluKmXNNoNKrOp0/x/6Iwf+hS011WTk1jC11dnbTUV1NalEdebh4FxWVU1jbQ2t6OtkJDwVcs36+rotIyqmtraairpbzw+es/FJ22sRJNFTVVFZR8j2nNzy+kSKmPylpqNaXfWV1IfZGUus8lJyeHnOwscvLEc0RTTVNTE5rcHHKFe7ZQ3hfVi+KutJ3KGqprqsSzpOR5P5+piMLiCurFPaERz5LC567/cJNUyk9aSOm/Arbj4HBS19LLq+HmyejVv53+PYYcp7HrSUXUuBvV06h0Z5WN5H23ZQtNYjdT+UuFZabTWorW9DNxOtpkVItgnU5qXj6qkP8dHpqqmy1QyLN47k+tf08WfuoZd5OlD9lj8+9+rzhwGCggKCiICxL8JOAWdiwH93oRZIcj8tFabsGGOF+zFbSeRs5BMORANiLo64KF6u5wyjddDgheDD0x8BgGhzgcDofDuYOhfU8X7Yta23vQPzh60zb6tnWp7robG6lq3+Gk8tzzg5WaC/PJDczjYa281ooionkuX8dF1dfHK0OU5ebRLBfNF2LewLxA07P/413jlwGkePHMTpy7cwq7KgxK3+3FpOG1ugG[[[[[[wGAwGg/H85AoFxJNJTPb14VfpVI6g
[IzwTN4qnfmF3UGXKlClTpkyZsi9km5ubu/XVQgEv/UwvrrEyPUJrSQo1IxNUJoUTFOjPDXI/gtqCLCL9AwlPSKRIjEf60hS8b57k6JlzXofN97CHybjfCE40juUNxxSOwLwyh7Oqn+KxLAci9xYhWieGVyRaKiLs6z96MmWvAHYzJEW+b+TUwOSSE/FdtmaphO21OYwP9KG7sxNdne2Y2QiebhVDGwtBrGmq/JzbJeRnMslWqJGS6szxO7k0B66SW6vtXgx0NERW4phmDHACBYt+XbT6Qwqo2VpyIfydO/Af/yP8zu/ApUvGV4hqUMPXKYTGSjpnhADoYHlGbnm6xbxffssCRFqOmvJ9HysnAr0s4dieFjIJSKhNv8s6P3uLDg4c4GZlKQ38pdCJHSm2lnwh/sf/yMIv/zILf/3X4WNqU4HiS5V06A6n948yoslQ8KeI9pTmWzs5mfuPGsE2rd0[[[[[[UyMHFrl3OhGF7pwbj5QUUswFouQ
[6P4ja9KkiWsHAEDUJQStIkWKaM2aNS4o2U81EQ652y0FW35x8uaNlk/0efe9kLgXtVp8dY7eUsabYdu2SSpXyg9bdd0utWgVbAACAiDh48KAcAnE[[[[[[[CfTz[CfTz[CfTzVUZP79LhjOn
[CfTzuXr8CixV14++23Bh8PhcDj9sGLFTPqBNaegpiqa0tbdww3HsMvD1doSDBFTTFl8SuZ9AyCPVNKqukZ5fQUqw+liDQ0lMNpcADSqKrc87r8Lrjgggv/+PiFROvzrUOFaIkPp7wOHY1f/SkZZK9O6ccHx9xfLBJUohZdS0RksXa2VNdsZ/jJy1X4FRZM3f8UVoMB+R1jnCenq7wIjYtcMFDqjFBRX+Lq+YF03xtk/MfYRTQWSaT8MacvGZnBWHsd0rOa8ejNA5Ta7mH56JAm5GLOYizU4dfE9K5Z/F3A2HpHTbox9NvrH3F9P9Y0h2LI2PP+Ta9KpMF3vNysHYQ0fNr7cwQy1bIvBeP2U/kPXblwfU03HMZny6iEy7+6LZ8BPGlPuhfkoV5HZj3L2J/TJfccXkJs08+bSzZ3M18rrYO95ZboY2JQnQ0i/mTcTbH2XQYnK2S7Vx/xnTDyo1j5VOfYO3BiCfTV1y4TIb4cEwYr8+r063xsdd0ROKl08ugddRUtjEiXR4OtBIfE8+7Eirf7Q3RRKWRHr+ldt1Bf3sH7777hxaN99g5OePbyCb5eUgfyvONqeZ7CjmcbacjKjIyns3OT1Ya/SJicxPPzNVZNf2cj3r/apSwgnWYzh8/1JhVBKraIcLlz6nImMD3bSUC12/9lpRAX5Udg1xenRBo3l5zG8B4xIbblBagtKGDIWkXK+au5nn597COuslNvL5dPdwUIjaOmb4rjw02q0yOxWy2iDXqscbnDQlP/CjRurDRkncdeojWrw2/CNEKCSbAPwhHcySp5zIMtQTprC3Hazu5ddJdByDahpIvJuWlcuNeP+MNnR6Q4w8lvmqSpuZOxySkm+puJiUnaaPNJgwwZolllf1r9/sVQdaaNE3KLW9NDj8lHHjsDW6Gw66wpIjgnRyk3M4M0XL2mIt+LmfLJiR6VP5WXPNihw+CbQNfGO/74mzPmD1/zq3egPy8/45ssHSLeY0Lb4HP/2y5+ord+jMtuMlPOM2GMXO4bIcSREM5HCK/F+DiXUzjfWRtC7lBEZdGFXeir6kYUUoiHvIwWOPiERwkRmppI/p6Wdr
[image70]: <data:image/png;base64ALw3jvyP/Trzj+0L49HwZXPL4b00QBEEQxPLMaiblCEOG8PvP+z1/Dau29h/+mbGNZq0ZkhLhBPVE/hx6gh+mjaKnnETbvTrkdKnR+6QG3tw1G1MGqBqcUkRLYf0xjoA2xS5acl57YtMujcT8HKd9ep72/Bv47DxJeFY1h04nUF2dhuvH2XZGVS9VKgNN2k9f5pNEx1mI1sk6I26t4ucL9CyREA6TUpD/VkjI529RF5Mo7ZrgkkhWXM3zbnrRDx5XtPb2aPfSDWbpG8sc2Zn71hYWpr9derHHTXTk7iEVIrek4EreGBTmo8RWSnp5Pnqqa75DhHMnUNgIfkF/bS3t1MZYkTd1kzE0aNgPrPnJ/c4wc4nuOgur6ZnpAKRVNhBjuacNjs1PSMMT/eT7dap+nJMKOhEP6uFrWcfKYXTzZjrUbGcRQWUuhSn11pCfnZOURi41TlpZJT4FLr5sRX18loxEIjhZ9F0NJObTqMLa+yFFtW2+Y0Zb5GPBWttHSEaGs[[[[[[jQgkhxHYkQcviXjZoaUtL8PDD8b
[/GiFYluDtqYVHXgfqjUUNdnQq6WeiJWiqcqMDP/tKCX7kmzX4hT0S7M0exP7bMhyo1mGcLlrPFi5aXLReWLZCtKKRMHz+IILhCGIrqWjojcbMKBR2+X+bNWkh6J4PzK5iEoc+/T0AiOn95BqdrGzK+URNXQTs+iXtJ8pWuENyz2ipbL/U/ZbOOeT/cVqUCNQ6iKRTqAUsUAuskCn8SDzjiBTKMPLmIR07gU9OTcCXLSHssyNiVUEkUxgFrtoZ9ZRtf+OW2an6X4ZTfb/UWo4XkDV8mskIRC+NxQMEovFKM8vkhVBt8WkxWqzY/elRYBeytv3st6rkYWvUUU1NzDA0rqa13WBX3eizkx6ziOq4cT0ZTUzdCDuxFRGgoLuffROjR3Ti1/QNwVq85CkBLRtJQMt68iVoEaY4bEgwunLlil7zjSRUmvoPEjkTW9sCWiIBLSvKx6BFqCEgrV27FjelJR5evHXHG3n8D0sP0LRYGgLknnUpmcMskcq6PAqjZnSnzs8CdUZKaooJ8jpcqHb+MZ4+IpSEPPFJ9yMRLASI9lM/ooVAcW1EoWgfEscYrDlRQ[[[[[[[vd8d[vd8d[vd8dU1QPviRWZvt
[vd8dPaBfuAgwq0cUL92+cmYDDNi7v0Gc7EgBAE57QiP8Yf113CkZJTgbqWTvQ1JCEi8t450WG5x755BnXMDxjhm83zqDOvMibIuPL+N5KTQ0FKdPn8aZM2dw4cIF+Pj4bHh82U468oSEBHz44YfYt28fdu3ahbi4OKUfqPr6ely+fFnpH5Z75coVBdIJDc9ShMLY2Fj85Cc/wZEjR7B3717cuXNHqQvr2dnZifb29hcCGQMDA7h586ayb41Gs3bxE6uwsFDpw4qKCuj1euU79rvJZFIg/9atWwpg8nz08PBQ+ph9ff78eaXNvHYoHksej9ZeVxbAxTyXhbVomHU2MmFjjEuNQ4yseFEY7SvY0vPKIs6kwxaUQW0FH0e+mxA67X3ugtlb9YYqAGZld0gltjhlJMfVwn3EoaFWVrqRuXFtgvJZuPeVuno/WvatwP69CXZgNrJ3heRDvkanoD27L50qm4g3jn55ht6melZCu7gT2wTWNOL8SSmmbpr2xjOqyduqrxmT3NZJ2k06cFg097UPojWraRYd0SbMi6tU1+uqaGR8dpa+xk5HeYYwBLxP9XSiaG/DGpHK+i3lOANn0JMMqLf6gH384yurKDLqxLroVs6jnlaJjomVidpk1wxiDgyO41/24g+t4pE6yepgF5Qh2rxOXz8LoQA21d+opvdlG+KHe695OWjyLQRQ9DRReqmF4Uo81ISDLp8a4NIvRpsVgXqStqpFZAZKWmNRIiw7JbphgIC7aLhVlgTxdTMyrZ129vl8Q2AYwzSoYbvhq08pkXZ/unWzkxpV6HtT2k0wEUXY0cGDfJ5w8eZOL13ro67hBjcj83vusmmYBZftPHuNG7X1ahMM8ffACD5urOXjiNOfv1qJPllGMdHOxXo9qOfjM6KqK/npUSHpIevV01E6g1azsgFYpSz5mYnZwhv6WGUIBJy7DBLMGD9a1hNyctpF009HSy9j0BAq9goHuUWanZunrG2BoaBSdSLCnxgYZHeyWR4BPTc7J6cQGCMlBOi/AM4bDZMO8oMOgGqS7R/y+SOQdpnmMQw/oVZlZdYfk9fhedI1WNqBhYWqQexfuMaWaR6FRMDPcSF27krQou7RE2beRBNsb2TjpRIJgJPkdarS2mW9vYHpglBGtX67d/DoVBOx6NN30dA/T3DmLPxQlJGJ+dn2T4sYXa7TW2SglGautYWJUwbT1SSvMdlmq0coQDkblmr2/CtDyeb07oLW0RM2kiqtD0zyYNdCqFS+EK82AdYs+y5b8Oewv9dbNF/csKKKKvoKSQlGNp0lGs4+swrHN5WujAT47dpmhMRUaEX7aKGDarafxWicaneiYiR63bkHW2TJkRT7dBa3TZKyPk/PfC1rS472woFwv28f7OlTKrxFb8mLRiXzR65mZnWVm3kI08+VSJvh4ovhS1+Cj38cvv51aG+HIe+eCVxEfIt/h
[image73]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAIoCAYAAACxsUUgAACAAElEQVR4Xuy9d3cbyZ3v7bfz/LVn38Ce3fvs2XP23utN3rXX67Be22NN8thje+wZT06aoCwxiTlnggRAEiAIkiAAJjATJEAEggABIucc+b31axASxZFmpBE1I9H18SkP1ehY3V316V9VV38HHA6Hw+FwOJwnwndOT+BwOBwOh8PhnA3fKRQK4IknnnjiiSeeeOLp7NN3otEoeOKJJ5544oknnng6+/SdTCYDnnjiiSeeeOKJJ57OPvE+WhwOh8PhcDhPCC5aHA6Hw+FwOE+IL4jW0dERSqWS8F9K94N+r8zzpKnsD6XTfNk+nifud5yVPDl9Hu43L4fD4XA4nG+HO6JFPePfeecd/Ou//iv+5V/+Bd/97nfxxhtvCNMJqtAPDw/R2toqzPOjH/0IH374Iba2tpDNZu+s8Kygds3u7m786le/EvaF9unNN9+EyWRCMpkU5mlubsbY2NNl2b532siKrj9MZZEvlLiF5dp9ncgUUiux6YfdRgU0vnYMb5lyK1lExgaOsBTffvYE3epcRYyc3y05WIZeBx6hBe98irMfTOBzO08uXiVbM64BtYQy/fKEW047ECbmh/y+gp7oRP/5DIyadSdjT9yz6JbiwOqvBtD2M1bVNrM3pIF5yIRAKYKLlNn59dRxVwwtY3N7BmFQLU6TcnH10lEbY48D88Dg6lEWvM4bvRtwV/wYkG9iPkIq4+1c5i9R7Sk05Dk3sNHL72JF567jK2ECTeefxVV2ggS7CZ06t09+D/uExiKVSjI1LsaS3M0G+95uzXwdBtKIOJjsG+DIQPsPzdaFv2WYiu1jXLDCJ3/iKdVH+l5D0mSERiTG1tIP1bQMOrFtMupw4eaYq5JJMop3rmB5fwLbZiWDFpo7oswQJOE3bMO0YYXTFuGhxHpszE62Mn0TrJRScl8pNhhTN8tbdI1nw3BT6asW3LzxQtIzSG2h550Pssr9P/lr+EOuR8D2xEiX6fOeitS6J1gkOg1c59J3jUIjWoRCsQyFahz41fL7IjhPybLCk7qO9qZEWsZ09HGB7fZ2t5TXCHvX2ihRJR0JCHjOUBHvZjmfIRvx4RJlWJVdNyfvnDVZE4G+K/enaK/VB0YaOUCgyRW/pq09if1ANI7j5DbfkikB8kJAJMgLLvzILHFvyW6+N+ILv9QhrNa+c4JwgPRXo7V3stcOHeajw+/wBu/+A5/8/hRrDfdVitSpOhPopvNniJFihQpquvAQKucNpGxfUbWcZqs84L4e16kc2Tsd6aU9ZRIJ0k7rsnfkbbmHrj2Msw1H+fjD97nnbeO8vbhT+hesZO/NZehSJGiP4UU0FKkSJGiO3VgoCU5Hy1GNRsFlyokskFy3g2GbnzB4ddf5s2GBSzCsH+5j1xhRZFmlcGMwmb6zkWLNd6K4Vb9LQatWglaJYpZO9tCRfQWf8LC+37TxWSUnpy+lWg9Y3Ujv6ysgTKCDfL6c8/Fa88/H82mvUwxWVvTRWSqo2LCPHHm9tm7kh6V7BXz3twxZg1dOmgBEaDFYuNBHtDKALSwvnD0MY2nwQM6wkvDdCNQkScNWZ5ojyqDl1HlgR8ATPVmk8hQhATIgRh433njjpuC/60SBCGk4BZSktGSkJDQQ0QrIBIVLYD5GYI6CLL1KBBA+rRoweXE1FGxH0Lu3XrRtOmTaMtWeI8JU7RTJGPaJmyhf3x5Mo8Nh56vxFc54+BKblA
[image74]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGXCAYAAABrxf4dAACAAElEQVR4Xuy9Z3Rc15Xv+T7Pt1mzpudNz3rT4bW7V3dPrw6rbbdD224HyZYtWRIlUaIoikkMophzzjmDBEmQBDMAEpHIOeecCzkDFVBVQAVURFX9Zt8qUCSh6CeTlq3716oFse69556zzw7/fVL9N1SoUKFChQoVKlQ8E/y32V+oUKV+tiDXkcje7lgcjfJ3U3dXXx2juZrI3u4UHZGVDAU08B2fte5pUPD3EkJZeHe9ZxYkcElyLLULF9aK5dwSfr3biQW0JpaTJn313Aqh0ejE1reboP5aHAlxccTEJpFRoIxIieMQx1JSUiL+rsjm9ZY6YcwYjZlEElSBBgiAgggqIgCQlSs455q7mzmf+2v1s19uK3k49/FNrUbaU014XxpGfzEdbnoJ0zNa0uun0s0uLf89jtJ+rRlKPwIqUft08OLg/YhoCZ5GRMsNIlqCIAjej4iW4GlEtNw4HDO/fw2l7dqXcPaSd9+sJsEGTqjJrd9p59oxzbo
[image75]: <data:image/png;base64YE5wog+3C6X4USEDNeyhtBDo1e99QlCy0RCKygDH10dkNbenxYa5oRWoBxawyQac2rhR6PL//uDVBoJVsMjtIo+1dJUsnt4I1STJtQXNOFuVCn2+pTiq9NFiMofQp7cLL00dCFOoRVxNBbH77sIrQkVakhouc8KLQ0JrdoZoXWbOkIaeT+L0FpDQit3kIKomQJ5eRvcKF9bzxbh5I1G3MxSoFBhhW58Ap01vbh5vRKeQWU4EliB40coSK/MxJ9IfCQJI5h6aqRMcw9s7c7A/qhvJ3WYaOTiQGp6KF0N6YaMGMdg/iPKGYcRVTGJSOYzizGpsXfcAH1zrR3KHAQMDo/gnGrFdLhzH2IzQuh2QjuWh8m8VWgVxRfiHy90kLqzQK4ZQlVyJlR/dwa0qNYb0ZiqnHmXFgyirHoNJM4CMqlFkN2gxorVATx3rmVMkILaWo2DSjtEFN3LAKB6/vpmK97cXIHPcmVZjViW8zqrHG+espHgmbzPRbarJ/T3Mf/tWzFXfqtNIDFrMYRd3MtAPhezppEM4w350fKLSoEYhGLAkB58cmNQynG0oNUhIBzvbg+t3s97PfSQ3bJZ3FQke6bkG68+fbpFcALLyH6MAlQTITyMQrDb4tmAtmr118f1HOuTLOpjWTD9djC8TSUxB5mcv7nC0W3VOkLWzr8noDcd5s3ubsOPP/i+06a6P5enHN2+z58zE/vJ2V8msrqCmrSM0lJqKSvsYDqGHdsJI/OzlvVLIzfDzcSLHN1uR6QccmpWGihfB1y27+vpDlEh/hy1d0FBztHXLwDCQxPICmrgPzcWCItV4ZmvitZOF7VZUXirG1PW2EBx6l1unjuPRtdBNjzAYG8dGWWj9IkD7GzKWOzNJd75Dq1ri+rQynxZKancmj/Hj54/x2ef/YZtbm3mOHlhc16rB+zjlHrALPqwb7kSk4YSas75M7zHX3n400nYWIVgeIaAmC8LmnuRmmTIHf/AbuuutK7t/PyCCptJsfhpqa6gX27cukfqG7KKq2rIpWtN91wKwLulQbBWlcP31ufR0BGAfJKy1FaVivz
[image76]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAHUCAYAAADiCYbfAACAAElEQVR4Xuzdd3BX1733+zNz/7h37sydecp97r1nnjzPec5JTstJcnLSnDhxN64Yh95NFV2oFyQECIGoEh0EiCoJIUASSIB677333nvv9X3X+gnZoEDiOJbt2N/XzB5be+/f2n3vz2+t9dv8DUIIIYQQYlb8zcwRQgghhBDiyyFBSwQnotosVbi6suXSLNe4xKmSlsuRCLMsuJmHjm0tL7xDjM4KWbv7TgUP3UXqa/lWfriHSfZ90+IqLi8POzg5zc3PDL/x0qNGf10FI12jpQLNnzx5DLZfuJF9dXW0INToY6WZEXSOll6U7metmO90UqGuYOjs7P+2jpYONrmHTfbj0fHoddfiKiIgwBDXdb2zfvn2G9dJNiDo86bJ086L+taKeV9dk6fXTy9YBUvfLysnJMZRrbW1taAbV4/Sy9biOjg+u27+Wy8vLi7O8F89ny5LL18vR0/XyywpKaGwsNDwd0JCAhUVFYSGhtLb2ztzE4QQQgjxFZGg9Wfq7u42BB1fX19D6NEBSAceHXyysrKIj48nNzfXMF4HKR18dJDSYUjPr4fk5ORPA9N0wNLT9fjpQKY/r8vT43Tw0uXr4KX/1iEsIiLCsBz9t15mcXEx+fn5hs/r0FdeXk5QUBBeXl6G/xdCCCHEV++5QWqFGfGdX7YWSEmsZeAmvH6BwapaKqC9/wB9e/hUkyKOtFC2f8vczlwNZWU6l71DSSA3f/+2bEhLQVTIz2hx8aYW9/iflwBta057LmcTVrVZdHfjSYGMNiHHr3e9oIuK2xa4n9nPnoPGWz5VrZKqpwyXVdNXizChyUVZHewedPQMMjU274HC/NW5juruf27x3kqbgzX/Dzm5iru+UEcyHmZ+mAfk1XHaEMJpUlppGa1MY3+xF5ARLQITxyneQ/4SSgqKh+SkLINYBGixBCbnR0erCszipmC1wYf6QEHkTQb22t0fJj8ugsdNgSREju23kBt[[[[[[X0XjSOsxeOA7P/uoZdNuYC1N+F
[nDt30VSI0JxUlhTtYud4Pb9nOoNlcgY8CbIutN/rs4mtObOO4rT2JaJmPetbBciMWY0VU+kZ9x/ZHL2Tk4e/k6jl+4jMQzaUg4fQEPKhV/H3o[[[[[[[[hJK6l5fELn4+MjkaNeOB3teF
[xjdxp96fhxH7MvD4ggg8MtEf/2bjjl9/5C5j+pKI+wZwiw/30pw7ZW6OLDvdh40x5YB1swY7IjRg0bhz52zhgzZRJ6PP0ZrOedwjyPvUy4T+EyzaOExMMSIlrmDxEtQbAc3Dwj4fjnIBUsEt/0A+AG2UBLYAWeTJG9JWWQb9zPdE+XhvLdfpkqIIWU8BAM/AH9NFX9AmQSPSJ8QCuA3C/WbI/XdITQzvDR8eEFLw2nEKg5eXryUDLzKWs3SgB4t1dGNlJ4K2f+AFQAKbrQB/HHZTuM/ysAZFxdV/pHG4wTYJxtttlqe53vVRngV/nZ3jHrWSKDAipMK1ksL4jHeivrsAQ+2RTHCcp6V59[[[[[b999963ABI533HHHMsMMM5RFF12Rbn
[8Y9/jLffflsaoSORohFDivWdd97B2bNlzSYvEJ6HyuCub0bF6LKsDmmF0VKj5S/fpcLbi88hG3G9yPHnOEVhbO3Aovh3R7W74hq1fZBhmdHkBohWUFslWJhRizpJofLg8FR+vDH0+WpyIt6fewUvrK3GhfsSiFb8TmsIyfDI9A6sTBgZHicS5ZDLcPp2JT8NKhWiZYRc3+k3iphRZ7gqJljQK5UR3YjZe3ZwnOpQBXNn9EL+aU4Rr4vHXTGtraAqLRoroBh4MrdF66mJ4Ei2bCW2JBfiPTzMQXmKW1kBRHN62FmzfkoA39rahTG5Cd34FZixifCcaA1rxyLFsYhvccDp/QgIPKe7ik6A0iiXTS/ybcAoOqIAfC4rdL1KqJU9Ip0K+ALGcRHbGeEEpISKD4PIi8+v7vXpi5vMjiXJ/oGIqv8wEaaSokLcgd/8gk8lqGGF11J2WWqTQrhej14heDs2TIV3Fy4lc0iEvDyZPNn+BKMPEiWqelFHM1A/c06H15ZVLH97H77tz5z4NZAiqYhoq4PH54+E5SArPIBTOrt3JuqnAZpsHaqhtBSkozwmGpbbKxdIpu8B2K8FU6VfeEYCoksGVUaxNTLsJ0mIiLkIdSc2SIHwaJFRETWc/kyEBoKvPqqnX4lL[[[[[[[I7pwgTFnqsfaePwZi0WcLVlPb
[C1euXHkiRPIqB+E4r6bMUIp7kRzcTGGR55ubiwoULgpTMRxB523jX4M2bN4X1uECUlJTAzc0NVVVVgqh4eXkJXWhZWVn3lBxL0Vp1NRsbkwdhUwFYc8niXYaFwNIs4FdMst6ermRxyXotEfhZrAGv+vfiy1lESy6XIzk5GWfOnBFEhx+n+0kNF6eLFy8KY+8s4e3lf1demVq0aBE2btwoSCUXVY5ZtHbs2IG0tDShMsZFy9/fXzjGfPn53ihAEARBEM8zVlZ//zp+8IsHfzJ8cXGxIBBHjhyBjBQ6nzk5+XAGSZao2wH8/8GEoJ4liHRIhbEk64+sGzFqsQLbO2lMi4Eqo6+ultLiTJex0x+hF2qLs882/+Srf+9ULJOakkHjci8UvPsyvn3iC604QNZBIvpVoyoVoXblbk6X9borvZF+pBT1F56PRlGeAeJRCKRfC4eS7SUJNcNcX3Az4oiWkKe4ktbic2pIC63koT8apIKa4dMXK5umfjiBOFBNel0P6QECJK1Ems4UklzXxob5oYQ29euz+Oheddnrd0ArczQE6xdcYigwi60AuDOG5ljmxWSmRqOePX+fD7SUZyiIjH31kpoG0dUQH76un3f4+c7l/TmPN2RQmhxGTV023GADKF1Ps8o36tu6d8dLk0p9RirOkhIznVrNraxotWTWYC/Nlb8jt3bsX3/ve90Rg3Y3bb79dGc7gunthlus6HG[[[[[[[[SUTrV[SUTrV[SUTrVI1YWiRh
[SUTrV+S4OWKqeViVqzcQuZNq4D9XL14yvGl+pavXIPGTRpTvZIOpUr9T8eGMnIeOgYs0XaKsrEHKLFWVLOyvEjHt85YGawidz0JPfBfRNCeY4iRffruGgSKAlgdPo5m0OpxrQ6iVYCcAU7/VaUlwXEhFLek4eIVI/zj8AH20M/QdPuD1+K1OEZEKKYVNGJ/0wx8YhVkpYycuF9uMXivJNlTQ1oed3U00FXoIEWqBPzQHrc6GrJYxbKz4UiSiMgk/BH6pi+9P7rp7P//TIkHnbjv7YRy0Zs4g01wX8UYJFHGF6OzpREmSGVpNFJobypAaoL/uujenEZ5khVGYxyqO0epTyxhfqQbeQkGAi/R2tGafMIMmLMsJX24P03Z0jTSJDWvIRMWyw8JNsl483UVquAJ+8iCEJ+bicK4bGfFmBPjLkVzR9UDZGMBCSkFjGzc47MX92nrXeD8ZIGCaH8SiNrmdShSbmUFNXR0NzG02tdeTnppOclEJheTUNuw+yc3Wfb0k5uahGtMjbDPRVE59RhXpqjNpcDrvaUkJcQRHmDlgYuO6pkj2qpKyUiIJtDyUfsoirr+BU7ffMf7d+/47s0uMcWj2GdaiPUTe8myQwz9WUyUTHoeOTJbsQZzARfvA3xZgO/mQ9VuTaJIoMEETEqvHu1AJfRjMWztxirTaaI7PRs0a/eb3ZKDakOoqxNJEL9rrmjC7uY3BCjckYYvtWmVZHoFtpfBpqq5rQD09qygtRWE2R11Q93BO9kkTjciopQosHcS4DvCykQP7MU50CujBTuv0cYslQkRQqqsPHv/HW9WO9AuAXa7gymlSk631earOohjl6+4dmzU14eyASfHEKEmqDXj3jGf/BhNRWn46gJkbCqgXdK0jYzS01jimPh0xQVmepFmeH2iiSKFn9a2gOPlYU6Ikmh8DE59By/Xd9Aa0EiUnKKUF5ejJLyCgwTgazKSkFKStSB
[image82]: <data:image/png;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
[image83]: <data:image/png;base64,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
[image84]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbAAAALvCAIAAACLHAfCAACAAElEQVR4XuydBXwTWf7AYe1u7393e34L7MICu8susrhLKXWcYsWKlgJF6u6upO7u7u7ubZo2qcXTNNVUNyx+/5lJ2oaklAJN09y97+f32Z08mZlMZ76892Yyb5E4ALAg2bB5xx+/2bjo623csXjJdv5YBMXShRRL3tjnWQVcZSscS5BlKPhXy73+yWBX//e2TyZi8b8nEvkrgnhn8J6GAMDCAAjxrQGEKLjgPQ0BgIXB/5wQpw3+lbPX/04hvq0uiJmD9zQEABYGQIhvldqshMhXC8Rsgvc0BAAWBrAQl2/kFQRbf/zBf2YLMeBd4lPbhwX/yuH1cxUAQpzb4D0NAYCFAUeI/KcsCCBEwQXvaQgALAyAEN8aQIiCC97TEABYGAAhvjWAEAUXvKchALAwAEJ8awAhCi54T0MAYGEAhPjWmELFo5T7md+e8x8wvRPZziPxPI3Iuv2mCfW1AJIBoJM5NtKWoKfp6BrX2JRmpHhE5o5TRgvfXGELbd9Y5YpdYTeBS4kSXeTKhzG6fXlAWht49W12qapmmSEv+VSMosl4PWGv+JYjQkRs6BsdnykL2Ehh/eTRhc3jhI3Vuts79iUcBE5BcSohIiFzL5HtWeSE7vnHu0HAL5C+L0hDgc9+qFuF400piSTHZ4ZcgnsL4w2gJqCgsyCrI1QnyglAt7yCjNtZWQfSzuWLtElLCQJwobvC1d3fwjs9F7iXtW6baBVS1FIYomQpbMRZFr6/Cz6im8hkULD5jUKruQs8HoMBZ80v2BDOl0tK4Hy50XGvRZ7QOqho1Q/2h4dY6z4x8d3mxyn8AEIUtQBCBAFiNaf0ij[[[[[[4qRmULzbx9lMlj5lt8ZZdDGXy7
[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
[image86]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAADvCAIAAACloe1SAACAAElEQVR4Xuy9Z3RVR7Yu6r9vvB933Pfeve/dMW7fc06f7nanc04n2+3udsSAwYAJJglEzjlnkBBRSCCUQQIJCRAiR5ERQRFFFFDOcW/tvFfOb85aW1sbgfuYvu1u467PZbH2WrUqzKqaX81aFd46fvz4unXrwsLC1qxZs2LFivXr12/atGnr1q2bN2/eREFBQUFB8Y+Bt06ePBkREfHw4cNsgidPnty9e/fevXsPKCgoKCgo/mHw1okTJ44dOyZJkmEYmqbpui7Lsk5BQUFBQfGPhLdSU1OPHz9u0qEgCKIowjU8UCkoKCgoKP5h8NbRo0eTkpLgyrQOAXA9mDQpKCgoKCi+1/DRoSzL/sFSRVHMCwoKCgoKin8QvJWRkXHq1CnTIhQEgXIhBQUFBcU/IN5KTExMTk42f/itQ0qKFBQUFB5ASZB+0K7RXUs0jISuZE0HnQ0iVDFg3gbu5MXxOP389v6KmzWp3C7hTgiqzmuwRGWvoxhXaFtEF8NiB2yE5has3TgvikKf2rNdJpCM+9jKAOImDSpOaHd5bmJ0VcpkLMz8u8kRh7taKoRCGSlZeiz2DyVcbLTKNQa41KHSIBlviEpvF8TUcwjHE61K9HWj8EylVcFRV4lwBAIjTQAXwNsm6Rf8WfhNSAmLwV48JPB+dAOIoIockg6tgn0UZ3XaglVkO4ZrHD+hIBfYOLmP0pfEyIylcPObze+1+ly3i8yZ4CRYrIyNvg7sAFRsPBmO+gM7msJM91v1CJMcmSkiE46KEbmOyrvWwGoIcLwFKV8MhgqWE/RdwzfDkTfgeFSt1k0MkzVVE7AMN9pDuv6g+sU8TfFt5Ynra8Z6mqWBimd9rDjjADisBZgXs70RMTnq1Oydt4oMHqiif3Za2ZMnj4mY+G0uZsuHT1kFiavqE4crM0mUwiFUSiiNxENM0Yd00xMDAwMyVF9WPL1ulmI5xMA4PRFUg1415FaD7kDAF1RDEk52y[[[[[[[AyLU[AyLU[AyLUYf8YArsJSWH
[AyLUXT2wlPkp+rYF6dgEFMv8VrfJctjUODVGkOZYk9WZDa1ba3W2bQz1mz3BxdQ1dtYQEv/HgT86TzecjDLLZMAWkGGnVO02CU5mQeXYT7rWFZ7t/BQUERi7InhCRGtUKWFRzha2b8YHhy6VV46GbBu86PnE8PTqhne6+MhnmVXSzuGJrFyJlYILwcQQXCFLQ8EBWFBojUNSdSG1hcQAS+qhJ3XYhNa2oqspMO12s7UlO1tKxE2aNnLBrT8hm/e0fWzX6XXv3fvzFZwP8fCxWc2Dg2g6dPpLqpyeRMwRuX8FHCEgU34DFGWSVRIpycLj5dobwhPyC4sM9x+sHDs9ol2/rxd8a2BEr8KzdXVFzcpiZumoPWLgyUx0W7y8G6l//z3TC5lCqpap5yC9+yNdeqKte2AF7ahi4qoNoXJtgVYuXKSQq[[[[[[DVJNGXYdppVVJ3jgVQBLtQo+os9
[LGtobKYZloED82iaB61v0dcAFgwTeKvD0jkuqrSBoMxQPk3E4cDjTGS2BIEYjA6eHYBMEFto3f5yLunrzzImzfb2D0fcebtnqce7CFa3RjDMN37cX9pXzrQsm2I2jEU3qcM7xsOHOu3n+23XeiL3zWs4SCXooKU8xtpkO0Hy0YWkoFqvYUx5GRKL/iK6kpabeLS9vbW87lnJ8+47tmzZtmvX6G7nXUds2lRReddvGSm8Wr14dv3TlinWbNgZRJIgi0NhJA95/LWNLRopOUUrFUeiyOGyQ3fffWd9Y+GhMe/wkD8YCUZx4CxDCInTPEGzBEHhGKFnJ0REkd04nNAQXq/FlAIiwiwLM7q+zD4reddf3YCLbusy40S5J49e/anpExOTIJiHD927OTJk2aZyP4xkihJBMEqZx4eT/vFj360aeWm1MikqA1Ymi5Xg9cwIHBNAAmxHm3duDooaGoFfpFiwwhKFsNhGyAE0VuLkCBAAI4DBFiLBhBQT8vaaIDCld1xhMxl4WJubyPNh5+fcke1s3W99ce+lP48X2pEvbt/tcjTh46J0op7309fO/h89Xn6zXcyr4PN8Us2ZN69Kr4vNBwQWq+ILWkC/RcnvZsfvNftjC2ZvCYPHOq2B5T2rbsIPdXoIFzd8L2pPz8f1auOHo9qUS5nZn/r9nUljR0eyZyuk6Fjk6TDFgS3oSGN6PhLUR4yie/2uZmRSCVBWX/uqJp8IDztcWV/3Xj5+MCYkaaO/73TO/CzwVVFNR29PV/9yfXjp6bPMIFNmBRiENQpaRyksIrcE0LFZaHmATcEUGA6dsWicwFFlDIZNp5MUoHkRRrMUnoqGYLhJEkldUeUBujBvTgi9AVobYnv9hCbISI1TB4DKBv2oRJ6UEOU9U3N4cctUQxQnzA9mkQBiqCqm8YwSLRJekaGTVstWDPQOaohKM6irLv/fX/+dwWs5w7zjU9yUkGI1czru4+aP3G+tq/DoZkOjk/RAYx7XrTMnnvzxD9xTMUUj0Uik8n7xmpXv2IaHystKlyx+a9euFBrAIU2PxMSoJMn0Fq6IYd9k0c2ruWcvToy5JUmlH/HRshGXBZp/GA1bzpylFwlyIGJj1XsLKjGz4RT
[image89]: <data:image/png;base64,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
[image90]: <data:image/png;base6mzdvBgbFgsTOsQC4X6FQeOrUqfXr16empQxFuT396waeOIRExrtUkpqX/+y1+BpVizxmT+m0XIiXUUhroTgGg97A6PUaVq8y6EmjUVL8ppRKZMMj4tq6+qjomJjde9QEXKPg+NCdMjPS3bRarrgt6zWyi5wfmSq8VXgyOWHoYR/lskfQRrNaVqAQ67X6yclJyAG8jSCg1EIxgMzCw3wnXnh1aupG8WSpNzHqmp3LPph+KOtI7OzFzavQkaGwsKP/8i//fPToYbJAxuBgf09n26KvF3L5UKjtkEwVwcsSJeuH5Z6m8cTooq+/SXjwi6Z47q/XMj1ky+jFITWD+XUsTE8LiDHLGkiqFR95C0iLnixTYhEkqL3VKqJgabxJmSIqHekUUD+V4D07ePsIVlc0WZZyNrXw4f9bXb/ehQDbNz+VlFISGzZxBMDNiXgQMHAhmARQMDBD4KGCA4+MnwElYg4zllYWDB+/FiQBQvmCYIAr/lwXf9i5BBT2S0uLvZ4PGxRD2Aps6mhsqK4ublRkBQ3Lq25yLWLQ5yJtc6Z965l19IfOz+kg//pRzeTepizKFHy5jmieTSBGEfXbkaFdXV2np1dWrV0GcKArdk4nwKMRUqkeoon09qkC0RKiUKPmFV6naE11hcsEPx+T+dPyqpyetgT0zcfV/Tih4bkLa2UvDg3KmTWyIjg9YHxe/YeTX1xq3bd/cdSbyAKiD2y4smU8g9/nJSSDlxptOxRT2qKKK1mv
[image91]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAItCAIAAABuHkPEAACAAElEQVR4Xuy9B3Rc15Ulyu72LI+n/XvaM+PuGf9x/7basiXbsixZrWBbWVZiJkWKOQeQBEiACCRyInIgMgmQABhABAYwAyRBACRA5JxzBgqFylWoQmXg73cPqlQESYhSt2V1++31Vq1Xr+6799x09tn3hVoglcs02qnpmRmjaRqbaWZGPz2tNZuNMzOG2W3ayDbzjMk8YzTPGLBNf3WYsc0g/9ncnnozo9wZmGM2YJvGNmMwzRiMbDNYNuOsVTCWbVxiE4o0T8+wbbZcw4zRegrbjMYZEzZLsnk2znib7YumsGb5Bh2ruUzspHhrYsHLlhs9WX8q+2N09WlxXSQIE2pS1vLkqdGeqBH2iT8ohlCwPz6jIGmP0Z5+tXr06OfnEK79+9Sf/77O//c0b69ZsB+E+omhrCajy9x7POxT+9tIKewWTq0+YVRdEjc1561xt5D+eb8RqzdavS7aEzLaCtd+KbJlMs2P/4RQ3oqh+MCLuJrMIRcQEBC4+vGloEOD+Wrt+1j2kI/7gBz/Yt2+fs7PzdSsaGxsPHz5cXU3eSnkd5oCbdIxao1MynJbOmsqTpTJkvKjYZTqkBduT6NDOh+Ijj13vOwYTaxay+nZlflFjiXT1jZ2tVrBCElz7nccNfYy4tSTp3cGbhcWHE1IS56hy418/W1waFBPr4eSOcLAbStwwOD5WXnr3U1AnQJPZQzZOng72mxgoDyzHYSbAUn6ECrRByVg6LHevs7KqJDfveuctRIdzC/MRkRFAfmERwf4byrEhwsmahl/IIRfM3YKgQUR7W24ieACEsrkUfUuR21/n37denUmduIm0Y++fiY4sKy/NziV8aai09OJRqOpI4lJJqquJki7Q1ZFimTQuBuxLy0YzSwzlV0d17LKzdZvcN9+AqJ1QVQpBD1CbWhYnWHTxcOrIHOJqjAXcQiLEoGl6qzuctB1FnqQtt1WXyRKY25qKsrrqmtqycnNFMdDWyd+uh3JK30kZprlRozjkZL35UhOgR12NJan1+QvXXbpqtUWXp1eXFxAVwivzAvOzcHoMgryFUUZGXn5RelT
[image92]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAJJCAIAAAD9ew6IAACAAElEQVR4XuydB4AURd72V0SUtJEkGMBEzqAEMZ8nZg8zGURPPSOSRAFBJOecc87sEpZll81xdnYn74SdnPNM51hfdfeyrqD3nfe+r+fpPD42Pd3V1T091fXrf3VVbxILAELgOEkwHMsDAM3CGZ7nOA5OARAX/ZJ/lWB6BgAKABr+B3AAUMBjAO6JB3DPDAcYhqRJhKfjPIsAjgI8y/CABILhVgTcgAM4J+UAaB7QLEMzwgGLFsSJu6DFxHDKww2iJG8nWBPJGAGwAFYFyCpAVgC6CrDQMsBWAx66FoBawKsAr+D5ap6rAEAGQDWBFgPeADhDPKIIBxSAj/B8nIPHwdHC/nlAwQMUpwzPCbuEazk8hgZiRAShUQywMY4OsYQbi+I8E2NxhEUJFuMBjmPBkN8GTwPN4Sz85oAmWYLkCJqnWEDDL0lQcYKMwtx4nkCxEEXHeB5jmBiC+OEZYVic5Uhht4BhOSqORjAiDudxEqFonOrNlOBCYQusHDSIEgmqKUE7qmC2pA2036LXEoBziiz3+fMW3jHbt59AE6Bczdw7eIcu2nHAW3IsaQgvSz8Kw5JFngLGmMAEXmKxyCUBzciw9oeHmpvcd+4S8ZuVn3xa+0KX1rc+hr4b67l8X1OS7a/9qb3n86rX/qDu8Qdt9z9aX+0CdX3Z2OUF/SvPq1/6o/qV5zu6PN/e9U8d3V/s6PFS+2uviOrxiqp7l06pX31V0627tutrui5Ar3u3Pf8qcLzr609sO4/0fBSzazdd167itls37/4T6tb1kbwR9F6BaNpu4KSvdPR4GeRBVPcu7d27tXd/tb17j/bur7V3AlmbwTLwGw4FG5C+DbA7ZAIsQ9bBGSF/gFhis3Drrht56Ou8/6GtKDtRKQpPeLKDDWfDrjO+BJrwV65/UJE8es37Bq4cIFgwcNeeqpZ772tbuPsntFJNiAxST4wQxfVwwKwrjyyc7erd3fHXl9CgcVgyZrTF5NAbkawsMqw/jrnhiUrun3S5a1B56Q0vm/HrqXzF85Nm1lZURsMRCPhRFVl3Zz4rJf6nbX9oEgZxOJBHjEM2fOHDx48MiRI5mZmARXGDHdCGiGT9V9qhbR9Zhhxg0zqhlhWDZNyx4qJ19NwwSeYmmQziqceLeH6epJP5Owf8v2Wd/OUAptMEyT8okI/bhENpJkEACoiw6Eg3tPxaMxL+O7ScA3d6BM4iUBrZaZK5zuunUod//MnoQqxlMwQwHKw8RrEWr1btKStzHsswhsxqeeSRzpOgudjsoLhAfwF0VMVNrbKF93WczXO5RSII1OZ30GWSDDUOD+iKEiCV0LflEpPUL9l6N8NZwOpbMof3PTIAqZUrrGIAtVUFKJ8g04EwJ6CfnZxtzcbxZdhVEenz9J7UpfFbDbafQLEczfA0J+OiH5MDuJ+HDSwlPyOEKU7B21ku7LWpZw6rW9YGXhpJXnsTk9hCSEjiEhPyBA3z2vu7dLnnni6fzvs8vzDPVW3+5OUxI5/R1Y2HXPu1ne7jv8Uc/6byDPf0y6t3EfQUmo4mT+7FHzGbMAOuYidi1h5iIWHmOCr6hEdV6xkXQ0mQ6h2uRwOl83mMOtdeqWjLF+FpDScO+pI0Pn3wZN7dHCIiW2vbsUOHf/aPz4wdNfbgvXCZKFKrP1T1KxLcBFf26+770dC/6hCZi8g7gP7Dty5mxy+q2y8qKk5IQrVxJycwrdLsi7M/4gv/c+HTpywtnLNwrKGnmomAASkGzDXF1HVvXScIPOP8DkZowekzffoOu3M4vtwY4/YGPlgNPDyjHkUiaMqUqc5WIE7+qChjFOuOcBjCOBQVYHwczMvJQ8PbNm9auWB8w/8zR/RHbt8741StcDZ3vg01bg6trmuvqW8vKq0/HJy1auGRncKh41tQ
[image93]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAADxCAYAAAATHxnuAACAAElEQVR4Xuy9B3xbx5m3+/1+9+6399vy3a3f3Ww2seOWbJqTOHHiFK9tucmSbBWr92I1qjeqkmokJVFdonolJZLqjWqURLH33nvvBAtAgCBAAM+dOSAlkqaSWBY3TjxPMoYIHJx55513Zv5nZs7B/7Db7XR0dGCz2ZD/VkkllVRSSSWVVFLpiyWpo7rrqS7+R1paGjt37iQkJIUygUij8eS3s7jY2NlJSUiFRKS7NzGVHboC/YEUCHhSQ2y7i5vcILWwmqpIucNzNhTlDhjBxdN8fUidry4GPlgz7EFmPlg/l551LiCSPgpri49sF5hMmMdf+FDZny7s8YxfQmmmn5NFS0kte++XgprLBd1tzPZUpISSGLGfeZANWLhF6IkDKfh23LiwhAwtSmkpldD66QeYnn1BbLxeg0kEjth1
[image94]: <data:image/png;base64,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
[image95]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfcAAAD8CAIAAADlp3oHAACAAElEQVR4XuydB3bd3drnudrvbut23ejy3JCQ083ohoG5iYo2ZNXTPTjml/I/9z+8Z66c8H8UbKT/MT/lBZ7Y0R23P4Un50eE5ydoKu0UYYEMI2mvsYe8QGlN/9h/z6258NkI569aM2H56hMffvOEh9486t6Xh25BG[[[[[[[PHv2[PHv2[PHv2[PHv2BIdBGz
[PHv2xPf/rTY8eOQTehktB65kE07l0e3TSlzZgxY2Dh9wRhVR5x0GEQR3b8A/abD2ZFi0V3mTLdunVjktjY2HLlytGOODt27EAAOdy/fMQxSXbp0KRCi8nPmzOGQjKoF3kTlUS9jt25jn3bc[[[[[[[Dx+eBD/s17/+ddFyabhuyHps4Fr
[G0cEf6GSxaxflvI40IjyI/m9ypDbXUyH5wdoyGssPti7Aahq1OTi9wD9eHZJNEvEQY9y4SWYIkPzXfyQhtLhnv9tx4bXWuuzjVnupkTWJ0rTEtT9Vz6S8338R7TzqbN8d3762vNk/uXBhbsEreqlOKjYqKItWJhW2dgLXfXD+B5eAqOgjIPiEQiPsUToOaeSsktJCyuxqwi7GrNqaGDAI+1/VBcTXChULmoWNPwDTQzv5Ae6DflMjLBwPwZjKUB6ZXj3Wq7A4AQ9QiyGTcBQyHrh4IGjbSav+5pv5uU143zduG83VgvMPiArdC9YmFOzimdjVpDkAqoKdImUkiWgZOmGaWpCVpE7TiAV0oHgKjy8wL+9jUIg+reCWz5e9MfI7p/N7p85SVZfnOXb0IwE8bvASiLzx4CTdsAAC/338DKN5/lXvwCt6gq9RmSLQ51p2Zss051VGPKmTlO/S0QTUFpF0Kr/bwfxesvfVmye3AH+1CPtWZ4+1Pp9y7evPoTip+6KMmNxZizJjCTZkTQ3kuYHL+lLZyyvKAyR0HVGdUsp2qyKeosan5oQHEMvCGbVpGAA4rPD0+XrvtH6wCTDUaY3r92zb/OREw1Gp9rqm9jSsg2hoGHwVDAD4gUMzOieMpUjiZHqM3ntBSwmh+e4HeZaeJyBr3bzyQ3d23af3Q4/v1MuF6ungXccTKbtpMlU8TA8AMFKzkWGVsvmtSL6Frhh7k+hRbxzRaCVLl7rAcUD8NseDho1qlxDWZ4GpJMoyBoZWS2bUEmZOtmETcs2QN9DysynQ7/grqyuqNEZtPjCjhDiBAUi3gjiCyGReCIQRd3rfGDqvq8qlxlBQd50bosAwwjdGSPdFySXjY1FxCN+uig0j+oDA8rg6Py4KiCHVTRgwa6gnvLbHyE107QuWzF6ByM304AC0IHJ8FbkUUrtEBJ8lZnNsqhsYLPMimFDq3UKGYbRGz4SMAkt0Ng/DTPdHLnDvBpK9OcS/5X36Yr/DUdZU2lryu8kZj+Ycnj3+YpHft28ON7w7K3+5Vv9mrAN8/HCLip5HTodFzNcugS78S5tBPEzKa+2lGYCeq7hMl3FafO1kDslMxOu9lhM5HObqsRCmyJ025xO2wuye6ZFWGFxAGEAKyCOVysClMIVFOJhGMNlJPKdCUfUJ1Wo
[image98]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV0AAALvCAIAAABJAIEDAAA/QUlEQVR4Xu3dB3xUVd7/8UNLJnRCCKEjHRWkumBvVAUBRVXEQCMXAGjkAgCNXACgkQsANHIBgEYuANDIBsQyuO[[[[[[[coNazidsV5b2WO7PLbSCES+tN4
[IbcyeuJJy+vZs2fjI+KfvSUIcUpMTAyRTOLAIhlHOeUL9+/ZkzZ54+fZppu5/zEOzDPmzdunX1yurBNtiCjIaINafYzc6dO5NZmFOkIaQMWIbpFa63xwJ/4rISHBASHy6dOlCfvRLEP437QvRvIHW+vU7evRou3bt+OgmJ2LAkC5Z4wLnc8koXvODGeXIkaOwIAj2gaurq3WI2mB3MmqqaQd1G89Ej1qxZ06FDB3p48ODBUaNGiYyEMMUnymjVX906TD7m//TuxundOnZr17v/+OnTp06a3r9Fo/G791/Ys3PuqIHNeg9Yduq+v/+rayun9Orco//MBccf+b967n95/h+N/piy6uDxJ/7+T++9PL9l+huG9G7Vqd+Q+RtuKBnVHbbkyMEbz/39b9w4u/zN0x1/X33w0v/JMb8VY7t7N+s6evo0Cg3t0n3krNps7rvv3D68e/fuxxxzzLHHHtu7d283dHp3Hde5c+d8S8k4FJgaNENmbUaGu/KjeGfEZgRy6N1y3rJlC5oRgnz77bf8ReEofa+XSgYxSgh40SKX7wiTc69bty71UZxIL9M++2jOlM2b+5bv6rXm015rdhc+eq/ZddWG111X0mbUrXPllx5Zg6mHK8yqWDb1oBnH0GtGJ5btuPCRj2dX7F317pdr3vsKx9PvIFx
[image100]: <data:image/png;base6z08GrbRIF9YpVKCU6/ToZ/Pn1crFPXva2qfHyB0NKkZV0bu602m80y5QjKDZ24rJn3pSWWJzHvBcYvmll1gDJKyhsi7c3262fMpVl5dbAV5fe2ReUHWuclrcdqmS229zIhMQo9+QyPSMlsIaAEYdsvF1Y+Ac38bFFH28L4kmOLH3ghvPhRERMAV2+W+evyLAaT7hW4kNhS3XPBXnag48j1sqWu0IEmlSYqBXUP0sFq6k7qOAeDTGZKU1kiO0U+L03gqS+3MoRaaUoVR6hlyzwuUVjAAQ8Hqs07C8xkqpi3nF7Ul84ERNt9g3SnrN3Jlo7c+izcEuPsKOupvFlbjwpRCFo6gZoyEwNUBI53X+ML0puxL7rEEfCHwVMteuNEqnQNqDlsTTkOG0OT4WRZFRtHqzvv13SdDSvdtRJrGBgMmvF2LbmuJxmZ0p3HwbmnLKWlue6ymfUvLlcahe1v2nPAN9owbil/xGuuADKKsDoAQQKeiG4gpTiyBxcuZ0nWNbJJu5lEmUcCcUXkyLExpc6mLJSBuKBKjEACC8xBceVt+562L//2dyJj0eXnmxQ6tVlgIl/FtMPXo5e791Y2DQ0ey8+1dfYeejg2Q/HDz28uMHc4W+eDVSDeQ4CjdI3dC5vKJ+WhQAK4CdLdTUb6oamqWxdI/f8TeNeteMHrr+1YbBK1tHruereJmsa88sqho2+VlK9LUZtki0O7T7yn1HtSFBSQElScGvdGVralo233rXPv/Ovl9/5boad7bkr4xpDJl8Il0+oXZ/qXazRE0FEkE9Sr19RVo6D2gFiEiFwSDWM0a4mWWGuoA6MkgJQ7BcUg+QeAgHMjxN3sjHQ42wcGj39LF5RFYVXRSjMfLlx8MynuTKTA799He018MHn2KbOeYDLdQabGsP9R75OG2IjlqjcNH33rne//j6t2frZZbyPVFzgHYULKuoNBv5ZXbOKqjKvSang5tVypSVW6Vdu43945k29jcb6G8v8/e28ZHVeSZosms9hiJZw8ySlmtBl1L3PAGtPA9rz8ciyM4DZQhGYyqiWyLbhIO4cViGnq5w/vvlk//x6dU4pj6oscS+MnPwiTmCErrRNuRKc7LyJ2oG3+o6dKtu92zV0Mk11gaIitYz8q/IW5ToWOduczeM5jdMrM5qXx5TwJWbuQKywCRH77/h7r9q/qS/pYD55NUTeHpNQ0DF5M0Mv6Xo6dkW3JjwuTTQ6tfvn5j0fnP5oZOZ0QIW2fC
[image101]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfcAAAFfCAIAAADcWBLzAACAAElEQVR4Xux9B1hTSfd+Gkmo0jvpCd2uiChKLwkJqYTekSJNmigqKsWColix996xFxSw995d26q7doGQHv4zwd11Zdfd/367+/2e5+P4PpfJ3Gl37tz3nDl35op4/Pjx7t27d2hl586du74pmzdvBskaGhr27Nmzs0d6pEd6pEf+zwuiqKgIoRWkVrrCvydoNBocUSjUH6bskR7pkR7pkf8TUlxcjNDSNxDUHwleK7q6ulgsFofDYXukR3qkR3rk/7ZAWx4Y5l0sD6TLov89sbW1HTt27NmzZ09r5UyP9EiP9EiP/N8WRGFhYReDA4rHYDBfm/q/Fisrq0WLFqnVaoVCAY6aHumRHumRHvm/Lb/45VEo1K8p/TfEzMxs+fLlIJtKpQLHzi8E/FR/U76s9cuMPdIjPdIjPfLPyd/J8n9SuUabo/uclX24L+AP2J55K9+WZiarFxW3wm/JiTkvkxdvufy3gs/6pACMXZ+OmA6TxXqUMU64BZr4zbpc0byE472ngB9IEp+IxT+JDH5O578O1nJ+dOdyw9NnH89wzp/pmfx3NXHOpcemL1scvbnWMz4NnQxCO8cgFYz6KcloHxuy0rTjK1DqbBAVP1TjidClIdnD5+VgIHlXFWtBglh+HCjCZ8rgdnToAhVYRDsF2kq+qoynt3O0lQIi8dHiLuQ3aVX5mrbF0SYa9J6dyET23Wkhb0R+ppepvljLWHMmXQLN6Fy5OL10ZmzkTKaqgYYabgyl0A6CmKj9GfDwNGmoVP8JFemvj/PvoMuMQMjxkwbIZXGMXZpWJ0KQTyxIMKRWxQUFmuVA9U6QrQYvW3ADNVUtMbpmxTGlyiLWepFE1Ms6LZvR6RwJIK61dzvkkCImF+BBSfbmYdeFnIv5bEP/1lfELtCCwXDI92rnQUDutv/dWH3/HRmysAQbE2olKbrpCHxJrwsqCKnm+V6QuT2BhnXNmTpo9xd2Wrg9LiJmiYtwsg0G2QSwbmmxaWaMnjRkT2/AY37sOWXW/6BR985UGkd1EI9nl+dusVBIdRo2dX2HVVb7m/+v+TCVYgfKdJ/IKj1X+l0EvlfJCsYCKIw8TLyLyWjtu[[[[[[Whc6GNnpFzPQDg7/GMlI/c9JX7w
[NHzcwZc04cP7Nm9YbDh46/ef2+e+cOOWe/FlVzy9epX8f8OH9N0jdTv5f0dcy/IupjQNZQpApocNR0YGthCiVQEtghEEkXRLq07gvzHbJWH2oAuv8m6s/3QWzsnr40c+cHmxFJff1FIxlg73DAF1S+RxtMwcSudb2EIgIJsYKFGNq5PgoLe62GqKjdURiIuZmFGNl/DQoDAkNNEKry0775Eec5LxOuFGI1jkLJGCW2TgK2XUJBXukSlJCJ7pBZg0SbATCs3b/sH4Fea3FVS1oOE4ER3G8qP2oavV687ve3Im4uNzZTKyhO5IEV1dFGI2By7MbF4I79lwTMoCS74gJkNx4ximTmS6upsyGHMLVYusxPVBEkKd/Al3dMXE4rG5Yk7yxWiiHXt6haWaEZBXsnJ9YvLX46q+VmR2b43N67N0CzUMzEDm61m4kY3rmSIVXahgoAqmUEFHwHaEj82hgxiN6KmSHW6lCPQB62NhAqCfFGOniQ8e2SKFGgIUwKnk0hAV9Doi4BoNkKgD0zIQNZH9qWX53gCpfkOcNVpZEyzXpZr6ZDvr18ksQa7Bl0J7Kmrtm3u9tudIEKpcF1+0fP3bzRMnRgLIwNup9jibTjJ7W6sbj23PDogYs7n7RIZlyNz/ml1HG8cKauf2eseKfKPbs0JiFTv5WJ0wmG5ynbj9iHLbcaLI7EIZq/CJdZ6JGow1QZw+CQa6HflQbgW3/L4GpT/NSVURqH8Lz795LNffPq7yOgfS25CRPlx28oiNc5otWNjqn9Dmh+R6pgJX8RW7/JLzASnj0gXp2xN1nfmNS7Onv8gICZ3Jn51KwS2Sr/mNyqkesVA5caxq/XDl9smbhU2nvWXl6iL5kameoTpxWMrT2Ztvc3cy80YCYPCSplQJcVusc1zoEd+u7NqbUS3aQwp40rKCYya7G+t3eTBa5kw+7epcfM2OxQWenk4QdJuQ333v+NNTOKlvDfEScjiU2hsaV7Zo9ExOn5YpVcer/+sxF0QXzHb6cCm9mqS+/EhY+jFB5hRV4IWofuNt4Tp26MUTfS4syeF8JwwfbiWWgpjTXTb+UywR0RkEQPOsQNyuAFZwhCskBL4ak7K2YTWTpK/iQ3ZRmKZbWdNcyYyJWL1ZVdh1ZPy2+/Nqkn1gaomRjopYH9WPglkdTQNBQrqOjHsEqjkzqDxxgbGTYlVLLkxQOngyD0UsYGrsPPldr7IAXRZ0PiYGedzJEsANhoUqBniUFU8sChwADjXfTsemk7n6hO5NfAcy5d3gseIcEtp6hQ4f39YpdACx5b[[[[[[[[[[[[[6GkzFGLVM6WlF0xoWUsj
[cJSmLOWwxeMH6BRMdUL6qGqSte1NRW442BdVWVpe/+O1BxoFtd+/c/uOPP0DVTZs2DSLm5OR89913gKRv3ryByYRFIVng2GJyyxLKivJWs9H+BCN9+++2xY8emT58+YMAA9rQaDSxcz11Ey1x2TN+cHT1mQGRU9z9hlhx5VgwOuR1hhUdfq9ig5nZvnw9GXjFxpmL8Wry1asejO6xvPv7atE37O9rvnzz0Bso/+eVPfzY9Pm6ZUfpKdldU//JwQWVvvzAsuhPPWVVVmVVVmV/28FcdstQMrPjiWo7YDPNFhQYa9C0cfuE5MmV7242G7wFyj8SCtLDMs+A5T3kZqlmRWHb7xva5zJLNpTN7KszmkbOnBle2pOdGbhyt3vK3O6Fq8+Glu8P3HihfzWwzHaBn3FhC+R7WAOP8QZHXDx37UwfciZL1EESeN4J733zjr5EDczhx4JfgcTTqs2BPl7Ku4LlgZ6KTqp3tZetg80G11pocC6RhpT974riQftc/wy4ltmkKWs7RQ7Ml9WNNZ/+G3J9rI9p96Pklf7JebFqhuCMqr7Dz3KbV7gxuS5sjIYHDmdo8LSa0Ni0UhjjzZvryClsnHidkBiBTsyl5tZkVM6zZLq1weaFWX7c9r3i1PtWdaB2KxOS9nsqZs/YoZrNvmp/dLqGiZvbwo2+UY6TJWT3Ah72+jlxsGzraMX28YvBm4vdBfI0+z9UeqWdQIVK9JR03/FTRFaqyEQToPFMI2xNRmKJiO4LFayMTkIzzs8PZu647RtDMhCbHiB8kLdlqiiMF2PvnJ2i7aTsTKGRLgduZaWvM9Di7XSxlSLU02XZNGkWk6tgP25+KgP/asSlXaEYjOnx8O1cdQNssgYlEf1CMHYbgvCGAvin8rHQANYMwVb2+10oEsQ2ySOszGOSQ+BuGX5Hc0j90s9Ix1j19pH7zQsnt57uk8GQQ5caKCIdR+lDN0d8zvyIyz/c+Xxs6/LxSfuN4cS1gEQq/DJyXxu7SdykwKQZJjOacGEbNkR0NNX5ajzcRQkDIhBeutIT/mq62MFV+JjYD0X6OkkdfIUXWQg2ygALcUMwZqfpFd+jaxHz22pVgpUb14UciI[[[[[[[V[V[V[V[V[V[Vv[Vv[Vv[Vv[Vv[Vv[VvJ[VvJ[VvJ[VvJSg3BkaM5uEA
[VvJLB7sT1z50p7Hrs/VK4TUeq6Ww0WMDOEMpYEQ2VImcrzrMaHrKaHnHqbzNq7rN33NrUdilwQy5LkspW6HlKMNMsTELPkhm5AOsE9hRjizU0r4KGr4TlbWPBvJTbkM1AhnxSYNmxJDkChYm9Mh3MMa7Mwlc4RSoPH2BrTQ5HbhYAZq3J4cJ0pxw8uYVP2YURblh4QrWLLTNzSVi0Oj5pQUYRuZFPmtmEgSc3cgisx+HKjWypnk0YWVisaGWFw/Kz0QkJDrqWnUZUPowHl5SgoDL4Ye9rl/RVgo9wS3fKXKLv4KeV27Rr5jJvY3mMpHlw+U12ultbPXX41k+2nw4CLAAgZcGDBiNRGTE3nwv7hQsJD0wAF48SsoqJuI6MmYnIKp8Ws0+BALBdPSBZoqPrfrrwYqYpB4uJD+GdEJPoQ3zD3XMM5uiZHVtBMNpMXa0/0TxSt3mphSjzaoQoCbaYhKStIuSBKKM0RlJabwhBKghUjZY/O8Juqk3uRbDMxPRbqX/UDNkEVraMKx28gJForQvL/akXu0z3Ls[[[[[[qhWA[qhWAYZDQXDz9DFgLAc/04
[qhWAYZDQXDz9DFgLAd5bwTioeajGrjyCDhVe14Zvqc52BZlKe0SgSvxXP+ZMyT89rF42i9wFZmXbVJ+vza2wFnWltqdPotUvfYQDupYb6GShHVgVWe9fnpHtF8+bqFjVxE5evq+nmi+I7KK/k3V1fIq0P81bWg50FpcRk3QKh6rE38QPJnTj8vY3K5khEUFJQvikOovIdXVGJK/mNVqHZqBu+IyRSsLG1sldEyr4NQ1tjGZ4cDzPrm1tzIq/YuwRUws+M//2vlzUpuJPWSbgF74+Obd59Wx/kACN1woq9tbE3yMVIUXIYTllT5prX1WG9hknIYSZV3pHZVFhZfVdvtOQGYFfOW5nYFUVBQvkwOpfJf7t3XLwrRWH5vHAUFBeVfD6ry/3wsIqgP9wRRUFBQ/i38uSoPgNB5FcJx2d3xfztH5Qnn1cRPeKKgoKB8wxxO5c/rhqk6JWk5IBMcd5oAcQ80xZduLxqI70YCyn7nlLCAg[[[[[[[[d[d[d[d[d[d[df[df[df[df[df[df[[[[[[XH+R6
[dfPbf8x8h6XjP3VDVNi
[LG0cV+jG8VnK6kaFi/qLc2cgKigHoAcFr0JH87r5ZCeQHLldVtVxuebHdAXvr54xl663ZXe8RA1S9BNO0HaoCB66L10vKvEGxPgu1xoNJNXr2xBI82uAqymGEy7HP0smmycmIAmIj7UH+a9TPTlSKjWX1[[[[[[[i[i[i[i[i[i[iD[iD[iD[iD[iD[iD[iDP[iDP[iDP[iDP[iDP[iDPo002+fr66
[[[[[[[s[s[s[s[s[s[sm[sm[sm[sm[sm[sm[smOcjdGonfwLqa71V6a
[smOcjdGonf1xtYRlVTiiKAhFzA1PIEvrXe+jAZWH6LYLSWnrHVbcy30l7vrV7Pg68KuUGqXHP/mu+kCIUob9Ir1p6hbf66glke46NzOiz/y19KvvMddBTjmDiblgdlszVwDeTyoz2bPSFrhAFRTfGavYKooWKLAVt+aygDMvp8rbUNyeW35yY24m5Ic/nRra4IodnnayWt6zF3NoZL1oJ+uZ7alFtIj+8jfE[[[[[[[[Y[Y[Y[Y[Y[Y[YA[YA[YA[YA[YAM9q35poMKwcnA
[YAsXecNzpAv8zV2uc7FHzVwQkXcc/wln9MEB0kbWtp4LPmkebjvlyf5noUHlHzVcMBEEtX0kYWMwQGbCXshFh+hPLhKK9Vru3QUfDWG80BHp8PzChgyMymevBTKxFJK1ovHWsfdSFP5immKgw88P6u1LIQm<<<<<<<<
</details>
</details>

<details>
<summary>
FICHES
</summary>
</details>
























