#Importing the shuffle function from the random module to shuffle the deck afterwards
from random import shuffle 
#Initializing lists for cards
suits=['clubs','hearts','diamonds','spades']
ranks=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':11,
       'king':11,'ace':11}


#Card Class
class Card:
    
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        self.number=values[rank] 
        
    def __str__(self):
        return self.rank+' of '+self.suit

#Deck Class
class Deck:
    
    def __init__(self):
        self.game_deck=[]
        for suit in suits:
            for rank in ranks:
                self.game_deck.append(Card(rank,suit))
    
    def __str__(self):
        my_deck=''
        for card in self.game_deck:
            my_deck+='\n'+str(card)
        return my_deck
    #Shuffling the deck
    def shuffle_deck(self):
        shuffle(self.game_deck)
    #Removing a card from the deck
    def deal_card(self):
        return self.game_deck.pop()