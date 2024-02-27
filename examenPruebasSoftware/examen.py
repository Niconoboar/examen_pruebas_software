class CuentaBancaria:
    def __init__(self, persona, saldo=0):
        self.persona = persona
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def realizar_deposito(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}")

    def realizar_retiro(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficientes fondos en la cuenta.")
        self.saldo -= cantidad
        print(f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}")


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class CajeroAutomático:
    def __init__(self):
        pass

    def operar(self, cuenta, accion, cantidad=None):
        if accion == 'consultar':
            print(f"Saldo actual: {cuenta.consultar_saldo()}")
            return cuenta.consultar_saldo()
        elif accion == 'depositar':
            cuenta.realizar_deposito(cantidad)
            return cuenta.consultar_saldo()
        elif accion == 'retirar':
            cuenta.realizar_retiro(cantidad)
            return cuenta.consultar_saldo()


if __name__ == "__main__":
    nombre_persona = input("Ingrese su nombre: ")
    persona = Persona(nombre_persona)
    cuenta = CuentaBancaria(persona)

    cajero = CajeroAutomático()

    while True:
        print("\nOpciones:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar retiro")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            cajero.operar(cuenta, 'consultar')
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cajero.operar(cuenta, 'depositar', cantidad)
        elif opcion == '3':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cajero.operar(cuenta, 'retirar', cantidad)
        elif opcion == '4':
            print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
