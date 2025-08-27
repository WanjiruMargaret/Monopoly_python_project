class Player:
    def __init__(self, name, starting_money=1500):
        self.name = name
        self.money = starting_money
        self.position = 0  # start at GO
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.bankrupt = False

    def move(self, steps, board_size):
        """Move player around the board"""
        if self.in_jail:
            print(f"{self.name} is in Jail and cannot move.")
            return

        old_position = self.position
        self.position = (self.position + steps) % board_size

        # Passed GO → collect $200
        if self.position < old_position:
            self.money += 200
            print(f"{self.name} passed GO and collected $200!")

    def pay(self, amount, recipient=None):
        """Pay money to bank or another player"""
        if self.money >= amount:
            self.money -= amount
            if recipient:
                recipient.money += amount
            print(f"{self.name} paid ${amount}")
        else:
            self.go_bankrupt()

    def earn(self, amount):
        """Earn money (salary, rent, card effect, etc.)"""
        self.money += amount
        print(f"{self.name} received ${amount}")

    def go_to_jail(self, jail_position):
        """Send player to Jail"""
        self.position = jail_position
        self.in_jail = True
        self.jail_turns = 3
        print(f"{self.name} has been sent to Jail!")

    def release_from_jail(self):
        """Release player from Jail"""
        self.in_jail = False
        self.jail_turns = 0
        print(f"{self.name} is free from Jail!")

    def go_bankrupt(self):
        """Handle bankruptcy"""
        self.money = 0
        self.bankrupt = True
        self.properties.clear()
        print(f"{self.name} has gone bankrupt!")

    def __str__(self):
        return f"{self.name} | Money: ${self.money} | Position: {self.position} | Properties: {len(self.properties)}"