class Usuario:
    def __init__(self, usuario, pin):
        self.usuario = usuario
        self.pin = pin
        self.saldo = 0
        self.movimientos = []

    def depositar(self, valor):
        self.saldo += valor
        self.movimientos.append(valor)

    def retirar(self, valor):
        self.saldo -= valor
        self.movimientos.append(-valor)