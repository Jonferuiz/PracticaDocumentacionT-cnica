# api_v2.py (Nueva Arquitectura)
from pydantic import BaseModel

# Nueva estructura de respuesta requerida
class UsuarioResponse(BaseModel):
    usuario_id: int
    nombre_completo: str
    activo: bool

class UsuarioAPI:
    def __init__(self, db_session):
        self.db = db_session

    def fetch_user(self, user_id: int) -> UsuarioResponse:
        """
        Obtiene los datos del usuario usando el nuevo motor de base de datos.
        Devuelve un objeto UsuarioResponse validado.
        """
        # Lógica simulada con la nueva arquitectura
        return UsuarioResponse(
            usuario_id=user_id,
            nombre_completo="Carlos",
            activo=True 
        )

# Uso en v2 (Rompe la compatibilidad con v1):
# api = UsuarioAPI(db_session=mi_conexion)
# usuario = api.fetch_user(user_id=10)
# print(usuario.nombre_completo) # Ya no es un diccionario, ni se llama "nombre"