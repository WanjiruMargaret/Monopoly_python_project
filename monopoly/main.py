from board import print_board, board
from player import Player
from tile import Tile
from cards import draw_chance, draw_community_chest
import random

def setup_tiles():
    tiles = []
    for i, space in enumerate(board):
        if "Avenue" in space or "Gardens" in space or "Place" in space or "Boardwalk" in space or "Park Place" in space:
            tiles.append(Tile(space, i, "property", price=100 + i*2, rent=10 + i))
        elif "Railroad" in space or "Company" in space or "Works" in space:
            tiles.append(Tile(space, i, "property", price=150, rent=25))
        elif "Tax" in space:
            tiles.append(Tile(space, i, "tax"))
        elif space in ["Chance"]:
            tiles.append(Tile(space, i, "chance"))
        elif space in ["Community Chest"]:
            tiles.append(Tile(space, i, "community"))
        elif space == "Jail":
            tiles.append(Tile(space, i, "jail"))
        elif space == "Go to Jail":
            tiles.append(Tile(space, i, "go_to_jail"))
        else:
            tiles.append(Tile(space, i, "other"))
    return tiles

def take_turn(player, tiles):
    roll = random.randint(1, 6) + random.randint(1, 6)
    print(f"{player.name} rolled {roll}")
    print(player.move(roll, len(tiles)))

    current_tile = tiles[player.position]
    print(f"Landed on {current_tile.name}")

    if current_tile.tile_type == "property":
        if not current_tile.owner:
            decision = random.choice([True, False])
            if decision:
                print(current_tile.buy(player))
        else:
            print(current_tile.pay_rent(player))

    elif current_tile.tile_type == "tax":
        print(player.pay(100))

    elif current_tile.tile_type == "chance":
        card = draw_chance()
        print(f"Chance Card: {card[0]}")
        handle_card(player, card)

    elif current_tile.tile_type == "community":
        card = draw_community_chest()
        print(f"Community Chest Card: {card[0]}")
        handle_card(player, card)

    elif current_tile.tile_type == "go_to_jail":
        print(player.go_to_jail())

def handle_card(player, card):
    action, effect = card[1], card[2]
    if action == "move":
        player.position = effect
        print(f"{player.name} moves to {effect}")
    elif action == "money":
        player.money += effect
        print(f"{player.name}'s money is now ${player.money}")
    elif action == "jail":
        print(player.go_to_jail())

def main():
    print_board()
    tiles = setup_tiles()

    p1 = Player("Alice")
    p2 = Player("Bob")
    players = [p1, p2]

    for turn in range(5):
        print(f"\n--- Turn {turn+1} ---")
        for player in players:
            take_turn(player, tiles)
            print(player)

if __name__ == "__main__":
    main()
