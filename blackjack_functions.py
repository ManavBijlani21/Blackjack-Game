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
