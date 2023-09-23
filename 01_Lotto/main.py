import random


def gamble(n):
    if n <= 0:
        print("number must be positive")
        return

    max = 45
    num = []

    for i in range(max):
        num.append(i)

    res = {}
    for i in range(n):
        index = random.randint(0, max - 1)

        old = num[index]
        new = num[max - 1 - i]
        num[index], num[max - 1 - i] = new, old

    j = 0
    for i in range(max - n, max):
        res[j] = num[i]
        j += 1

    return res


res = {}
res = gamble(6)

if res.__sizeof__() >= 0:
    for i in range(len(res)):
        print(f"{i}: {res.get(i)}")
