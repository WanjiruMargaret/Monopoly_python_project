from player import Player

def main():
    # Create 2 players
    p1 = Player("Maggie")
    p2 = Player("Yuffi")

    print("\n--- Starting Game State ---")
    print(p1)
    print(p2)

    # Move players
    print("\n--- Movement ---")
    p1.move(5, 40)   # move 5 steps on a 40-tile board
    print(p1)
    p2.move(12, 40)  # move 12 steps
    print(p2)

    # Passing GO
    print("\n--- Passing GO ---")
    p1.move(40, 40)  # full board loop
    print(p1)

    # Payments
    print("\n--- Payments ---")
    p1.pay(200, p2)  # Maggie pays Yuffi
    print(p1)
    print(p2)

    # Earn money
    print("\n--- Earnings ---")
    p2.earn(500)
    print(p2)

    # Jail
    print("\n--- Jail ---")
    p1.go_to_jail(10)   # send Maggie to tile 10
    print(p1)
    p1.release_from_jail()
    print(p1)

    # Bankruptcy
    print("\n--- Bankruptcy ---")
    p1.pay(99999)  # force bankruptcy
    print(p1)

if __name__ == "__main__":
    main()
