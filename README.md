## ⚠️ CAMBIOS IMPORTANTES (BREAKING CHANGES)
Esta versión introduce una reestructuración completa de la API. El código de la versión `v1.x` **no será compatible** con esta actualización sin modificaciones previas.

### ¿Qué cambió?
* **Migración a Clases:** Las funciones independientes como `obtener_usuario()` han sido reemplazadas por la clase `UsuarioAPI`.
* **Modelos Estrictos:** Las respuestas ya no devuelven diccionarios (`dict`), sino modelos validados por Pydantic (`UsuarioResponse`).
* **Nombres de Variables:** Las claves de respuesta han cambiado (ej. `id` ahora es `usuario_id`, `nombre` ahora es `nombre_completo`).
* **Dependencias:** Ahora es obligatorio instanciar la API pasándole una sesión de base de datos (`db_session`).

### Nuevas Características (Features)
* Integración con validación de datos automática usando Pydantic.
* Arquitectura orientada a objetos más escalable.

### Guía de Migración
Para actualizar desde `v1.x`, por favor revisa nuestra [Guía de Migración a v2.0.0](link-a-tu-wiki-o-doc).