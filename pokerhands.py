from hand import Hand
from hand import Rating
from enum import Enum
from card import value

# All possibilities of the hand
class Result(Enum):
     WIN = 0
     LOSS = 1
     
# class PokerHand to help us to change the best among two hands
class PokerHand:
    '''
        Constructor to initialize PokerHand object
        hand is a string that change the cards value
    '''
    def __init__(self,hand):
        self.hand = Hand(hand)

    '''
    If had a draw, the code will verify which hand is the winner
    '''
    def draw(self,hand : Hand):
        myHand = self.hand.hand
        myEquals = self.hand.equals
        advHand = hand.hand
        advEquals = hand.equals

        rate = self.hand.rating  #hand rate

        isSequence = rate == Rating.STRAIGHT_FLUSH or rate == Rating.STRAIGHT
        isPair = rate == Rating.ONE_PAIR or rate == Rating.TWO_PAIR
        isThree = rate == Rating.FULL_HOUSE or rate == Rating.THREE_OF_A_KIND
        majorCard = rate == Rating.FLUSH or rate == Rating.HIGH_CARD

        #return the index of the major pair/three/four kinds
        def index(h : Hand,n:int,less:int):
            index = -1
            for i in range(0,len(h.equals)-less):
                if h.equals[i][0] == n:
                    index = h.equals[i][2]
            return index

        # -1 if has a draw with the pairs
        # else return win if we are the winner
        def winner(n):
            less = 0
            while True:
                mineIndex = index(self.hand,n,less)
                adversaryIndex = index(hand,n,less)
                if self.hand.hand[mineIndex]>advHand[adversaryIndex]:
                    return Result.WIN
                elif self.hand.hand[mineIndex]<advHand[adversaryIndex]:
                    return Result.LOSS
                else:
                    if less == 2:
                        break
                    less+=1
            return -1

        #checking what type of draw we have to treat
        if rate == Rating.FOUR_OF_A_KIND:
            return Result.WIN if myEquals[0][1]>advEquals[0][1] else Result.LOSS
        if isThree:
            return winner(2)
        if isPair or majorCard or isSequence:
            if isPair:
                result = winner(1)
                if result != -1:
                    return result
                    
            mineLess = 1 if myHand[4] == value["A"] and isSequence else 0
            advLess = 1 if advHand[4] == value["A"] and isSequence else 0

            for i in range(4,-1,-1):
                if myHand[i-mineLess]>advHand[i-advLess]:
                    return Result.WIN
                if myHand[i-mineLess]<advHand[i-advLess]:
                    return Result.LOSS
        return Result.LOSS
    
    # compare with other hand
    def compare_with(self,hand):
        if self > hand:
            return Result.WIN
        elif self < hand:
            return Result.LOSS
        else:
            return self.draw(hand.hand)

    #redefining < operator
    def __lt__(self, hand):
        return self.hand < hand.hand

    #redefining > operator
    def __gt__(self, hand):
        return self.hand > hand.hand

    #redefining string
    def __str__(self):
        return self.hand.__str__()
