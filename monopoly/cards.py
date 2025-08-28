import random

chance_cards = [
    ("Advance to Go (Collect $200)", "move", 0),
    ("Bank pays you dividend of $50", "money", 50),
    ("Go to Jail", "jail", None),
    ("Pay poor tax of $15", "money", -15),
]

community_chest_cards = [
    ("Doctor's fees – Pay $50", "money", -50),
    ("From sale of stock you get $50", "money", 50),
    ("Go to Jail", "jail", None),
    ("Life insurance matures – Collect $100", "money", 100),
]

def draw_chance():
    return random.choice(chance_cards)

def draw_community_chest():
    return random.choice(community_chest_cards)
