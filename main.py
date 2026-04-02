def input_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            if numero >= 0:
                return numero
            else:
                print("Por favor ingresar un numero positivo")
        except ValueError:
            print("Por favor ingresar un numero valido")

def input_int(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if numero >= 0:
                return numero
            else:
                print("Por favor ingresar un numero positivo")
        except ValueError:
            print("Por favor ingresar un numero valido")

saldo = 0
opcion = 0
print("--- Cajero Automático ----")

run = True
while run:
    print("\n-----------------------------")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input_int("Ingrese su opcion: ")

    match opcion:
        case 1:
            print(f"\nSaldo: {saldo}$")

        case 2:
            deposito = input_float(f"Cuanto dinero desea depositar? ")
            saldo += deposito
            print(f"\nDepositado {deposito}$")

        case 3:
            retiro = input_float(f"Cuanto dinero desea retirar? ")
            saldo -= retiro
            print(f"\nRetirado {retiro}$")

        case 4:
            run = False

        case _:
            print("\nOpcion invalida")
