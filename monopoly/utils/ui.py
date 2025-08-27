# utils/ui.py
# simple colored print helper using rich

from rich.console import Console

console = Console()

def print_colored(text, color="white"):
    # color can be things like "red", "green", "bold yellow", "cyan", etc.
    console.print(text, style=color)
