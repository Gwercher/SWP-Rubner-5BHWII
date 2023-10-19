"""
poker mit indexes, keine klassse!

irgendwie mit module farbe oder symbol und dann auswerten oder so :3

list 0 - 51
5 karten ziehen
20 // 13 = 1 (farbe)
43 // 13 = 3 (andere farbe)
20 % 13 = 7 (symbol 7)
43 % 13 = 4 (symbol 4)

paar vergleichen: karte 1 == gleich?, wenn ja (gleiche symbol oder farbe) return true (kombination methoden!)
"""
import random

cards = []
cards_amount = 52

for i in range(cards_amount):
    cards.append(i)

pull_cards_amount = 5
current_pair = []
for i in range(pull_cards_amount):
    r = random.randint(0, cards_amount-1)

    current_pair.append(r)

print(current_pair)


