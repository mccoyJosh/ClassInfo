
# Deck Of Cards

This example shows some code making a deck of cards. This example shows how one can create 
a set of items without defining literally everything. 


```python
import random

class Card:
    RANKS = tuple(range(1, 14))
    SUITS = ("Spades", "Clubs", "Diamonds", "Hearts")


    def __init__(self, rank, suit):
        if rank in self.RANKS and suit in self.SUITS:
            self.rank = rank
            self.suit = suit
        else:
            raise Exception('Card does not exist: ', rank, suit)

    def __str__(self):
        r = self.rank
        if r == 1:
            r = 'Ace'
        elif r == 11:
            r = 'Jack'
        elif r == 12:
            r = 'Queen'
        elif r == 13:
            r = 'King'
        else:
            r = str(r)
        return r + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.gather_deck()

    def gather_deck(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        rtn = []
        for card in self.cards:
            rtn.append(str(card))
        return '    '.join(rtn)


d = Deck()
d.shuffle()
print(d)
print()
d.gather_deck()
print(d)
```
