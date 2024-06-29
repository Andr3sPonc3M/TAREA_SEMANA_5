# Tarea semana 5
# Programa para calcular la temperatura media semanal de una ciudad utilizando programación orientada a objetos
# El programa solicita al usuario que ingrese las temperaturas diarias y luego calcula y muestra la temperatura media de la semana

class TemperaturaSemanal:

    # Clase que representa las temperaturas semanales de una ciudad.

    def __init__(self, ciudad):

        # Inicializa la clase con el nombre de la ciudad y una lista vacía de temperaturas.
        self.ciudad = ciudad  # Nombre de la ciudad (tipo string)
        self.temperaturas = []  # Lista para almacenar las temperaturas diarias (tipo float)

    def agregar_temperatura(self, temperatura):

        # Agrega una temperatura a la lista de temperaturas.
        self.temperaturas.append(temperatura)  # Agrega la temperatura a la lista

    def calcular_temperatura_media(self):

        # Calcula la temperatura media de la semana.

        total_temperaturas = sum(self.temperaturas)  # Suma todas las temperaturas de la lista
        numero_dias = len(self.temperaturas)  # Cuenta el número de días (longitud de la lista)
        temperatura_media = total_temperaturas / numero_dias  # Calcula la media
        return temperatura_media  # Retorna la temperatura media

def main():

    # Función principal del programa.
    # Crea una instancia de la clase TemperaturaSemanal, obtiene las temperaturas diarias, calcula la temperatura media y muestra el resultado.

    ciudad = input("Ingrese el nombre de la ciudad: ")  # Solicita al usuario el nombre de la ciudad
    temperatura_semanal = TemperaturaSemanal(ciudad)  # Crea una instancia de TemperaturaSemanal con el nombre de la ciudad

    for dia in range(1, 8):
        # Solicita al usuario que ingrese la temperatura para cada día de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))  # Convierte la entrada a float
        temperatura_semanal.agregar_temperatura(temperatura)  # Agrega la temperatura a la instancia

    # Calcula la temperatura media de la semana
    temperatura_media = temperatura_semanal.calcular_temperatura_media()
    # Muestra la temperatura media
    print(f"La temperatura media de la semana en {ciudad} es: {temperatura_media:.2f}°C")

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se está ejecutando directamente

# Fin del programa