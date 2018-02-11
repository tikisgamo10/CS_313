# File: Poker.py
#Description: Simulates a game of poker
#Student's Name: Luis Jimenez
#Student's UT EID: laj987
#Partner's Name: N/A
#Partner's UT EID: N/A
#Course Name: CS 313E
#Unique Number: 51335
#Date Created: February 9th 3:13PM
#Date Last Modified: February 10th 2:36PM

import random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)

class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card (rank, suit)
                self.deck.append (card)

    def shuffle (self):
        random.shuffle (self.deck)

    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    def __init__ (self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        numcards_in_hand = 5

        for i in range (num_players):
            hand = []
            for j in range (numcards_in_hand):
                hand.append (self.deck.deal())
            self.players.append (hand)



    def play (self):
    # sort the hands of each player and print
        for i in range (len(self.players)):
            sortedHand = sorted (self.players[i], reverse = True)
            self.players[i] = sortedHand
            hand = ''
            for card in sortedHand:
                hand = hand + str (card) + ' '
            print ('Player ' + str (i + 1) + " : " + hand)

        print('')

        # determine the each type of hand and print

        points_hand = []
        tie_breaker = []

        # determine winner and print

        for i in range (len(self.players)):
            points_hand.append(i)
            tie_breaker.append(i)
            if(self.is_royal(self.players[i])):
                print ('Player ' + str(i + 1) + ': Royal Flush' )
                points_hand[i] = 10
                tie_breaker[i] = self.is_royal(self.players[i])
                continue
            if(self.is_straight_flush(self.players[i])):
                print ('Player ' + str(i + 1) + ': Straight Flush' )
                points_hand[i] = 9
                tie_breaker[i] = self.is_straight_flush(self.players[i])
                continue
            if(self.is_four_kind(self.players[i])):
                print ('Player ' + str(i + 1) + ': Four of a Kind' )
                points_hand[i] = 8
                tie_breaker[i] = self.is_four_kind(self.players[i])
                continue
            if(self.is_full_house(self.players[i])):
                print ('Player ' + str(i + 1) + ': Full House' )
                points_hand[i] = 7
                tie_breaker[i] = self.is_full_house(self.players[i])
                continue
            if(self.is_flush(self.players[i])):
                print ('Player ' + str(i + 1) + ': Flush' )
                points_hand[i] = 6
                tie_breaker[i] = self.is_flush(self.players[i])
                continue
            if(self.is_straight(self.players[i])):
                print ('Player ' + str(i + 1) + ': Straight' )
                points_hand[i] = 5
                tie_breaker[i] = self.is_straight(self.players[i])
                continue
            if(self.is_three_kind(self.players[i])):
                print ('Player ' + str(i + 1) + ': Three of a Kind' )
                points_hand[i] = 4
                tie_breaker[i] = self.is_three_kind(self.players[i])
                continue
            if(self.is_two_pair(self.players[i])):
                print ('Player ' + str(i + 1) + ': Two Pair' )
                points_hand[i] = 3
                tie_breaker[i] = self.is_two_pair(self.players[i])
                continue
            if(self.is_one_pair(self.players[i])):
                print ('Player ' + str(i + 1) + ': One Pair' )
                points_hand[i] = 2
                tie_breaker[i] = self.is_one_pair(self.players[i])
                continue
            else:
                print ('Player ' + str(i + 1) + ': High Card' )
                points_hand[i] = 1
                tie_breaker[i] = self.is_high_card(self.players[i])

        print('')

        #Find the Winner

        max_hand = 0
        is_tie = False
        for i in range(len(points_hand)):
            if(points_hand[i] > max_hand):
                max_hand = points_hand[i]
                is_tie = False
            elif(points_hand[i] == max_hand):
                is_tie = True

        if(not is_tie):
            print('Player ' + str(points_hand.index(max_hand) + 1) + ' wins')
        else:
            #Tie breaker should be non-zero ONLY for those hands that are the highest, i.e, the ties
            for i in range(len(points_hand)):
                if(points_hand[i] == max_hand):
                    pass
                else:
                    tie_breaker[i] = 0

            #Will keep printing the tied players
            still_tied = True
            printed_winner = False
            while(still_tied):
                index_of_next_highest = tie_breaker.index(max(tie_breaker))

                #If winner has not been printed, print it, the rest are ties in descending order
                if( not printed_winner):
                    print('Player ' + str(index_of_next_highest + 1) + ' wins')
                    printed_winner = True
                else:
                    print('Player ' + str(index_of_next_highest + 1) + ' ties')


                #Record already printed so we can set equal to zero so that max function gets next biggest one
                tie_breaker[index_of_next_highest] = 0


                #Check if there are no more non-zero values
                if(tie_breaker.count(0) == len(tie_breaker)):
                    still_tied = False


  # determine if a hand is a royal flush
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return False

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if(not rank_order):
            return False
        else:
            return 10 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank


    def is_straight_flush (self, hand):

        if(self.is_straight(hand) == 0):
            return False

        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if(not same_suit):
            return False
        else:
            return 9 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank





    def is_four_kind (self, hand):
        #Since hands are sorted by rank, four of a kind happen only if the first four cards have same rank or if last four cards have same rank
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank and hand[0].rank == hand[3].rank):
            return 8 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
        if(hand[1].rank == hand[2].rank and hand[1].rank == hand[3].rank and hand[1].rank == hand[4].rank):
            return 8 * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[0].rank
        return False





    def is_full_house (self, hand):
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank and hand[3].rank == hand[4].rank):
            return 7 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
        if(hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank):
            return 7 * 13**5 + hand[2].rank * 13**4 + hand[3].rank * 13**3 + hand[4].rank * 13**2 + hand[0].rank * 13 + hand[1].rank
        return False


    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if(not same_suit):
            return False
        else:
            return 6 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank


    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand) - 1):
            rank_order = rank_order and (hand[i+1].rank == hand[i].rank - 1)

        if(not rank_order):
            return False
        else:
            return 5 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank

    def is_three_kind (self, hand):
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank):
            return 4 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
        if(hand[1].rank == hand[2].rank and hand[1].rank == hand[3].rank):
            return 4 * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[0].rank * 13 + hand[4].rank
        if(hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank):
            return 4 * 13**5 + hand[2].rank * 13**4 + hand[3].rank * 13**3 + hand[4].rank * 13**2 + hand[0].rank * 13 + hand[1].rank
        return False

    def is_two_pair (self, hand):
        #We do not need to check if the two pairs are not equal (i.e. a four of kind) because this is caught by the is_four_kind method, which is checked before this one
        if(hand[0].rank == hand[1].rank):
            if(hand[2].rank == hand[3].rank):
                return 3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
            elif(hand[3].rank == hand[4].rank):
                return 3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[2].rank
            else:
                return False

        elif(hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
                return 3 * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[0].rank

        else:
            return False

  # determine if a hand is one pair
    def is_one_pair (self, hand):
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                break
        else:
            return False

        #The pair is at position i and i+1
        #We now add the points
        c = [] #List to hold the coefficients
        c.append(hand[i].rank)
        c.append(hand[i+1].rank)
        for j in range(0, i):
            c.append(hand[j].rank)

        for j in range(i, len(hand)):
            c.append(hand[j].rank)

        return 2 * 13**5 + c[0] * 13**4 + c[1] * 13**3 + c[2] * 13**2 + c[3] * 13 + c[4]




    def is_high_card (self, hand):
        #This is the last method to be checked, and so if no other condition has been met, then we have a high card
        return 1 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank



def main():
  # prompt user to enter the number of players
    num_players = int (input ('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int (input ('Enter number of players: '))

  # create the Poker object
    game = Poker (num_players)

  # play the game (poker)
    game.play()




main()
