# diccionario que contiene las bebidas, sus ingredientes y el costo de cada una
MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 25.0,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 45.5,
    },
    "capuchino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 40.0,
    }
}

ganancias = 0

# ingredientes que tiene la cafetera, se van a ir restando a medida que se vayan haciendo las bebidas
reporte = {
    "agua": 400,
    "leche": 300,
    "cafe": 150,
}

# toman de argumento los ingredientes que se ocupan para hacer la bebida y los resta al reporte
def preparar_cafe(ing_bebida):

    reporte["agua"] -= ing_bebida["agua"]
    reporte["cafe"] -= ing_bebida["cafe"]
    if "leche" in ing_bebida:
        reporte["leche"] -= ing_bebida["leche"]

    print(f"Aqui tienes tu {orden}☕. Que lo disfrutes!\n")


# toma de argumentos 2 variables, la del costo_bebida y la del dinero_cliente ( ambas estan en transferencia_exitosa) 
# checa si hay suficiente dinero para dar el cambio, sumar la ganacia y seguir con preparar_cafe
def procesar_dinero(costo_bebida,dinero_cliente):
    global ganancias
    cambio = dinero_cliente - costo_bebida
    cambio = round(cambio, 2)
    ganancias += costo_bebida

    if cambio > 0:
        print(f"Aqui esta su cambio: ${cambio}\n")
        preparar_cafe(MENU[orden]["ingredientes"])

    else:
        print("No hay cambio\n")
        preparar_cafe(MENU[orden]["ingredientes"])


# toma de argumento el costo_bebida ( está en hay_suficientes_ingredientes) y crea la variable (dinero_cliente) que le pide al cliente dinero para poder procesarlo
def transferencia_exitosa(costo_bebida):
    dinero_cliente = float(input(f"Inserte ${costo_bebida} para continuar al transacción\n$"))
    if dinero_cliente >= costo_bebida:
        procesar_dinero(costo_bebida, dinero_cliente)
    else:
        print("No hay suficiente dinero para continuar 💰\n")


#  toma de argumento la variable (orden) y checa si hay suficientes ingredientes en el reporte para hacer la bebida que ordeno el cliente
def hay_suficientes_ingredientes(bebida):
    ingredientes_bebida = []     
    ingrediente_que_hay = []      # ingredientes que si hay en el reporte para hacer la bebida
    ingrediente_que_faltan = []

    for item in MENU[bebida]["ingredientes"]:      # agrega los ingredientes que necesita la bebida en una lista
        ingredientes_bebida.append(item)


    # Condicionales para agregar los ingredientes a su respectiva lista (checa si hay o no hay de ese ingrediente)

    if "agua" in ingredientes_bebida:
        if reporte["agua"] >= MENU[bebida]["ingredientes"]["agua"]:
            ingrediente_que_hay.append("agua")
        else:
            ingrediente_que_faltan.append("agua")

    if "leche" in ingredientes_bebida:
        if reporte["leche"] >= MENU[bebida]["ingredientes"]["leche"]:
            ingrediente_que_hay.append("leche")
        else:
            ingrediente_que_faltan.append("leche")

    if "cafe" in ingredientes_bebida:
        if reporte["cafe"] >= MENU[bebida]["ingredientes"]["cafe"]:
            ingrediente_que_hay.append("cafe")
        else:
            ingrediente_que_faltan.append("cafe")


    # Condicionales para checar si hay suficientes ingredientes para hacer la bebida que ordeno el cliente

    if ingredientes_bebida != ingrediente_que_hay:
        print(f"Falta {ingrediente_que_faltan}, Porfavor escoge otra bebida o termina el proceso:'off'\n")

    if ingredientes_bebida == ingrediente_que_hay:
        transferencia_exitosa(MENU[bebida]["costo"])



# loop principal que mantiene la cafetera encendida hasta que el usuario escriba 'off'
on = True
while on:
    orden = input("Qué cafe le gustaría ordenar? expresso☕ / latte🥛☕ / capuchino ☕🥛\n").lower()

    if orden == "off":
        on = False
    elif orden == "reporte":
        print(f"Agua: {reporte['agua']}ml")
        print(f"Leche: {reporte['leche']}ml")
        print(f"Café: {reporte['cafe']} g")
        print(f"Ganancias: ${ganancias} \n")
    else:
        hay_suficientes_ingredientes(orden)










