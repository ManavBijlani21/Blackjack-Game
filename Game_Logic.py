import blackjack_classes
import blackjack_functions

#Importing the shuffle function from the random module to shuffle the deck afterwards
from random import shuffle 
#Initializing lists for cards
suits=['clubs','hearts','diamonds','spades']
ranks=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':11,
       'king':11,'ace':11}


while True:
    print("Welcome to the BlackJack Game!")
    #Initializing the deck
    BlackJack_deck=blackjack_classes.Deck()
    #Shuffling the deck
    BlackJack_deck.shuffle_deck()
    #Initializing the player and dealer hand
    player=blackjack_classes.Player()
    dealer=blackjack_classes.Player()
    #Initializing chips for the player
    player_chips=blackjack_classes.Chips() 
    #Taking the bet to be made by the player
    player_bet=blackjack_functions.take_bet(player_chips)
    #Distributing two cards to each of them
    for i in range(2):
        player.add_card(BlackJack_deck.deal_card())
        player.value_of_ace()
        dealer.add_card(BlackJack_deck.deal_card())
        dealer.value_of_ace()
    blackjack_functions.show_some(player,dealer)
    playing=True
    flag='green'

    while playing:
        #Asking player whether he wants to hit or stand
        playing=blackjack_functions.hit_or_stand(player,BlackJack_deck)
        blackjack_functions.show_some(player,dealer)
        if blackjack_functions.player_busts(player,player_chips,player_bet):
            print("The player busts!")
            print("Dealer Wins!!!")
            print("Player looses the bet")
            playing=False
            flag='red'
            #Showing all cards of dealer and player
            blackjack_functions.show_all(player,dealer)
        
        elif (playing==False):
            flag='green'
            break

        else:
            flag='green'
            playing=True

    
    #Checking all the winning scenarios if player hasn't busted
    if flag=='green':
        while dealer.value<17:
            blackjack_functions.hit(dealer,BlackJack_deck)
        if blackjack_functions.dealer_busts(dealer,player_chips,player_bet):
            print("The dealer busted!!")
            print("Congratulations the player wins the game!!!")
        elif blackjack_functions.player_wins(player,dealer,player_chips,player_bet):
            print("Congratulations the player wins the game!!!")
            print("The dealer looses..")
        elif blackjack_functions.dealer_wins(player,dealer,player_chips,player_bet):
            print("Dealer wins the game!!!")
            print("Player looses the bet")
        elif blackjack_functions.tie(player,dealer):
            print("The game is tied...")
        else:
            pass
        #Showing all cards of dealer and player
        blackjack_functions.show_all(player,dealer)
    
    print("Remaining chips of the player:",player_chips.total_chips)
    #Asking the player whether to continue playing or not
    play_on=blackjack_functions.continue_playing()
    if play_on==False:
        print("\n")
        break
    print("-"*50)
    print("\n")

print("Thanks for playing!")
print("Hope you enjoyed the game!") 

    