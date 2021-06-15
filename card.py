#value dictionarie to help to convert string to Value enum
value = {
    "2":0,
    "3":1,
    "4":2,
    "5":3,
    "6":4,
    "7":5,
    "8":6,
    "9":7,
    "T":8,
    "J":9,
    "Q":10,
    "K":11,
    "A":12
}
     
class Card:
    #Constructor to organize the value
    def __init__(self,card):
        self.valueStr = card[0]
        self.suit = card[1]
        self.value = value[card[0]]
    
    #return true if the self value less than to the card value
    def __lt__(self,card):
        return self.value < card.value
    
    #return true if the self value greather than to the card value
    def __gt__(self,card):
        return self.value > card.value
    
    #return true if the self value greather than to the card value
    def __eq__(self,card):
        return self.value == card.value
    
    #return true if the self value greather than to the card value
    def __eq__(self,value : int):
        return self.value == value
    
    #return the string of the card
    def __str__(self):
        return "({0},{1})".format(self.valueStr, self.suit)
