from card import Card
from random import shuffle 

class deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # nb this is the same as this - which looks more logical
        # for suit in suits:
        #     for value in values:
        #         self.cards.append((Card(value, suit)))

    def __repr__(self):
        return f"This deck contains {len(self.cards)} cards"

    def shuffle(self):
        if len(self.cards) < 52:
             raise ValueError(f"You can't have to have a full deck ") 
        # this is the shuffle we imported
        shuffle(self.cards)
        # convention/best practice to return self
        return self
        

    def _deal(self, num):
        
        count = len(self.cards)
        if count == 0:
            raise ValueError("All cards have been dealt")
        actual = min([count, num])
        print(f"Going to remove {actual} cards")
            
        dealt = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return dealt

    def deal_card(self):
         #using[0] to get the actual 
        # card not a list with a item
        return self._deal(1)[0] 
    
    def deal_hand(self, hand_size):
         #using[0] to get the actual 
        # card not a list with a item
        return self._deal(hand_size)
       
    

            
x = deck()
# print(x.cards)
print(x)
x.shuffle()
# print(x.cards)
print(x.deal_hand(12))
print(x)
