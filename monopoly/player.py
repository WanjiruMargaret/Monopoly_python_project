class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0
        self.in_jail = False
        self.jail_turns = 0
        # list of Tile objects (from tile.py)
        self.properties = []

    # -------- GAME LOGIC METHODS ---------- #
    def move(self, steps, board_size=40):
        if self.in_jail:
            self.jail_turns -= 1
            if self.jail_turns <= 0:
                self.in_jail = False
                return f"{self.name} has served their jail time and is free!"
            return f"{self.name} is in jail for {self.jail_turns} more turn(s)."
        self.position = (self.position + steps) % board_size
        return f"{self.name} moved to position {self.position}"

    def pay(self, amount, receiver=None):
        if self.money >= amount:
            self.money -= amount
            if receiver:
                receiver.money += amount
            return f"{self.name} paid ${amount}{' to ' + receiver.name if receiver else ''}."
        else:
            self.money = 0
            return f"{self.name} is bankrupt!"

    def go_to_jail(self):
        self.in_jail = True
        self.position = 10  # Jail tile index
        self.jail_turns = 2
        return f"{self.name} was sent to Jail!"

    def __repr__(self):
        return f"<Player(name='{self.name}', money={self.money}, position={self.position}, in_jail={self.in_jail})>"

    def __str__(self):
        owned_props = [prop.name for prop in self.properties] if self.properties else []
        return (
            f"{self.name} | Money: ${self.money} | "
            f"Position: {self.position} | "
            f"Properties: {owned_props if owned_props else 'None'}"
        )
