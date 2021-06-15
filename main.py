from hand import Rating
from pokerhands import PokerHand
from pokerhands import Result
from unittest import main, TestCase

class TestPokerHand(TestCase):
    #default test function
    def test_default(self):
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")) == Result.LOSS)
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")) == Result.WIN)
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")) == Result.LOSS)
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)

    #sequence test function
    def test_sequence(self):
        self.assertTrue(PokerHand("2C 5D 3C AS 4H").hand.isSequence())
        self.assertTrue(not PokerHand("TD 5D 3C AS 4H").hand.isSequence())
        self.assertTrue(PokerHand("TH 9D QS JH KD").hand.isSequence())
        self.assertTrue(PokerHand("TH AD QS JH KD").hand.isSequence())
        self.assertTrue(PokerHand("6H TS 9D 7D 8H").hand.isSequence())
    
    #royal flush test function
    def test_royal_flush(self):
        self.assertEqual(PokerHand("TH JH QH KH AH").hand.rating,Rating.ROYAL_FLUSH)
        self.assertEqual(PokerHand("JD KD QD AD TD").hand.rating,Rating.ROYAL_FLUSH)
        self.assertEqual(PokerHand("QC TC JC KC AC").hand.rating,Rating.ROYAL_FLUSH)
        self.assertEqual(PokerHand("TS AS QS KS JS").hand.rating,Rating.ROYAL_FLUSH)

    #straight flush test function
    def test_straight_flush(self):
        self.assertEqual(PokerHand("TH JH QH 8H 9H").hand.rating,Rating.STRAIGHT_FLUSH)
        self.assertEqual(PokerHand("3D 5D 2D AD 4D").hand.rating,Rating.STRAIGHT_FLUSH)
        self.assertEqual(PokerHand("5S 9S 7S 8S 6S").hand.rating,Rating.STRAIGHT_FLUSH)
        self.assertEqual(PokerHand("TC 9C KC JC QC").hand.rating,Rating.STRAIGHT_FLUSH)
        self.assertTrue(PokerHand("TH JH QH 8H 9H").compare_with(PokerHand("TC 9C KC JC QC")) == Result.LOSS)
        self.assertTrue(PokerHand("5S 9S 7S 8S 6S").compare_with(PokerHand("3D 5D 2D AD 4D")) == Result.WIN)

    #four of a kind test function
    def test_four(self):
        self.assertEqual(PokerHand("5D 5S 5C 8S 5H").hand.rating,Rating.FOUR_OF_A_KIND)
        self.assertEqual(PokerHand("AC 6D 6C 6C 6H").hand.rating,Rating.FOUR_OF_A_KIND)
        self.assertEqual(PokerHand("3S JD 3H 3D 3D").hand.rating,Rating.FOUR_OF_A_KIND)
        self.assertEqual(PokerHand("3C AS AS AC AH").hand.rating,Rating.FOUR_OF_A_KIND)
        self.assertTrue(PokerHand("5D 5S 5C 8S 5H").compare_with(PokerHand("AC 6D 6C 6C 6H")) == Result.LOSS)
        self.assertTrue(PokerHand("3C AS AS AC AH").compare_with(PokerHand("3S JD 3H 3D 3D")) == Result.WIN)

    #full house test function
    def test_full_house(self):
        self.assertEqual(PokerHand("5D 9S 5C 9H 5H").hand.rating,Rating.FULL_HOUSE)
        self.assertEqual(PokerHand("KS 6C KC 6C 6H").hand.rating,Rating.FULL_HOUSE)
        self.assertEqual(PokerHand("3S JS 3H 3H JD").hand.rating,Rating.FULL_HOUSE)
        self.assertEqual(PokerHand("3H AS AH AC 3H").hand.rating,Rating.FULL_HOUSE)
        self.assertTrue(PokerHand("3H KS KH KC 3H").compare_with(PokerHand("3H AS AH AC 3H")) == Result.LOSS)
        self.assertTrue(PokerHand("6S KS KH KC 6H").compare_with(PokerHand("3S JS 3H 3H JD")) == Result.WIN)

    #straight test function
    def test_straight(self):
        self.assertEqual(PokerHand("5C 9D 7C 8S 6H").hand.rating,Rating.STRAIGHT)
        self.assertEqual(PokerHand("TS 9H KC JC QS").hand.rating,Rating.STRAIGHT)
        self.assertEqual(PokerHand("TC JS QH KS 9D").hand.rating,Rating.STRAIGHT)
        self.assertEqual(PokerHand("3H 5D 2S AC 4H").hand.rating,Rating.STRAIGHT)
        self.assertTrue(PokerHand("5C 9D 7C 8S 6H").compare_with(PokerHand("TS 9H KC JC QS")) == Result.LOSS)
        self.assertTrue(PokerHand("TC JS QH KS 9D").compare_with(PokerHand("5C 9D 7C 8S 6H")) == Result.WIN)

    #three of a kind test function
    def test_three(self):
        self.assertEqual(PokerHand("5D 9S 5C 8H 5H").hand.rating,Rating.THREE_OF_A_KIND)
        self.assertEqual(PokerHand("TS 6C KC 6C 6H").hand.rating,Rating.THREE_OF_A_KIND)
        self.assertEqual(PokerHand("3S JS 3S 3H 9D").hand.rating,Rating.THREE_OF_A_KIND)
        self.assertEqual(PokerHand("3H AS AH AC 4H").hand.rating,Rating.THREE_OF_A_KIND)
        self.assertTrue(PokerHand("5D 9S 5C 8H 5H").compare_with(PokerHand("TS 6C KC 6C 6H")) == Result.LOSS)
        self.assertTrue(PokerHand("3H AS AH AC 4H").compare_with(PokerHand("3S JS 3S 3H 9D")) == Result.WIN)

    #two pairs test function
    def test_two_pairs(self):
        self.assertEqual(PokerHand("5H 8S AD 8H 5C").hand.rating,Rating.TWO_PAIR)
        self.assertEqual(PokerHand("8S 8C KC 6S 6S").hand.rating,Rating.TWO_PAIR)
        self.assertEqual(PokerHand("2D JH 3D 3H JD").hand.rating,Rating.TWO_PAIR)
        self.assertEqual(PokerHand("3H AS TH AC 3H").hand.rating,Rating.TWO_PAIR)
        self.assertTrue(PokerHand("5H 8S AD 8H 5C").compare_with(PokerHand("8S 8C KC 6S 6S")) == Result.LOSS)
        self.assertTrue(PokerHand("3H AS TH AC 3H").compare_with(PokerHand("2D JH 3D 3H JD")) == Result.WIN)

    #one pair test function
    def test_one_pairs(self):
        self.assertEqual(PokerHand("5H 9S AD 8H 5C").hand.rating,Rating.ONE_PAIR)
        self.assertEqual(PokerHand("TS 3C KC 6S 6S").hand.rating,Rating.ONE_PAIR)
        self.assertEqual(PokerHand("2D JH 3D 3H 9D").hand.rating,Rating.ONE_PAIR)
        self.assertEqual(PokerHand("3H AS TH AC 4H").hand.rating,Rating.ONE_PAIR)
        self.assertTrue(PokerHand("5H 9S AD 8H 5C").compare_with(PokerHand("3H AS TH AC 4H")) == Result.LOSS)
        self.assertTrue(PokerHand("TS 3C KC 6S 6S").compare_with(PokerHand("2D JH 3D 3H 9D")) == Result.WIN)

    #high card test function
    def test_high_card(self):
        self.assertEqual(PokerHand("5H 9S AD 8S 2C").hand.rating,Rating.HIGH_CARD)
        self.assertEqual(PokerHand("4H 2S 3D 8D 5C").hand.rating,Rating.HIGH_CARD)
        self.assertEqual(PokerHand("7H 4S AD 2H 5C").hand.rating,Rating.HIGH_CARD)
        self.assertEqual(PokerHand("8H 2C TD 9S 5H").hand.rating,Rating.HIGH_CARD)
        self.assertTrue(PokerHand("4H 2S 3D 8D 5C").compare_with(PokerHand("5H 9S AD 8S 2C")) == Result.LOSS)
        self.assertTrue(PokerHand("7H 4S AD 2H 5C").compare_with(PokerHand("8H 2C TD 9S 5H")) == Result.WIN)
    
        
if __name__ == '__main__':
    main()
