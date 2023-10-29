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

----------------------------------------------------------
13 ... anzahl an symbolen, 1-10 + Jack + Queen + King
4 ... unteschiedliche '''farben''' also symbole



card	|	color 	|	value	|   card name
--------|-----------|-----------|-------------
0		|	0		|	0		|   CLUB ACE
1		|	0		|	1		|   CLUB 2
2		|	0		|	2		|   CLUB 3
3		|	0		|	3		|   CLUB 4
4		|	0		|	4		|   CLUB 5
5		|	0		|	5		|   CLUB 6
6		|	0		|	6		|   CLUB 7
7		|	0		|	7		|   CLUB 8
8		|	0		|	8		|   CLUB 9
9		|	0		|	9		|   CLUB 10
10		|	0		|	10		|   CLUB JACK
11		|	0		|	11		|   CLUB QUEEN
12		|	0		|	12		|   CLUB KING

card	|	color 	|	value	|   card name
--------|-----------|-----------|-------------
13		|	1		|	0		|   DIAMOND ACE
14		|	1		|	1		|   DIAMOND 2
15		|	1		|	2		|   DIAMOND 3
16		|	1		|	3		|   DIAMOND 4
17		|	1		|	4		|   DIAMOND 5
18		|	1		|	5		|   DIAMOND 6
19		|	1		|	6		|   DIAMOND 7
20		|	1		|	7		|   DIAMOND 8
21		|	1		|	8		|   DIAMOND 9
22		|	1		|	9		|   DIAMOND 10
23		|	1		|	10		|   DIAMOND JACK
24		|	1		|	11		|   DIAMOND QUEEN
25		|	1		|	12		|   DIAMOND KING

card	|	color 	|	value	|   card name
--------|-----------|-----------|-------------
26		|	2		|	0		|   HEART ACE
27		|	2		|	1		|   HEART 2
28		|	2		|	2		|   HEART 3
29		|	2		|	3		|   HEART 4
30		|	2		|	4		|   HEART 5
31		|	2		|	5		|   HEART 6
32		|	2		|	6		|   HEART 7
33		|	2		|	7		|   HEART 8
34		|	2		|	8		|   HEART 9
35		|	2		|	9		|   HEART 10
36		|	2		|	10		|   HEART JACK
37		|	2		|	11		|   HEART QUEEN
38		|	2		|	12		|   HEART KING

card	|	color 	|	value	|   card name
--------|-----------|-----------|-------------
39		|	3		|	0		|   SPADE ACE
40		|	3		|	1		|   SPADE 2
41		|	3		|	2		|   SPADE 3
42		|	3		|	3		|   SPADE 4
43		|	3		|	4		|   SPADE 5
44		|	3		|	5		|   SPADE 6
45		|	3		|	6		|   SPADE 7
46		|	3		|	7		|   SPADE 8
47		|	3		|	8		|   SPADE 9
48		|	3		|	9		|   SPADE 10
49		|	3		|	10		|   SPADE JACK
50		|	3		|	11		|   SPADE QUEEN
51		|	3		|	12		|   SPADE KING

10  HIGH CARD                   die höchste einzelne Karte

TODO: test if range(1,5) or range(1,6)
TODO: combine certains methods, like straight_flush() and straight(), or four_of_a_kind() and three_of_a_kind()

"""
import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

"""
def pair_three_of_a_kind_four_of_a_kind(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)
    # print(mods)
    # print(occ.most_common())
    # print(type(occ.most_common()[0][1]))

    if occ.most_common()[0][1] == 2:
        statistics['pair'] += 1
        return True
    elif occ.most_common()[0][1] == 3:
        statistics['three_of_a_kind'] += 1
        return True
    elif occ.most_common()[0][1] == 4:
        statistics['four_of_a_kind'] += 1
        return True
    return False
"""


def royal_flush(list):
    royal_flush_values = [0, 9, 10, 11, 12]
    list.sort()

    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

        # check for royal flush values
        if list[i - 1] % 13 != royal_flush_values[i - 1]:
            return False

    statistics['royal_flush'] += 1
    return True


def straight(list):
    mods = []
    for i in range(0, 5):
        mods.append(list[i] % 13)
    mods.sort()

    for i in range(1, 5):
        if mods[i - 1] + 1 != mods[i]:
            return False
    statistics['straight'] += 1
    return True


def straight_flush(list):
    list.sort()
    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

        # check for ascending values
        if list[i - 1] + 1 != list[i]:
            return False

    statistics['straight_flush'] += 1
    return True


def flush(list):
    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

    statistics['flush'] += 1
    return True


def four_of_a_kind(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 4:
        statistics['four_of_a_kind'] += 1
        return True
    return False


def three_of_a_kind(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 3:
        statistics['three_of_a_kind'] += 1
        return True
    return False


def pair(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)
    # print(mods)
    # print(occ.most_common())
    # print(type(occ.most_common()[0][1]))

    if occ.most_common()[0][1] == 2:
        statistics['pair'] += 1
        return True
    return False


def two_pair(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 2 and occ.most_common()[1][1] == 2:
        statistics['two_pair'] += 1
        return True
    return False


def full_house(list):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 3 and occ.most_common()[1][1] == 2:
        statistics['full_house'] += 1
        return True
    return False


def high_card():
    statistics['high_card'] += 1


statistics = {
    'royal_flush': 0,
    'straight_flush': 0,
    'four_of_a_kind': 0,
    'full_house': 0,
    'flush': 0,
    'straight': 0,
    'three_of_a_kind': 0,
    'two_pair': 0,
    'pair': 0,
    'high_card': 0,
}

cards = []
cards_amount = 52

for i in range(cards_amount):
    cards.append(i)

pull_cards_amount = 5
tries = 100000
# tries = 1


for i in range(tries):
    # current_pair = []

    # print(f"card\t|\tcolor\t|\tvalue")

    current_pair = random.sample(range(0, cards_amount), 5)
    # current_pair = [11,12,13,14,15]
    """
    straight is way off? 0% wtf
    """
    # for i in range(len(current_pair)):
    # print(f"{current_pair[i]}\t\t|\t{current_pair[i] // 13}\t\t|\t{current_pair[i] % 13}")

    if not royal_flush(current_pair):
        if not straight_flush(current_pair):
            if not four_of_a_kind(current_pair):
                if not full_house(current_pair):
                    if not flush(current_pair):
                        if not straight(current_pair):
                            if not three_of_a_kind(current_pair):
                                if not two_pair(current_pair):
                                    if not pair(current_pair):
                                        high_card()
# print()
# print(statistics)
# print(sum(statistics.values()))
"""
print("\n\n")
for i in statistics:
    print(f"{i}\t\t|\t{str(statistics[i])}")
    statistics[i] = statistics[i] / tries
"""

for i in statistics:
    # print(f"{str(statistics[i])}\t\t|\t\t{i}")
    statistics[i] = (statistics[i] / sum(statistics.values())) * 100
    # print(f"{str(statistics[i])}\t\t|\t\t{i}")

# https://en.wikipedia.org/wiki/Poker_probability#5-card_poker_hands

wikipedia_x = [0.000154, 0.00139, 0.02401, 0.1441, 0.1965, 0.3925, 2.1128, 4.7539, 42.2569, 50.1177]
plt.bar(statistics.keys(), wikipedia_x, color="red")
plt.xticks(rotation=45)
plt.title("Wikipedia")
plt.show()

plt.bar(statistics.keys(), statistics.values())
plt.xticks(rotation=45)
plt.show()

print(f"Wikipedia %\t\t|\t\tGwercher %\t|\t\tCard Hand")
print(f"----------------|-------------------|-----------------------")

j = 0
for i in statistics:
    #print(f"{str(statistics[i])}\t\t|\t\t{i}\t\t|\t\t{wikipedia_x[j]}")
    print(f"{round(wikipedia_x[j],4):.4f}\t\t\t|\t\t{round(statistics[i],4):.4f}\t\t|\t\t{i}")
    j += 1
"""
print(f"card\t|\tcolor \t|\tvalue\t|card name")
test = []
for i in range(52):
    test.append(i)
    print(f"{i}\t\t|\t{i // 13}\t\t|\t{i % 13}\t\t|\t")
"""
"""
test = [2, 15, 25, 12, 51]
full_house(test)

print(statistics)
"""
