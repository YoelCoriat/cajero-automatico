from usuario import Usuario

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

def input_pin(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if numero >= 0:
                return numero
            else:
                print("Por favor ingresar un pin positivo")
        except ValueError:
            return -1

usuarios = [
    Usuario("Yoel Coriat", 2602),
    Usuario("Maryane Holt", 4954),
    Usuario("Jose De Gracia", 1819)
]
usuario_actual = Usuario("", 0000)

run = True
logged_in = False

print("--- Cajero Automático ----")
while run:
    pin = input_pin("Ingrese su pin para iniciar. Si desea salir escriba 'salir': ")
    if pin == -1:
        if input("Seguro que desea salir? (si/no): ").lower() == "si":
            run = False
            continue

        else:
            continue

    for usuario in usuarios:
        if pin == usuario.pin:
            usuario_actual = usuario
            logged_in = True
            break
    else:
        print("Pin no encontrado. Ingrese otro pin.")

    while logged_in:
        print("\n-----------------------------")
        print(f"Bienvenido/a {usuario_actual.usuario}")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir o cambiar usuario")
        opcion = input_int("Ingrese su opcion: ")

        if opcion == 1:
            print(f"\nSaldo: {usuario_actual.saldo}$")

        elif opcion == 2:
            deposito = input_float("Cuanto dinero desea depositar? ")
            usuario_actual.depositar(deposito)
            print(f"\nDepositado {deposito}$")

        elif opcion == 3:
            retiro = input_float("Cuanto dinero desea retirar? ")
            usuario_actual.retirar(retiro)
            print(f"\nRetirado {retiro}$")

        elif opcion == 4:
            logged_in = False

        else:
            print("\nOpcion invalida")
