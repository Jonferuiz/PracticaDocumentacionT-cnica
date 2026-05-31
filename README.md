# Proyecto API - Documentación (v2.0.0)

Bienvenido a la versión `2.0.0` de nuestra API. Esta actualización introduce una nueva arquitectura orientada a objetos, enfocada en la validación estricta de datos, mayor seguridad y escalabilidad a largo plazo.

## ⚠️ ATENCIÓN: Cambios Incompatibles (Breaking Changes)

Esta versión incluye cambios estructurales mayores. El código que dependía de la versión `v1.x` **dejará de funcionar** sin antes aplicar modificaciones en la implementación.

### Resumen de Cambios Principales:
1. **Reemplazo de Funciones por Clases:** Las consultas independientes (ej. `obtener_usuario`) ahora se manejan instanciando clases controladoras como `UsuarioAPI`.
2. **Tipado y Validación Estricta:** Implementación de [Pydantic](https://docs.pydantic.dev/). Las respuestas de la API ahora retornan modelos de datos validados (`UsuarioResponse`) en lugar de diccionarios nativos (`dict`).
3. **Cambio en Esquemas de Datos:** Se han renombrado varias propiedades para mayor claridad:
   * `id` ➔ `usuario_id`
   * `nombre` ➔ `nombre_completo`
4. **Inyección de Dependencias:** Ahora se requiere pasar explícitamente la conexión o sesión de la base de datos (`db_session`) al instanciar las clases de la API.

---

## Guía de Migración Rápida

Si estás actualizando desde `v1.x`, a continuación se muestra la comparación de uso.

### ❌ Antes (v1.x - Obsoleto)
```python
# Función simple que devuelve un diccionario
from api_v1 import obtener_usuario

usuario = obtener_usuario(10)
print(usuario["nombre"])  # Imprime: Carlos
```

### ✅ Ahora (v2.0.0)
```python
from api_v2 import UsuarioAPI
from db import mi_conexion

# 1. Instanciar el controlador de la API con la sesión de DB
api = UsuarioAPI(db_session=mi_conexion)

# 2. Llamar al nuevo método que devuelve un objeto Pydantic
usuario = api.fetch_user(user_id=10)

# 3. Acceder a las propiedades usando la sintaxis de objetos
print(usuario.nombre_completo)  # Imprime: Carlos
print(usuario.usuario_id)       # Imprime: 10
```

---

## Instalación y Requisitos

Para ejecutar esta nueva versión asegúrate de tener:
- **Python:** 3.8 o superior.
- **Dependencias:** Ahora es necesario instalar `pydantic`.

Puedes instalar las nuevas dependencias ejecutando:
```bash
pip install pydantic
```

