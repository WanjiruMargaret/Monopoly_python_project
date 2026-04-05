# Simple Monopoly Game

A simple console-based Monopoly game in Python using **Rich** for styling and **SQLite** for persistent player data.

---

## Features

- Play with 2–4 players.
- Roll dice and move around the board.
- Buy properties and pay rent.
- Jail, Chance, and Community Chest placeholders.
- Player data saved to an SQLAchemy database.
- Styled output using Rich tables and console formatting.

---

## Requirements

- Python 3.8+
- Rich (`pip install rich`)

---

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd Monopoly_python_project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Initialize the database:

bash
Copy code
python db.py
Start the game:

bash
Copy code
python main.py
Follow prompts to add players and play turns.

Folder Structure
css
Copy code
Monopoly_python_project/
├── monopoly/
│   ├── __init__.py
│   ├── main.py
│   ├── player.py
│   ├── tile.py
│   ├── board.py
│   ├── db.py
├── requirements.txt
└── README.md
Notes
Properties, rent, and taxes are simplified.

Chance and Community Chest tiles currently have no effect.

Game ends when only one player has money remaining.

License
MIT License

pgsql
Copy code


markdown
Copy code
```
