def obtener_numero(mensaje):
    """
    Pide un número al usuario y asegura que la entrada sea válida.
    Si el usuario ingresa texto, muestra un error y vuelve a preguntar.
    """
    while True:
        try:
            # Intentamos convertir la entrada a un número decimal
            valor = float(input(mensaje))
            return valor
        except ValueError:
            # Si hay un error (ej. escriben "hola"), mostramos este mensaje
            print("❌ Error: Entrada inválida. Por favor, ingresa un número.")

def main():
    """Función principal que ejecuta la lógica de la suma."""
    print("--- Calculadora de Sumas ---")
    
    # Usamos la función obtener_numero para cada valor
    numero1 = obtener_numero("Ingresa el primer número: ")
    numero2 = obtener_numero("Ingresa el segundo número: ")
    
    # Realizamos la suma
    suma = numero1 + numero2
    
    # Usamos f-strings (la 'f' antes de las comillas) para insertar variables directamente
    print(f"\n✅ El resultado de sumar {numero1} y {numero2} es: {suma}")

# Esta línea asegura que el código solo se ejecute si corres este archivo directamente
if __name__ == "__main__":
    main()