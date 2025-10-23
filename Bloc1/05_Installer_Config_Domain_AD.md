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

![][image1]

Ici se trouve l'assistant d'ajout de rôles et de fonctionnalités. Il faut lire les informations avant de commencer l'installation. Puis, cliquez sur « ***Suivant*** ».

### ***Exemple***

###     **Assistant d'installation**

**![][image2]**

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

![][image25]

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

![][image65]

### ***Remarque***

Vous pouvez constater la progression de l'installation du serveur de sauvegarde. Il est possible de fermer l'assistant sans interrompre les tâches en cours.

### ***Exemple*****Progression de l'installation**

**![][image66]**

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

![][image74]

![][image75]

**Étape 5 :** dans la capture ci-dessous, on peut constater que le dossier « ***Sauvegarde*** » a bien été partagé. Cliquez sur « ***Terminé*** ».

![][image76]

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

![][image83]

**Suppression d'un objet d'Active Directory:**

Malgré les nombreuses précautions et contrôles qui sont pris pour les éviter, des suppressions ou des modifications accidentelles peuvent toujours se produire. Selon le type de modification apportée, cela peut affecter un seul utilisateur, par exemple en empêchant l'utilisateur de se connecter ou d'accéder à un fichier, ou cela peut affecter un contrôleur de domaine (DC) et affecter de nombreux, voire tous les utilisateurs.

Ces types d'incidents perturbent souvent des processus commerciaux importants. Cependant, des modifications non autorisées, même minimes, peuvent nuire à la productivité de votre organisation. S'ils ne sont pas corrigés, ces changements involontaires peuvent paralyser l'ensemble de votre organisation.

Nous allons montrer comment supprimer un objet de l'AD et nous verrons également comment le restaurer.

Après avoir supprimé un objet dans Active Directory (un utilisateur, un groupe, un ordinateur ou une unité d'organisation), vous pouvez le restaurer.

Pour commencer, avant de restaurer un annuaire Active Directory, nous allons déjà supprimer un objet de l'Active Directory.

### ***Méthode***

###     **Découvrez comment supprimer un objet d'un annuaire Active Directory**

**Étape 1** : rendez-vous dans le « ***Gestionnaire de serveur*** », allez ensuite sur « ***Outils*** » puis cliquez sur « ***Utilisateurs et ordinateurs Active Directory*** ».

![][image84]

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

![][image91]

**Étape 7** : désormais, il sera possible de supprimer l'objet sans encombre.

Faites de nouveau un clic droit sur le dossier « ***SMOG*** », puis cliquez sur « ***Supprimer*** ».

Encore une fois, le message pour valider la suppression du dossier des services de domaine Active Directory s'affiche. Cliquez sur « ***Oui*** ».

![][image92]

![][image93]

Le dossier SMOG a bien disparu. Cela signifie donc que la désactivation contre la protection de suppression accidentelle a bien fonctionné.

### ***Exemple***

###     **Dossier SMOG supprimé de l'Active Directory**

**![][image94]**

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

![][image95]

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

![][image101]

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
</details>
 
<details>
<summary>
.
 </summary>
[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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[[[[[[[ITqa[ITqa[ITqa[ITqae19TN5
[ITqa0tZ+9WTa3vdpacCWvaaboi0MipdY7OY6FAzQyRYT6sqXjY1oiaO9bhNezRPUdHQHooNPrKD8pMxmPReCKe+H5+HffVyUmHoIKkF1B6tmH2hSRJzlooUfv3k1Gkc9495krZh7jVCKzrFNh0vQ3nj+ZGBN6KL5qlIdI5FxWSV5KaGRsBoFtdNstA5dyQt8PyzjTqZ0zIjoUCBTYvr7e6qyYwjapin4+PSE0NKmGxEFyR0xVVmhoQit1uae3fzegQwAANgLocHFL6DAiLi7rVK1Eway+1KuzeV0Luo7GBr6IW37qNF1j9ZrGy+soFsFwfTN1uc+SpexQOVQ9wLNMIQmi207vaRmgc+vPlIywtV6bqLqyx+Lln0k8xTZ5zWpeWyt26fUTTktfT6tIrEB1yFcMdHXJNBaja56OH2Qpkn2/uypxG0ffwNDVD/F+noJDSn5bKWqd0TVMwQAbxyWfnuRKTUuf7Hoqdtp8XQUAADYE6DBgbyPk94AqP1VfLMqn4PHvTlndzcW7U2K5svY0NHT2zvbcXnDJ2rq8VuLhXt/eWd1Ba0540zbjnno[[[[[[9cYM/4cP7vsEe/mFNW5sUZJ874
[lBuckD17f5e3WPFmcu/vZx19fA9Lkidrjl7C7Ex7+6w3JlvcVM23XG/om9g51FX27HVak0opIX3q+XRFhM1hxFM0m4uvbL3SYU1O2ZfTbjJZQ0mkiKYD/mg46EfyhZDLFkfyEZ9dozNEUtlU2AMq9EXS5YYSQZdOq98idB+Y4pmYT6vVgqrKWWgmrtdp+buraDZh0GiMVlc2X4gFfC6H1eoKeB0mo8WTQ1G/06TRGkIJJBULxDO5YMDtMOktrmChiEa9DpAVKYsOTZCnB/r7pp3YPQgLTrPGYLHr+Out/TP+aDzo8/u9PiRfzMSD0XQ+7LFq9KZo6ZjwLoA6rD4unQ7zsbA3Go165eu7ahN/W2DyITlsstToVuywVCAnmc7qDtZpYVHstUyHkdFr3Bns4XkmEvSLe6g0giHEtjNBxPV+yslSIiPr/V6ZZSkUK/fVdLp4u9Wl4hoMHkiXf+/e8qz1wsOMwSSM6h4Kl89fWahyMdGf6RM9iSfiuAniH60oVypdZuNz3XhwtLjGS19YqtQa5k4wp5MtoojX/u8Agpl7+TSEYoJqAor9vY1OVvtADpUWF1Li3C1Wh0KuulIjMEVLinZ8SiG3X9tRUcZs7XDMztNfPqGKZYvTkwI+XDr[[[[[[[DzaB[DzaB[DzaB[DzaBgUm5JK
[DzaBQhqhM/C6sqOWfj6qwrQ9AMXe5Z9iXbDqWB9B8+soPpj547by8iRlfAFYoyhR1+7Ogq1PnpPNUnAPnVfOSVN8ecbCRUTBGtAtVJ/72WP/vs4Iv5XP5zPucNAK402dzNDwYk9wBGGc2eRiHIy+eNpSbeejOsGTgqiSMpmMXde90IkHOKicC/pB4JSWriF2f9gXxqsVXn+ZjbtrB8dWUq+TTXj5PVqjd94X4KkA6fNtomA5z2WQwAJJInY+Kz/r9znAanFb/RcIeTyRdSqcusl6SzYJTk15Pe8N4nTosu4+JE7SFmQkYmeY+Xe3uxtJoNLExIDmflaZa1bHwd7qWmPN96JEJ2irLFfbOdsOJtBV4+4MXdMhuh/fQaCv93Qim3vNsVpqKWzTZh1mYCAwWD92CmjL13NOgZbHnRPrleKkWFpWU6nzW0dS/TvS4ZvIRt1U3HAbAHQODJ2q7JVyDNv+qKO762ErJlgtHOJ7W3E7RytkldU8P0Uxmvmjg0ALDOWvW76U87f3wIa7HrKstYcu8crjR88723sWGHLj4XIL0AmMjKHxu2bx/uaZthpSYOY48WQARybblEfLRwrL8WQ6ZJtdppm49B2mfI+EBlp6FvmG3OXJlw9GDgVH5FVWtZBcGX3eAgBfDSAtHt8BbniMtHewhuNZoifUUaCjXe5LcrZmxLZkVLdPPNE2Tkp+NN35dcfEYGcPVRivvT8Si2md1D9czxjKhvjb07NbIqVR+SFLXlIRy7md+UW+4rT1p//uMwSVs005lBpBHSpNcnDtjl/fpW/HDEXp4k2tlyvn/yNQe5HJmdqmMdu1Y
[image7]: <data:image/png;base64,zApC26FLncIsUaX4K4r6gj+SRAqNiOjw6OvGeZ49wEAp8Tj8cD7cTjA+5V+YgAd5oW86NC7uTFgAv8ARB4iBAgARx8iYB3iQuAgRA4iJAXACcHgSiWjUKl8ms87xL8dmDT7pAoM7+MZ5KjBD1KBmH+5bQSJM2qMNgMMj7MuLx1ljlu8wb02wlaU2WCjvnYU0rqmjOfTyEXAkmMxxCx9SB7pjcu6qO2c9WYdiXOiSyTu2FrBfW1WUK3EzHr7aV17Ed1HXuYBcM+JrWbLSi9zw+1eAgUi7aGZ1cy0f0aCjqRocxrxo9SggFnRRoD6DDOQRWFymqOXOLB6qb0uoH1GFDAHXYeOoJaf06VKvVHA7HarUCV42MjPz5n//5vYkWqJPw4LEPxtH/r/3c/6pd3HtwPXnm2zo3/BOCWmAPz51dc3XX/0sv/+db11SOauHK/A/6xUBT78fTF3+xcz0ncc1JXQg9JWbi5aVGz3r0kiwUkswxRrlxOGraRMBCBviEMRnPic7Ml7lIuZB0mjUwms3ii98891YzQU2ts/LnfXXJVLLTLI5LHe55/0KRM58SMok61jKrUW/WLt8EzcO9RUsSaz23fGmmeFL6aSiiOPPaA8+uof/+k3H/32X7/9CUcsvkddlC
[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGECAIAAABh5Rl/AACAAElEQVR4Xuy993Mjx4KgqX/g4u5fuI27/WFvJ+72LmIu4nYnbmJndszeM/PMjN57klpP6pZa7b1hN9lsmqb33nuCIAka0IEAAcIT3nvvvfeuunlVAC26JbEF6ambnV9UBICsrMysLPNVZiWqPkq/D1itVrPZXBz6nZDJ5Ax+OPrVv3svpldR/z4AAAAAfj4+KtbIOwnQIQAAAAB+UoAO34kJ6BAAAAB+XoAO34kJ6BAAAAB+XoAO34kJ6BAAAAB+XoAO34kJ6BAAAAB+XoAO34npJ9XhS58VMoogJRNSMSGj+KXftv/qVXEkAAAA+LABOnwnpp9Eh69evUrFc9LdeOU/xe79dez6f4zd+KvY/f87/vyfUxOPINXeq3SieBEAAAD4UAE6fCemn0KHkJabaPlj9PL/+np2yHT1PyTbL7y0q4sXAwAAgA8SoMN3YvqRdfjqZYYwEn/0X17PqGiKV/y37N7y/kuoOAUAAAD4wPgoEvT7/YFIPJlKxsPRGCySZCIWjcXTyXgoFA4SbDd4EvuvXhr5OxMjk7tiy/5+XEbhBjL7HpEMph3dWu2RDnkC7PwEam66v32WpGuZwBq8iNO6KmYZ73fVlvVgpbepAh9euPlOeGs8GQAA6kYeIt8OThwwjelZoO5/upglwhtYAc7x0n1miOXF2hy0ihwCUi1XE65UTADuQEjqTjoeqOxZHaS9CCoc6I2l7FcMrCo7SDQ4BTV5rQeMXmFvhadqnX92a4+bZsa9zjmIZn/Oovt3aHi3l4rzFhD6mVruNYesTb7cOszrmv/znN0OwV//4zpgokEpCef3e2WlipJjXHBxa9JLf/Ns/9MKZTUhQbPFGfTWc+kezTVI7Q+da9DuQQNSCH5YOqle7PleIVCxjRVr+uDtIFHlZ24wZbn9d3jNGx106L6WLDaNzZNGO7rnlkcGB5xGgT1Dx9znIHFocE9+lJtz2hdz4zfK6+8+2Rqib09P0FaW8Z29gqM57MBGDlLjdUt6xxdceSM/A2xu7021VWHoWveOpXdjYEcogbksByQQ5QoJ4dGoxG5+sXC98zhq9FhTrs5uG0ofMKffbnKkXT00kK53Doeu8LYxOAomVzeeTgxuGNMBGxIDnc3yEfKQnrZy8PLXDa2A+dPxhkDzQcOy8RLHDIcEy5PLR/INuYHm5qq73x9T+Q+y+EUT104DV/sk9GkOUlSCHJYDcogS18hh8GymZhgd3oLPJ4fBx
[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGvCAIAAAAMjuyKAACAAElEQVR4Xuy9B3MbSYKgO3/kxcW+fRd7Ebt7dxF3sffeXezbfXtzc7s9Oz3dPeru6W55R3lRogE9QRK0oPcGNCBB70kYgiQMvQMJEJ7w3ntbMJReFUAnSN0raaQh1Z1fVEhAViIzqyqRX2ZWFvgr6BNHo9EoFIrEUAAAAAAA3oVfJQZ8agAdAgAAAOBPB+gQAAAAAIAEHR7Qijpp9leCLjrvoUOTyWQAAAAAAOAMr+qQN/WgfMr6StBF5z10OD09vQ8AAAAAwBl+tUtqzkhOuX03mcjW/kJ0SKfTgwP53uf/9RPaoOGilwAAAAD4aPzKqJKYnd7dCWzpwOovSIddqZ47/+cntAXxGYmXDgAAAAAfjl9R8eW5GRmPblxK7VgEOrywG9AhAAAAfFR+VfoIvSlSzrVnZwMdXuAN6BAAAAA+Kr9anWrDYmu6uvBElhjSccdpXHeiPi40QIcAAAAA+NP5JT53CHQIAAAAgASADj+NDegQAAAAPipAh5/GBnQIAAAAHxWgw09jAzoEAACAjwrQ4aexAR0CAADARwXo8NPYgA4BAADgowJ0+GlsH1uHL7yOqHI/RG4O4p4Fqi77sd8FWh9Ck1VR4doLpykxNgAAAPzsADr8NLaPp8MXQV9kj+qvuep98p9ez9dz/z/4S7964bUnfgwAAAB+XgAdfhrbR9Hh4eGhRQ2PAmHnvZ7j2c2P+f2hmv8yGk5MAQAAAH4uAB1+GtvH0OGhWeXHfudJ+r9ez+71zVfwWVS4mpgEAAAA/Fz41ejUFJW0ZYYt4XfzVrbVbp9BuNzf3z82t+2CILlgE4K8il262AQ5lNz5xcUZMkWjUxOHBwcQhl1s9ymWH9z8/srTu9d/+2jX6Wu5/9sv0ElC7qeHT2moHVl3+6Fg7GxY7c5QGC4zXEi7xWvsN5Gi9LdI+dSR0lHUylPffn373tt9b9/xzPM2wsX0824UG26MEKkdj0r+tw7BtD/j6xeIJv4Zu//uu/7ujouJl2o8OYoYvClKn2KDXlKKndONjWp/emzefawQJUIqhio8pa5g2KDMmbYMkTLSP8wT7DK3RFe3vQLQYJB7PJmMnT3Be+AUi+nv8gpRjz/9aEb8DW0YNwLR4f2A6PBOuVt/VndcM4TsAm4pj3VYfotsA0eH9gOjwTnlHIcuX3[[[[[[L339yfZrTXrtkYM7sqp1z1awtVW
[aq5Qvvm8zpEHjLFKpVxdwhvPYw2gQwDgI+LxC+1+uRSPtttwAA4D0BdAjoCdDhh8WbdJjffArPDWKewlypN8+YzEyrFrBbLPYAdFgpZ+MGr+u7i6Q1UO25DFYS+K4WSx6rbU6mOrd5I2B9kHTU2L2J2JWZsbFnumJkjH4fzrAWEkj0xNNrBLfltRTbnv/fZzZ7GhXYWvHTRP/AVS5hG8+ulsPeHcaQDIIXwAclhYjpLDgNf6UrlE3glvR56M
[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGJCAIAAADdewqhAACAAElEQVR4Xuy9aXAbSb7g1961HfvlfdgX74vt2A9rxzocsZ8cYX9zhPd5N96+WO+G37HvnJ15szOve3qmT0mUWjdFiRQpkSLFS5R4i/cJgCB4AiSIiwBBEAQIEiRxH4UqVBVuoG5IdBZAsSlI3S2pKQ1byl9kSIV/ZmUWQKB+yERW1kd/DIFAIBDIB89HpQEIBAKBQD48oA4hEAgEAoE6hEAgEAgE6hACgUAgkD+GOoRAIBAI5I+hDiEQCAQCAXzk/xHYbDaPx1MahUAgEAjkp8ZH7I/A6XSm0+nSKAQCgUAgPzWgDiEQCAQCgTqEQCAQCOTd6JB+GcUshmFKM2gaBJ+vAAKBQCCQt8u70GFPT0/zC+A4DrLkcnlpRnPz7u5uaRUQCAQCgbxN3oUOGxoaKl4AwzCQNTg4WJpRUWG324/v3nH35oULFy5eavCw3qZrl8H2hRs1Fruzo+6auH3hwuCszaYaqbrzyEeyuQzSXHFh3mJ5dOu6mHe96n7FZbMHVEMONd6cUHtti0lhjvfNQzMpVgOJJ96l9bNRkm/vL/+rPHm8HvJ6jDGIZEwhGay6dT4slb4LPpDAWCoTDCg1RsS7pkz+WygsBqZqVB8kcvG/FhAHUIOTgjWwRQ56an1vYurqYQf3MkrLOZqemtY5rtbuYnwymZWZ3zexNV/VuM0/l2NDqmqndeY7SatZKRRTEdA1xPWDs6pE46uEVwcluVILiL4GRarRZyhtaC1i0kPDNFi2b6M6G3uIN+pheSbt24Nr07d[[[[[AAb+nscxjzmV3hQtI7+6BjeJWJjM
[R7ZsfJzjAwCARwsLCzt58uTiZX/r1q0p8VROHozqSejrTFTKaoSavBuUxNzoKEg7TKKwlg1+8TI5tlP543hWZJfq29cpp5tk7zVIfC2bX9ILQ3gebmZl5ovgMeuRuPLWnW/Pc/LzM/pTflv50WwQAgMexCuNwMrJBOj7rp8oeWKAQ+g1joX1PbDG6GhgaTL8RO+RaPj8Qb8GvWHM5PNUsc3W/LXTA5JTGPiKw+Aa1gapodnY2GJ+kQXM5xzIeMvoBgrtBFVpGpuZC5y0z3XvPDjxccM1CqTmTZqjhWGYWVu+weaz+0G/8GZ+ZG3V6mJrRkP4n9RSvBgAA4DGtwjicqO1VtQuNBL6ljKIvoxub6ao0vDKbrCGqxmanZyso2lvN0rp+85fSsEpd9c59uyJKq5wFfiOPN2U2XaU6a7qO+xq
[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATMAAAJ2CAIAAAC8R/JLAACAAElEQVR4Xuy9B1RjaX7g27Pr987ZXZ99e9bPe94ZH/utvcf7nsNz9oxneuzZ6q7q6urKoMpQUOQMIuccRRA5iCByBhEFCCQRhIRyAAUkIaGcszQee2zP+wQURVNUd3VVzTQN93fu4Ug3fPe7Qr/7/76rL3z0SwiI7wL9/f2PXuOf//mfT+/3zQHpHL/u6+sbHh4ODg4+sf29+PnPf97R0XHji5ulZWU/+9nPTm9+Mx+dXgEBcck4ZeaPf/zj8PDwE9vfnV/8y790dnUBJ202W0dHZ2Vl1dvLCZkJcdn5+OOPe14CnJydnT29x7sCEqxAIP7xH/8RvP7FL37R0dmJQCBO7/QGIDMhLjuLi4vYExgMhtN7vCssFutkkAQlWwaDcWL7VwGZCQFxHoHMhIA4j0BmQkCcRyAzISDOIx+NQEBAnD8+ugIBAXH+gMyEgDiPQGZCQJxHIDMhIM4jkJkQEOcRyEwIiPMIZCYExHkEMhMC4jv4KElMTk5Jy8CQdt/0FfU4TaSVzf0zVXsN5TOxmqlUD2eHR8KLiqoaVgW6udfM5CvFzanxdCMhIM4jH95MBGH/PZe6vg85QhcExHeRD2/yVS//JW2AaXltpnu/K2ucfTN0ljzf0Np/xoDfSU85QoXZY9ZdQGW+wqGB6nDMlck5V5OHgB3mp/w6re6dsrrMW5hMwrHDI9vonKPPteYgEIjJ87dAaJvVXH958EvX5f/q4gEIcbBxcDRW8jVrI0bymMzP7y0aOyDMjmfHxz+9nTgiNG82fRu14FLrLKgMv7vbKTo2V4a3FTcpHv3m8gD2Q8rYp[[[[[[epsVpFZD2RmxsuVZlY2QqWalle
[ljrRd2/vZCIR+ILOLt1q1bTnz5IC/s7EYRNMLQ/lQP5Stj5e2gBC/++67c4QW9cyULcSpdGmc5OOjjz6yBQsW5FxTCnwddIZvv/22t+do7ILQYmKJ58lD/tEXySFoco20AdRWNzT5UvzjHzn5orP2j7yj7e58shwR/v/LxF/b+/KCsH5UVE230HLOL2Zh+LPN8A441NxjDhfNqfa/ktCS0hGgsSWkKUHwmtjENCS0JLiMaChJYqMuzSp4FYQbQgMrDoEI7zPuMCwVFuocXnHmxAxn+2w5xPhY29V1QR+KThwX5IsXrckCxbtwvYv
[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAG5CAYAAABWY5pbAACAAElEQVR4Xuy9B3QUV57vP//dmX07L5zd93b3/87/vd05uzM7O2HD7OzM2JPsdcIJTLIBGzA5CxBBCEkkEUQOQiAQoICEcs4SyjlLrZylbnW3Wp1bnZPs7/9Wd6PQkjHGaOwxv985nwN9q+reurequz51763St0BBQUFBQUFBQTEv8S33BAoKCgoKCgoKimcTJFoUFBQUFBQUFPMUJFoUFBQUFBQUFPMUJFoUFBQUFBQUFPMUjxUtucGObrllBnrrJ+6rUVBQUFBQUFBQzBGPFa3L1Qr8w7W+GRQPG9xXo6CgoKCgoKCgmCNItCgoKCgoKCj+4BEbGws/P785SUxMdF993qOqqgqFhYWwWq3uiyCXy3Ht2jX35CeKx4rWgMqKgkH9DBRGu/tqnxuKznwEBN9Gm1jnvmjO0PZm4JxPKDq17kvmI9QourQNS5YswZKPDyC8pB9m91UeF4YxFNzzw5Kt51Bcl4mzO86iWum+0rMLVU3GBBBx89RCqlEDN6e3wSmtBdsRx3M0fwezwMZNtfQ4YmUVvQUh2HvjsNIaBA5htv0wiZdggbTgLPizO382hT4ez1Wte+NCBUoEaAXyV+n7sEI2kUFBQUFBReND9Y0ZocbCA/r0ERrR85xyVaU1NTFBQUMD4+LkvXf/3Xf8msr6+j0WhISkqSww+nk9mapTLoJjdDa9h8GjZajYNLFM2zO3PSviMb4nwbu/MKf9isr62zKfV2PuPY1socdTGPsHFLZmhOxNlcZ6Q6Hv/o4/+da425THCt6Uj417IyTk5gOIXdM9+ypt53Z3N9kcJQG8JrtUeOfVekJVj8RLl276HjRJQvragTw76Xaf52VnDMs25K1o5WmjieRkntIEtSXsYJOgZm2bCYmBpooa6Wfh9yWMSGzbtyyc0Il1z2T7tn/nm27FBR+aAOVqfh4eDE7ct3SO7R7gjZCoNVGaTlNsgib17sJu1JCJ3i/irxi6c4zZczNx9TO7pT5o4E/vLOW7z54RUC8rox7quPSdtJcloowc73+PTdN7ngVsyMfGycPLc7fCjK8u6nl4ht1JPrEi3u10W5DfoqckhLKyY33IbgUmvPn2G0idi0NHp1ZlbqQ631P3WLyMpBzF8jWstVQbz5yR1ia4dZeVouo47SoFv85y/+g9+fuEmxdpnxxiTufGRtm8uqCizra0z3V5Pk84j7N2/hktbG0mw7/pelOOrJa2HDv2OeGg9QEdKGopGF+TlbkQMaEhLQ377OxTzeQlKbaXu6DU8Tjvz7OQw55blgeFiDyUPG/taSTa9YdKO96uNKFSGb3tFa31/+IZ1OYutur
[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAG5CAYAAABWY5pbAACAAElEQVR4Xuy9hXtcR7ruu/+H89yz7717n33O7L0HMpmZwCRxmMFOYsd27MScmClmZrZlkgVGySjLYmZmZqYWN6iZueW8p9bqltTqlim2Jpnk++b5Tdy1Cr6CXuvtqlqlfwEZGRkZGRkZGdmk2L94BpCRkZGRkZGRkT0bI6FFRkZGRkxx3GsmFEdh77B561E+4PYGMjOyfzn6JQoubcb90+TI2btqMvr4+VFVVYd36H7z2bTlUl4ruHRSucb1Z3TcccBq0vHxxWIJ1CPL/9zsP1u8rk0m6rp4XMlxzn4+GSb01WUiIaoEkon1cYWtkr88VvazkEVLRkZGRuaHzrcnWvea0SvcKEmNr0Ij9azjbTtcuwR3XZIbmumk9sh73WlzuxOewOKmFEaZcO9NKqMWSr3F1Z1pM0GrUu7WE7uWY7UDAX7e8PQKR0EL9+D1+4jYyDXtyPKrd7hctRr56sLS0I2h7oiXi5OFVVPLe+WTUYzm+0pkBivMySUnNoLhuCM2y2F5tlXRNGZgdakRHxZcxYnrCgm6EgytkqWgcDssUBfRn1YBU2mxjurKCpuYEYvhMfYSc7tBuYs08aaCM+sQaTWLeyUOyHtH8dhruZ+TAWSnqHGzph8Tj2fKBzh[[[[[[[YYigOx9t13sPqrGKhmGc/39bM
[qMoxHexupsJ2jsweZ+X8Gu7tpbNZ2Q/lDdh2nljBgy9whZqVHpaVf0UFuay8Vq4radsfh2CIAjN1Or5rTcb+gYeXjiBszL/4KlL2HpkDjtz8vICYfrQVx/ap7IMx7jIvEdHTi6FFsnmcoSXepJudJYRTysfSzej7XvkAmZ2dqE4rRPucEWHvGGAWyYmgREZGSMbRIVgwtIiJSMoYWyYqhRUR2Qk5IaAkhxAwzWFTEv//937ti66X1t3/L7TV
[fukb/dmVvPWbV5i2eRVz/20aN0t6KAi2qhMhkxt717LXIZ7mHHduJ7Ujk8mQyZXIe2KlF39TE6XSfrIJtj1vhGgJBALB1CNEa2qZYtGqZ+v69ayXOHzpDgUtY7d/Hzq6KtNwt7XnflYJab7n8MromSDfsyKjoKCQAbWcwjhvvNLqJ8jzw/GPy6K9f3z691ERHU2YJFZGadL0URzng6NHPA29j393VXNuLmFRUbRMsM2IXkduqD1+uc/+B0iFaAkEAsHUI0Rrapky0dL1VOB78SrVDQ00SLS0d6EcHNXRqhTI5XLkin7UWh16wz46DSq1GqVCSpcPputV1BbF4eUWRoNSjbyriQ651liGstRyP1G0nBjMjUVWuxBu5k7dhkeH7UnXyXH0XtEjXw8D1+u98zXc8V7RCfxgLvj+Xcb4fCYHt8DXwO2uJUGzfNpR1DTdKRtifLUIOymtaIDZFnqg98j+ev2Gef5z732bv3biCX3H1ys0k2mYtiXl0nu8Mpp3GMtTWVqrU5ZK+vUH1NucqM4W
[image19]: <data:image/png;base64CftyPNuN7ZAsXwyvRmOdODsw1WsfZeOg+9cNtbjEaFZsroXhazY5rRSp8d/2fYinFax9SM0hziILzBa0k3BYBFeV0NpmFDQnBvEpVN7Of4JI15OTvT29v4qhYeH09m5PQzp39UfArR+Wk+yTFRX9W5qff3odv1+vPy9obS5TFeDMg6SWLjigdf5/bcZ1yi8pgkhcx7UssjLWQmZDB+Lqq9hfRazbjSDm8onpvuxUxLBU5K4w8cxuU+a/ZLiwiKUV0sxEYVpqgMVFwtRfOkSepcMMJmdIwIJqCd/LG8E28Y+R6vE5fKdwCUaxff+SHIQe
[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAG5CAYAAABWY5pbAACAAElEQVR4Xuy993cUWX7/7T/g+fX7y+Pn+Dn28fHaXnsfe+21j8PszuzspGWAGfIQZsggRM4iiCSCAIFQQigDyjnnHFDOWS2pu6Vudc65W8z7udXdCrQEAzNoCPN5n/M6qG/dunWrqlG9+tbt0l+AQqFQKBQKhbIk+QvPAgqFQqFQKBTK6wmJFoVCoVAoFMoShUSLQqFQKBQKZYlCokWhUCgUCoWyRHmhaEkNDvTJrM9gsD31rEahUCgUCoVCWSQvFC3/egX++u7wM9QIjJ7VKBQKhUKhUCiLhESLQqFQKBTKz5qGhgacOnVqUa5fv+5ZfckzPj6Ox48fw2hc6DgajQaBgYGwWCyei14qLxStUbUNlePGZ1CZpz2r/WCkXdk4H/wAg5KFO7BYZO3JuOH7CEN6zyVLESXSTq/FsmXLsGzLaaS2CGH3rPKiqHmIv3UIy/YEoq0nGxf23kG7xrPSa8q0GYOlsQi8l4cJk+fCV40JQ5v9QTQowPsuPQ2gfnoeNilKB7ROJ+QaFQ3upKgfMy5jwaTxSmNnsfkVXhtonW6xtMk3z5+GUXlY3/s8vJFXq8Eqtk5WjrWh+vY7nUJRFi/19JIz/A0JrPILU7SasnV0jGgxrCsLJpfR9yuMDjVS1F6GL5PHXGNrmVqfpLqnHD83Vx44/wsdivrdu4k1wrRcsM1ugztUA63Pvkcz7wO5/82IPIH029sy2o+UY/XwWB7zSpoibxeue6X5ChkOYSdu0z1wh7PHwilrGg3ln8ehWg9az91sDwQNawat2Y3PopfjVVoBcW7fS3xV7LvaawUUxc3+AbknQQtciwcy/Eh885R17x6iJgTmCPQsmKbxA977o7gwGCERqeiZngN4mOgtWdQwsPblYzFUMQmlmFZKkFtTg7KegV/9wTkx0RBi/rC+32D1hsCQqr1eYyNjRHPYE1uIHD0BjaTEoJZJowxD6o9kvfSGGZXpSe/eWTRYm1ljo03OT2LbfYE3w7N5jpkGsd03rdAsc7DFJuWAJsyAXt7yayWwrZvhkwghIa92m7H7sYatnU2ssDLsMzGXwSPXj165BdPA7FeDGc7nzH7uvkl4RJqQTNMSXoBWHtqC040HrhAC2FuBYxjwrB2ydjb3qYnTsqg4epf//ZTBCesQeOEBDabDWrpGlZF8o/6eyuxnFFrEpN4+tFYxMT6JYt4AolsHwOEOQjyv+c
[image21]: <data:image/png;base64+kUlJSY1UWe4Xvrwag+mHtmJSUlNSPVs81W/6dOVeTKlBrNLRWpHPa/VN69U2EHNvIyt1eIqGTQqxw+vp/1i2fy2WeHyHc85KG6lMt7VzjPqPHqMq87RNI8ZxLhkkoiLb/P2h59w6fKnxQP/uQjTt8MoLx3kcaYcyQHe4m61yuX82DOEsrx0ON6UwL1b98kuaxHH+xiZWcEiLR2+CLG8eOc+Twu5y4cIOMukWMa+14v36F+95XudQVMs9QtJToziuA2svMUM8sWyGbqsfDu9WQe4L0zMH1l214nDPwW3D53iN1mFrl5r4qWU4+lqDTC6zRirTfDnuVMMGa8OeSPKgGhloCL6CHE82DasJ3Y9hZui/vdq6nLUV1t9m5Zjckd0TDSzLaek5B79D6nfJ0cbibzghsqX6owO5OOq7KiA7QkN2CdWNojF4f5qW7Ii5VdfV+hPUfJeQ0cuRQ0zq45nPzufFeKgvT5f2plU20V9fKEhvSNCq7iQv4AxnrTI0HpmlJeEmvgS0IriwZR/5Ci3itr0iVZlAc7tkfgVl4NkTTCgzVqOJ5x4UHtpvXDfcSd+yL2oePgz/GW3fewqchn+JwzNy0gRYH7Dmhbe8BE7zw0z1siKLcVYoUCPeX34GgXi4aeEtyzuoqzJB0dXWvUpzjCKaKAfb030V2JYE8rFPXOoNz/FPRsXWB8zZbUMXc+DyMptvjynDlsTO2RUFKHxrxoXNPWgsbxczD2iEMzuWH0PfKExrnLMNLXhIU/I7Sm0JIfAYeLTLkOw9A2Fq0cMR57nYKWiSPMdQ/hhJErUoJdoXGC+F/PDIl1AnLDaUOY0QWyzwmc0jMlN6YK2G/Xh6WrMa773EeY+3VctzHB+YuXEF/J+O7mvO+u+yErxFdx8QG5SQgWGWiNxmWlnjF+0XFE8PInicHMEFDLCnoNcb2dEVo6yDwjFCeEIf9QEfl8mrh0+gJ37j0JTxxxDU0SAa3ijhs0LD+XhvgjPboWEGa+kGEfJIt8dt4hb4jt5dzLO7yK+OngK586bECFXAq5EjjwvbRzXPY9zl/xRMjgJ6UQ/IuxO4JsLTigiAqPpgYWqHe44BNNbqejhKyBtT4SVfTr7Snq86gEcwjPAJe1lrCMX4d6haOGOYO933+McXaeJ9a0IKjXjQJoKhZ1T97MRQh4uFFrEoA2
[image22]: <data:image/png;base64,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[[[[[[[X/lp[X/lp[X/lp[X/lpgTSih2
[X/lpM4+4txxM0ulpO1ynCcY5n/uRP77Q76GkU8X3VXUWwMXeHj7RRRidXTGKaInE2PrdJt0VgG24WCTH3BvdmDcaPH9P6pA9XpiaQUHvLmIyGEIokcFbk2utzgB270DYcnr2DImEwyyzYiSQQ2bHCyoTLky6XUruEk0QE5nk1lA6cLYfbAPY4f4najHv+m2oSfSVbwd2L2MA+vaaQQPXvQiuLcDeUcHZp1hzMq7MbKyBpWkDUXS






[image24]:




g==>

[image24]:RRGLiupw7EH/tZHFwW5S+zjscXG41tL1lXU4YcKE5s2bT548eWY5a9asQhNhHnrHV0yEWcGOBNYsXL0blaPa8efNQSfVaKKMykX3/9NcyUx39bEVstLS2Rve3evRuDtFqSvvD7vUu3//z93v0kUl9X4SDpUEJCQsJQSaiJhAtFsqgvajiOn88c93NY+zWRZH61bJLzsL4ztGkUZmZmapWLpayKsLAwT09PVoUoSU5OPmjxNTTt37tyxY8d27dq1bdu2efPmjRs3btiS8mBj0FR+BwAJ+RaP4GD7ykRwcHIwW8VE/sOrc
[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUMAAAEFCAIAAAD2UBIhAABiWUlEQVR4Xuy9d1hUSb7/z73PPs8+++y9/+xd9v6+d9i7dycnd/Lo6BhnUAdnxogiI4iSJIkCIkgGRW1ooYEmKTk3OTZNkzMNkhGEblKTQwNNVGfm/D7nnG5oGkRwHMGmXk/9AZVOVZ3zPvWpOtVVchgCgXj1kZP2QCAQryBIyQiELICUjEDIAkjJCIQsgJSMQMgCSMkIhCyAlIxAyAJIyQiELICUjEDIAkjJCIQsgJSMQMgCSMkIhCyAlIxAyAJIyQiELICUjEDIAkjJCIQsgJSMQMgCSMkIhCyAlIxAyAJIyQiELLCOSu7HMI7F+2cOKijLi9x5eQUzl+qpgmHpqC+Rusr4WGMFM7eCoaxB/P8i51txPuF0HiZ4JB113ZgexHiJxgccVI/4QcH6Zh+0FKZCmV0S25N6peMuoZlbno5HZrQmPDvyZqZDOFQIDXWDWhLQIR22AVl3JRtoKjoqWzOcXRmOVz0sVc1OudXQC/oFGP2epFsiJSNeHuun5OcZJ3uaWeSy8FNDfpuSnZ2537rTxOd6pHWwmsgzP/q66hrAkGOmsSKi8+lkbG+C9sUjJ2TsXlJyzTeSyt4L78dCalGxKDk/P9/e3t7F7JsiX2IFiOSnY6Ir/qN2odz5ErlzJXIaJXJni3GnXvzXU8EfHja3trFjsVjSOS7D0u/JYInR4gQz4g5iyfnJnRkpd0IVFWgJg1NN4lzIsxrNU0ejmpYoWXR+8tlPFy5BOF22oV8eBKl94WVsjJd18U9AnqVkHjvvbjgUI7J1tFacpr+2FIphldAVUCe2rk8HQ+ThOYzseG/vv35NJQh8hnAfMVN9UAx93UQTu1IecfTkkhmvtSi5wqICUjELIAUjICIQsgJSMQsgBSMgIhCyA/dE
[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkcAAALvCAIAAADgbvYjAACAAElEQVR4XuydB1xTWdr/2fc/++67u+7udKev4zhVpzlGxd57711EKSqiUhQEURSidKSo9F5D79J7J9RACkkISUhCChFRAZH8n3tDM6LijM6MeL6f7Gy857nnPOc5zz2/nHNvgpoCgUAgEIjxgprqAQQCgUAgXlmQqiEQCARi/IBUDYFAIBDjB6RqCAQCgRg/IFVDIBAIxPgBqRoCgUAgxg9I1RAIBAIxfkCqhkAgEIg/C0KhkMPhdHd3P3z4ULUMp7+/H0r5fD6Xy1Utw0GqhkAgEIg/C1lZWREREWKxuLe3V7UMp6+vD0qTk5NjYmJUy3CeqWo8LqUwP3CI4MDAxIKmNuYdVbsXT3+foqOuJi8nLTanrkPRObKDdwQKTn5Ycm0ZTSQfcXh0Wgury8rD0xo7FIoe1bLfm652Nic/MLVWQGm7p1qGQCAQrz0SiaSxsTEwKIjBYHR2dqqU3r17F1ZpUFpVVSUSiVRKlTxT1TgtNfyvfIZPGkT9iV7OtRsDKzSmujy3iPHG8trTVr4aKldtBBf9O1Fsu+1iCSKygC7JF1MsnwkxMXKlH77h5VQxOTH5HjsuzzjL9AvTZuEJHE/QkTmSY2MTczDeHHBsIZRzgZndZQ1rB8/XSys11WH3I3qlO+UY82XLqzn0tP0o04jW95G3vffIymcibKXuSHzqZ5DI9E8Tkz01zQmyJw5bvqM/cqGuCM9QqrGP5U9LWV186eyqb5nEDQDb7qIJhIeLE33N3UnmVhbGvg4yB0+biFzzgoepE+oRS1tXVVSLKKxmT1BLhySbnP6BqaIdnuC31cVN0o5vQP4Cq5aEhwvPb+CFRZkZrGY22578TJ/d6prq6Oj4/PwdiLgDNLpVJ3n/In5Fmr2mhWQ+TAiXqn+ufXdne2FQQJ84qpf3DVroBWQ3DE+IeHh/nbhkNhXX6prOqQXb6rByhxo1FNdxmCFnsRi00ZhpbyhzvIuijZD7+bK6zsM8lv19n0JpHkaWV/UXilxKdBf3/rcEbG/iCsZXLZJiUv1r10zsxA+zXzK3SLcJAdD9507jqia6OiAq[[[[[[[tSDZjsV041bh7ffd+qL2U++0bIU
[/PBgF3qKyTzZ1tM3DupPDrc16HxZr5w8gUJVgqqEMI5OIBOhQIBAqFQq/XOxwOqEMI5BrlfOfx3nC5C1yDv7zBCDVPvPP2a30Sm1s7ec+b7uCx1586d/H8wV3nel/eWDakQwiIzcFL16FIpUnM6RACYkOBdAgBsTmAdAgBsaEUFBQ0NTUB52uZ1IBAkCRqm1a2Tof6GVJedj6axQTzsiZnDeIDytfYgW2aSPUdZlEvqSI7j8g2jNjdY74LqV8iZWd/Kx263W7LzYA9SIBPh+GonDQ8va22OO/cif0nqziynsb4/WfOnz4VHbonkW7gJb76qw9PH9n8+pYjp2MTwk8fq6orSDx9+N0t+w5Fhu8KCY2jdLHqzr3y9MfBZ7KKE/eciToN2BdPHlRbHL7Uxc0JqRGfHA46Ehq0+80VHdp0r72Rzvf/LEhub0/c+vJnB4+dPhN69vRXn5XTVFZfiNPpXJNzCOSb47+/vs5qHVZHfnHgqy+PHw8KiThZ0sS6LXX399tQ43bdoEGosDBw7cSodGAQ0d/eadjqtbR3dWK7t34MmthZx2tMdeh3I59qo1CORVcUzOACeZFh0xUIcQCGQ7+9bhqnZhJqp72jDrHq9[[[[[[[p7X[p7X[p7X[p7X[p7X[p7XT26
[p7XMGDapevTr5p06dGj52y8RfDokdNpM2CXLl2iy7t37/4u5s8OCyGE+AVIvHJ45syx10zzaJIdZYXTowIFCvDC5BD/xX6W1jIoZ0dQeHeHHAohhBC3iORQCCGEkBwKIYQQkkMhUOzMyFERi/U7JG05ISHB+g6LsWXLFl1uBmT5vyS[[[[[[[y+sF[y+sF[y+sF[y+sFVBERET
[y+sFCmgj400OgbMMgC95ZKnu54DmTN1sQH3NDGdqaqRaYXACPEwcd+cYJklKa5XTIG3vopvhKpsKEfUC8RjxZp0ohGyQ+1qw1XqePPWvszOaOGAzRUnf46gm2NTTNzbT1QSbq3eYLp0q88wX4GTswUkNF8vQx7YM7FKFpn7z/q3URO/b1xx/vptFOYFXA/NYR9gtH2qur2zt5Y0YZaNkdxgcgKclV3lhsfYfmpyeiIM/QaAP8raqUrEARZytyGFR6A5yAhCIIgdwe0AoIgCDI7g5LaFF+IyYgoCBfteczSnAgx/7vRWelcZuuJjw91ewN1tAKCIP8jd8AKxcXFsNzDJz8/v5S/iNGOV+Jt5ODBgzAxMiAIgtwx7Nu3j1qwuRzQ5MaUqd2m5Sf5pxWx6qB0m6GurYYFd4Er1b6cPmJ18HPjOMTpUw4LfqIogyCTlrlGFPH7oYGvewqhHloV/cDwjid0oVWhtduJvgXvXAEEda
[image30]: <data:image/png;base647MESLZVTVCTmphXabIFcRsXWgwb7VUlnTwEwytkD6Zub+vbFOHqYueyLLrtcOGgbzK1Wr9/a/iqYT4El4+DJ17kH6PZfipJWphSuO9Twk9hvNc/OREEMDYxCvJ4Sw/qxgSAS4WsN41CHSP1PcxjjKLTv3E87wIeaDuYuP6Fhc7PANLatmHEjsdWNtc01JZn5lRU1DI9PhvzgtLZTGyoq6bA3UkiSR/HYFERGYlF/KODy2owWrUrb3z/4z8
[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
[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAIHCAIAAADIKWWUAACAAElEQVR4XuydCVwV19n/L+bNm75v07RN3zZp/22TpomaxCTGpKQxi153EQVccEEFtyvijoiiqKC4olxRXHHfF8AFdxZFZEeUfd9l34WbpU2T/5mZu8yc5+4MCOb5fb5NceacMzNn7j1fzszci0TyppRlsIa/DTEBfkWtwCqw+huDlMACWssb2TiEV9fiDe30eHOIHizeBG12NuSoB7H/5X4Ywv5X/YP6n8q1Fm9xDCVIdDJM8tZwPhZ/H0EhIbytxOKdkabSo6eVLizesbJ4W4nkHTMYJek5uivyzugeNNY93hnF++9o9gfmv+oe0HTF30eq4S/nCvPXwj6ddRmHE5gSdrF5uQIej2S8+VaEsrL4WylugpG9AhR/fUodYRHDZoLBas1QzSg1hQg2Y5Pph3zycccPBkNv34hOPAvQUnE9mZolCHr382hja+nFcRgzEhqEORY6oOm6qLc++fPjbjlZmb9NY71qGWZUJ9fe5o5x1dPf19Q/y+DngcpLto3D/VNG8jZ9jx5jH1Ijppt0CE384E9tBBADpkQQW3ttbzW6uZuqEdR0wDF6Jj6Oht4TXQq1GiDZzSnSdhyF1po6YcWxOL+DjKvg5qIrB8GXMR2PHJeMtm53npyaAnJqfxB6hesSqco652LjG9mysLCdehCGxXLQZTx8d0jeO4Sl+BoWP6eLzy/
[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAHUCAIAAABtaxGIAACAAElEQVR4XuzdB1hTh9rA8fbW3n7dvd3W1aptta1Va90LHIDiBhEQBAGRvYey99577733DnvvvfdeCRsCIZzvJAEkUaxFbB3v73mfPsnJWdhe//eEjLfoAQAAgDfPnjPsG/7gfXv/Xcq8Rfs4AAAA8Aag5PAtNISUoX0cAAAAeAP8dob9nQO8b/1xd3FoHwcAAADeAJBDAAAAAHIIAAAAQA4BAAAAesghAAAAQA85BAAAAFC/neV45yD/WwfI86fAW3cAAACAN89eBi6qHOIBAACA18joszl1UxRyCAAA4LVF271VQA4BAAC8zmi7twrIIQAAgNcZbfdWATkEAADwOqPt3ujo0NBQZ2fnyMjIyoVUOUSHdjcAAADAq2xl80bJLayoqEhMTERvrCwi5BAAAMDrbEUKF1sYTVZVVTU8PLxcRFIO/+SDJ0sBAAC8nlbmEE0gGsLc3Ny2traoqKimpiYcDkebQ7SFkEMAAACvmZU5RPWzeHh4enr6+fmhPXN3d7ezszM2NlZQUBAVFFZlx6KzZfGfUdvown4+53lX3CowIAC91qQ9wIb7y3Md3H7/IxsamZBeNCTHneaBlk7b0KWtUc0Gb3Pb9bfvR6yjGqc2P1yGas1Rz/79+PI1mYzXn6+wABHQIAwgE6BAggig5h4kxXnNZ2FZVkg5+VBikYsjaOb0EHRL2Jmjp2TlnYqnD5s4gOKKHu7XU7nC7r6c6hujNnucOjC8YSbqYH0zk3[[[[[[[nq5[nq5[nq5[nq5[nq5[nq5304
[nq5ivo8ZvnjE0XR9jKJc11JnpJCK1a06BBJpaAvpKAvFYTU+Nz8E6dGYRfppiCQ5wjnEmR4yyIXO72C86IXNs/t6GtyvS8RtIrb0mGu3R14kQl0FqeK602DiNieqQzehKMVg7lT8usmWyHzo01BbXhhutP1vdVhot/UP9Qh+t75rh+Eqv2yxL2NzKh0fV9fWNaB0UPslaeul2uV9By9NG7p2WOlxcNI5p/SCCrhXO5mfVwbRobRlVF0Hst6XaBFejUOydicZrTiIrXx+dsklz/d1eAh6Z7pe73l6dcHLC6cd0FlW/trhX+lQR0zd+El0LvoDqYxMJ5lzd50SKpFsbX1oCb+j4/A0shSdhUXXDiujTA9r3bAOQrq1IRlxPuwgEIAOAQABAXQoi37/gNx7jy3jylH+vw7GWjoBwcE6Kl3T+Y4REd7GVt7ZDZRcj1NSskeu2r2Ilzdx881GfFgTdCW4iPhZk7hfA6BDAEBAAB0KDwPUIQvflHk/uQPiMAm1yeayU2SxWY4HJ8v7tiPH8+2PLDB4B+vQT3n4JgqHTqxwlh624U4GhVLjtn+ozONmJDyUlISjvrUzf9t2r7KvDhfDQSKEfSL1yx7Xeva+38YuFpXYs0dSct0Mcp9Z0WY/+VYKiwtRYB+uN30LtQSenydrk4Uh85UZrzdd0iqhBYLeojde3TqsfFBI5e2bibo0QtwW0WHP2mGMTVoHmUqV[[[[[[vmQVwhyCABBIIfksbgcIrwJ2hP7T
[8rekCqabhye8IrUx8Jc/jmZ3xaWLWsGyL/berfMHHpq2lwY73MYcnGG0SK5/33/H/SQ4L3erO9w7PS83uHHEaoqgatzkf6QSEmkYL4UKEP/GTWF1yT4dIOrrTzY7vBs/fEm2//OokeA5rmVMFApZ/aRdUfjuvYOpOJDDQ/4GMk/t7DymEuTW//9ttvIHUgcsJKSCAqKgpVqampYPOPf/xkBBuXHoROvSvq0bUojXaAfhxsXG7Xc2qvg2dqP+ZdkGkXcP5yZmatrNXk0FlamEvOruLmrkHrvT8vhzD7lH3RguGPsxRtAkW08IzlXoHsdt7dJuE4HNGAY73bMYLtk1s2EIc3BxgNZRdpYig2nLsroKvW3W/ENR+XVfhYHQhvqFOSwR0b1d+sms
[image36]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAGbCAIAAACTZakxAABVWUlEQVR4Xuy9B1hbR9qwzff/+77bvt2872azyaY4yW6ycYoTO7GduPdecMPGNjZgsOnFgME0g+mY3nvvVRTREb2D6EVIgEQVIBACFVCB882RMBbCOPYmZkmY+3qu3XPmPDNnjnB0a+Y0KQQCgUAgkA2PlGQBBAKBQCAbD6k4t1NxridiXY7GOh+JdT4U43Qg5sneKPvdVVmOfDaHx2RK1oBAIBAI5FeHVGmebXHGg5wEhewYmazwMxlBe1P9v45x+CgvUm2gqJgYHTnHmJKsBIFAIBDIv0XTKkjm/WRmZmaIRKJ4CZfL7evrm5ycFC9cQopDL6STUmjdIcMdDkON5uQanc7CS224a9lJ2o2ZqRXKd0iZ6WL5M0OtjbUE6tL6wvx8bX3X2JxYiiTs8Z7egWE6uY3QP87kziPI9EBlywCTNdJW3Uadlcx+LpQOAmVsZm5esvwFcCYHCD2kEYaoZ8yRjpb6SpSWfgZPsACK+BMkYUMITBIIXSsvwAFd4gh1KOBO0scHRgZ7RgaIE6KwLglwp18vfe4ARYVD72zINlHP2nx0sxnk6VnDbr[[[[[[[IKK[IKK[IKK[IKKxwukkPC5JBL
[IKKeJkbrwyLJOYZlN6c8ryGyITiptG2S6/TLiCUdUqnUtrY2CoWyKAD+aKJhYZHJKx9XP4VQXtfSSEoxkWU9kQXtITkdiC8FS/1zMfAsa90Vg4yHEmriBTYQYx0OMdHwFq8kBlofh86wfXtq/Y8cR+w1/WGuZQ4zbcdvJ/vQZe2unmkJ//9HeCtGM00jvOkPb7nt20T4fuv2FNMbtNdg
[image38]: <data:image/png;base64sB8lcLpXK1q2bu4JcJoV/s8oVxeRLpSVwAWWRO0xtR41zWusMFDosSWzExqT7a79/0Tap+KKxTZpBy56cxKFg044r28IMiE/EZ3Cc+7OOp6E0CSAXk4ZqslNWBOGuoR/i7WVuDj2Fr79CvnBPYWDnHJ6bl5+RNNUeanHFsWpnJMr/nEpGV1FXgVsA5htgKvVYdSCareWTDmIUBBF5mEY167/Y/6oDmnzPPupIXNrMsNw37VQxCxq9uKJopRUtNAfYB3C6AOPVocEAqG+vr6/vx/8NGvPU2VpgPHvT5XR1sfLwxyMwoC1dtsPb2ZMM6QKRbsfNs+zlgUd6H9afPHGwVKpDmtmlnEmrx5EkRqlU1mrdbomESZdTwlvCX6Q/Jqqdzxju7Jfy+zyLuc7R9zLUrZbHZZM0moiffw8nfV1bZZFV
[mWOIjNFbXMo3LoWBgYGBeQYs1iHMI6IdCdzgLDtJwMq8fohOUMFnrvfffuTr37YvHnaULBJKr5iZnnYtT2mqPu7fkFHZ4Ogaaq0L52PjgX06+/vazw+ezNthqd/4f3PZW2LB7ArbWEPjv50+Mx1nbQhBrrCTvnCYRWZ238WmdFitslFVxJsNmpis3sPL1JX+syX34ELbctX4N8OOZTJShelG+CSw1YlSyVW4P8VzZKG4XAvEJX/508ffQU9eOmxdZziE7eU3jU2NOBnsCTIXM6r46WdejhEdK759Q+/OHVv/qingqRC4+iKV08CGkvWcK7C7fLvdP/YgM7X1v17ZrSY6O/NdpO5IqUCTUIAgit78iiwHtN40QR9tjbaVgp84dRCh4h0ykp9qLpwJiNCZ0spqZDaQ3QMcmjA7q2MpT4wgDJLT4JxM/NUCjF723LTiBPZwilS67XG8YX5dVOlQOyrXJDHRnd7fORrbLYh2Mzx79tBHf9jrUDmu/f6Z6G6mhCggrx+qdIhrCZyfiEMyWozKM1qMIRktZkaus8azq9KobT4ghLfaAAEdAjYB0CFA/VGlQ0K0L3n1zgImeB4dvIAJlaBD58aDxGPBM2NBQ2WWk0
[image40]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAKtCAIAAABwrlccAACAAElEQVR4XuzdB1wUZ94H8HlzySU576KJiWka46WYS+Il8WKboNjoNkSajepSlo6Agqh0pA4iUgVUUHqVFRvSRUB6k6X3zgLSwXmfWVBhRRQVFfx/P5t8dud55plnZ8b97TNlwUiSTE9P19DQyFuyhMSwxGXLNACYXRQVFTkngVdOQUFB6oWhTUmn01Fre/bu5+ETlJc/QH9ARERESEho7dq1/Pz8OwCYOowjDos2bjwHwOxy5swZzknglUNbwfmFoUa8vLxQa05Op80tTri5uXs9YG9vb2VlZWRkZGlpaQvA1HHGIamoSAIAAABvGYhDAAAAAOIQAAAAgDgEAAAASIhDAAAAgIQ4BAAAABBssLftdvJNNVXlvG8XQxwCAAB4O2HMy4phThJy4lxZX34McQgAAODthJ0OcjYjDtP2bs75+lOIQwAAAG8njO9shoi1N11uW+6izyEOAQNukj32mk9By7zJnHPaWmwhsEHjnC1STR5zWnCZWoXuwuR5arld+PbvlKrTQxPic+IRCtKTvS2cpYBAKbX5HEoPUZmZiZn8RhvbxzevWiRcHDjLpF921WsBD0rkyu6yeFBstLnZohPbEFDzVA3es644LN/v09KeWsdx8yVPj7OVFFhtsOl54jDSp8QL2r2jPqOyT6bwTSYPA7Tj/12xPb0RufKzt5xf+2sylPIz1EXP5beN3bqQxCHALw+T4rDxMREfX39sXF48OBBKysrznoPvLVx2J/uahq6f8PBo1qyx09uMMqILWL1Dw+gD7VwdyLiTlXZYBh0V/fAMCqquZODipiF/pdDT6GikxdvXG7oGr5/f7A5W1Hd/r9b3evq3P08TvL9ZHI+puz2PWq5A423ujJNpCRsX14c9gx0Vpb465zU3Mu3ehPOo7rtgF0R8zoVh2tM9+09l9BF1rPT+16yfqSH0U987hf8HSeIw3t3ybqLh9fv2b9s/5kS9sHb7qquppL4+JLS6uousiE3Ojn3WmIJMz0h7OTyzyVFxK0DusiqwXFdmR3q3Pn0bE//ZJLJyj/1IA79UjUuIo/6Rx1EnOYhaRFtRb923ykcs1LRVdp+2cMupE0ehZSPRCk1o2evQsptl/aRZqGUdpokBbM2ka/0k1rvpqrkdkGYTIvKnKu9fRuUboS5jpSpcGjXnaqOZkE/mMq6pA2lb96AYT9vgSJGBly9hUv/kDk5VBI+024Xm/5A+WwirhxiapEau/Ij4YjRbR2ZktGgsAwCxipsOhjsLMRH/5c6MnyxXi8frXSR/1/DhXCkALE/ETId1uSZR3iquvP5Z/uAxOlr4hpejqYuZCYqgkeVHX8LBPDDVMTQXZH8pXw+wQAAAAeK54DB3ONJqzo9Ur7D1[[[[[[oNVj0XgA8q4z2Ffl4G9Y/8Hyw8J
[q24GMCO8hlu4/dONCrTkZJ+74g6XFpM++u/o3cgl1iVufsk3ZVdctHd1TfA0cKaHry3vjT2Cf+ijc4asdEP0Eb33nbUzxyxKWghAGCSvNYuVpEtwsvGMGHWXddeO6syDoxBV1dDV3dS7qXFWX0bIMTm8vD+QrxEf+8uF1OXXOx+F07mFYby+Yx5ZCkk1SP431ZZqqBRtrgFBLTQZfGgFMgdB0TJ8ikI/e1cAT16Q0JNhiDvoNhKa2bik/9BHgDORDkORUj14QlSZUWO/dqByr6FrXA55+TYYF5bsYTzVZUNom9Irle2cLfctEeH5LaBoPieyhAjLR3cdmV1ezx3k87iN7Zxb5qVoIgQz9Llj9knpmPgQrbVaLRR1xjgpdjelVEXOQFn1nAlRrKLRpcALvqYRC6WdM4DYOgi4/unemvaAjw0yw9C656ZRXn7sLbN7/1IC19HKA7qCz718MusuWunIdk+bu1BH/NElFSEYQPk1WemUhOVQd1vZKLE5Nj8uPc7+1TdPFOju+c4sYpm1sYbLkGlZ8clhyXlBRpKrvd2t7TkTrW5kjy8ycrxnEXH1kwRlsgtSuH79/X9oTUCpJ9gh4YQWpRjLHalhqU6rjn+P0LGgiklpDs421x996+TfZZ7XFJmZCaSlSDZ+WyFXV9+brB985tIOxX9yA7CRsnkJ5fXtw2NsbJrEj0Vdx3z94/JSw5rTjZy1zxhrmGTRwAOfYKKfM7Dg7pJSOpMnGBjFfMOjM3v4AO30jwQWi5Wenn7nzh3RcP3DTJauFy0sLi4Gz7Kol/RnGxZdyX9a/7GAohnxyj+XW4oyaaML1R
[image42]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlkAAALvCAIAAADZCUd4AACAAElEQVR4XuzdB1xT5/4/8Pz+93p77V56vbd22draXWsbLXXWPaoW96obFfdWxIGocSJ1IUNENoQ9QoCwNyRhhB0IkIRAEkgOm4TA+T8nCSs4wA35vl/n1YbnPOc5zxmcD8/JSSThAAAAgH/nK5+bbr9LhCrNp7y8mVPxHL/zJ/zOR5GsuqezxOMT5lcLudkZ6PhIJqCaTQ0OkQBqVvbE8oDAHhBmpubCwsLd+/es2Dhwus3bqDpxMmz6QvIQgAAAKsdZCEAAIDVDrIQAADAagdZCAAueKvJWPcAnduymQS4rf+avg0heOMtf+Lvd6kddawLAsgdZuAgLysKu/KL4IF8zgrOvs19Mg0yxUbcUeVN159nn2uug9ZTn233j4DecDf39pSYak9uSl3k/+uiTjz46fPgwLy/vR7zu+kH5D0H/p1F0qgUUXf37X5lPj9/Gke8EfIhkcOFGi2wN0ryww4XjU8O9NYk1feMzg4PNICkJGbNb+G9aC/zjz4ikfdCAVzDkexsOzKZoiu7T/3o5W3sa+hA0F3QwulJKElbaYEoMzy/gtJWKMmEUSUpUkW9mX1l2CP65Pw7O8V+60WHqToWWfROZ+PTYVfymvom/+mxL7M6C7uloiIsNRW7UtM/Mr4ZJT[[[[[[[J0aP[J0aP[J0aP[J0aPG2FWth
[J0aPBZUVWzNFz3/slnOnzo2Eo96HGxnKEn5+Pikp6dnqAEJ8BZ4ESmK7w5nZ2cUCoXnl6+BXE4hFa/sSHmMqhC7996R6ROdVaiIxJrELhMAdAgAAABfGkCHMXhfh2azmcPhRF1QCgAUOMzZlTrgthzSqBJ9OFLUq7w4OuVKDFaXTSNUqtiN3dVc4O6OVF0OIEUw1QaNHBm+AOCHALgCqAg[[[[[[[nTq8[nTq8[nTq8[nTq8hBRPX1
[nTq8V1bGyMzWZ/txH3RYfMypCikThYbcG209pqGtc5bG38iyO+hy3NXVhYz4RI9Sq7TEikboYPr8uxg13OWludO2qYMceI9rlpYWJdvQZRca5QyMBWpz1EE2tWnRSSlnNBXmZnV7420nc2iEGcKKysWyDIKMphstHCx7ZGx0RVN35OAPMIG+/lGIJix+qSEtNiwqe3CDxSYNZvjAQ16fuQBpvcWWqf/DoIBeqa2n7Un5lBIIy7M4knAeQXH3cx9Bar3fNRrgv9rWLQqAzfoPhgn4I2kHPj[[[[[[Wxx+JRILu257R0dGFhYXovFCpV7
[5wfO3d9zw33Pufv7zjJ72fq/QbnO+uXKFdB79c/uoC0O18SjQgMDAzzszR44+5WPjtYVBd1QU9HxiMKMkfuqipNCQ0JC/FxMNfTCiFQqKVNXS/X1KNcPfUdvV203U1jJvUu2lRRb3B5mgVWKJf1rIPF3rawJxlFGwyIKz5plHiW0Tv5D7Gzg+GHb0IZD3qjWyFm0iKLz8GPzv40d08qfd8JsVlMP6wjUT8Pw33thn0smXCpmOXg6vTPUxdrAwNDIyMY3BD05P4ZORMWnYckdhShzdVXLjLbx+VZfc+0n/r0O82AY3C0tzjUCHJtbiiKD86MKxsa7G1JN2+Py96arY/zMDfT1DAxTupY4Eil7fbQJrzzDFsfc//SRZ0BE6L2fv5PcusJVsjvuf1iuYkLw2e5wXNgvwEmQpDMlqw3EmLg1BtYXIFXDIiJ6lw71lzbZfqvPWwF9O6A6KpXWYDDDFhivKIKu1dWp2tywzzdXErGmVIDoueuVJcOjrYk+nu7hCZVLpxojbCYMj49VFKQlpreOMsQypnTmeG+7p4+gWULTI1OyV7vSvLzdHGNKevautBdbHeWx3h5uLjFdq6dSi+2a9AmZHqLUUqergzwdnNxDcisHj+WGCDFyWT/7HhHWWKkt6tL3MC+yOisjoSB8bbzwysX+glSHA6k11V27F5CMCzd70mN8nN7KoAsuKCI2PCo+zPv96jUWeXGsp7KJcM7das9Pj4mOi0uI8Hv0IKiNJNCCrFr1mRnJCZFxiVn1M+S9leb49975/X8+jm6cp54crS735eamp6UkRiaWo+JJW+tNy5xDxd6sOZps76zvPeBx16pTEmLCg+MSW/AspclZvwgD4+3nh1cuBIFhJXkoo66qnciHIFhOmyjLivW7/4vkKSbzYCTy3z/2DI6IiQp8/KF7YFrvSFNahGdwzeTmEU+qM2ml3Kn4D4cy/3s9jECcrl2WZ7TUHgwKHMYDIdtntn1LUp2u0wxB7yfRgU4Zw2I1UYT20WxAwyIkDmy9A6WLTOVlfck9C+ff2LF0bBdl1aUFjO8Cy+Ih2kxqHZzBCj3dWhZoqy3h3z/33pGhKJNC82OqWOZHzJtJbLIOMGrzAXGImpWSMdzXk1SyKVmj3fiVl52WpR/cED7GmN7piUPG5ueX11TP7KwD5WmV0wfHgwG33NKqJthcmHLzIjHNCxKT15obhPNjOkckl2iMRp1colRqjWAqZbXBWt4xUsfFZenFLU1bp5qNyntJ7QsC6AKSrZV+9k/PA2IMtmnb89dKBcMwxLaEZsrgi6vfn9p3Cj4RVwt8KfGVGKyRHlIOKEyxQqmU8xU6kOkXNigErKOsK03H//K/vps0wNM6zozi7a7M277V81tLazNxon3v5w+SheaXGbJenRqBA3uM2o2i9xPqhkmvw8J[[[[[[[[[NZAMrc[NZAMrcHgfSKl6An7
[NZAMrcTwbnjw/arehHBUerNDnRSFBZ4+4R9fmB3rra4rTQ3zc5XAihr6JzX0D3bVZTt6hGYUNQ8MD01PE6EcQr4u7pFD4H4BDUMPtbW1ra2tb+Xww9jb2wMZ45RDcXFxcPcNlFJdXR0o6/tZoQ4fug/KxbKnFbnkEIA+BGnHnmu8d/3OZ8P79LGlT2SYuz7iyqCDPoICT9k8Af94+PmFZMxDqsZJrdG2ssggKkbC2i9jiNqDkVLxnD6VcCcceeL/XVO/X7fP5ab67EzZFbgukSPXz84OEMht923xkBxujFW7YKT0XPwiouPIxPpwPmv2MJWb36EYXpCEF1IvxbC/COgem0J5WwLomfAIODzdDfVPT1GO3HY35uXUCDmt0km61omhj4RfAwX8dabIl5djVxbAXfnYfVGviE0eQXIy2lCnkUjGfwzgedKpUyMU8BplGZzE4AmiECvZRx58D5isElsPzuYgcGo1GJpM5MjIyMzPzsNyEuSAjKTQwMGN7MMvqT/fDS8dWCfyjI+VUXiLPqvS71leFlNPvXg5vBG8NziLNAaBDwLkAdi4UMbN0PvOQxRNJ4XwWE85nsgUShVzC57LoT1hZCHkCuKhcKjpgsLg8vlgKd3NoPl8gkkilYah97C9OD5clhD188JhigNhrs72jMxubFL5cTqtCy[[[[[64r/07dtVPQ8Lza4cIo9VBn4XxSH
[djGHX8LJSksCwshngcseRnpcbCKWnEG+uwdTWEMlLQt6BOhgvjYqiRuYyC9mtRWFZ98KIBls1myuSzZAnW+PWSi3ne0NqC/swrqEAKVgczMntqQ7B7d+s8/tf/Z5+5plaEuXkGJVVO8/+F4fG5ngY2KODN9eTFZEYE+Hq5OWjypyeTkjmFQ0q9X+7AMOOEfSIg7p2IQXNUuD/bFGx6y8/PLWvu7u7rG6gMja4qzkvub/DVUnHJzXFxda2AKysr6+vr6+CL1NbW5ufnl5WVra6ukob42w12
[image48]: <data:image/png;base64Q1qGHQnE/AdAqg8EArt3d9b0pjU6nJ5MIdrvRgGC7y2WUkHtiorPyBvbr3Q4QAWI8Xo9rf/vLO/0WI0dxPvyFy2kza6Xa728eOqAyh3AMlaNbNid1GATbI6vTx/vVfGS1SXOxz1IXdm2iubSJmkN02EmFd8iOy2WENiUPXjY2v7FeLcV3WPX9DdT5luRgv4Dyhp4NHmu+3O/KP3yYHuZ61zyQDNkhTrcSFNyVpihXL8/YkqbaiLimDZ7ioDPHH3IaVkRahjZMrayNtCb5BdjduBqc3jU53xYbl677mjWeFOpumEdlLYRlj/G++keyN1aS4dJQWxqWV11WVl6RF5OfmpidndU4RZ5szzd0CwoITawbXeWoo1dorr3GBdyKYKYibkzJaXa19fOu2ECjWKqRhYLQ5IcbJoegMG6ka5m4PZtj4jrcWBZmFt61yNE9OCfkWj1e3u3OSg4NCPKwfDB7u6nVYssRcSyx9TFdiEzqi/4dnKmKaiYNP3DD3m29apPkaTyKRsUneivT0qvWe+ITPQATnIYfdGAWdEMgouMbGpLTEiJSinqJ1O3Z+o8/uhVQjF1iCDnUqUhUYkHd6KZYAamWLtvayvqOtU9UzQSJxxmrj09yu3rWDBVcHWjrFFE4wpIB3Vp9FyrI+dINa7+U6m6KhDpblx9i/uChgzkm2jsgKG9KvLtv0Btok3WJSJ+CYTJ0Ee86sByePmA5NDmmlUPhUmN8ZERu96Zoa8E/v3tTwjXKYTPSJzygeGimK84nlCtca460v34WOaZiWpjF9lAZc205Hg8Qf3FuCMkc04Ge7aysE+3s60FMmlUgOm0PAUeVymQJcQxvIUyqVKkE7hSrwAFKJTK4Ez0gFLgADBEnlkMURlUIKJDiMIjncAoqyRKrTi5bb88MsEVVjVIVULJaAphmBBGCYDFwvFUqtANMBWcDtKQhYDk8fsByaHNPKYXuUj69t2jSbPl2f1IxfXWhPsvr3s/bxLb0lob42XvEFpenRfj2Uzdl69JX/9aVtulQKBSIZOIxCpwdIRYLJQoVBrQ8AXwaDJss/nr0R1Uxtw0QnxrWQhQJyX95Xn3x73zGhrD3hzv/7/5xxTuhaZP6g5wrzYWBaOdTtHaCRTsUzsoODvd39/eZ8lF9V61h1WsjDOM5sbcjj83+6eOG2rUPd9LZMTu5Icv7093+66prQQeTqwYGnMK+FSqfTrK4eXLny7D//56f/8N9ey/0j7D409w/P/v7/evaf/tOTR4+OyaFalYNOSC2f4h2+PdRo9c7iZc0f+YD7Pk0CZvPDXQUG7h3HAbXgdnF/OTnkEBPqx1kSoIewVp2IWN0htJSkRMXHJqCjKmdo+j1Wd0KIvZV/UVV5ThzC7tpdW/9EJnm0KCI4JAAoR3FJFdh1kUa1M1Uc+Sgntqh9fKavDh3k5h0TFuQVEFWQl1+Um+geljJI0+yrpGuD9XHxYX5u3ojCSbFhlzaSHxyTmYNBBHi4hmV16UVb2BoMCo2Mj8V04pe3yFM1Wanh8YnIsNR6okgtWm/N7
[image49]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAIQCAIAAADW+le3AACAAElEQVR4Xuy9dXgcV4Lo6/e+7/1x77d7Z/e+2ZmdhZmXmWRnMhOexI4pZhQzMzPaYmZmlmWLLGYmi5mZWmpSq5kZ61W17MSSA3YSJ9fZ88v54u5TdbBK9atTp6r6FJfUySH2SAQECBJBEBZHM7vkzC6dPL124RDJ1YFo+33CkjWJTnfW60/vcw8lHO3V+dy+aumalRaanwX1bWNvdsAwBx6Mvb8zWjpTHxmc3LcrFDKECGTM1EJLVLhgF9vTLHKnuAKyCNmfkFWB+AzyInmvvyg1EMm0Ao7cijWzSV2FEdd2UbzFysaE/zt7GwePnhg8p90K0JiKZfPpVDh8p4VskTMANHhdwboEACUucVqteL8TCF5dfxbiW6rkKAy1fm5Qi5F0Ffinw1NuSF+rs7ptdFZuZ35uLtW1aeqra2t7o7kxrFrfDM6XB8ZDnX3Q2dkt/PEUslcBfwxOjX0TonbmBsfmd3lziwsTXR0Dgy2NRJxGHxGDppJnVerICo2mso/fybUSGSLXR0Y1+tJETZJRMesHHB2lgDgdWBxcXHZAjqNw8LCOjo6pFLpZh1Rk61sztaiVjramJzWRlptU30j8wlFNtOByncqLic[[[[[[[[[tRsNPT[tRsNPT[tRsNPTDeg
[tRsNPT84b5/EsIjkCGAl+lJkZJKuC6/18WZ7vt32rY6hdwWBdP+q937vQ7v9skampqGa6L5E+MtaeX30o2MYhpQuHwg+lddz21//rSS17LmGZgh8ZBxS0d/QQi8anYIfLFHRxIhHJkaK9UMDwx8OgpzaFfCo2KZIf/foO1oxLVgKj4/44JupOfiRoTw/k6J5Ey2Gh203b4LZ53gRXtKzP9BICcalB7ykxaHAF84AD0OAK0IAD0OAK0DD3tMz8wlBmRXFwXmpvh5+8dUNWcFR5aGRdeNdRcOZ10zOXVgz7YdW3deC86fG59hSfmLS+Ue5ju3HN62ZcuWrdsP2RArOkJdr0ZeeO+vf3jjyyvJAYU9I3wBb47ka6ZhpLVtK/S57JQ/y20d76f154A9g4uCOS5fLuOxp+pdnNIiwtPa29MiosLv2JtbWV4/eIzgndLIhjMSHHEgUszumLtazobbd2t8ceTA7o+Oun5y5n4niztJG8z0vUAw0wAjth40y9QUVxSN8ng8yEu6DNEDZnEI8fDiIkdDTMCmXF3kCJYXeqpGWqqLi3oWBRIxWpsCqVClEnOl3NWhtgIQLKegPr+sc4SzJ+XOT0/M99HnOSKYSksleyzR9lxf//y2SMbfXBEuj3SXFkJLpeWVgLeue5LFnpmemaPT59e396C8TLQt4sxNjM1ti+VCqfBQubU03FtVVpCXExuBe3LJCTe0vsfki07kOyxYjuRDu8W5TQOdU2t7u6s89gKdNjs9vyFBhcReYCgrBpUHbcOLK8tIUYxL1HHp5RUU1uiEzeyDBs2to/snA/9daKAc4EDvgxQsAt0WoEGKQQO7Qwp2Bw70YkjfhQZqAQ52iEHDioEaIQNngWYwaOBFyMJ3eRn40Ao0h0GD1hnoLsHAB2ggHmRATjAlDL/AB/kBGsAB/gJKkAc+Bk0oFGKbSb35zP6fnn70cAjgkc/yi8WgMhpK9B9AUAxcB84CxSFfX1SpwN6gcS6XC8ZjowRlIA9MMB7wocOAYbAdrsLGBvksIeXhkls0V8gX0tBAzI1sTI2Pjx8aSetMYOVkS25WCvGmBTCBE+zoevPDgOq5qUa8Q2mkW0RqRmFlZVEePiWF8MS9YnxTKEJvuasDopp+fPoLCofrNDeHWF29xCGudBnC4UwVqzdWVyvE3jrI0Tn0lha+YWyWNjUYG0q4fw9fWkoogHCIi2pqwFvYkExtkvIIAX6fXjZ39TDB45JTyRFutZ1DqzN7QvkWtTQ+NirYz9vTxdFMV+NBdBAupLrU74F+eMsCm7E0uLNcH/3wprblc3MnFw8vMAmbzSEO89y2N0Lh06eGBnLe4VmwZ4OH1oTa+ojbF9+KZYM+YyLrNr786+lrWz+ijxBMa53cEyoMDleptONQleQVV0JloODQguXoVo3kIhyR7h8S24Upf7QvhZZTU/tWjVyfsSsv7jpEaVvG9LTH6BsllPYsjXMkRsjpEhAFfEW60+tzWCIlLw3fNSo+PWKU2Ae7eH2lGFHaU+l/+IsSLiK9i7cmOv1b0zC7lSEXOlI7b+cbi6emwvR0meWN3GDXjVM3nGpv5vbpBLgnVVyiRcikL2enu0Za/8yzumxdI0evmz+thoZjgEqwl+kR5RUH58znKLIOLD9Y3KksgIriMyYrY6LKMJ22jFDbx7YxT0Z8tXO7aAGPyWUpi2QiFvcbhf8evHwDAu+ddiEMqlYri0MzMbGtra3t7e8/uv0r1JZqoqKiXcShHcbjYElf/KFRNIzI8renNOMTv5kKRCnkO7439k2uQJx1froU0+oXudvc5DheHTW1IRnTZatFAfcv7K/VGTJP62dqy929PWmcmG3IDzbvl2cfWTSzPtWZOtd+fvH6+8/dZNN7e12eHTdcjlcpuamiYmJSPxC3[[[[[[fEi8fX3v38zOnqRw8EH6Bs31ve
[G1nPLN37z03aK5cl9heoVtZUq3PTVqfpl2yVObl4ZXDCMJHWIlGJjdOXr7gkFvWMTSh4qUFhzdraFR12jffCLS47lDy+Rw2c7bwPKA+FudX+6eOVivi8WsCg2MRWA+fmGmxTqsCdYRMIZfJeBuHE2yzhkQkq6eKWmqXXa3eMcmh7Ud9skMNn6QTCmkDJ7CmPjAp0Q3j5evggMYS+wdGqSOF2iC8rLigtqSwu7xpeEZ/vgujjr/ABWGyN98PNdK9c/f6xQtvve9HZqWxI0ODb334+Z34+jdecRZaXucEpQafadyUum0gzrDTiNaeDxVQ361qt3Z6JmpCuZoWNhHVBSleGSHWpFO3uK7Z2QEzRLJlDcWd+hPFXjuHXaysWbpAHHVAQe5aTs7Py/uYYq/M/HN2/c9eu3T/sO3ZU36ZCODagUPw4L+BWhX72pz+/819/fm3VqtdXrV7/6fmDhl6O+a0DI8Qu+BynIbkq3l5TO4LmkidHDtUFcqiKlccsnZc3VtdXlTc2dgl50jFiU6AYk04OVFWXFKWl5/fyxfPT3KGWnOaS+Ijw+JDI7PJ2fjtX3N/Z4X8gASxJxLBIMDA8SVHCSuplhOXkXlmo+ANzTjEOZTjweuAIqlMIh/vq8qvS49NLK1L6xQOdXKyMBgGh4Zam5ram5v1Op2+pYXIEzO0t
[image52]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAG3CAIAAADjC2x8AACAAElEQVR4Xuy9d3AbR77vu1X3/vHqVZ1767176753zjt3d8/u2bV3vbYsZ8mWJdlyDso5B0oixSTmnHPOOeccwQhmMIAJJEiCyAABEDnnDL4eQJIpkJQpW/Ja8nzqRxQ40z39m0HPfPvX09PzO90Lgl6vVygUy8vL9itgYGBgYGB+NrQq3qZL9Psoo2wYdHIZRKJajdJYWBgYH6bKJV8gddTHd6YPZ0j8ohh3ElecaYofwsqd5VD8731rwxez+asDxQ2jq1x1UZTa1L1DBcymlSsuQox/zpgpdw9IL+pfJgzlPFrmo9fn1NShwpZNwqYXtXj+sfdafyBxLJwwGoYbCuMQup8vYUhxcgw54dc82jY5xbpPZRFznCJo35CfGSAk5GDTwVoR79XBmbvWqQm1g2aBsZ9aWT8+ms3QxsaLr5CR9TYLsLO3+2Cv4dAcp17mz6I5xOk8G3s99sgA6PJ0AHerK3iGhVKsUMpqvUVzvgkKJ6EYuFomQHls1CoQ06Rjp81wmU28L6ePZVr/RyycIxEhzAJKINSWR3tAhqQRZDB7b1SGjNfay9YIYzpYyqaZGTQNCph3RLAJnU5mYh/e1yxhgSWRKmYhPGx7ra24ZJdFWpHKFTFM9XFa1JXJ4zbiUKBRJJBKpVLvZcEUSbT3Ihkjhosh2nMAGJJlMDgkJ9Cp6GzJMhs5UqpaYUUghGtI57EOwb7FU0PEvsHCYtieTaWZoFYDRjKqWmaoVSrYJrOihewH6OQIfIvTA4pbFdwKeWwRfdoi/aOHi08xI6G7561cSkVpLU2m1sbPaJfthl++A78VNxGGFUUcEVY8uLjh7vnTE6798e2DH03jeu5xwivjExO2NYnTY+bW12542vPC45x5mVMkHr8AQF0OEpB+hQV/blXRmfZJ3uXL9lHVY9vSOQf1vhCCAg4dLI5G36y9FxcupbW2N0cGhHvljFNm7U0MFhbYjYLXHn/3rTQOPO1eca9dpmByeBjA5PCqHWwbGCeNtvzs8kMPInCGSHOBT24K/NBLuKriECsff3c2aF4JCxkCK8dVbN0LaFvyNo3t2ACXEwQ8UJJdNk1k0Ok8gUqhGMiwvemVPEIR7e0/29jUquURC2doWK/mwOeito59e11MY628QIZGsNUUGhnhk9/bVxtfM0nkLJe6uSVX9LnoeJSNUKaigDEdnzVLWuhOMRfWkg3oP42xWOv9fLn6PZ6+h7JFf1TS5SuIgcTrOXWhOCA5yyJYKZYifXkOiWdSEYf9sqtmKWyiTNpD86c+aTD/90O3d+Z7ErFScFVWrmbH2Kn25Q89pqkENKz8ZsTbBfsG+ZhDeebe4Uk9kxM17ZuUyHnkBCWpPPe/cpc6UOV86ePXfdxLF0tilc51e//eCfZ85dNN2QAgo1CiRPdrhnElI6sNgRdeGL4OpIDhkgc8khDjJftzbtXvbJaZ9a7E+9bBBduqED6VJBSvbsHs69RYxfSieFN5VB7CeLx+zb7IQ[[[[H8FcCpchlEJ0LzaiorCzNz0c/iRemn
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

