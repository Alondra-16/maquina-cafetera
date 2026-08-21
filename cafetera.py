#English version
#diccionario que contiene las bebidas, sus ingredientes y el costo de cada una
MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "cost": 25.0,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "cost": 45.5,
    },
    "capuchino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "cost": 40.0,
    }
}

earnings = 0

# ingredientes que tiene la cafetera, se van a ir restando a medida que se vayan haciendo las bebidas
report = {
    "agua": 400,
    "leche": 300,
    "cafe": 150,
}

# toman de argumento los ingredientes que se ocupan para hacer la bebida y los resta al reporte
def make_coffe(drink_ingredients):

    report["agua"] -= drink_ingredients["agua"]
    report["cafe"] -= drink_ingredients["cafe"]
    if "leche" in drink_ingredients:
        report["leche"] -= drink_ingredients["leche"]

    print(f"Aqui tienes tu {user_order}☕. Que lo disfrutes!\n")


# toma de argumentos 2 variables, la del costo_bebida y la del dinero_cliente ( ambas estan en transferencia_exitosa) 
# checa si hay suficiente dinero para dar el cambio, sumar la ganacia y seguir con preparar_cafe
def process_money(drink_cost, client_money):
    global earnings
    change = client_money - drink_cost
    change = round(change, 2)
    earnings += drink_cost

    if change > 0:
        print(f"Aqui esta su change: ${change}\n")
        make_coffe(MENU[user_order]["ingredientes"])

    else:
        print("No hay change\n")
        make_coffe(MENU[user_order]["ingredientes"])


# toma de argumento el costo_bebida ( está en hay_suficientes_ingredientes) y crea la variable (dinero_cliente) que le pide al cliente dinero para poder procesarlo
def successful_transference(drink_cost):
    client_money = float(input(f"Insert ${drink_cost} to continue the transaction\n$"))
    if client_money >= drink_cost:
        process_money(drink_cost, client_money)
    else:
        print("No hay suficiente dinero para continuar 💰\n")


#  toma de argumento la variable (user_order) y checa si hay suficientes ingredientes en el reporte para hacer la bebida que ordeno el cliente
def enough_ingredients(drink):
    ingredients_per_drink = []
    ingredients_in_drink = []      # ingredientes que si hay en el reporte para hacer la bebida
    lacked_ingredients = []

    for item in MENU[drink]["ingredientes"]:      # agrega los ingredientes que necesita la bebida en una lista
        ingredients_per_drink.append(item)


    # Condicionales para agregar los ingredientes a su respectiva lista (checa si hay o no hay de ese ingrediente)

    if "agua" in ingredients_per_drink:
        if report["agua"] >= MENU[drink]["ingredientes"]["agua"]:
            ingredients_in_drink.append("agua")
        else:
            lacked_ingredients.append("agua")

    if "leche" in ingredients_per_drink:
        if report["leche"] >= MENU[drink]["ingredientes"]["leche"]:
            ingredients_in_drink.append("leche")
        else:
            lacked_ingredients.append("leche")

    if "cafe" in ingredients_per_drink:
        if report["cafe"] >= MENU[drink]["ingredientes"]["cafe"]:
            ingredients_in_drink.append("cafe")
        else:
            lacked_ingredients.append("cafe")


    # Condicionales para checar si hay suficientes ingredientes para hacer la bebida que ordeno el cliente

    if ingredients_per_drink != ingredients_in_drink:
        print(f"Falta {lacked_ingredients}, Porfavor escoge otra bebida o termina el proceso:'off'\n")

    if ingredients_per_drink == ingredients_in_drink:
        successful_transference(MENU[drink]["costo"])



# loop principal que mantiene la cafetera encendida hasta que el usuario escriba 'off'
on = True
while on:
    user_order = input("Qué cafe le gustaría ordenar? expresso☕ / latte🥛☕ / capuchino ☕🥛\n").lower()

    if user_order == "off":
        on = False
    elif user_order == "report":
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']} g")
        print(f"Earnings: ${earnings} \n")
    else:
        enough_ingredients(user_order)










