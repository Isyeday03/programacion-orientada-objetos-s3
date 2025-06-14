# PROGRAMACIÓN ORIENTADA A OBJETOS - PROMEDIO SEMANAL DEL CLIMA
# Descripción: Programa que calcula el promedio semanal de temperaturas usando POO

from datetime import datetime

class RegistroClimatico:
    """
    Clase que representa un registro diario del clima
    Demuestra el concepto de ENCAPSULAMIENTO
    """
    
    def __init__(self, dia, temperatura):
        """
        Constructor de la clase RegistroClimatico
        
        Parámetros:
        dia (str): Día de la semana
        temperatura (float): Temperatura del día
        """
        self.__dia = dia  # Atributo privado (encapsulamiento)
        self.__temperatura = temperatura  # Atributo privado (encapsulamiento)
    
    # Métodos getter (acceso controlado a atributos privados)
    def get_dia(self):
        """Retorna el día del registro"""
        return self.__dia
    
    def get_temperatura(self):
        """Retorna la temperatura del registro"""
        return self.__temperatura
    
    # Métodos setter (modificación controlada de atributos privados)
    def set_temperatura(self, nueva_temperatura):
        """
        Establece una nueva temperatura con validación
        
        Parámetros:
        nueva_temperatura (float): Nueva temperatura a establecer
        """
        if isinstance(nueva_temperatura, (int, float)):
            self.__temperatura = nueva_temperatura
        else:
            raise ValueError("La temperatura debe ser un número")
    
    def __str__(self):
        """
        Método especial para representación en cadena del objeto
        """
        return f"{self.__dia}: {self.__temperatura:.1f}°C"

class SemanaClimatica:
    """
    Clase que representa una semana completa de registros climáticos
    Demuestra COMPOSICIÓN (contiene objetos RegistroClimatico)
    """
    
    DIAS_SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    def __init__(self):
        """
        Constructor que inicializa una semana vacía
        """
        self.__registros = []  # Lista privada de registros climáticos
        self.__fecha_creacion = datetime.now()
    
    def agregar_registro(self, dia, temperatura):
        """
        Agrega un nuevo registro climático a la semana
        
        Parámetros:
        dia (str): Día de la semana
        temperatura (float): Temperatura del día
        """
        if dia in self.DIAS_SEMANA:
            registro = RegistroClimatico(dia, temperatura)
            self.__registros.append(registro)
        else:
            raise ValueError(f"Día '{dia}' no válido. Use: {', '.join(self.DIAS_SEMANA)}")
    
    def ingresar_temperaturas(self):
        """
        Método interactivo para ingresar todas las temperaturas de la semana
        """
        print("Ingrese las temperaturas de cada día de la semana:")
        print("-" * 40)
        
        self.__registros.clear()  # Limpiar registros anteriores
        
        for dia in self.DIAS_SEMANA:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia} (°C): "))
                    self.agregar_registro(dia, temp)
                    break
                except ValueError as e:
                    if "could not convert" in str(e):
                        print("Error: Ingrese un número válido.")
                    else:
                        print(f"Error: {e}")
    
    def calcular_promedio(self):
        """
        Calcula el promedio de temperaturas de la semana
        
        Retorna:
        float: Promedio de temperaturas
        """
        if len(self.__registros) == 0:
            return 0
        
        suma = sum(registro.get_temperatura() for registro in self.__registros)
        return suma / len(self.__registros)
    
    def obtener_temperatura_maxima(self):
        """
        Obtiene la temperatura máxima de la semana
        
        Retorna:
        float: Temperatura máxima
        """
        if len(self.__registros) == 0:
            return None
        
        return max(registro.get_temperatura() for registro in self.__registros)
    
    def obtener_temperatura_minima(self):
        """
        Obtiene la temperatura mínima de la semana
        
        Retorna:
        float: Temperatura mínima
        """
        if len(self.__registros) == 0:
            return None
        
        return min(registro.get_temperatura() for registro in self.__registros)
    
    def obtener_registros(self):
        """
        Retorna una copia de los registros para acceso de solo lectura
        
        Retorna:
        list: Lista de registros climáticos
        """
        return self.__registros.copy()
    
    def tiene_datos_completos(self):
        """
        Verifica si la semana tiene datos completos (7 días)
        
        Retorna:
        bool: True si tiene 7 registros, False en caso contrario
        """
        return len(self.__registros) == 7

class GeneradorReportes:
    """
    Clase utilitaria para generar reportes del clima
    Demuestra el principio de RESPONSABILIDAD ÚNICA
    """
    
    @staticmethod
    def mostrar_bienvenida():
        """Muestra el mensaje de bienvenida"""
        print("=" * 50)
        print("    CALCULADORA DE PROMEDIO SEMANAL DEL CLIMA")
        print("               (Versión POO)")
        print("=" * 50)
        print("Este programa utiliza Programación Orientada a Objetos")
        print("para calcular el promedio de temperaturas semanales.\n")
    
    @staticmethod
    def generar_resumen(semana):
        """
        Genera un resumen completo de la semana climática
        
        Parámetros:
        semana (SemanaClimatica): Objeto semana con los datos
        """
        if not semana.tiene_datos_completos():
            print("Error: No hay suficientes datos para generar el resumen.")
            return
        
        print("\n" + "=" * 50)
        print("         RESUMEN SEMANAL DEL CLIMA")
        print("=" * 50)
        
        # Mostrar temperaturas diarias
        print("\nTemperaturas registradas:")
        print("-" * 25)
        for registro in semana.obtener_registros():
            print(f"{registro.get_dia():<10}: {registro.get_temperatura():>6.1f}°C")
        
        # Mostrar estadísticas
        promedio = semana.calcular_promedio()
        temp_max = semana.obtener_temperatura_maxima()
        temp_min = semana.obtener_temperatura_minima()
        
        print(f"\n{'Estadísticas:':<15}")
        print("-" * 25)
        print(f"{'Promedio:':<15} {promedio:>6.1f}°C")
        print(f"{'Máxima:':<15} {temp_max:>6.1f}°C")
        print(f"{'Mínima:':<15} {temp_min:>6.1f}°C")
        
        # Análisis adicional
        GeneradorReportes._mostrar_analisis(promedio, temp_max, temp_min)
    
    @staticmethod
    def _mostrar_analisis(promedio, temp_max, temp_min):
        """
        Muestra un análisis básico de las temperaturas
        
        Parámetros:
        promedio (float): Temperatura promedio
        temp_max (float): Temperatura máxima
        temp_min (float): Temperatura mínima
        """
        rango = temp_max - temp_min
        print(f"\n{'Análisis:':<15}")
        print("-" * 25)
        print(f"{'Rango:':<15} {rango:>6.1f}°C")
        
        if promedio < 15:
            clima = "Frío"
        elif promedio > 25:
            clima = "Cálido"
        else:
            clima = "Templado"
        
        print(f"{'Clima general:':<15} {clima}")

class AplicacionClima:
    """
    Clase principal que maneja la aplicación completa
    Demuestra COMPOSICIÓN y COORDINACIÓN de objetos
    """
    
    def __init__(self):
        """Constructor de la aplicación"""
        self.__semana = SemanaClimatica()
        self.__generador = GeneradorReportes()
    
    def ejecutar(self):
        """
        Método principal que ejecuta la aplicación
        """
        self.__generador.mostrar_bienvenida()
        
        while True:
            # Crear nueva semana para cada iteración
            self.__semana = SemanaClimatica()
            
            # Ingresar datos
            self.__semana.ingresar_temperaturas()
            
            # Generar y mostrar reporte
            self.__generador.generar_resumen(self.__semana)
            
            # Preguntar si continuar
            if not self._preguntar_continuar():
                break
        
        print("\n¡Gracias por usar la Calculadora de Clima POO!")
        print("=" * 50)
    
    def _preguntar_continuar(self):
        """
        Método privado que pregunta si continuar
        
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

# Función principal para ejecutar la aplicación
def main():
    """
    Función principal que inicia la aplicación POO
    """
    app = AplicacionClima()
    app.ejecutar()

# Punto de entrada del programa
if __name__ == "__main__":
    main()