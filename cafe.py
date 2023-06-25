#First we create a list and 2 dictionaries with items, keys and values required. 
menu = ["coffee", "milk", "croissant", "cake"]
stock = {'coffee': 50, 'milk': 20, 'croissant': 25, "cake": 12}
price = {'coffee': 2.40, 'milk': 1.65, "croissant": 0.60, "cake": 1.25}

#Set a count for our total_stock.
total_stock = 0

#for loop to iterate over our menu items and process all required calculations through values in dictionaries.
for item in menu:
    
    item_value = (stock[item] * price[item])
    print (f"{(item)}: {item_value}") #print the stock value of each item.
    total_stock += item_value #add stock value to our count. 

print (f"Total stock: {total_stock}")
