from rich.console import Console
from tile import Tile

console = Console()

# Monopoly board tiles
def board():
    return [
        Tile("Go", 0, "go"),
        Tile("Mediterranean Avenue", 1, "property", 60, 2),
        Tile("Community Chest", 2, "community"),
        Tile("Baltic Avenue", 3, "property", 60, 4),
        Tile("Income Tax", 4, "tax"),
        Tile("Reading Railroad", 5, "property", 200, 25),
        Tile("Chance", 7, "chance"),
        Tile("Jail", 10, "jail"),
        Tile("Ventnor Avenue", 27, "property", 260, 22),
    ]
