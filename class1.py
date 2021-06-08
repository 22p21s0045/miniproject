import random as rd
import re 

class Deck:
    def __init__(self,card_number):
        card_number = 13
        self.number = card_number
    def all(self):
        cards = []
        for i in range(self):
            cards.append(i)
        card = [cards]*4
        print(card)
        return card
        card = cards
    def pick(self):
        x = rd.randint(0,3)
        c = rd.randint(0,3)
        y = rd.randint(0,14)
        s = ['Spades','Club','Diamond','Heart']
        e = s[x]
        show = y,e
        print(show)
        return show
class Player:
    
    
    def __init__(self, name):
        name = 'gg'
        self.name = name
        self.hand = []
        print ("\n--Welcome {}--".format(self.name))

    def draw(self, deck):
        print("\n{} draw a card".format(self.name))
        self.hand.append(Deck.pick())
        return self
name =str(input())

g = Player.draw()        
       




