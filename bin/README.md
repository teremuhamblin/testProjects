# Switch Utilities Toolkit

Boîte à outils d'utilitaires pour la manipulation de fichiers, la conversion et la création de paquets pour Nintendo Switch.

---

## 🛠️ Description des outils

### 📦 Conversion & Empaquetage
* **`4nxci.exe`** : Convertit les sauvegardes de jeux au format `.xci` (cartouche) en fichiers `.nsp` installables sur la console.
* **`hacbrewpack.exe`** : Permet de compiler et d'empaqueter des homebrews (fichiers `.nro`) sous forme de `.nsp` (forwarders ou applications installables sur le menu Home).
* **`renxpack.exe`** : Décompresse, patche et ré-empaquette les jeux/mises à jour `.nsp` pour contourner les prérequis de version de firmware (abaisse le firmware requis).

### 🔍 Extraction & Analyse
* **`hactool.exe`** : Outil en ligne de commande pour inspecter, décrypter et extraire les formats de fichiers Nintendo Switch (NCA, XCI, RomFS, ExeFS, etc.).
* **`hactoolnet.exe`** : Version réécrite en .NET de *hactool*, offrant des fonctionnalités modernes et rapides d'extraction/déchiffrement.
* **`hptnacp.exe`** : Outil de lecture et manipulation des fichiers `.nacp` (métadonnées des titres : nom du jeu, auteur, version, etc.).

### 💾 Formatage
* **`guiformat.exe`** (FAT32 Format) : Utilitaire Windows simple pour formater les cartes microSD (même supérieures à 32 Go) en **FAT32**, le format recommandé pour la Switch afin d'éviter la corruption de données.

---

## 📁 Fichiers complémentaires & Ressources

* **`fw_nca_mapping.csv`** : Fichier de correspondance associant les identifiants NCA aux versions respectives du firmware officiel.
* **Fichiers `nro_fw_*`** (`nro_fw_main`, `.npdm`, images et animations) : Modèles et ressources de base (templates) nécessaires pour la génération de **forwarders NRO** (raccourcis d'homebrews directement sur le menu principal de la console).

---

> ⚠️ **Note :** La plupart des outils de déchiffrement (`hactool`, `4nxci`, `renxpack`) nécessitent vos propres clés d'authentification (`prod.keys` / `keys.dat`) extraites légalement de votre console pour fonctionner.
