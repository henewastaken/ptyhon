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
        #self.cards.insert(53, (0, "joker"))

        # Testipakka
        self.cards = [(1,"a"), (7,"b"), (2,"a"), (13,"a"),(3,"a")]
                
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
    joker = False  


    def __init__(self, hand, name):        
        self.name = name
        self.hand = hand
        # Lisätään luvut omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            Poker_hands.numbers.append(i[0])
        
        # Lisätään maat omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            Poker_hands.suits.append(i[1])

        self.check_hand()
        
        

    def check_hand(self):

        # Tarkistetaan jokeri
        for card in self.hand:
            if (card[0] == 0):
                Poker_hands.joker = True

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


        # pair_check = self.check_pair()
        # two_pair_check = self.check_two_pair()
        # triple_check = self.check_triples()
        # fours_check = self.check_fours()
        # flush_check = self.check_flush()
        # straight_check = self.check_straight()
        # full_house_check = self.check_full_house()
        # ordered_hand = self.high_card()
        # Tarkistetaan värisuora
        print(Poker_hands.numbers)
        # if (self.check_straight() and self.check_flush()):
        #     Poker_hands.result = self.name + " has Straight flush of:"
        #Täyskäsi
        if (self.check_full_house()):
            Poker_hands.result = self.name + " has full house of:"
        #Väri
        elif (self.check_flush()):
            Poker_hands.result = self.name + " has a flush of:"
       # Suora
        elif (self.check_straight()):
            Poker_hands.result = self.name + " had a straigh of:"
        #Neljä samaa
        elif (self.check_fours()):
            Poker_hands.result = self.name + " has fours of:"
        # Kolme samaa
        elif(self.check_triples()):
            Poker_hands.result = self.name + " has tripes of:"
       # Kaksi paria
        elif (self.check_two_pair()):
            Poker_hands.result = self.name + " have two pairs of:"
        #Pari
        elif(self.check_pair()):
            Poker_hands.result = self.name + " have a pair of:"
        # Suurin kortti
        elif(self.check_high_card()):
            Poker_hands.result = self.name + " has high card of:"
        #Ei mitään / Korkein kortti
        # else:
        #     return Player.name + " has only a high card:", ordered_hand


        # elif (self.check_fours()):
        #     Poker_hands.result = self.check_triples()
        # # Kolmoset (jokeri -> neloset)
        # elif (self.check_triples()):
        #     Poker_hands.result =  self.check_triples()
        # # Kaksi pari (jokeri -> täyskäsi)
        # elif (self.check_two_pair()):
        #     Poker_hands.result =  self.check_two_pair()
        # # Pari (jokeri -> kolmoset)
        # elif (self.check_pair()):
        #     Poker_hands.result = self.check_pair()
        # Else jotain muuta
        print(Poker_hands.numbers)
            # Kutstutaan tulostajaa joka tulostaa käden kivasti
        self.printer()
        
        
    def check_pair(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää parin jos v == 2 && len(x) == 1
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 2])
        if (len(x) == 1):
            if (0 in Poker_hands.numbers):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
                Poker_hands.joker = False # Jokeri on poistettu (muutetuu), asetetaan falseksi
                if (self.check_triples()):
                    return self.check_triples()
            else:
                #return "pair of:", x
                return True

    def check_two_pair(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos v == 2 && len(x) == 2
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 2])
        if (len(x) == 2):
           # Jos jokeri ja kaksi paria, tulee kädestä täyskäsi
            if (0 in Poker_hands.numbers):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(max(x))
              #  Poker_hands.joker = False # Jokeri on poistettu (muutetuu), asetetaan falseksi
                if (self.check_full_house):
                    return self.check_full_house
            else:
                #return "two pairs of:", x
                return True

    def check_triples(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos v == 3 && len(x) == 3
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 3])
        if (len(x) == 1):
            if (0 in Poker_hands.numbers):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
               # Poker_hands.joker = False # Jokeri on poistettu (muutetuu), asetetaan falseksi
                if (self.check_fours()):
                    return self.check_fours()
            else:
                #return "Triples of:", x
                return True  
            
    def check_fours(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää neloset v == 4 && len(x) == 1
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 4])
        if (len(x) == 1):
            if (0 in Poker_hands.numbers):
                Poker_hands.numbers.remove(0)
                Poker_hands.numbers.append(x[0])
               # Poker_hands.joker = False # Jokeri on poistettu (muutetuu), asetetaan falseksi
                if (self.check_fours()):
                    self.check_fives()
            else:
               # print("Fours of:", x)
                return True

    def check_fives(self):
        # Tarkistetaan uniikit esiintymisest. Sisältää vitoset v == 5 &&len(x) == 1
        x = ([k for (k, v) in Counter(Poker_hands.numbers).items() if v == 5])
        if (len(x) == 1):
           #return "Fives of", x
            return True

    def check_full_house(self):
        if (self.check_pair() and self.check_triples()):
            return True

    def check_flush(self):
        if ('joker' in Poker_hands.suits):
            Poker_hands.suits.remove('joker')
            x = ([k for (k, v) in Counter(Poker_hands.suits).items() if v == 4])
            if (len(x) == 1):
                Poker_hands.suits.append(x[0])
              #  Poker_hands.joker = False
                return True
        else:    
            x = ([k for (k, v) in Counter(Poker_hands.suits).items() if v == 5])
            if (len(x) == 1):
                return True
# TODO jokeri käsittely
    def check_straight(self):
        Poker_hands.numbers.sort()
        # Tarkistetaan onko kädessä ässää ja kuningasta, tarkastetaan suora jos on
        # Poistetaan ässä (1), tarkistetaan suora ja lisätään loppuun 14 jos suora on
        if 1 in Poker_hands.numbers and 13 in Poker_hands.numbers:
            Poker_hands.numbers.remove(1)
            for i in range(len(Poker_hands.numbers)):
                if (i+1 < len(Poker_hands.numbers) and Poker_hands.numbers[i+1] - Poker_hands.numbers[i] != 1):
                    Poker_hands.numbers.append(1) # Asetetaan 1 takaisin, jos ei ole suora
                    return False
            Poker_hands.numbers.append(14)

        for i in range(len(Poker_hands.numbers)):
            if (i+1 < len(Poker_hands.numbers) and Poker_hands.numbers[i+1] - Poker_hands.numbers[i] != 1):
                return False
        return True   

    def check_high_card(self):
        # Jos sisältää ässän (1), muutetaan se olemaan 14
        print(Poker_hands.numbers)
        if (1 in Poker_hands.numbers):
            print("on ässä")
            Poker_hands.numbers.remove(1)
            Poker_hands.numbers.append(14)
        # Tarkistetaan jokeri    
        if (0 in Poker_hands.numbers):
            Poker_hands.numbers.remove(0)
            Poker_hands.numbers.append(max(Poker_hands.numbers))
            return self.check_pair()   

        Poker_hands.numbers.sort(reverse=True) 
        return True


    # Palauttaa käsien tarkistuksen tuloksen
    def printer(self):
        return Poker_hands.result

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
    
    bob_hand = Poker_hands(bob.hand, bob.name)
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
    