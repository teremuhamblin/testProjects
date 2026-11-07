# Mon Projet Test - testProjects v1.0
- Développement du concept en **Python / CustomTkinter**
- *Boîte à outils tout-en-un*

*Une boîte à outils modulaire* permettant de **centraliser et d'automatiser des scripts et utilitaires CLI via une interface graphique simple**.

### ✨ Fonctionnalités
- [x] Interface graphique moderne et réactive (CustomTkinter)
- [x] Exécution asynchrone des processus (sans gel de l'interface)
- [x] Console intégrée pour afficher les logs en temps réel
- [ ] Outil 1 : [Décrivez l'outil 1]
- [ ] Outil 2 : [Décrivez l'outil 2]

## 📁 Structure du projet

```text
testProjects/
│
├── bin/                   # Vos exécutables (.exe / scripts CLI)
│   └── (placez vos outils ici : tool1.exe, script.py, etc.)
│
├── src/                   # Code source de l'interface
│   ├── __init__.py
│   ├── main.py            # Point d'entrée CustomTkinter
│   └── process_runner.py  # Moteur d'exécution multi-threadé
│
├── assets/                # Logos, icônes, images
│   └── icon.ico
│
├── .gitignore             # Exclusion des fichiers temporaires et caches
├── README.md              # Documentation du projet
└── requirements.txt       # Dépendances Python
