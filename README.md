# Calculadora de Sumas en Python

Un script de Python sencillo pero robusto para sumar dos números. Este proyecto demuestra buenas prácticas de programación en Python, como el manejo de excepciones, la modularización del código mediante funciones y el uso de texto formateado (f-strings).

## Características

* **Manejo de Errores (`try...except`):** Si el usuario introduce texto o caracteres no válidos en lugar de números, el programa captura el error de forma segura y pide intentarlo de nuevo, evitando que la aplicación colapse.
* **Código Modular:** Utiliza la función `obtener_numero()` para evitar repetir código. Esto hace que el programa sea más limpio, fácil de leer y escalable.
* **Entrada Segura:** Usa un bucle `while True` que garantiza que el programa no avance hasta obtener un valor numérico válido.
* **Formato Moderno:** Emplea *f-strings* (disponibles desde Python 3.6+) para mostrar el resultado en consola de forma clara y directa.

## Requisitos

* Python 3.6 o una versión superior.

## Cómo ejecutar el código

1. Descarga o copia el código y guárdalo en un archivo llamado `suma.py`.
2. Abre tu terminal (Símbolo del sistema, PowerShell, bash, etc.).
3. Navega a la carpeta donde guardaste `suma.py`.
4. Ejecuta el siguiente comando:

   ```bash
   python suma.py
   ```
5. Sigue las instrucciones que aparecen en pantalla para ingresar los valores.

## Ejemplo de Uso

```text
--- Calculadora de Sumas ---
Ingresa el primer número: hola
❌ Error: Entrada inválida. Por favor, ingresa un número.
Ingresa el primer número: 10
Ingresa el segundo número: 5.5

✅ El resultado de sumar 10.0 y 5.5 es: 15.5
```