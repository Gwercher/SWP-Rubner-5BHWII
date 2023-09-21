import random


def gamble(n):
    max = 45
    num = []
    res = {}
    for i in range(max):
        num.append(i)

    for i in range(n):
        print("i=" + str(i))
        print("num=" + str(num))
        print("res=" + str(res))
        x = random.randint(0, max - 1)
        print("x="+str(x))
        res[i] = num[x]

        num[i], num[max - 1 - i] = num[max - 1 - i], num[i] # logic error here!!!
        # print(x)
        # print(num[x])
        print()

    return res


res = {}
res = gamble(6)
print(res)
