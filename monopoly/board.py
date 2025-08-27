from rich.console import Console
Console = Console()

## board and tile setup

board = [ ## id borad that has a row that is loop into
    "Go",
    "Mediterranean Avenue",
    "Community Chest",
    "Baltic Avenue",
    "Income Tax",
    "Reading Railroad",
    "Oriental Avenue",
    "Chance",
    "Vermont Avenue",
    "Connecticut Avenue",
    "Jail",
    "St. Charles Place",
    "Electric Company",
    "States Avenue",
    "Virginia Avenue",
    "Pennsylvania Railroad",
    "St. James Place",
    "Community Chest",
    "Tennessee Avenue",
    "New York Avenue",
    "Free Parking",
    "Kentucky Avenue",
    "Chance",
    "Indiana Avenue",
    "Illinois Avenue",
    "B. & O. Railroad",
    "Atlantic Avenue",
    "Ventnor Avenue",
    "Water Works",
    "Marvin Gardens",
    "Go to Jail",
    "Pacific Avenue",
    "North Carolina Avenue",
    "Community Chest",
    "Pennsylvania Avenue",
    "Short Line Railroad",
    "Chance",
    "Park Place",
    "Luxury Tax",
    "Boardwalk"
]
property_colors = {
    "Mediterranean Avenue": "#A52A2A",
    "Baltic Avenue": "#A52A2A",
    "Oriental Avenue": "cyan",
    "Vermont Avenue": "cyan",
    "Connecticut Avenue": "cyan",
    "St. Charles Place": "magenta",
    "States Avenue": "magenta",
    "Virginia Avenue": "magenta",
    "St. James Place": "dark_orange",
    "Tennessee Avenue": "dark_orange",
    "New York Avenue": "dark_orange",
    "Kentucky Avenue": "red",
    "Indiana Avenue": "red",
    "Illinois Avenue": "red",
    "Atlantic Avenue": "yellow",
    "Ventnor Avenue": "yellow",
    "Marvin Gardens": "yellow",
    "Pacific Avenue": "green",
    "North Carolina Avenue": "green",
    "Pennsylvania Avenue": "green",
    "Park Place": "blue",
    "Boardwalk": "blue"
}




def real_board(board):

    Console.print("[mint_green]board[/mint_green]\n") ## board color
    for space in board:
        color = property_colors.get(space, "boal green")  # Default "boal greean" if not in dictionary (like Go, Jail, Chance, etc.)
        Console.print(f"[bold {color}]{space}[/bold {color}]")
real_board(board) ## calling out the board 



