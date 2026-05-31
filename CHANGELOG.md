changelog_content = """# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y este proyecto se adhiere a [Versión Semántica](https://semver.org/lang/es/).

## [1.0.0] - 2026-05-21

### Añadido
- Lanzamiento inicial del programa interactivo de suma de dos números en Python.
- Entrada dinámica de datos utilizando la función `input()`.
- Soporte para operaciones con números enteros y decimales mediante la conversión a `float()`.
- Salida formateada en consola para mostrar de forma clara los operandos y el resultado obtenido.
"""

with open("CHANGELOG.md", "w", encoding="utf-8") as f:
    f.write(changelog_content)

print("Archivo CHANGELOG.md generado exitosamente.")

# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Versionamiento Semántico](https://semver.org/lang/es/).

## [1.1.0] - 2026-05-30
### Añadido (Added)
- **Manejo de Errores:** Se implementó un bloque `try...except ValueError` para prevenir caídas del programa si el usuario ingresa caracteres no válidos.
- **Validación Continua:** Se agregó un bucle `while True` que solicita la entrada de datos hasta que el usuario proporcione un valor numérico válido.
- **Modularidad:** Se dividió el código en funciones reutilizables, agregando `obtener_numero()` y una función principal `main()`.

### Cambiado (Changed)
- **Formato de Cadenas:** El formato de salida en consola fue actualizado para utilizar *f-strings*, mejorando la legibilidad y modernizando el código.


## [2.0.0] - 2026-05-30
### ⚠️ Añadido (Cambios Incompatibles / Breaking Changes)
- **Inyección de Dependencias:** Ahora es obligatorio inyectar explícitamente la sesión de base de datos (`db_session`) al instanciar `UsuarioAPI`.
- **Pydantic:** Se añadieron modelos de validación estricta de datos (`UsuarioResponse`).

### Cambiado (Changed)
- **Migración a POO:** Se reemplazó la función independiente `obtener_usuario()` por la arquitectura basada en clases (`UsuarioAPI`).
- **Estructura de Retorno:** Los métodos de la API ahora devuelven objetos validados en lugar de diccionarios básicos (`dict`).
- **Renombrado de Variables:** Las propiedades de respuesta fueron modificadas (`id` pasó a ser `usuario_id`, y `nombre` pasó a ser `nombre_completo`).

