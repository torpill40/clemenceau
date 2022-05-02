
stock = {"pommes": 143, "poires": 97, "oranges": 155}
stock["cerises"] = 144

# for (fruit, masse) in stock.items():
#     print(f"{fruit}: quantité {masse} kg")

for (fruit, masse) in stock.items():
    if masse > 100:
        print(f"{fruit}: quantité {masse} kg")
