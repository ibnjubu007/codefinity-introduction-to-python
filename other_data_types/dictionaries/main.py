grocery_inventory = {"Milk":(113,"Dairy"),
                   "Eggs":(116,"Dairy"),
                   "Bread":(117,"Bakery"),
                   "Apples":(114,"Produce")
                   }
bread_details = grocery_inventory["Bread"]
print("Bread: Details of Bread:",bread_details)
grocery_inventory.update({"Cookies":(143,"Bakery")})
print("inventory after adding cookies:",grocery_inventory)
grocery_inventory.pop("Eggs")
print("inventory after removing eggs:",grocery_inventory)