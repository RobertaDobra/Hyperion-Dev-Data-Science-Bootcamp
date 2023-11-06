menu = ["coffee", "to-go coffee", "unsweetened coffee", "strong coffee"] #list

stock = {
  "coffee": 0.5,
  "to-go coffee": 0.6,
  "unsweetened coffee": 0.5,
  "strong coffee": 0.7
} #dictionary, each key is assigned a value

price = {
  "coffee": 1,
  "to-go coffee": 1.1,
  "unsweetened coffee": 1,
  "strong coffee": 1.2
} #dictionary each key is assigned a value

total = 0
for item in menu:
    total += stock[item] * price[item] #total increases with each result from the mutlitplication of (stock)*(its corresponding) price for each item from the menu

print(total)