
def total(stock):
    tot = 0
    for i in stock.values():
        tot += i
    return tot


# stock = {'pommes': 143, 'poires': 97, 'oranges': 155}
# print(total(stock))


def maj_heure(stock):
    for (fruit, n) in stock.items():
        if n > 10:
            stock[fruit] -= 10
        else:
            stock[fruit] = 0


# stock = {'pommes': 143, 'poires': 7, 'oranges': 155}
# print(stock)
# maj_heure(stock)
# print(stock)


def maj_totale(stock, n):
    for _ in range(n):
        maj_heure(stock)


# stock = {'pommes': 143, 'poires': 97, 'oranges': 155}
# print(stock)
# maj_totale(stock, 10)
# print(stock)


def maj_totale1(stock, n):
    maj_totale(stock, n)
    for n in list(stock.keys()):
        if stock[n] == 0:
            del stock[n]


# stock = {'pommes': 143, 'poires': 97, 'oranges': 155}
# print(stock)
# maj_totale1(stock, 10)
# print(stock)


def maj_arrivage(stock, arrivage):
    for (fruit, n) in arrivage:
        if fruit in stock:
            stock[fruit] += n
        else:
            stock[fruit] = n


# stock = {'pommes':143, 'poires': 97, 'oranges': 155}
# arrivage = [('cerises', 144), ('poires',100), ('cerises',200)]
# print(stock)
# maj_arrivage(stock, arrivage)
# print(stock)
