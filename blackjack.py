import tkinter as tk
from tkinter import messagebox
from src.deck import Deck, Hand

##def check_A(card,player):
##
##    if card.name=='A':
##        score=player.scores()
##        if score+1==21:
##            card.value=1
##        elif score+11<=21:
##            card.value=11
##        else:
##            card.value=1
##
##    return card
##
##def hand_card(deck,player):
##    card=deck.deal_card(0)
##    card=check_A(card,player)
##    return card

def hand_fn():
    global player
    player=Hand()
    global deck
    deck = Deck()
    player.player_initialisation(deck)
    update_card(player)
    update_score(player)
    check_winner(player)

def update_card(player):
    string=''
    for i in player.hand:
        string+=i.name
        string+=' '
##        string+=str(i.value)
##        string+=' '
        string+=i.suit+'\n'
        
    label_cards_val.config(
    text=string
    )
    label_cards_val.pack()

def update_score(player):
    score=player.scores()
    label_score_val.config(
    text=str(score)
    )
    label_score_val.pack()
    

def hit_fn():
    global deck
    global player
    card=deck.deal_card()
    player.hand.append(card)
    update_card(player)
    update_score(player)
    check_winner(player)

def stand_fn():
    global deck
    global player
    update_card(player)
    update_score(player)
    check_winner(player)


def check_winner(player):
    score=player.scores()
    if score==21:
        messagebox.showinfo(title="Winner", message="Winner! You hit 21!.")
        
    if player.valid_invalid_hand():
        pass
    else:
        messagebox.showinfo(title="Bust", message="Bust! You went over 21!.")
    
##def player_initialisation(deck):
##    player=Hand()
##    card=hand_card(deck,player)
##
##    print(card.suit,card.value,card.name)
##    player.hand.append(card)
##
##    card=hand_card(deck,player)
##    player.hand.append(card)

##    return player
window = tk.Tk()
label = tk.Label(
text="Hello, Player",
foreground="white",  # Set the text color to white
background="black"  # Set the background color to black
)
label.pack()

button_hand = tk.Button(
text="Hand",
command = hand_fn,
width=25,
height=5,
)
button_hand.pack()

button_hit = tk.Button(
text="Hit",
command = hit_fn,
width=25,
height=5,
)
button_hit.pack()

button_stand = tk.Button(
text="Stand",
command = stand_fn,
width=25,
height=5,
)
button_stand.pack()

label_cards = tk.Label(
text="Cards"
)
label_cards.pack()

label_cards_val = tk.Label(
text=""
)
label_cards_val.pack()

label_score = tk.Label(
text="Score"
)
label_score.pack()

label_score_val = tk.Label(
text=""
)
label_score_val.pack()

    

    
def play():
    print('Hello, potential future BBC developer!')  # execution starts here! delete this line and add your game code.



##    deck=Deck()
##    player1=Hand()
##    player1.player_initialisation(deck)
##    #player1 = player_initialisation(deck)
##
##    print(player1.hand[0].value,player1.hand[0].name,player1.hand[0].suit)
##    print(player1.hand[1].value,player1.hand[1].name,player1.hand[1].suit)
##
##
##    while True:
##        if stand pressed
##        hit_stand=True

    

if __name__ == '__main__':
    play()
