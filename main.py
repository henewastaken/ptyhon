import itertools, random
from collections import defaultdict, Counter
from copy import deepcopy
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
        # Luodaan pakka
        self.cards = list(itertools.product(range(1,14), ["Spades", "Clubs", "Diamonds", "Hearts"]))
        self.cards.insert(53, (0, "joker"))

        # Testipakka
        # self.cards = [(5,"c"), (3,"b"), (7,"a"), (2,"a"), (0,"joker")]

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

    #def get_card_value(self, hand):
     #   value = self.hand.


    def show_hand(self):
        for card in self.hand:
            print(card)

    def hand_total(self):
        return sum([p[0] for p in self.hand])


class Poker_hands:
    numbers = []
    suits = []
    result = []
    has_joker = False
    joker_numbers = []

    def __init__(self, hand, name):        
        self.name = name
        self.hand = hand
        # Lisätään luvut omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            self.numbers.append(i[0])
        
        # Lisätään maat omaan listaan käsittelyn helpottamiseksi
        for i in self.hand:
            self.suits.append(i[1])

        self.check_hand()

    # Tulostaa pelaajan nimen, ja handler funktion palauttaman kokonaisluvun
    # mukaan pokerikäden.    
    def check_hand(self):
        switcher = {
            1: "high card",
            2: "pair",
            3: "two pair",
            4: "triple",
            5: "straight",
            6: "flush",
            7: "full house",
            8: "fours",
            9: "straight flush",
            10: "fives"
        }
        result = switcher.get(self.handdeler())
        print(self.name, "has a", result)

    # Kutsutaan käden tarkastus funktioita, ja palautetaan int. 
    # 1=hai, 2=pari, 3=kaksi paria, 4=kolmoset, 5=suora, 6=väri, 7=täyskäsi,
    # 8=neloset, 9=vitoset(vain check_fours palauttaa tämän), 10 = värisuora
    def handdeler(self):
        self.check_joker()
        # Värisuora
        if (self.check_straight_flush(deepcopy(self.numbers))):
           return 9
        # Täyskäs
        elif (self.check_full_house(deepcopy(self.numbers))):
            return 7
        # Väri
        elif (self.check_flush()):
            return 6
        # Suora
        if (self.check_straight(deepcopy(self.numbers))):
            return 5
        # Viisi samaa
        elif (self.check_fives(deepcopy(self.numbers))):
            return 10
        # Neljä samaa
        elif (self.check_fours(deepcopy(self.numbers))):
            return 8
        # Kolme samaa
        elif(self.check_triples(deepcopy(self.numbers))):
            return 4
       # Kaksi paria
        elif (self.check_two_pair(deepcopy(self.numbers))):
            return 3
        #Pari
        elif(self.check_pair(deepcopy(self.numbers))):
            return 2
        # Suurin kortti
        elif(self.check_high_card(deepcopy(self.numbers))):
            return 1
        


    def check_high_card(self, cards):  
        # Jos sisältää ässän (1), muutetaan se olemaan 14

        self.check_ace(cards)

        return True

    def check_pair(self, cards):
        self.check_ace(cards)
        v_amount = 2
        # Tarkistetaan jokeri
        if (self.has_joker): 
            # Muutetaan jokeri suurimman kortin arvoksi
            cards.remove(0)
            cards.append(max(cards))

        # Tarkistetaan uniikit esiintymisest. Pari => v == 2 && len(x) == 1
        x = ([k for (k, v) in Counter(cards).items() if v == v_amount])
        if (len(x) == 1):
            return True
        else:
            return False

    def check_two_pair(self, cards):
        # Kahden parin kohdalla ei tarkisteta jokeria, sillä jokerilla ei voi saada kahta paria
        self.check_ace(cards)
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos v == 2 && len(x) == 2
        x = ([k for (k, v) in Counter(cards).items() if v == 2])
        if (len(x) == 2):
            return True
        else: 
            return False

    def check_triples(self, cards):
        self.check_ace(cards)
        v_amount = 3
        
        # Asetetaan v_amount uusi arvo, jos löytyy jokeri
        if (self.has_joker): 
            v_amount = 2
    
        # Tarkistetaan uniikit esiintymisest.
        x = ([k for (k, v) in Counter(cards).items() if v == v_amount])
        if (len(x) == 1):
            return True 
        else: 
            return False
            
    def check_fours(self, cards):
        self.check_ace(cards)
        v_ammount = 4

        # Asetetaan v:lle auusi arvo jos on jokeri
        if (self.has_joker):
            v_ammount = 3

        # Tarkistetaan uniikit esiintymisest.    
        x = ([k for (k, v) in Counter(cards).items() if v == v_ammount])
        
        if (len(x) == 1):
            return True
        else:
            return False

    def check_fives(self, cards):
        v_amount = 4
        self.check_ace(cards)

        # Tarkistetaan vitoset. Tosi vain jos kädestä löytyy jokeri
        if (self.has_joker):
            x = ([k for (k, v) in Counter(cards).items() if v == v_amount])
            # Tarkistetaan korttien samuus
            if (len(x) == 1):
                return True
            else:
                return False
        # Kädessä ei ole jokeria, joten ei voi olla vitoset
        else:
            return False

    def check_flush(self):
        # Poisrtetaan mahdollinen jokeri, tarksitetaan 4 kortin väri, ja muutetaan
        # jokeri halutuksi maaksi
        v_amount = 5
        
        if ('joker' in self.suits):
            self.suits.remove('joker')
            v_amount = 4  
        x = ([k for (k, v) in Counter(self.suits).items() if v == v_amount])
        if (len(x) == 1):
            return True

    def check_straight(self, cards):
        # Muutetaan ässä 14 jos kädessä on 13
        if (13 in cards):
            self.check_ace(cards)
        # Järjestetään käsi
        cards.sort()      

        #  Jokerin käsittely.
        if (self.has_joker):
            # Apulista, jota käsitellään
            help_joker = deepcopy(self.joker_numbers)
            help_joker.sort()
            # Booleand onko jokereita kädessä
            joker_slot = True
            
            i = 0
            # Käydään käsi läpi ja laksetaan korttien erotukset. 
            # Palautetaan False jo erotus != 1
            while (i < len(help_joker)):
                # Tarkistetaan erotus
                if (i+1 < len(help_joker) and 
                        help_joker[i+1] - help_joker[i] != 1):
                    # Jos joekria ei ole vielä käytetty, merkitään se käytetyksi
                    # Lisätään jokeri arvo listaan, ja vähennetään i yhdellä,
                    # jotta jokeri tulee tarkistukseen mukaan
                    if (joker_slot):
                        joker_slot = False
                        help_joker.append(help_joker[i]+1)
                        help_joker.sort()
                        i -= 1
                    # Jokeri on jo kertaalleen käytetty palautetaan false
                    else:
                        return False
                i += 1
            # Suora löytyi, palautetaan true
            return True

        # Suora jokeria, tarkistetaan normaalsiti vertaamalla erotuksia
        for i in range(len(cards)):
            if (i+1 < len(cards) and cards[i+1] - cards[i] != 1):
                return False

        return True   

    def check_full_house(self, cards):
        # Tarkistetaan ässä
        self.check_ace(cards)

        # Jos on jokeri, tarkistetaan käsi ilman jokeria onko kädessä kaksi paria
        if (self.has_joker):
            if (self.check_two_pair(deepcopy(self.joker_numbers))):
                # self.joker_numbers.append(max(self.joker_numbers))
                return True

        # Ei ole jokeria, tarksitetaan onko kädessä pari ja kolmoset
        elif (self.check_pair(cards) == True and self.check_triples(cards)):
            return True
        else:
            return False

    def check_straight_flush(self, cards):
        if (self.check_straight(cards) == True and self.check_flush() == True):
            return True
        else: 
            return False
    
    # Muuttaa ässät arvosta 1 arvoon 14
    def check_ace(self, cards):
        for i, value in enumerate(cards):
            if (value == 1):
                cards[i] = 14
        return cards
    
    # Palauttaa boolean onko jokeri
    def check_joker(self):
        if (0 in self.numbers):
            self.has_joker = True
            self.joker_numbers = self.numbers.copy()
            self.joker_numbers.remove(0)


def main():

    deck = Deck()
    deck.shuffle()

   # alice = Player("Alice")
    bob = Player("Bob")

    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)

   # print(bob.name)
    bob.show_hand()

  #  print(alice.name)
   # alice.show_hand()


    Poker_hands(bob.hand, bob.name)
   # Poker_hands(alice.hand, alice.name)

if __name__ == "__main__":
    main()


    # Vertaa kahta ekaa korttia. Tarvitaan blackjack toteutuksen 

    #print(" sum:", bob.hand_total())
    # if (alice.hand_total() == bob.hand_total()):
    #     print("Tie!")
    # else:       
    #     winner = ("Alice won", "Bob won",) [alice.hand_total() < bob.hand_total()]
    #     print(f'{winner}')
    
    #    def check_same_numbers(self, l, amount):
    #     result = dict((i, Poker_hands.numbers.count(i)) for i in Poker_hands.numbers)

    #     print("max", max(result.values()))
    #     print("count", list(result.values()).count(max(result.values())))
    #     print(result.values())

    #     # täyskäsi
    #     if ()

    #     # Palautetaan max value, joka käsitellään myöhemmin.
    #     if (max(result.values()) >= 2):
    #         print("returned", max(result.values()))
    #         return max(result.values())
        

        # Lasketaan käden keskiarvo.
            # Jos keskiarvo on kokonaisluku, on jokeri keskellä suoraa ja kokonaisluvun arvo.
            # Lisätään käteen ja järjestetään uudelleen
            # average = sum(help_joker) / len(help_joker)
            # print(int(average))
            # if (average.is_integer()):
            #     help_joker.append(int(average))
            #     help_joker.sort()
            # # Else, jotta järjestetään lista vaan kerran
            # else:
            #     help_joker.sort()