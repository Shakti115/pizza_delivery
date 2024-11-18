#This is a edit

import time
import sys

#Variables:
delivery_fee = 0
pizza_price = 0
crust_price = 0
mushroom_price = 0
onion_price = 0
pepperoni_price = 0
tips_price = 0

#part-1+part-2
print("Greetings! Welcome to Honey Pizzas! We are so pleased to have you here! Before you can order, you will first need to create an account.")

print("To do that, type your first name:")
first_name = input()
print("Now, type your last name:")
last_name = input()
print("Now, type a username:")
user_name = input()
print("Now, type your email:")
email_address = input()

time.sleep(1)
print("Hello" + " " + first_name + " " + last_name + "! Your account will be set up with " + "" + email_address + " as your email address. And your username is " + user_name + ".")
i = 0
while i==0:
  print("Now, type a password: (Must be 8 characters long)")
  password = input()
  if len(password) >= 8:
    while True:
      print("PLease confirm your password:")
      confirmed_password = input()
    
      if confirmed_password == password: #if this line works, only then you should able to order your pizza
        print("Passwords match! You can now proceed to ordering your Pizza.") 
        time.sleep(1)
        #Pizza delivery code
        while True:
          print("Now, do you want a Delivery(D) or a Carryout(C)? Please type D for Delivery or C for Carryout")
          response = input()
          if response == "C" or response == "c":
            break
          elif response == "D" or response == "d":
            print("We deliver to the following zip codes: 12205, 12206, 12207.")
            zip_codes = ["12205", "12206", "12207"]
            while True:
              print("Please type a zip code:")
              response = input()
              if response == zip_codes[0]:
                delivery_fee = "5"
                time.sleep(1)
                print("You have selected " + zip_codes[0] + "! Your deliver fee is $" + delivery_fee)
                break
              if response == zip_codes[1]:
                delivery_fee = "6"
                time.sleep(1)
                print("You have selected " + zip_codes[1] + "! Your deliver fee is $" + delivery_fee)
                break
              if response == zip_codes[2]:
                delivery_fee = "3"
                time.sleep(1)
                print("You have selected " + zip_codes[2] + "! Your deliver fee is $" + delivery_fee)
                break
              else:
                print("Sorry, that zip code is not available!")
            break
          else: 
            print("Sorry, that is not a valid option!")
        
        break
      elif confirmed_password != password:
        print("These passwords do not match, please try again!")
    break
  else:
    print("Your password is not 8 characters long! Please try again!")





#part 3
while True:
  print("Now please select a pizza size. We have Small(S), Medium(M), and Large(L). Select your size by typing S for Small, M for Medium and L for Large.")
  pizza_size = ["S for Small", "M for Medium", "L for Large"]
  print("Please type a letter to select your size:")
  response = input()
  #small
  if response == "S" or response == "s":
    pizza_price = "5"
    time.sleep(1)
    print("You have selected", pizza_size[0] + ", Your fee is $" + pizza_price)
    break
  #medium
  if response == "M" or response == "m":
    pizza_price = "7"
    time.sleep(1)
    print("You have selected", pizza_size[1] + ", Your fee is $" + pizza_price)
    break
  #large
  if response == "L" or response == "l":
    pizza_price = "10"
    time.sleep(1)
    print("You have selected", pizza_size[2] + ", Your fee is $" + pizza_price)
    break
  #main loop
  else:
    print("Sorry, that is not a valid option! Please try again.")

#crusts
while True:
  print("Now please select a crust. We have Deep-Dish(D), Thick-Crust(T), and Hand-Tossed(H). Select your crust by typing D for Deep-Dish, T for Thick-Crust, and H for Hand-tossed")
  crusts = ["D for Deep-Dish", "T for Thick Crust", "H for Hand-tossed"]
  print("Please type a letter to select your crust:")
  response = input()
  #Deep-dish
  if response == "D" or response == "d":
    crust_price = "1"
    time.sleep(1)
    print("You have selected", crusts[0] + ", Your fee is $" + crust_price)
    break
  #Thick-crust
  if response == "T" or response == "t":
    crust_price = "2"
    time.sleep(1)
    print("You have selected", crusts[1] + ", Your fee is $" + crust_price)
    break
  #Hand-tossed
  if response == "H" or response == "h":
    crust_price = "3"
    time.sleep(1)
    print("You have selected", crusts[2] + ", Your fee is $" + crust_price) 
    break
  #loop
  else:
    print("Sorry, that is not a valid option! Please try again.")

  


#part-4
  #toppings
print("Now would you like to add toppings? Type Y for YES and N for NO")
response = input()
#no
if response == "N" or response == "n":
  print("Okay! No toppings will be added!")
#yes
if response == "Y" or response == "y":
  toppings_price = "0.5"
  print("Wonderful! We have the following three toppings available: 1. Mushroom, 2. Pepperoni, 3. Onion. All are an extra $" + toppings_price + " each.")
  #mushrooms
  print("Would you like to add Mushroom? Type Y for YES and N for NO")
  response = input()
  #no
  if response == "N" or response == "n":
    print("Okay! No mushrooms will be added!")
  #yes
  if response == "Y" or response == "y":
    mushroom_price = toppings_price
    time.sleep(1)
    print("Okay! Mushroom will be added! Your aditional fee is $" + mushroom_price)
  #pepperoni
  print("Would you like to add Pepperoni? Type Y for YES and N for NO")
  response = input()
  #no
  if response == "N" or response == "n":
    print("Okay! No Pepperoni will be added!")
  #yes
  if response == "Y" or response == "y":
    pepperoni_price = toppings_price
    time.sleep(1)
    print("Okay! Pepperoni will be added! Your aditional fee is $" + pepperoni_price)
  #onions
  print("Would you like to add Onions? Type Y for YES and N for NO")
  response = input()
  #no
  if response == "N" or response == "n":
    print("Okay! No onions will be added!")
  #yes
  if response == "Y" or response == "y":
    onion_price = toppings_price
    time.sleep(1)
    print("Okay! Onions will be added! Your aditional fee is $" + onion_price)

#tips      
print("Would you like to add any tips? Type Y for YES and N for NO")
response = input()
#no
if response == "N" or response == "n":
  "Okay! No tips will be added!"
#yes
if response == "Y" or response == "y":
  print("How much would you like to tip?")
  tips_price = input()
  time.sleep(1)
  print("Okay! Your tips will be added! Your aditional fee is $" + tips_price)


#total
total_cost = float(delivery_fee)+float(pizza_price)+float(crust_price)+float(mushroom_price)+float(onion_price)+float(pepperoni_price)+float(tips_price)
print("Thank you for choosing all your preferances! Your total cost is being calculated...")
time.sleep(3)
print("Your total cost is $" + str(total_cost))
while True:
  print("Please pay the correct ammount below:")
  payment = input()
  if payment == str(total_cost):
    time.sleep(1)
    print("Thank you for ordering" + " " + first_name + " " + last_name + "! Your pizza will be ready in 20 minutes!")
    sys.exit()
  else:
    print("Sorry, that is not the correct ammount! Please try again.")
