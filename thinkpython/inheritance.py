import random

class Card:
    """Represent a standard playing card
    Attributes:
        rank: integer 1 - 13
        suit: integer 0 - 3
    """
    
    suit_names = ['Clubs','Diamonds','Heart','Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __init__(self,suit = 0,rank = 2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank],self.suit_names[self.suit])
    
    def __lt__(self,other):#重载小于<
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank
    
class Deck:
    """represent 牌组
    Atrributes:
        cards: list of Card object
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self,card):#饰面veneer 
        self.cards.append(card)
    
    def shuffle(self):#洗牌
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
        
    def move_cards(self,hand,num):
        for i in range(num):#这里虽然写的像是从牌堆发牌到手上，但是也可反着调用实现手牌放回牌堆
            hand.add_card(self.pop_card())

class Hand(Deck):
    """represents 手牌,继承自Deck"""
    def __init__(self,lable = ''):
        self.cards = []
        self.lable = lable
        
  
card1 = Card(2,11)
print(card1)
deck = Deck()
print(deck)

deck.shuffle()

hand = Hand("My_cards")
deck.move_cards(hand,8)
print(hand)

#Practice
print("---------------------------------------------------Practice------------------------------------")
def deal_hands(hands,cards):
    Hands = []
    for i in range(hands):
        hand = Hand()
        deck.move_cards(hand,cards)
        Hands.append(hand)
    return Hands
      
game = deal_hands(3,8)
for i in range(3):
    print(game[i])
    
    
    
class PokerHand(Hand):
    """Represents a poker hand.
    Atrributes:
        all_lables : list of lables
        suits : dict of suits
        ranks : dict of ranks
        cards : inherit from Hand
    """
    
    all_labels = ['StraightFlush', 'FourOfaKind', 'FullHouse', 'flush',
                  'straight', 'threeOfaKind', 'twoPair', 'pair','HighCard']
    
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank,0) + 1
            
    def has_HighCard(self):
        return len(self.cards)
            
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_twoPair(self):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count+=1
        if count >= 2:
            return True
        else:
            return False
        
    def has_threeOfaKind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_FourOfaKind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_FullHouse(self):
        if self.has_threeOfaKind() and self.has_pair():
            return True
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_straight(self):
        self.rank_hist()
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1,0)
        return self.in_a_row(ranks,5)
    
    def in_a_row(self,ranks,n=5):
        count = 0
        for i in range(1,15):
            if ranks.get(i,0):
                count+=1
                if count == n:
                    return True
            else:
                count =0
        return False
    
    def has_StraightFlush(self):
        self.sort()
        count = 0
        ranks_club = {}
        ranks_diamond = {}
        ranks_spade = {}
        ranks_heart = {}
        for card in self.cards:
            if card.suit == 0: ranks_club[card.rank] = ranks_club.get(card.rank,0)+1
            if card.suit == 1: ranks_diamond[card.rank] = ranks_diamond.get(card.rank,0)+1
            if card.suit == 2: ranks_heart[card.rank] = ranks_heart.get(card.rank,0)+1
            if card.suit == 3: ranks_spade[card.rank] = ranks_spade.get(card.rank,0)+1
        ranks_club[14] = ranks_club.get(1,0)
        ranks_diamond[14] = ranks_diamond.get(1,0)
        ranks_heart[14] = ranks_heart.get(1,0)
        ranks_spade[14] = ranks_spade.get(1,0)
        if self.in_a_row(ranks_spade,5) or self.in_a_row(ranks_club,5) or self.in_a_row(ranks_diamond,5) or self.in_a_row(ranks_heart,5):
            return True
        
    def classify(self):
        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)   
        
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()
    print("----------------------------Poker-------------------------------")
    # deal the cards and classify the hands
    for i in range(3):
        hand = PokerHand()
        deck.move_cards(hand,10)
        hand.sort()
        print(hand)
        hand.classify()
        print(hand.labels)
        print('')
