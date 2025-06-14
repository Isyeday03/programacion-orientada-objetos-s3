# PROGRAMACIÓN TRADICIONAL - PROMEDIO SEMANAL DEL CLIMA
# Descripción: Programa que calcula el promedio semanal de temperaturas usando funciones

# Lista de días de la semana para mejor presentación
DIAS_SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

def mostrar_bienvenida():
    """
    Función que muestra el mensaje de bienvenida del programa
    """
    print("=" * 50)
    print("    CALCULADORA DE PROMEDIO SEMANAL DEL CLIMA")
    print("=" * 50)
    print("Este programa te ayudará a calcular el promedio de")
    print("temperaturas durante una semana completa.\n")

def solicitar_temperatura(dia):
    """
    Función que solicita la temperatura de un día específico
    
    Parámetros:
    dia (str): Nombre del día de la semana
    
    Retorna:
    float: Temperatura ingresada por el usuario
    """
    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura del {dia} (°C): "))
            return temperatura
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def ingresar_temperaturas():
    """
    Función que solicita las temperaturas de todos los días de la semana
    
    Retorna:
    list: Lista con las 7 temperaturas de la semana
    """
    temperaturas = []
    print("Ingrese las temperaturas de cada día de la semana:")
    print("-" * 40)
    
    for dia in DIAS_SEMANA:
        temp = solicitar_temperatura(dia)
        temperaturas.append(temp)
    
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio de temperaturas
    
    Parámetros:
    temperaturas (list): Lista de temperaturas
    
    Retorna:
    float: Promedio de las temperaturas
    """
    if len(temperaturas) == 0:
        return 0
    
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

def obtener_temperatura_maxima(temperaturas):
    """
    Función que obtiene la temperatura máxima
    
    Parámetros:
    temperaturas (list): Lista de temperaturas
    
    Retorna:
    float: Temperatura máxima
    """
    return max(temperaturas)

def obtener_temperatura_minima(temperaturas):
    """
    Función que obtiene la temperatura mínima
    
    Parámetros:
    temperaturas (list): Lista de temperaturas
    
    Retorna:
    float: Temperatura mínima
    """
    return min(temperaturas)

def mostrar_resumen(temperaturas, promedio):
    """
    Función que muestra el resumen completo de temperaturas
    
    Parámetros:
    temperaturas (list): Lista de temperaturas
    promedio (float): Promedio calculado
    """
    print("\n" + "=" * 50)
    print("         RESUMEN SEMANAL DEL CLIMA")
    print("=" * 50)
    
    print("\nTemperaturas registradas:")
    print("-" * 25)
    for i, dia in enumerate(DIAS_SEMANA):
        print(f"{dia:<10}: {temperaturas[i]:>6.1f}°C")
    
    print(f"\n{'Estadísticas:':<15}")
    print("-" * 25)
    print(f"{'Promedio:':<15} {promedio:>6.1f}°C")
    print(f"{'Máxima:':<15} {obtener_temperatura_maxima(temperaturas):>6.1f}°C")
    print(f"{'Mínima:':<15} {obtener_temperatura_minima(temperaturas):>6.1f}°C")

def preguntar_continuar():
    """
    Función que pregunta si el usuario desea continuar
    
    Retorna:
    bool: True si desea continuar, False si no
    """
    while True:
        respuesta = input("\n¿Desea calcular otra semana? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor responda 's' para sí o 'n' para no.")

def main():
    """
    Función principal que coordina la ejecución del programa
    """
    mostrar_bienvenida()
    
    while True:
        # Ingresar temperaturas de la semana
        temperaturas_semana = ingresar_temperaturas()
        
        # Calcular el promedio semanal
        promedio_semanal = calcular_promedio(temperaturas_semana)
        
        # Mostrar resultados
        mostrar_resumen(temperaturas_semana, promedio_semanal)
        
        # Preguntar si desea continuar
        if not preguntar_continuar():
            break
    
    print("\n¡Gracias por usar la Calculadora de Promedio Semanal del Clima!")
    print("=" * 50)

# Punto de entrada del programa
if __name__ == "__main__":
    main()