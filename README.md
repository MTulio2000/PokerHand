# PokerHand Solution

To solve this problem we are dividing it into a small pieces. I propose to have three important classes. They are:

* Card
* Hand
* PokerHand

## Card

Card redefine logical operators to help us when we need to separate cards, or to compare them. To make new Card you have to:

```Python
ace_hearts = Card("AH")
four_clubs = Card("4C")
```
In the example we declare a new **Ace of Hearts** and **Four of Clubs**.

## Hand 

Hand has five cards and its function is to classify the hand between 10 possibilities:

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

If you want to make a new Hand, you can:
```Python
hand = Hand("AH 2C 5H 3S 4D")
```

Here we have a **Straight**, and our hand is made up of **Ace of Hearts**, **two of Clubs**, **five of Hearts**,**three of Spades** and **four of Diamonds**

## PokerHand

This class has the function of organizing the poker hand, and checking drawing scenario. For instance:

```Python
poker_hand = PokerHand("AH 2C 5H 3S 4D")
```
The example is the same of the last, about the hand.

PokerHand has a method, which we can compare two hands.

```Python
print(poker_hand.compare_with(PokerHand("AH JH TH QH KH"))) #Result.LOSS
```

We compare a **Straight** with a **Royal Flush**. In this case the second Poker Hand wins, and the first loses.
