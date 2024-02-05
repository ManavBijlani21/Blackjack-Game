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

#Player class
class Player:
    
    def __init__(self):
        self.hand=[]
        self.value=0
        self.aces=0

    #Function to add a card to the player's deck
    def add_card(self,card):
        self.hand.append(card)
        self.value+=card.number
        #Adjusting the number of aces
        if card.rank=='ace':
            self.aces+=1
    #This function checks whether to keep the value of ace as 1 or 11
    def value_of_ace(self):
        while self.aces>0 and self.value>21:
            self.value-=10
            self.aces-=1

#Chips class
#This class alters the chips of each player
class Chips:
    
    def __init__(self,total_chips=100):
        self.total_chips=total_chips
    
    def win_bet(self,bet):
        self.total_chips+=bet
    
    def loose_bet(self,bet):
        self.total_chips-=bet