import itertools, random
from collections import defaultdict, Counter
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def prtin_card(self):
        print(self.suit, self.number)
    
class Deck:
    def __init__(self):
        self.cards = list()
        self.make_deck()

    def make_deck(self):
        self.cards = list(itertools.product(range(1,14), ["Spades", "Clubs", "Diamonds", "Hearts"]))
        # Testimuuttuja
        #self.cards = [(1,"a"), (10,"b"), (11,"a"), (12,"a"),(13,"a")]
        self.cards.insert(53, (0, "joker"))

                
    # Pakan tulostus
    def print_deck(self):
        for c in self.cards:
            c.prtin_card()

    # Pakan sekoitus
    def shuffle(self):
        random.shuffle(self.cards)
       

    def draw(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        return self.hand.append(deck.draw())

    #def get_card_value(self, hank):
     #   value = self.hand.


    def show_hand(self):
        for card in self.hand:
            print(card)

    def hand_total(self):
        return sum([p[0] for p in self.hand])


class Poker_hands:
    # muistiinpano, pätkä laskee montako samooja elem esiintyy
    #        indices = len(set(values))

    def __init__(self, hand):
        self.hand = hand


    def check_pair(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        # Tarkistetaan uniikit esiintymisest. Sisältää parin jos len(x) == 1
        x = ([k for (k, v) in Counter(values).items() if v == 2])
        if (len(x) == 1):
            return x


    def check_two_pair(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos len(x) == 2
        x = ([k for (k, v) in Counter(values).items() if v == 2])
        if (len(x) == 2):
            return x


    def check_triples(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos len(x) == 3
        x = ([k for (k, v) in Counter(values).items() if v == 3])
        if (len(x) == 1):
            return x


    def check_fours(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos len(x) == 3
        x = ([k for (k, v) in Counter(values).items() if v == 4])
        if (len(x) == 1):
            return x


    def check_flush(self):
        values = []
        for i in self.hand:
            values.append(i[1])
        x = ([k for (k, v) in Counter(values).items() if v == 5])
        if (len(x) == 1):
            return x


    def check_straight(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        values.sort()

        # Tarkistetaan onko kädessä ässää ja kuningasta, tarkastetaan suora jos on
        if 1 in values and 13 in values:
            values.remove(1)
            for i in range(len(values)):
                if (i+1 < len(values) and values[i+1] - values[i] != 1):
                    return False
            values.append(14)

        for i in range(len(values)):
            if (i+1 < len(values) and values[i+1] - values[i] != 1):
                return False

        return values   


    def high_card(self):
        values = []
        for i in self.hand:
            values.append(i[0])
        values.sort(reverse=True) 
        return values


def main():

    deck = Deck()
    deck.shuffle()

    #alice = Player("Alice")
    bob = Player("Bob")

    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)

    print(bob.name)
    bob.show_hand()
    
    bob_hand = Poker_hands(bob.hand)
    pair_check = bob_hand.check_pair()
    two_pair_check = bob_hand.check_two_pair()
    triple_check = bob_hand.check_triples()
    fours_check = bob_hand.check_fours()
    flush_check = bob_hand.check_flush()
    straight_check = bob_hand.check_straight()
    ordered_hand = bob_hand.high_card()
   
    if (straight_check and flush_check):
        print("Bob has Straight flush of:", straight_check, flush_check)
    elif (triple_check and pair_check):
        print("Bob has full house of:", triple_check, pair_check)
    elif (flush_check):
        print("Bob has a straigh of:", flush_check)
    elif (straight_check):
        print("Bob had a flush of:", straight_check)
    elif (fours_check):
        print("Bob has fours of:", fours_check)
    elif(triple_check):
        print("Bob has trippes of:", triple_check)
    elif (two_pair_check):
        print("Bob have two pairs of:",two_pair_check)
    elif(pair_check):
        print("Bob have a pair of:", pair_check)
    else:
        print("Bob has a high card:", ordered_hand)




if __name__ == "__main__":
    main()


    # Vertaa kahta ekaa korttia. Tarvitaan blackjack toteutuksen 

    #print(" sum:", bob.hand_total())
    # if (alice.hand_total() == bob.hand_total()):
    #     print("Tie!")
    # else:       
    #     winner = ("Alice won", "Bob won",) [alice.hand_total() < bob.hand_total()]
    #     print(f'{winner}')
    