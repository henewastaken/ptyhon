import itertools, random
from collections import defaultdict, Counter
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def print_card(self):
        print(self.suit, self.number)
    
class Deck:
    def __init__(self):
        self.cards = list()
        self.make_deck()

    def make_deck(self):
        #self.cards = list(itertools.product(range(1,14), ["Spades", "Clubs", "Diamonds", "Hearts"]))
        # Testipakka
        #self.cards = [(0,"a"), (10,"b"), (10,"a"), (11,"a"),(12,"a")]
        self.cards.insert(53, (0, "joker"))

                
    # Pakan tulostus
    def print_deck(self):
        for c in self.cards:
            c.print_card()

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
    numbers = []
    suits = []
    result = []
         


    def __init__(self, hand):
        self.hand = hand
        # Lisätään luvut omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            Poker_hands.numbers.append(i[0])
        
        # Lisätään maat omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            Poker_hands.suits.append(i[1])
        self.check_hand()

    def check_hand(self):

        joker = False
        # Tarkistetaan jokeri
        for card in self.hand:
            if (card[0] == 0):
                joker = True

        # kolmoset (jokeri -> neloset)
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 3])
        if (len(x) == 1):
            # Jos on kolmoset ja jokeri, tulee kädestä neloset
            if (joker):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
                self.check_fours()
            else:
                Poker_hands.result = ["tripple of", x]

        # Kaksi paria (jokeri -> täyskäsi)
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 2])
        if (len(x) == 2):
            # Jos jokeri ja kaksi paria, tulee kädestä täyskäsi
            if (joker):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
                # Muuta tää täyskädeksi  self.check_fours()
            else:
                Poker_hands.result = ["two pairs of", x]

        # Pari (jokeri -> kolmoset)
        elif (len(x) == 1):
            # Jos jokeri ja para, tulee kädestä kolmoset
            if (joker):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
                self.check_triples()
            else:
                Poker_hands.result = ["pair of", x]


        
        
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
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 3])
        if (len(x) == 1):
            Poker_hands.result = ["triples of ", x]
            self.printer()


    def check_fours(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos len(x) == 3
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 4])
        if (len(x) == 1):
            Poker_hands.result = ["fours of ", x]
            self.printer()


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
        # Poistetaan ässä (1), tarkistetaan suora ja lisätään loppuun 14 jos suora on
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
        # Jos sisältää ässän (1), muutetaan se olemaan 14
        if 1 in values:
            values.remove(1)
            values.append(14)
        values.sort(reverse=True) 
        return values


    # Palauttaa käsien tarkistuksen tuloksen
    def printer(self):
        return Poker_hands.result

def check_poker_hand(Player):
    player = Poker_hands(Player.hand)


    pair_check = player.check_pair()
    two_pair_check = player.check_two_pair()
    triple_check = player.check_triples()
    fours_check = player.check_fours()
    flush_check = player.check_flush()
    straight_check = player.check_straight()
    ordered_hand = player.high_card()
    player.check_hand()
    # Tarkistetaan värisuora
    # if (straight_check and flush_check):
    #     return  Player.name + " has Straight flush of:", straight_check, flush_check
    # Täyskäsi
    # elif (triple_check and pair_check):
    #     return Player.name + " has full house of:", triple_check, pair_check
    # Väri
    # elif (flush_check):
    #     return Player.name + " has a straigh of:", flush_check
    # Suora
    # elif (straight_check):
    #     return Player.name + " had a flush of:", straight_check
    # Neljä samaa
    # elif (fours_check):
    #     return Player.name + " has fours of:", fours_check
    # Kolme samaa
    # elif(triple_check):
    #     return Player.name + " has trippes of:", triple_check
    # Kaksi paria
    # elif (two_pair_check):
    #     return Player.name + " have two pairs of:",two_pair_check
    # Pari
    # elif(pair_check):
    #     return Player.name + " have a pair of:", pair_check
    # Ei mitään / Korkein kortti
    # else:
    #     return Player.name + " has only a high card:", ordered_hand

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
    print(bob_hand.printer())
    #print (check_poker_hand(bob))
    #bob_hand = Poker_hands(bob.hand)
    #print(bob_hand.check_hand())

if __name__ == "__main__":
    main()


    # Vertaa kahta ekaa korttia. Tarvitaan blackjack toteutuksen 

    #print(" sum:", bob.hand_total())
    # if (alice.hand_total() == bob.hand_total()):
    #     print("Tie!")
    # else:       
    #     winner = ("Alice won", "Bob won",) [alice.hand_total() < bob.hand_total()]
    #     print(f'{winner}')
    