# main.py
import random
from player import Player
from tile import Tile
from cards import draw_chance, draw_community_chest
from board import board, print_board  # board is the list of names; print_board is optional styling

def setup_players():
    players = []
    while True:
        try:
            num = int(input("Enter number of players (2–4): ").strip())
            if 2 <= num <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    for i in range(num):
        name = input(f"Enter name for Player {i+1}: ").strip() or f"Player{i+1}"
        players.append(Player(name))
    return players

def setup_tiles():
    tiles = []
    for i, name in enumerate(board):
        # simple type inference from name
        if any(k in name for k in ["Avenue", "Gardens", "Place", "Boardwalk", "Park Place"]):
            # simple placeholder pricing
            price = 100 + (i % 10) * 10
            rent = 10 + (i % 10) * 2
            tiles.append(Tile(name, i, "property", price=price, rent=rent))
        elif any(k in name for k in ["Railroad", "Company", "Works"]):
            tiles.append(Tile(name, i, "property", price=200, rent=25))
        elif "Tax" in name:
            tiles.append(Tile(name, i, "tax"))
        elif name == "Chance":
            tiles.append(Tile(name, i, "chance"))
        elif name == "Community Chest":
            tiles.append(Tile(name, i, "community"))
        elif name == "Jail":
            tiles.append(Tile(name, i, "jail"))
        elif name == "Go to Jail":
            tiles.append(Tile(name, i, "go_to_jail"))
        elif name == "Go":
            tiles.append(Tile(name, i, "go"))
        else:
            tiles.append(Tile(name, i, "other"))
    return tiles

def handle_card(player, card_tuple, tiles_len):
    text, action, value = card_tuple
    print(f"Card: {text}")
    if action == "move":
        # moving directly: collect $200 if we pass Go
        old_pos = player.position
        player.position = value % tiles_len
        if player.position < old_pos:
            player.money += 200
            print(f"{player.name} passed GO and collected $200.")
    elif action == "money":
        player.money += value
        if value >= 0:
            print(f"{player.name} received ${value}.")
        else:
            print(f"{player.name} paid ${-value}.")
    elif action == "jail":
        # simple jail: move to 10 and mark jailed for 2 turns if your Player supports it
        if hasattr(player, "go_to_jail"):
            print(player.go_to_jail())
        else:
            player.position = 10
            print(f"{player.name} sent to Jail.")

def take_turn(player, tiles):
    input(f"\n{player.name}, press Enter to roll dice...")
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    roll = d1 + d2
    print(f"{player.name} rolled {d1} + {d2} = {roll}")

    # move (handle pass GO in your Player.move if you implemented it)
    if hasattr(player, "move"):
        # If your Player.move expects board_size:
        try:
            msg = player.move(roll, len(tiles))
            if msg:
                print(msg)
        except TypeError:
            # fallback if your Player.move only takes steps
            player.move(roll)
    else:
        player.position = (player.position + roll) % len(tiles)

    tile = tiles[player.position]
    print(f"{player.name} landed on {tile.name}")

    # Tile logic
    if tile.tile_type == "property":
        if tile.owner is None:
            choice = input(f"Do you want to buy {tile.name} for ${tile.price}? (y/n): ").strip().lower()
            if choice == "y":
                print(tile.buy(player))
        else:
            print(tile.pay_rent(player))

    elif tile.tile_type == "tax":
        tax = 100
        print(f"{player.name} pays ${tax} tax.")
        # Prefer using Player.pay if available
        if hasattr(player, "pay"):
            player.pay(tax)
        else:
            player.money -= tax

    elif tile.tile_type == "chance":
        card = draw_chance()
        handle_card(player, card, len(tiles))

    elif tile.tile_type == "community":
        card = draw_community_chest()
        handle_card(player, card, len(tiles))

    elif tile.tile_type == "go_to_jail":
        if hasattr(player, "go_to_jail"):
            print(player.go_to_jail())
        else:
            player.position = 10
            print(f"{player.name} sent to Jail.")

    elif tile.tile_type == "go":
        # Optional: award when landing on Go (rules vary)
        pass

    elif tile.tile_type == "jail":
        print(f"{player.name} is just visiting Jail.")

def play_game():
    # Show board styling if your board.py has it
    try:
        print_board()
    except Exception:
        pass

    tiles = setup_tiles()
    players = setup_players()

    # Simple loop: keep playing until someone hits $0 or less
    while True:
        for p in players:
            if p.money <= 0:
                print(f"\n{p.name} is bankrupt! Game over.")
                return
            take_turn(p, tiles)
            print(f"{p.name} now has ${p.money}")

if __name__ == "__main__":
    play_game()
