from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import random

from player import Player
from board import board
from db import init_db, save_player, load_players

console = Console()

def display_players(players):
    table = Table(title="🏦 Monopoly Game - Players")
    table.add_column("Name", style="cyan")
    table.add_column("Money", justify="right", style="green")
    table.add_column("Position", justify="right", style="magenta")
    table.add_column("Properties", style="yellow")

    for p in players:
        props = ", ".join([prop.name for prop in p.properties]) if p.properties else "-"
        table.add_row(p.name, f"${p.money}", str(p.position), props)

    console.print(table)

def take_turn(player, board, players):
    if player.in_jail:
        console.print(f"[red]{player.name} is in jail![/red] (turns left: {player.jail_turns})")
        player.move(0)
        return

    input(f"\n🎲 {player.name}, press ENTER to roll the dice... ")
    dice = random.randint(1, 6) + random.randint(1, 6)
    console.print(f"{player.name} rolled a [bold cyan]{dice}[/bold cyan]!")

    result = player.move(dice)
    console.print(result)

    tile = board[player.position % len(board)]
    if tile.tile_type == "property":
        if tile.owner is None:
            choice = Prompt.ask(f"Do you want to buy {tile.name} for ${tile.price}? (y/n)", choices=["y", "n"])
            if choice.lower() == "y":
                console.print(tile.buy(player))
        else:
            console.print(tile.pay_rent(player))
    elif tile.tile_type == "tax":
        console.print(f"{player.name} pays $100 tax")
        player.money -= 100
    elif tile.tile_type == "jail":
        console.print(f"{player.name} is just visiting Jail.")
    elif tile.tile_type in ["chance", "community"]:
        console.print(f"{player.name} landed on {tile.tile_type.title()} - no action implemented yet.")

def main():
    console.print("[bold green]🎲 Welcome to Simple Monopoly![/bold green]")
    init_db()
    players = load_players()
    if not players:
        num_players = int(Prompt.ask("How many players?", choices=["2", "3", "4"], default="2"))
        for i in range(num_players):
            name = Prompt.ask(f"Enter name for player {i+1}")
            players.append(Player(name))
        for p in players:
            save_player(p)

    game_board = board()
    turn = 0
    while True:
        console.print("\n" + "="*50)
        display_players(players)
        current_player = players[turn % len(players)]
        take_turn(current_player, game_board, players)

        for p in players:
            save_player(p)

        active_players = [p for p in players if p.money > 0]
        if len(active_players) == 1:
            console.print(f"\n🏆 [bold yellow]{active_players[0].name}[/bold yellow] wins the game!")
            break
        turn += 1

if __name__ == "__main__":
    main()
