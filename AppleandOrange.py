print("Our apple costs 20 pesos each while our orange is 25 pesos each.")
apple = int(input("How many apples do you want to buy? "))
orange = int(input("How many oranges do you want to buy? "))

pplprc = 20
rngprc = 25

applettl = apple * pplprc
orangettl = orange * rngprc
total = applettl + orangettl
print(f"The total amount is {total} pesos.")
