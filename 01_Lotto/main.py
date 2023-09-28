import random
import pandas as pd
from matplotlib import pyplot as plt
def gamble(n, res):
    if n <= 0:
        print("number must be positive")
        return

    max = 45
    num = []

    for i in range(max):
        num.append(i)

    for i in range(n):
        index = random.randint(0, max - 1 - i)

        old = num[index]
        new = num[max - 1 - i]
        num[index], num[max - 1 - i] = new, old
        res.append(old)

    return res


def statistic(res, dic):
    for i in range(len(res)):
        dic[res[i]] = dic[res[i]] + 1


dic = {}
for x in range(45):
    dic[x] = 0

tries = 100

for n in range(tries):
    res = []
    gamble(6, res)
    statistic(res, dic)

height = []
for i in range(len(dic)):
    print(f"{i}: {dic.get(i)}")
    height.append(dic.get(i))

x_coords = []
tick_label = []
for x in range(45):
    x_coords.append(x)
    tick_label.append(x)

left = []
for x in range(45):
    left.append(x)

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.5, color=['red', 'green'])

# naming the x-axis
plt.xlabel('count')
# naming the y-axis
plt.ylabel('numbers')

fig = plt.figure(figsize =(300, 300))

plt.show()

# https://www.w3schools.com/python/matplotlib_bars.asp