###### README.md >> markdown.
###### v1.0.0 Initiale.

<div align="center">

# ⚡ testProjects
### *Modular CLI Toolbox & Background Process Runner*

[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-orange?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/GUI-CustomTkinter-orange?style=for-the-badge&logo=tkinter&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange?style=for-the-badge)](https://github.com/teremuhamblin/testProjects)
[![Version](https://img.shields.io/badge/Version-v1.0--stable-orange?style=for-the-badge)](https://github.com/teremuhamblin/testProjects/releases)
[![Security Audited](https://img.shields.io/badge/Security-Safe_Subprocess-orange?style=for-the-badge&logo=securityscorecard&logoColor=white)](#-sécurité--bonnes-pratiques)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Une suite logicielle modulaire conçue pour ORCHESTRER, PILOTER et AUTOMATISER vos *outils CLI et scripts favoris à travers une interface graphique moderne*, ergonomique et non bloquante.</b>
</p>

[Fonctionnalités](#-fonctionnalités-clés) • [Architecture](#-architecture--flux-dexécution) • [Sécurité](#-sécurité--bonnes-pratiques) • [Installation](#-installation--démarrage-rapide) • [Personnalisation](#-thèmes--customisation) • [Structure](#-structure-du-projet)

---

</div>

### 🎯 Vision du projet

*`testProjects`* *résout la fragmentation des scripts système, outils de pentest, converters ou compilateurs en ligne de commande*. Il offre un **wrapper graphique moderne** qui :
》》 1. Découvre automatiquement les binaires ou scripts déposés dans le répertoire dédié.
》》 2. Isole leur exécution dans des threads séparés pour garantir une interface **fluide et réactive** à 60 FPS.
》》 3. Stream en direct les logs console (*`stdout` / `stderr`*) dans un terminal graphique haute performance.

---

### ✨ Fonctionnalités clés

| Fonctionnalité | Statut | Description |
| :--- | :---: | :--- |
| **Interface Graphique Moderne** | 🟢 Prêt | Interface réactive propulsée par **CustomTkinter** avec support natif Dark/Light mode. |
| **Moteur Async Multi-Thread** | 🟢 Prêt | Exécution déportée évitant tout freeze de l'interface graphique. |
| **Streaming I/O en direct** | 🟢 Prêt | Lecture continue bufferisée ligne par ligne des sorties consoles (`stdout` & `stderr`). |
| **Hot-Reloading des Outils** | 🟢 Prêt | Rafraîchissement dynamique des exécutables présents dans `bin/` sans redémarrer l'application. |
| **Gestionnaire d'Interruption** | 🟢 Prêt | Bouton d'arrêt d'urgence envoyant un signal de terminaison propre (`SIGTERM`). |
| **Module Outil 1** | 🟡 En cours | *[Spécifiez ici le rôle du premier outil tiers]* |
| **Module Outil 2** | 🟡 En cours | *[Spécifiez ici le rôle du deuxième outil tiers]* |

---

### 🏗 Architecture & Flux d'exécution
- 》》 **.github/workflows/**
- **VOIR docs/ARCHITECTURE.md**
- **VOIR docs/STRUCTURE.md**
- **VOIR LICENSE**

### 1. Diagramme de composants

*Le schéma ci-dessous illustre le découplage strict entre la vue graphique (GUI) et le moteur de processus* :

```mermaid
graph TD
    subgraph UI_Layer [" Couche Présentation (CustomTkinter) "]
        A[main.py] -->|1. Sélection outil + arguments| B(Contrôleur UI)
        B -->|2. Requête d'exécution| C[ProcessRunner Engine]
        D[Console Log Window] <---|5. Mise à jour UI thread-safe via after()| C
    end

    subgraph Core_Layer [" Moteur d'exécution asynchrone "]
        C -->|3. Spawn thread daemon| E[Worker Thread]
        E -->|4. Pipe I/O en direct| F[Subprocess Popen]
    end

    subgraph Binaries [" Espace Outils & Scripts "]
        F --> G[bin/tool1.exe]
        F --> H[bin/script.py]
        F --> I[bin/utility.bat]
    end

    classDef ui fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef core fill:#111827,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef bin fill:#374151,stroke:#f59e0b,stroke-width:2px,color:#fff;
    class A,B,D ui;
    class C,E,F core;
    class G,H,I bin;
```
