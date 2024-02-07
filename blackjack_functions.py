import blackjack_classes

#Importing the shuffle function from the random module to shuffle the deck afterwards
from random import shuffle 
#Initializing lists for cards
suits=['clubs','hearts','diamonds','spades']
ranks=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':11,
       'king':11,'ace':11}


#Function for taking the bet from the player
def take_bet(player_chips):
    while True:
        try:
            bet=int(input("Enter the bet to be made by the player:")) 
        except:
            print("Please enter an integer value")
            continue
        else:
            if bet>player_chips.total_chips:
                print('The bet should not exceed the total chips you have!')
                continue
            else:
                break
        finally:
            print('Thank you!')
    return bet


#Function to add a card to the player's deck
def hit(player,deck):
    player.add_card(deck.deal_card())
    player.value_of_ace()

#Function to take the input of choice (hit or stand)
def hit_or_stand(player,deck):
    global playing
    choice=False
    while choice not in ['hit','stand']:
        choice=input("Do you want to hit or stand?")
        if choice not in ['hit','stand']:
            print("Please type either 'hit' or 'stand':")
    
    if choice=='hit':
        hit(player,deck)
    else:
        playing=False