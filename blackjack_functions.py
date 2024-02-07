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
            pass
    return bet


#Function to add a card to the player's deck
def hit(player,deck):
    player.add_card(deck.deal_card())
    player.value_of_ace()
    return True

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
        return False
        


#This function shows two cards of the player and only 1 card of the dealer
def show_some(player,dealer):
    #Player's cards
    print('\n')
    print("Player's Cards:")
    for i in player.hand:
        print(i)
    print('Total:',player.value)
    #Showing only one card of the dealer
    print('\n')
    print("Dealer's Card:") 
    print(dealer.hand[0])


#This function shows all the cards of player and dealer
def show_all(player,dealer):
    show_some(player,dealer)
    for j in range(1,len(dealer.hand)):
        print(dealer.hand[j])
    print('Total:',dealer.value)
    print('\n')


#Checking all the winning scenarios 
def player_busts(player,player_chips,bet):
    if player.value>21:
        player_chips.loose_bet(bet)
        return True
    else:
        return False

def dealer_busts(dealer,player_chips,bet):
    if dealer.value>21:
        player_chips.win_bet(bet)
        return True
    else:
        return False

def player_wins(player,dealer,player_chips,bet):
    if player.value<=21 and player.value>dealer.value:
        player_chips.win_bet(bet)
        return True
    else:
        return False
def dealer_wins(player,dealer,player_chips,bet):
    if dealer.value<=21 and dealer.value>player.value:
        player_chips.loose_bet(bet)
        return True
    else:
        return False
    
def tie(player,dealer):
    if player.value==dealer.value:
        return True
    else:
        return False


#Function for asking the player if he wants to continue playing
def continue_playing():
    to_continue=False
    while to_continue not in ['Yes','No']:
        to_continue=input("Do you want to continue playing(Yes/No)?")
        if to_continue not in ['Yes','No']:
            print("Please enter a valid choice!")
    
    if to_continue=='Yes':
        print("\n")
        return True
    else:
        return False