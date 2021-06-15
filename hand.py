from card import Card
from card import value
from enum import IntEnum

'''
Rating enum to help us to change the correct value for the hand
'''
class Rating(IntEnum):
     HIGH_CARD = 0,
     ONE_PAIR = 1,
     TWO_PAIR = 2,
     THREE_OF_A_KIND = 3,
     STRAIGHT = 4,
     FLUSH = 5,
     FULL_HOUSE = 6,
     FOUR_OF_A_KIND = 7,
     STRAIGHT_FLUSH = 8,
     ROYAL_FLUSH = 9

#Hand class to represent a real Hand of cards
class Hand:
    '''
    Constructor make the cards in the hand list
    '''
    def __init__(self,hand):
        self.rating = Rating.HIGH_CARD
        cards = hand.split()
        self.hand = []
        for card in cards:
            self.hand.append(Card(card))
        self.hand.sort()
        self.evaluate()

    '''
    Verifying if the have a sequence
    '''
    def isSequence(self):
        less = 1 if self.hand[4].value == value["A"] else 0
        for i in range(0,4-less):
            if self.hand[i].value+1 != self.hand[i+1].value:
                return False
        return True
    
    '''
    Check if the hand is all in the same suit
    '''
    def __isSameSuit(self):
        for i in range(0,4):
            if self.hand[i].suit != self.hand[i+1].suit:
                return False
        return True

    '''
    Searching for pairs, Three or four kind
    '''
    def __equals(self):
        count = 0
        self.equals = []
        for i in range(0,4):
            if self.hand[i].value == self.hand[i+1].value:
                count+=1
            if (self.hand[i].value != self.hand[i+1].value or (i == 3)) and count != 0:
                self.equals.append((count,self.hand[i].value,i))
                count = 0
            
    '''
    Evaluating the main characteristics of the hand
    '''
    def evaluate(self):
        self.__sequence = self.isSequence()
        self.__sameSuit = self.__isSameSuit()
        self.__ace = self.hand[4].value == value["A"]
        self.__king = self.hand[3].value == value["K"]
        self.__equals()
        self.__pairs = 0
        self.__three = False
        self.__four = False
        for i in self.equals:
            if i[0] == 3:
                self.__four = True
                break
            if i[0] == 2:
                self.__three = True
            elif i[0] == 1:
                self.__pairs+=1
        self.__classify()

    '''
    Classify function, where the hand is classified in its correct class
    '''
    def __classify(self):
        if self.__sequence and self.__sameSuit:
            if self.__ace and self.__king:
                self.rating = Rating.ROYAL_FLUSH
            else:
                self.rating = Rating.STRAIGHT_FLUSH
        else:
            if self.__four:
                self.rating = Rating.FOUR_OF_A_KIND
            elif self.__three:
                if self.__pairs:
                    self.rating = Rating.FULL_HOUSE
                else:
                    self.rating = Rating.THREE_OF_A_KIND
            else:
                if not self.__sequence and self.__sameSuit:
                    self.rating = Rating.FLUSH
                elif self.__sequence and not self.__sameSuit:
                    self.rating = Rating.STRAIGHT
                else:
                    if self.__pairs == 1:
                        self.rating = Rating.ONE_PAIR
                    elif self.__pairs == 2:
                        self.rating = Rating.TWO_PAIR

    '''
    Return the string of Hand
    '''
    def __str__(self):
        str = "["
        for i in range(len(self.hand)):
            str+= self.hand[i].__str__()
            if i < len(self.hand)-1:
                str+=", "
        str += "]"
        return str

    def __lt__(self, hand):
        return self.rating.value < hand.rating.value

    def __gt__(self, hand):
        return self.rating.value > hand.rating.value