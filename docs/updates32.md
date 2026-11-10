###### docs/updates32.txt >> markdown 
# testProjects

### 1. Contexte général
Ce fichier est un manifeste de vérification d'intégrité / de mise à jour (manifest update) pour la version 32 bits de SAK (Switch Army Knife), une boîte à outils populaire sur Windows dédiée à la gestion, la conversion et le modding de fichiers pour Nintendo Switch.
Chaque ligne associe une empreinte de hachage (SHA-1 au format hexadécimal préfixé par 0x) au chemin relatif du fichier correspondant.

### 2. Statistiques clés
Nombre total d'éléments : 18 fichiers.
Répartition :
2 fichiers à la racine (SAK.exe et la documentation).
16 fichiers et dépendances situés dans le dossier bin\.

### 3. Principaux composants répertoriés
> Exécutable principal :
- SAK.exe : L'interface principale du programme Switch Army Knife.

> Outils et utilitaires (dans bin\) :
- hactool.exe & hactoolnet.exe : Outils d'extraction, déchiffrement et analyse de fichiers Nintendo Switch (NCA, XCI, NSP).
- 4nxci.exe & renxpack.exe : Outils de conversion (ex. XCI vers NSP) et de repackaging.
- hacbrewpack.exe : Outil de création de paquets NSP pour le homebrew.
- squirrel.exe : Dépendance utilitaire (souvent liée aux scripts de traitement de titres Switch/Nut).
- guiformat.exe : Utilitaire de formatage de cartes SD en FAT32.
- hptnacp.exe : Éditeur/analyseur de métadonnées NACP (titre, icône, auteur).

> Fichiers de modèles & forwarders (bin\nro_fw_*) :
- nro_fw_main, .npdm, .png, .gif : Fichiers modèles (logos, animations de démarrage et binaires) servant à créer des forwarders (raccourcis installables pour lancer des homebrews .nro depuis le menu principal de la console).

> Données, licences et documentation :
- fw_nca_mapping.csv : Table de correspondance entre firmwares et fichiers NCA.

> Fichiers de licences open source (4nxci_LICENSE, renxpack_LICENSE, hacbrewpack_LICENSE).
- liesmich_readme.txt : Fichier d'aide et d'instructions (en allemand/anglais).

### 4. Utilité technique
Ce manifeste permet à l'application (ou à un script de mise à jour) de comparer l'empreinte de chaque fichier local avec celle indiquée : si un hash ne correspond pas ou si un fichier est manquant, il est téléchargé ou réparé automatiquement.

0x2e2c9fc487e0ce3d964627041ce98c94771d529b bin\4nxci.exe

0xe1530fe47f34bfb18c7c01ce60010c7ff80652dd bin\guiformat.exe

0x0baccd07aac5a73f31b39173b8ed50e9065b3164 bin\hactool.exe

0x9be937331cd20d1ae0bdbf7bfa5d469eeeaf8ca5 bin\hactoolnet.exe

0xdf5131a26c6b18506275ebacc6c64dd029a119dc bin\renxpack.exe

0x3bd253fef6a3827e0b338b0c2db7cbd5d587a526 bin\squirrel.exe

0x14776056840eb8480ef456bd31d39bdea98b2f8e bin\hacbrewpack.exe

0xfe1c6bb5735bda2b86dc0cbe261966aea9132c56 bin\hptnacp.exe

0x9646e1f3e30be08f68c542739e1d0c0548f0d82a bin\nro_fw_main

0x6a65901ec2aa474c2e7605483ddd15052d53ba0b bin\nro_fw_main.npdm

0xd86be480d755ebf69809d256318bfef17051ce8b bin\nro_fw_NintendoLogo.png

0xd96fd2e48964adea1464ede0a1290cf39119c657 bin\nro_fw_StartupMovie.gif

0x21fe8a2cb89ead5f4439a7ac46f24166f16253ef bin\4nxci_LICENSE

0x79cf7ce731d839627a849be837760ecb656041e3 bin\renxpack_LICENSE

0x4cc77b90af91e615a64ae04893fdffa7939db84c bin\hacbrewpack_LICENSE

0xdf2acb3f2b0190da467ef0f5644b1cfb548dc5a2 bin\fw_nca_mapping.csv

0x451ae3a1870776ab617858b3d3c3e9ff032ad689 liesmich_readme.txt

0xa9153aebdc0924f182cf0cf688d90de96f0eed16 SAK.exe
