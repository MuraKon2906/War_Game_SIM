import random

suits =("Hearts","Diamonds","Spades","Clubs")

ranks=("Two",
       "Three",
       "Four",
       "Five",
       "Six",
       "Seven",
       "Eight",
       "Nine",
       "Ten",
       "Jack",
       "Queen",
       "King",
       "Ace")

values={"Two":2,
        "Three":3,
        "Four":4,
        "Five":5,
        "Six":6,
        "Seven":7,
        "Eight":8,
        "Nine":9,
        "Ten":10,
        "Jack":11,
        "Queen":12,
        "King":13,
        "Ace":14}

#card class 
class Card:
    def __init__(self,suit,rank) -> None:
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit  

# Deck class :- inititaite a new deck 
# creates all 52 deck

class Deck:
    def __init__(self) -> None:
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card=Card(suit=suit,rank=rank)

                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self,name) -> None:
        self.name=name
        self.all_cards=[]


    def remove_one(self):
        return self.all_cards.pop(0)


    # This function extends the player's deck if the player gets 
    # multiple cards or just appends them if player recieves one card at 
    # time

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):#checks if new_cards is a list or not. adds the elements to the all_cards list.
            self.all_cards.extend(new_cards)

        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} : has {len(self.all_cards)} cards"


if __name__ == "__main__":
    player_one=Player(name="One") 
    player_two=Player(name="Two")

    new_deck=Deck()
    new_deck.shuffle_deck()

    for x in range(26):     # each player will get 26 cards. 
        player_one.add_cards(new_deck.deal_one())

        player_two.add_cards(new_deck.deal_one())

    game_on=True

    round_num=0
    while game_on:
        round_num +=1
        print(f"Round : {round_num}")


        if len(player_one.all_cards)==0:
            print("Player Two Wins !!!!")
            game_on = False
            break

        if len(player_two.all_cards)==0:
            print("Player One Wins !!!!")
            game_on = False
            break

        # Start a new Round: 

        player_one_cards=[]
        player_one_cards.append(player_one.remove_one())


        player_two_cards=[]
        player_two_cards.append(player_two.remove_one())



        # While at_war : war comparison
        # There are only three situations:
        #     1) player one > player two 
        #     2) player one < player two 
        #     3) player one == player two
        at_war=True

        while at_war:
            if player_one_cards[-1].value >player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)

                player_one.add_cards(player_two_cards)

                at_war=False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)

                player_two.add_cards(player_two_cards)

                at_war=False

            else:
                print("-----------WAR!!!!-------------------")
                if len(player_one.all_cards)<5:
                    print("Player One cant play war :<")
                    print("Player Two Wins")
                    game_on=False
                    break


                elif len(player_two.all_cards)<5:
                    print("Player Two cant play war :<")
                    print("Player One Wins")
                    game_on=False
                    break

                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())

                        player_two_cards.append(player_two.remove_one())
