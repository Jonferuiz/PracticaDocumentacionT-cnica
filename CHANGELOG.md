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