from pydantic import BaseModel
from beanie import PydanticObjectId

class UsuarioOrganizador(BaseModel):
    id_usuario_organizador: PydanticObjectId
    nombre_usuario_organizador:str