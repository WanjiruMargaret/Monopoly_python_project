import random

class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0

    def move(self, steps, board_size=40):
        if self.in_jail:
            self.jail_turns -= 1
            if self.jail_turns <= 0:
                self.in_jail = False
            return f"{self.name} is in jail and cannot move."
        self.position = (self.position + steps) % board_size
        return f"{self.name} moved to position {self.position}"

    def pay(self, amount, receiver=None):
        if self.money >= amount:
            self.money -= amount
            if receiver:
                receiver.money += amount
        else:
            self.money = 0
            return f"{self.name} is bankrupt!"

    def go_to_jail(self):
        self.in_jail = True
        self.position = 10
        self.jail_turns = 2
        return f"{self.name} was sent to Jail!"

    def __str__(self):
        return f"{self.name} | Money: ${self.money} | Position: {self.position} | Properties: {[p.name for p in self.properties]}"
