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

        # determine the each type of hand and print
        
        points_hand = []
    
        # determine winner and print
        
        for i in range (len(self.players)):
            points_hand.append(i)
            if(self.is_royal(self.players[i])):
                points_hand[i] = 10
                continue
            if(self.is_straight_flush(self.players[i])):
                points_hand[i] = 9
                continue
            if(self.is_four_kind(self.players[i])):
                points_hand[i] = 8
                continue
            if(self.is_full_house(self.players[i])):
                points_hand[i] = 7
                continue
            if(self.is_flush(self.players[i])):
                points_hand[i] = 6
                continue
            if(self.is_straight(self.players[i])):
                points_hand[i] = 5
                continue
            if(self.is_three_kind(self.players[i])):
                points_hand[i] = 4
                continue
            if(self.is_two_pair(self.players[i])):
                points_hand[i] = 3
                continue
            if(self.is_one_pair(self.players[i])):
                points_hand[i] = 2
                continue
            else:
                points_hand[i] = 1
        
        for i in range(len(self.players)):
            print ('Player ' + str(i + 1) + ' has ' + str(points_hand[i]))
                
                
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
            return True


    def is_straight_flush (self, hand):
        
        if(self.is_straight(hand) == 0):
            return False
        
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        
        if(not same_suit):
            return False
        else:
            return True

        
        
        
    
    def is_four_kind (self, hand):
        #Since hands are sorted by rank, four of a kind happen only if the first four cards have same rank or if last four cards have same rank
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank and hand[0].rank == hand[3].rank):
            return True
        if(hand[1].rank == hand[2].rank and hand[1].rank == hand[3].rank and hand[1].rank == hand[4].rank):
            return True
        return False
        
           
    
    
    
    def is_full_house (self, hand):
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank and hand[3].rank == hand[4].rank):
            return True
        if(hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank):
            return True
        return False
        
        
    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
            
        if(not same_suit):
            return False
        else:
            return True
        
    
    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand) - 1):
            rank_order = rank_order and (hand[i+1].rank == hand[i].rank - i)
    
        if(not rank_order):
            return False
        else:
            return True
    
    def is_three_kind (self, hand):
        if(hand[0].rank == hand[1].rank and hand[0].rank == hand[2].rank):
            return True
        if(hand[1].rank == hand[2].rank and hand[1].rank == hand[3].rank):
            return True
        if(hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank):
            return True
        return False
    
    def is_two_pair (self, hand):
        #We do not need to check if the two pairs are not equal (i.e. a four of kind) because this is caught by the is_four_kind method, which is checked before this one
        if(hand[0].rank == hand[1].rank):
            if(hand[2].rank == hand[3].rank or hand[3].rank == hand[4].rank):
                return True
            else:
                return False
            
        elif(hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
            return True
        else:
            return False

  # determine if a hand is one pair
    def is_one_pair (self, hand):
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                return True
        return False

  
    def is_high_card (self, hand):
        #This is the last method to be checked, and so if no other condition has been met, then we have a high card
        return True

  

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
