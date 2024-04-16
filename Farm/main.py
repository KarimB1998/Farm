#creat the inventory that contains product,each product followd by id that includes the name ,type,quantity and price
inventory = {
  "001": {
    "type": "seed",
    "name": "wheat",
    "quantity": 1000,
    "price": 500
  },
  "002": {
    "type": "fertilizer",
    "name": "nitrogen",
    "quantity": 500,
    "price": 50
  },
  "003": {
    "type": "vegtable",
    "name": "tomatto",
    "quantity": 700,
    "price": 100
  },
  "004": {
    "type": "fruits",
    "name": "apple",
    "quantity": 300,
    "price": 200
  },
  "005": {
    "type": "fiber",
    "name": "sisal",
    "quantity": 1500,
    "price": 30
  },
}


#choice 1
#If the Admin chooses (1), the system should display the total quantity and value of the inventory
def quantity_value():
  quantity = 0
  value = 0
  for product_id in inventory:
    quantity = quantity + inventory[product_id]["quantity"]
    value = value + inventory[product_id]["quantity"] * inventory[product_id][
      "price"]
  print("Total quantity:", quantity)
  print("Total value: $", value)


#choice 2
#If the Admin chooses (2), the system should allow the Admin to add a new product to
#the inventory by specifying the type, name, quantity, and price.


def add_product():
  #the user input the typr,name,quantity and price
  producttype = input("Enter product type: ")
  productname = input("Enter product name: ")
  productquantity = int(input("Enter product quantity: "))
  productprice = float(input("Enter product price: "))

  #https://www.digitalocean.com/community/tutorials/python-add-to-dictionary

  inventory.update({
    "type": producttype,
    "name": productname,
    "quantity": productquantity,
    "price": productprice
  })
  print("Product added to inventory ☺")
  #gives to option for adding more product or stop adding
  print("1. dont add product to inventory")
  print("2. Add product to inventory")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    print("ok ,tahnk you ")

  elif choice == 2:
    #call the method
    add_product()
  else:
    print("Invalid choice.")


#choice4
#● If the Admin chooses (4), the system should allow the Admin to update the price of a product by specifying the product ID and the new price.


def update_price():
  #input the id and the new price bu user
  productid = input("Enter the product ID: ")
  newprice = float(input("Enter the new price: "))
  #check if the id entered by user in my inventory
  if productid in inventory:
    #gives a new price
    inventory[productid]["price"] = newprice
    print("Price updated ☺")
  else:
    print("Product not found.")
    print(inventory)


#choice5
#If the Admin chooses (5), the system should allow the Admin to update the quantity of a product by specifying the product ID and the new quantity.
def update_quantity():
  # inpt the id and the new quantity
  productid = input("Enter the product ID: ")
  newquantity = int(input("Enter the new quantity: "))
  #cgeck if the id is in the inventory
  if productid in inventory:
    # gives the new quantity
    inventory[productid]["quantity"] = newquantity
    print("quantity updated ☺")
  else:
    print("Product not found.")
    print(inventory)


#choice6
#If the Admin chooses (6), the system should allow the Admin to remove a product from the inventory by specifying the product ID
def delete_product():
  #gives the option for the id
  print("1.if 001 delete")
  print("2.if 002 delete")
  print("3.if 003 delete")
  print("4.if 004 delete")
  print("5.if 005 delete")
  choicee = int(input("Enter your choice: "))

  # choose 1
  if choicee == 1:
    id1 = "001"
    if id1 in inventory:

      del inventory[id1]
    print("001")
#choose 2
  elif choicee == 2:
    id2 = "1002"
    if id2 in inventory:

      del inventory[id2]
    print("002")
    #choose 3
  elif choicee == 3:
    id3 = "003"
    if id3 in inventory:

      del inventory[id3]
    print("003")
    #choose 4
  elif choicee == 4:
    id4 = "004"
    if id4 in inventory:
      del inventory[id4]
    print("004")
#choose 5
  elif choicee == 5:
    id5 = "005"
    if id5 in inventory:
      del inventory[id5]
    print("005")
  else:
    print("Invalid choice.")


#choice7
#If the Admin chooses (7), the system should allow the Admin to search for a product by name and display the results.
def search_product():
  #input the name you want to search for
  name = input("Enter product name: ")
  for product_id, product in inventory.items():
    if product["name"] == name:
      print("Product ID:", product_id)
      print(inventory[product_id])
      return
      print(inventory[name])


#choice8
#If the Admin chooses (8), the system should sort the products in the inventory by quantity in descending order and display the results.


#footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
#sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True)
#converted_dict = dict(sorted_footballers_by_goals)
#print(converted_dict)
# Output: {'Pele': 150, 'Ronaldo': 132, 'Messi': 125, 'Eusebio': 120, 'Cruyff': 104}
#https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
#thats my reffrence for this one (↑)(↓)
def sortquantity():
  sortedquantity = sorted(inventory.items(),
                          key=lambda x: x[1]["quantity"],
                          reverse=True)
  for item in sortedquantity:
    print("ID:", item[0])
    print("name:", item[1]['name'])
    print("type:", item[1]['type'])
    print("quantity:", item[1]['quantity'])


#choice 3
#If the Admin chooses (3), the system should display all the products in the inventory,sorted by product ID.
def sortbyid():
  sorted_inventory = sorted(inventory.items())
  for product_id, product in sorted_inventory:
    print("ID:", product_id, "Name:", product['name'], "Type:",
          product['type'], "Quantity:", product['quantity'], "Price:",
          product['price'])
  # print(inventory[productid]["quantity"])


#choice

# you have 5 attemtes ,hence bye bye system
ATTEMPTS = 5
loginattempts = 0

print("HELLO system!")
print("PLEASE LOG IN HERE :")

while loginattempts < ATTEMPTS:
  username = input("username: ")
  password = input("password: ")

  # let us know if he is user or a farmer
  if username == "farmer" and password == "":
    print("this is farmer menue :")
    while True:
      #the farmer menue
      print("Please select an option:")
      print("1. Check My Inventory")
      print("2. Search Product by Name")
      print("3. Sort Products by Quantity (descending)")
      print("4. exit")

      choice = input("Enter your choice (1-4): ")
      if choice == "1":
        print("1.Display Inventory Statistics :")
        sortbyid()
        continue

      elif choice == "2":
        print("2.Search Product by Name :")
        search_product()
        

        continue

      elif choice == "3":
        print("3. Sort Products by Quantity (descending):")
        sortquantity()
        continue
      elif choice == "4":
        print("4.Exit (BYE BYE ) :")
        break
    else:
      print("NO choice.")

    break
  elif username == "admin" and password == "admin123123":
    print("this is admin menue :")
    print("Welcome to the Admin menu!")
    while True:
      #the admin menue
      print("Please select an option:")
      print("1. Display Inventory Statistics")
      print("2. Add Product to Inventory")
      print("3. Display All Products in Inventory (sorted by product ID)")
      print("4. Update Product Price")
      print("5. Update Product Quantity")
      print("6. Remove Product from Inventory")
      print("7. Search Product by Name")
      print("8. Sort Products by Quantity (descending)")
      print("9. Exit")

      choice = input("Enter your choice (1-9): ")

      if choice == "1":
        print("1.Display Inventory Statistics :")
        quantity_value()
        continue

      elif choice == "2":
        print("2.Add Product to Inventory :")
        add_product()
        print(inventory)
        continue

      elif choice == "3":
        print("3. Display All Products in Inventory (sorted by product ID):")
        sortbyid()
        continue

      elif choice == "4":
        print("4.Update Product Price :")
        update_price()
        print(inventory)
        continue

      elif choice == "5":
        print("5. Update Product Quantity :")
        update_quantity()
        print(inventory)
        continue

      elif choice == "6":
        print("6.Remove Product from Inventory :")
        delete_product()
        print(inventory)
        continue

      elif choice == "7":
        print("7.Search Product by Name :")
        search_product()
        continue

      elif choice == "8":
        print("8.Sort Products by Quantity (descending) :")
        sortquantity()
        continue

      elif choice == "9":
        print("9.Exit (BYE BYE ) :")
        break
    else:
      print("NO choice.")

    break
  else:
    print("Incorrect Username and/or Password. Please try again.")
    loginattempts = loginattempts + 1

# checking if he loged in more than 5
if loginattempts == ATTEMPTS:
  print(
    "incorrect password and username ,exeeds 5 attempts. Please give a try again later,thank you."
  )
#else:
#print("display system")
