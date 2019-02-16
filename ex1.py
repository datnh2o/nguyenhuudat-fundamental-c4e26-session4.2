prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {"banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
total = 0
for fr in prices.keys():
    print(fr)
    print("price:", prices[fr])
    print("stock:", stock[fr])
    total += prices[fr] * stock[fr]
print()
print("Total: ", total)