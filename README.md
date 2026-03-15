# 🎮 Pokémon Pixel Battle

A retro-style **pixel battle game** built with **Python 3.12** and **Pygame**.

In this game, you play as a **Pokémon** and battle against other Pokémon opponents one by one. Your goal is to defeat as many enemies as possible and get the **highest score** before all available Pokémon on your side are defeated.

## ✨ Features

- Pixel-art battle style
- Turn-based Pokémon battles
- Four random abilities
- Element-based damage system
- Menu navigation with keyboard controls
- Smooth and pleasant animations
- Score system based on defeated opponents

## 🕹️ Gameplay

You control a Pokémon and choose abilities from the battle menu to attack your opponent.

Each turn, you can select one of **four random abilities**. The amount of damage depends on:

- the **element of the selected ability**
- the **element of your opponent**
- the **basic** ability damage

This means choosing the right move can deal **extra damage** and help you win battles more efficiently.

The main objective is to:

1. Defeat as many enemy Pokémon as possible
2. Increase your score
3. Continue battling until all Pokémon available to you are defeated

## ⌨️ Controls

Use the keyboard to navigate the game menu:

- **Arrow keys** — move through the menu
- **Space** — select
- **Esc** — go back

## 🛠️ Built With

- **Python 3.12**
- **Pygame**

## 📦 Installation

These instructions work on **Windows, Linux, and macOS**.

### 1. Clone or download the project

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Or simply download the project as a ZIP archive and extract it.

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the game

#### Windows

```bash
python code/main.py
```

#### Linux / macOS

```bash
python3 code/main.py
```

## 📌 Notes

- Make sure **Python 3.12** is installed on your system
- It is recommended to use a **virtual environment** to avoid dependency conflicts
- The game requires **Pygame** to run correctly

---

**Have fun battling and set the highest score possible! ⚡**
