# game.py
# Emmanuel: Game state + turn manager (core engine of the Monopoly game)

import random
from monopoly.board import Board
from player import Player
from card import draw_chance_card, draw_community_card
from utils.ui import print_colored

class Game:
    def __init__(self, player_names):
        """
        Initialize the game with players and the board.
        """
        self.players = [Player(name) for name in player_names]  # create player objects
        self.board = Board()                                   # create the board
        self.current_player_index = 0                          # keep track of whose turn it is
        self.running = True                                    # game loop control

    def roll_dice(self):
        """
        Roll two dice and return their values and the total.
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2, d1 + d2

    def next_turn(self):
        """
        Move to the next player's turn.
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self):
        """
        Get the player whose turn it is.
        """
        return self.players[self.current_player_index]

    def play_turn(self):
        """
        Play one full turn for the current player:
        - Roll dice
        - Move player
        - Handle the tile they land on
        - Check for bankruptcies
        """
        player = self.get_current_player()
        print_colored(f"\n🎯 It's [bold]{player.name}[/bold]'s turn!", "cyan")

        # Roll dice
        d1, d2, total = self.roll_dice()
        print_colored(f"🎲 {player.name} rolled [bold yellow]{d1}[/bold yellow] + [bold yellow]{d2}[/bold yellow] = [bold yellow]{total}[/bold yellow]", "yellow")

        # Move player around the board
        player.move(total, len(self.board.tiles))
        current_tile = self.board.tiles[player.position]
        print_colored(f"📍 {player.name} landed on [bold magenta]{current_tile.name}[/bold magenta]", "magenta")

        # Handle tile types
        if current_tile.type == "chance":
            print_colored("🎴 Drawing a Chance card...", "bold cyan")
            draw_chance_card(player)
        elif current_tile.type == "community":
            print_colored("🃏 Drawing a Community Chest card...", "bold cyan")
            draw_community_card(player)
        elif current_tile.type == "tax":
            player.money -= 100
            print_colored(f"💸 {player.name} paid 100 in taxes!", "bold red")

        # Check if player is bankrupt
        if player.money <= 0:
            print_colored(f"⚠️ {player.name} is bankrupt and removed!", "bold red underline")
            self.players.remove(player)

            # If only one player left → they win
            if len(self.players) == 1:
                self.running = False
                print_colored(f"\n🏆 {self.players[0].name} WINS THE GAME!", "bold green")
                return

        # End the turn and go to next player
        self.next_turn()

    def start(self):
        """
        Start the main game loop (core engine).
        The loop continues until there is only one player left.
        """
        print_colored("🎮 Starting Monopoly Game!", "bold cyan")
        while self.running:
            self.play_turn()
        print_colored("🎮 Game Over!", "bold red")
        