# yami
# 🪽 Projet Cosplay Yami - Ailes motorisées avec télécommande

Ce projet permet de construire et programmer un système d'ailes motorisées pour un cosplay (inspiré de Yami - *To Love-Ru*). Les ailes s’ouvrent et se ferment automatiquement à l’aide d’une télécommande ou d’un bouton, contrôlées par une carte Arduino.

---

## 🔧 Matériel nécessaire

### Electronique
- 1x Arduino Uno ou Nano
- 2x Servomoteurs (MG996R ou SG90)
- 1x Bouton poussoir ou télécommande RF (433 MHz ou 2.4 GHz)
- 1x Résistance 10kΩ (si bouton)
- Fils de connexion, breadboard
- Batterie 5V ou Powerbank (ou alimentation USB)

### Structure
- Armature d’ailes (PLA, mousse EVA, aluminium léger…)
- Système d’articulation ou bras mécanique
- Harnais ou support dorsal

---

## 💻 Développement en local avec Visual Studio Code

### 1. Prérequis

#### a. Installer le logiciel
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Visual Studio Code](https://code.visualstudio.com/)

#### b. Extensions VSCode
- Ouvrir VSCode
- Installer l’extension : `Arduino` (par Microsoft)

#### c. Configuration
Dans les **paramètres VSCode (`Ctrl + ,`)**, ajouter dans `settings.json` :

```json
"arduino.path": "C:\\Program Files (x86)\\Arduino",
"arduino.defaultBaudRate": 9600
