#Logan Flynn
#Card Game Program
#11/16/2025
import random

# Deck object from Section 11.5
class Deck:
    def __init__(self, num_cards):
        self._cards = list(range(num_cards))

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        if len(self._cards) == 0:
            return None
        return self._cards.pop()

    def new_hand(self):
        return Deck(len(self._cards))


# Card naming info (same style used in the book)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'J', 'Q', 'K', 'A']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


#Print a hand of cards
def print_hand(hand, title="Hand"):
    print(title)
    for i, card in enumerate(hand, start=1):
        rank = card % 13
        suit = card // 13
        print(f"{i}: {ranks[rank]} of {suits[suit]}")
    print()


# Deal a 5-card poker hand
def deal_hand(deck):
    hand = []
    deck.shuffle()
    for _ in range(5):
        hand.append(deck.deal())
    return hand


# Ask user which cards to replace (1–5)
def get_replacement_positions():
    user = input("Enter card numbers to replace (e.g. 1 3 5): ").strip()

    if user == "":
        return []

    # allow commas or spaces
    user = user.replace(",", " ")
    parts = user.split()

    positions = []
    for p in parts:
        if p.isdigit():
            pos = int(p)
            if 1 <= pos <= 5 and pos not in positions:
                positions.append(pos)

    return positions


# Main game logic
def main():
    deck = Deck(52)

    # Deal initial hand
    hand = deal_hand(deck)
    print_hand(hand, "Initial Poker Hand:")

    # Replace phase
    replace_positions = get_replacement_positions()

    for pos in replace_positions:
        hand[pos - 1] = deck.deal()

    print_hand(hand, "Final Poker Hand After Draw:")


# Run the program
if __name__ == "__main__":
    main()
