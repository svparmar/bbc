import random

def check_A(card,player):

    if card.name=='A':
        score=player.scores()
        if score+1==21:
            card.value=1
        elif score+11<=21:
            card.value=11
        else:
            card.value=1

    return card

def hand_card(deck,player):
    card=deck.deal_card()
    card=check_A(card,player)
    return card


class Hand:
    def __init__(self):
        self.hand=[]
        self.score=0

    def scores(self):
        self.score=0
        for i in self.hand:
            self.score+=i.value
        return self.score


    def player_initialisation(self,deck):

        card=hand_card(deck,self)

        #print(card.suit,card.value,card.name)
        self.hand.append(card)

        card=hand_card(deck,self)
        self.hand.append(card)

    def stand(self):
        return self.scores()

    def valid_invalid_hand(self):
        self.score=self.scores()
        return self.score<=21
        
    def add_card(self,card):
        card=check_A(card,self)
        self.hand.append(card)
        return self
    


class Card:
    def __init__(self,suit,value,name):
        self.suit=suit
        self.value=value
        self.name=name

        
class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        names= {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

        for su in ["Spades","Clubs","Diamonds","Hearts"]:
            for name,vals in names.items():
                self.cards.append(Card(su,vals,name))

    def deal_card(self,card=None):
        #card=randint(0,len(self.cards)-1)
        if card!=None:
            return self.cards.pop(card)
        else:
            card_index=random.randint(0,len(self.cards)-1)
            return self.cards.pop(card_index)


deck=Deck()
for i in deck.cards:
    print(i.suit,i.value,i.name)
        
        
