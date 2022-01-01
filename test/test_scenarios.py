import unittest
from src.deck import Deck,Hand
import blackjack

class ScenarioTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.player = Hand()

    def tearDown(self):  # this method will be run after each tests
        pass

    """
    Given I play a game of blackjack
    When I am dealt my opening hand
    Then I have two cards
    """
    def test_scenario1(self):  # any method beginning with 'test' will be run by unittest
        
        self.player.player_initialisation(self.deck)
        number_of_cards = len(self.player.hand)
        self.assertEqual(number_of_cards, 2)

    """
    Given I have a valid hand of cards
    When I choose to ‘hit’
    Then I receive another card
    And my score is updated
    """
    def test_scenario2(self):  # any method beginning with 'test' will be run by unittest
        #cards used = Ace 11, 2,3 = 16
        names= {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        #self.player.player_initialisation(self.deck)
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        card=self.deck.deal_card(0)
        self.player.hand.append(card)
        number_of_cards = len(self.player.hand)
        score=self.player.scores()
        t=0
        for i in self.player.hand:
            t+=names[i.name]
        self.assertEqual(number_of_cards, 3)
        self.assertEqual(score, t)

    """
    Given I have a valid hand of cards
    When I choose to ‘stand’
    Then I receive no further cards
    And my score is evaluated
    """
    def test_scenario3(self):

##        self.player.player_initialisation(self.deck)

        #49th card is val 10
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        
        score=self.player.stand()
        number_of_cards = len(self.player.hand)
        #score=self.player.scores()
        self.assertEqual(number_of_cards, 2)
        names= {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        t=0
        for i in self.player.hand:
              print(i.name)
              print(i.name)
              print(i.name)
              t+=names[i.name]
        self.assertEqual(score, t)
        
    """
    Given my score is updated or evaluated
    When it is 21 or less
    Then I have a valid hand
    """
    def test_scenario4(self):
        self.player.player_initialisation(self.deck)
        self.assertEqual(self.player.valid_invalid_hand(), True)


    """
    Given my score is updated
    When it is 22 or more 
    Then I am ‘bust’ and do not have a valid hand
    """
    def test_scenario5(self):
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        #self.player.player_initialisation(self.deck)
        card=self.deck.deal_card(49)
        self.player.hand.append(card)
        self.assertEqual(self.player.valid_invalid_hand(), False)

    """
    Given I have a king and an ace
    When my score is evaluated
    Then my score is 21
    """
    def test_scenario6(self):  # any method beginning with 'test' will be run by unittest
        #cards used = Ace 11, 2,10
##        self.player.player_initialisation(self.deck)
        card=self.deck.deal_card(51)
        self.player.add_card(card)
        card=self.deck.deal_card(0)
        self.player.add_card(card)
        score=self.player.scores()
        self.assertEqual(score, 21)

    """
    Given I have a king, a queen, and an ace
    When my score is evaluated
    Then my score is 21
    """
    def test_scenario6(self):
        card=self.deck.deal_card(51)
        self.player.add_card(card)
        card=self.deck.deal_card(50)
        self.player.add_card(card)
        card=self.deck.deal_card(0)
        self.player.add_card(card)
        score=self.player.scores()
        self.assertEqual(score, 21)

    """
    Given that I have a nine, an ace, and another ace
    When my score is evaluated
    Then my score is 21
    """
    def test_scenario7(self):
        card=self.deck.deal_card(8)
        self.player.add_card(card)
        card=self.deck.deal_card(0)
        self.player.add_card(card)
        card=self.deck.deal_card(11)
        self.player.add_card(card)
        score=self.player.scores()
        self.assertEqual(score, 21)
    
  
if __name__ == '__main__':
    unittest.main()
