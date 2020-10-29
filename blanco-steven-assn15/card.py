from gronkyutil import paw
from gronkyutil import coin

class Card:

    def __init__(self, id):
        self.__id = id

    def __repr__(self):
        message = str(self.getValue()) + " of " + self.getPaw() + " " + self.getCoin()
        return message

    def __gt__(self, other):
        if self.getId() > other.getId():
            return True
        else:
            return False

    def getId(self):
        return self.__id


    def getValue(self):
        b = self.__id // 40
        c = self.__id % 2
        a = (self.__id - c) / 2 - 20 * b + 1
        self.__value = int(a)
        return self.__value

    def getCoin(self):
        self.__coin = coin[self.__id % 2]
        return self.__coin

    def getPaw(self):
        self.__paw = paw[self.__id // 40]
        return self.__paw







