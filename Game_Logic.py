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
    BlackJack_deck=Deck()
    #Shuffling the deck
    BlackJack_deck.shuffle_deck()
    #Initializing the player and dealer hand
    player=Player()
    dealer=Player()
    #Initializing chips for the player
    player_chips=Chips() 
    #Taking the bet to be made by the player
    player_bet=take_bet(player_chips)
    #Distributing two cards to each of them
    for i in range(2):
        player.add_card(BlackJack_deck.deal_card())
        player.value_of_ace()
        dealer.add_card(BlackJack_deck.deal_card())
        dealer.value_of_ace()
    show_some(player,dealer)
    playing=True
    flag='green'

    while playing:
        #Asking player whether he wants to hit or stand
        hit_or_stand(player,BlackJack_deck)
        show_some(player,dealer)
        if player_busts(player,player_chips,player_bet):
            print("The player busts!")
            print("Dealer Wins!!!")
            print("Player looses the bet")
            playing=False
            flag='red'
            #Showing all cards of dealer and player
            show_all(player,dealer)
        else:
            flag='green'

    
    #Checking all the winning scenarios if player hasn't busted
    if flag=='green':
        while dealer.value<17:
            hit(dealer,BlackJack_deck)
        #Showing all cards of dealer and player
        show_all(player,dealer)
        if dealer_busts(dealer,player_chips,player_bet):
            print("The dealer busted!!")
            print("Congratulations the player wins the game!!!")
        elif player_wins(player,dealer,player_chips,player_bet):
            print("Congratulations the player wins the game!!!")
            print("The dealer looses..")
        elif dealer_wins(player,dealer,player_chips,player_bet):
            print("Dealer wins the game!!!")
            print("Player looses the bet")
        elif tie(player,dealer):
            print("The game is tied...")
        else:
            pass
    
    print("Remaining chips of the player:",player_chips.total_chips)
    #Asking the player whether to continue playing or not
    play_on=continue_playing()
    if play_on==False:
        break

print("Thanks for playing!")
print("Hope you enjoyed the game!") 

    