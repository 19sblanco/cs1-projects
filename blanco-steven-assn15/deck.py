import random
from card import Card

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = list()
        for i in range(120):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)
        return self.__deck


    def draw(self):
        return self.__deck.pop()

