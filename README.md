# PokerHand Solution

To solve this problem we are dividing it into a small pieces. I propose to have three important classes. They are:

* Card
* Hand
* PokerHand

## Card

Card has redefining logical operators to help us when we need to separate cards, or compare them with one another. To make new Card you have to do this:

```Python
ace_hearts = Card("AH")
four_clubs = Card("4C")
```
In the example we declare a new Card **Ace of Hearts** and a **Four of Clubs**.

## Hand 

Hand has five cards and the function of classify the hand between 10 possibilities:

* Royal Flush;
* Straight Flush;
* Four of a kind;
* Full House;
* Flush;
* Straight;
* Three of a kind;
* Two pair;
* One pair;
* High Card.

If you want to make a new Hand, you can do it like this:
```Python
hand = Hand("AH 2C 5H 3S 4D")
```

Here we have a **Straight**, and our hand is made up of **Ace of Hearts**, **Two of Clubs**, **5 of Hearts**,**Three of Spades** and **Four of Diamonds**

## PokerHand

This class has the function of organizing the poker hand, and checking draw scenario. To make a instance do this:

```Python
poker_hand = PokerHand("AH 2C 5H 3S 4D")
```
The example is the same of the last, about the hand.

PokerHand has a method, where we can compare two hands.

```Python
print(poker_hand.compare_with(PokerHand("AH JH TH QH KH"))) #Result.LOSS
```

We compare a **Straight** with a **Royal Flush**, in this case the second Poker Hand win, and the first lose.
