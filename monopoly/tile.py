class Tile:
    def __init__(self, name, position, tile_type="property", price=0, rent=0):
        """
        Base Tile class
        :param name: Name of the tile (e.g. 'GO', 'Baltic Avenue', 'Jail')
        :param position: Position on the board (0–39)
        :param tile_type: Type of tile ('go', 'property', 'jail', 'chance', 'community', 'tax', etc.)
        :param price: Price if it's a property
        :param rent: Rent if someone lands here and it's owned
        """
        self.name = name
        self.position = position
        self.tile_type = tile_type
        self.price = price
        self.rent = rent
        self.owner = None  # no owner at start

    def buy(self, player):
        """Player buys property if unowned and has enough money"""
        if self.tile_type != "property":
            return f"{self.name} is not a property!"
        if self.owner:
            return f"{self.name} is already owned by {self.owner.name}"
        if player.money >= self.price:   # ✅ fixed: use .money not .balance
            player.money -= self.price
            player.properties.append(self)  # ✅ also track property in player's list
            self.owner = player
            return f"{player.name} bought {self.name} for ${self.price}"
        else:
            return f"{player.name} cannot afford {self.name}"

    def pay_rent(self, player):
        """Player pays rent if landing on owned property"""
        if self.tile_type == "property" and self.owner and self.owner != player:
            player.pay(self.rent, self.owner)  # ✅ uses Player.pay
            return f"{player.name} paid ${self.rent} rent to {self.owner.name}"
        return f"No rent due on {self.name}"

    def __str__(self):
        owner = self.owner.name if self.owner else "None"
        return f"[{self.position}] {self.name} ({self.tile_type}) | Price: ${self.price} | Rent: ${self.rent} | Owner: {owner}"
