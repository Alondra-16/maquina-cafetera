#  Menu in a dictionary containing drinks, their ingredients and their cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 13.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 16.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15.4,
    }
}

earnings = 0

# Ingredients available in the coffee machine, they will be subtracted as drinks are made.
inventory = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}

# Takes the ingredients needed to make a drink as an argument and subtracts them from the inventory.
def make_coffee(drink_ingredients):

    inventory["water"] -= drink_ingredients["water"]
    inventory["coffee"] -= drink_ingredients["coffee"]
    if "milk" in drink_ingredients:
        inventory["milk"] -= drink_ingredients["milk"]

    print(f"Here's your {user_order}☕. Enjoy it!\n")


# Takes 2 variables as arguments: drink_cost and client_money (both from successful_transference)
# Checks if there's enough money to give change, adds money to earnings and proceeds to make coffee
def process_money(drink_cost, client_money):
    global earnings
    change = client_money - drink_cost
    change = round(change, 2)
    earnings += drink_cost

    if change > 0:
        print(f"Here's your change: ${change}\n")
        make_coffee(MENU[user_order]["ingredients"])

    else:
        print("No change available\n")
        make_coffee(MENU[user_order]["ingredients"])


# Takes drink_cost as an argument and asks the client for money to process the money. If the client doesn't have enough money, it will print a message and exit the transaction.
def successful_transference(drink_cost):
    client_money = float(input(f"Insert ${drink_cost} to continue the transaction\n$"))
    if client_money >= drink_cost:
        process_money(drink_cost, client_money)
    else:
        print("Insufficient funds to continue 💰\n")


# Takes drink as an argument and checks if there are enough ingredients in the inventory to do the drink.
def enough_ingredients(drink):
    ingredients_per_drink = []
    available_ingredients = []      # ingredients available in the inventory to make the drink
    lacked_ingredients = []

    for item in MENU[drink]["ingredients"]:      # adds the ingredients needed for each drink to a list.
        ingredients_per_drink.append(item)


    # Conditionals to add ingredients to their respective list (checks if available or not)

    if "water" in ingredients_per_drink:
        if inventory["water"] >= MENU[drink]["ingredients"]["water"]:
            available_ingredients.append("water")
        else:
            lacked_ingredients.append("water")

    if "milk" in ingredients_per_drink:
        if inventory["milk"] >= MENU[drink]["ingredients"]["milk"]:
            available_ingredients.append("milk")
        else:
            lacked_ingredients.append("milk")

    if "coffee" in ingredients_per_drink:
        if inventory["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
            available_ingredients.append("coffee")
        else:
            lacked_ingredients.append("coffee")


    # Conditionals to check if there are enough ingredients to make the ordered drink.

    if ingredients_per_drink != available_ingredients:
        print(f"Missing {lacked_ingredients}. Please choose another drink or exit with 'off'\n")

    if ingredients_per_drink == available_ingredients:
        successful_transference(MENU[drink]["cost"])



# Main loop that keeps the coffee machine running until the user enters 'off'
on = True
while on:
    user_order = input("What coffee would you like to order? espresso☕ / latte🥛☕ / cappuccino ☕🥛\n").lower()

    if user_order == "off":
        on = False
    elif user_order == "report":
        print(f"Water: {inventory['water']}ml")
        print(f"Milk: {inventory['milk']}ml")
        print(f"Coffee: {inventory['coffee']} g")
        print(f"Earnings: ${earnings} \n")
    else:
        enough_ingredients(user_order)










