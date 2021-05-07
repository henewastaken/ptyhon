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
        # Luodaan pakka
        self.cards = list(itertools.product(range(1,14), ["Spades", "Clubs", "Diamonds", "Hearts"]))
        self.cards.insert(53, (0, "joker"))

        # Testipakka
        #self.cards = [(12,"a"), (12,"c"), (0,"joker"), (4,"a"),(5,"a")]
                
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
    numbers = []
    suits = []
    result = []

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

        # Värisuorea
        if (self.check_straight_flush()):
            return 10
        # Täyskäs
        elif (self.check_full_house()):
            return 7
        # Väri
        elif (self.check_flush()):
            return 6
        # Suora
        elif (self.check_straight()):
            return 5
        # Neljä samaa
        elif (self.check_fours()):
            return 8
        # Kolme samaa
        elif(self.check_triples()):
            return 4
       # Kaksi paria
        elif (self.check_two_pair()):
            return 3
        #Pari
        elif(self.check_pair()):
            if (self.check_pair() == 3):
                return 4
            return 2
        # Suurin kortti
        elif(self.check_high_card()):
            return 1
        
    def check_high_card(self):  
        # Jos sisältää ässän (1), muutetaan se olemaan 14
        self.check_ace()
        # Tarkistetaan jokeri    
        if (self.joker_handler(max(Poker_hands.numbers))):
            return self.check_pair()   

        Poker_hands.numbers.sort(reverse=True) 
        return True

    def check_pair(self): 
        self.check_ace()
        # Tarkistetaan uniikit esiintymisest. Sisältää parin jos v == 2 && len(x) == 1
        x = ([k for (k, v) in Counter(self.numbers).items() if v == 2])
        if (len(x) == 1):
            if (self.joker_handler(x[0])):
                if (self.check_triples()):
                    # Palautetaan 3 returner funktion käsittelyn helpottamiseksi
                    return 3
            else:
                #return "pair of:", x
                return True

    def check_two_pair(self):
        self.check_ace()
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos v == 2 && len(x) == 2
        x = ([k for (k, v) in Counter(self.numbers).items() if v == 2])
        if (len(x) == 2):
           # Jos jokeri ja kaksi paria, tulee kädestä täyskäsi
            if (self.joker_handler(max(x))):
                if (self.check_full_house):
                     # Palautetaan 32 returner funktion käsittelyn helpottamiseksi
                    return 32
            else:
                #return "two pairs of:", x
                return True

    def check_triples(self):
        self.check_ace()
        # Tarkistetaan uniikit esiintymisest. Sisältää kaksi paria jos v == 3 && len(x) == 3
        x = ([k for (k, v) in Counter(self.numbers).items() if v == 3])
        if (len(x) == 1):
            if (self.joker_handler(x[0])):
                if (self.check_fours()):
                    # Palautetaan 4 returner funktion käsittelyn helpottamiseksi
                    return 4
            else:
                #return "Triples of:", x
                return True  
            
    def check_fours(self):
        self.check_ace()
        # Tarkistetaan uniikit esiintymisest. Sisältää neloset v == 4 && len(x) == 1
        x = ([k for (k, v) in Counter(self.numbers).items() if v == 4])
        if (len(x) == 1):
            if (self.joker_handler(x[0])):
                if (self.check_fives()):
                    # Palautetaan 9 returner funktion käsittelyn helpottamiseksi
                    return 9
            else:
               # print("Fours of:", x)
                return True

    def check_fives(self):
        self.check_ace()
        # Tarkistetaan uniikit esiintymisest. Sisältää vitoset v == 5 &&len(x) == 1
        x = ([k for (k, v) in Counter(self.numbers).items() if v == 5])
        if (len(x) == 1):
           #return "Fives of", x
            return True

    def check_flush(self):
        # Poisrtetaan mahdollinen jokeri, tarksitetaan 4 kortin väri, ja muutetaan
        # jokeri halutuksi maaksi
        if ('joker' in Poker_hands.suits):
            self.suits.remove('joker')
            x = ([k for (k, v) in Counter(self.suits).items() if v == 4])
            if (len(x) == 1):
                self.suits.append(x[0])
                return True
        else:    
            x = ([k for (k, v) in Counter(self.suits).items() if v == 5])
            if (len(x) == 1):
                return True

    def check_straight(self):
        # Muutetaan ässä 14 jos kädessä on 13
        if (13 in self.numbers):
            self.check_ace()
        # Järjestetään käsi
        self.numbers.sort()       

        #  Jokerin käsittely. Poisteaan jokeri ja lasketaan käden keskiarvo
        if (0 in self.numbers):
            self.numbers.remove(0)
            average = sum(self.numbers) / len(self.numbers)

            # Jos keskiarvo on kokonaisluku, on jokeri keskellä suoraa
            # ja kokonaisluvun arvo. Lisätään käteen ja järjestetään uudelleen
            if (average.is_integer()):
                self.numbers.append(int(average))
                self.numbers.sort()

            # Käydään käsi läpi ja laksetaan korttien erotukset. 
            # Palautetaan False jo erotus != 1
            for i in range(len(self.numbers)):
                if (i+1 < len(self.numbers) and 
                        self.numbers[i+1] - self.numbers[i] != 1):
                    return False
            
            # Jos käden koko on 4 korttia, lisätään jokeri suoran perään
            if (len(self.numbers) == 4):
                # Tarkisteaan onko kädessä ässä, jolloin jokerista tulee pienin kortti -1
                if (14 in self.numbers):
                    self.numbers.append(self.numbers[0]-1)
                else:
                    self.numbers.append(self.numbers[-1]+1)
            return True

        # Suora jokeria, tarkistetaan normaalsiti vertaamalla erotuksia
        for i in range(len(self.numbers)):
            if (i+1 < len(self.numbers) and self.numbers[i+1] - self.numbers[i] != 1):
                return False
        return True   

    def check_full_house(self):
        if (self.check_pair() == True and self.check_triples()):
            return True

    def check_straight_flush(self):
        if (self.check_flush() and self.check_straight()):
            return 10
    
    # Muuttaa ässät arvosta 1 arvoon 14
    def check_ace(self):
        for i, value in enumerate(self.numbers):
            if (value == 1):
                self.numbers[i] = 14
    
    # Tarkistetaan jokeri
    # Muuttaa jokerin parametrina annetuksi arvoksi ja palauttaa true jos jokeri on
    def joker_handler(self, new_value):
        if (0 in self.numbers):
            index = self.numbers.index(0)
            self.numbers[index] = new_value
            return True 

        return False
        

def main():

    deck = Deck()
    deck.shuffle()

    alice = Player("Alice")
    bob = Player("Bob")
    alice.draw(deck)
    alice.draw(deck)
    alice.draw(deck)
    alice.draw(deck)
    alice.draw(deck)

    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)
    bob.draw(deck)

    print(bob.name)
    bob.show_hand()

    print(alice.name)
    alice.show_hand()

    
    Poker_hands(bob.hand, bob.name)
    Poker_hands(alice.hand, alice.name)

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
        