# Simple Monopoly Game

A simple console-based Monopoly game in Python using **Rich** for styling and **SQLite** for persistent player data.

---

## Features

- Play with 2–4 players.
- Roll dice and move around the board.
- Buy properties and pay rent.
- Jail, Chance, and Community Chest placeholders.
- Player data saved to an SQLite database.
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

This README is concise and explains setup, running the game, and the project structure.  

I can also make a **rich version of this README** that displays as a styled console banner when you start `main.py`, if you want. Do you want me to do that?






You said:
naaah This is not good 


ChatGPT said:
Got it! Let’s make a clean, simple, beginner-friendly README that matches your “Simple Monopoly” project style. Here’s a revised version:

markdown
Copy code
# Simple Monopoly Game

A small, console-based Monopoly game in Python.  
Players can roll dice, move around the board, buy properties, and pay rent. Player data is saved to an SQLite database, and output is styled with Rich.

---

## Features

- 2–4 players
- Roll dice and move around the board
- Buy properties and pay rent
- Jail, Chance, and Community Chest spaces
- Player data stored in SQLite database
- Styled output using Rich

---

## Requirements

- Python 3.8 or higher
- [Rich](https://pypi.org/project/rich/)

Install Rich:

```bash
pip install rich
How to Play
Initialize the database:

bash
Copy code
python db.py
Start the game:

bash
Copy code
python main.py
Enter the number of players and their names when prompted.

Press Enter each turn to roll dice and follow on-screen instructions.

Project Structure
bash
Copy code
Monopoly_python_project/
├── monopoly/
│   ├── main.py       # Game entry point
│   ├── player.py     # Player class
│   ├── tile.py       # Tile class
│   ├── board.py      # Board layout and printing
│   ├── db.py         # Database functions
├── requirements.txt  # Dependencies (Rich)
└── README.md         # This file
Notes
The game ends when only one player has money remaining.

Chance and Community Chest spaces are currently placeholders.

This project is meant to be simple and educational.

pgsql
Copy code
