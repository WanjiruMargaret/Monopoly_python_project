class Tile:
    def __init__(self, name, position, tile_type="property", price=0, rent=0):
        self.name = name
        self.position = position
        self.tile_type = tile_type
        self.price = price
        self.rent = rent
        self.owner = None

    def buy(self, player):
        if self.tile_type != "property":
            return f"{self.name} is not a property!"
        if self.owner:
            return f"{self.name} is already owned by {self.owner.name}"
        if player.money >= self.price:
            player.money -= self.price
            player.properties.append(self)
            self.owner = player
            return f"{player.name} bought {self.name} for ${self.price}"
        return f"{player.name} cannot afford {self.name}"

    def pay_rent(self, player):
        if self.tile_type == "property" and self.owner and self.owner != player:
            player.pay(self.rent, self.owner)
            return f"{player.name} paid ${self.rent} rent to {self.owner.name}"
        return f"No rent due on {self.name}"

    def __str__(self):
        owner = self.owner.name if self.owner else "None"
        return f"[{self.position}] {self.name} ({self.tile_type}) | Price: ${self.price} | Rent: ${self.rent} | Owner: {owner}"
