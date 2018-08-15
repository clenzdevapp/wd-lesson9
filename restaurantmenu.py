# coding=utf8
menu = {}
while True:
    dish = raw_input("Enter a dish: ").lower()
    priceDish = raw_input("Enter the price of the dish: ")
    menu[dish] = priceDish
    decision = raw_input("Do you want enter more dishes? Yes / No ")
    if decision.lower() == "yes":
        print("---")
    elif decision.lower() == "no":
        break
    else:
        break

print("Erstellung der Menüdatei")
restaurant_menu = open("restaurant_menu.txt", "w+")
restaurant_menu.write("---Tagesmenü---\n\n")
for dishes in menu:
    restaurant_menu.write(dishes.capitalize() + " | Preis: " + menu[dishes] + " € \n")

restaurant_menu.close()