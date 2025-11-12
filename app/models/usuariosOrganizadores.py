from pydantic import BaseModel
from beanie import PydanticObjectId
from enum import Enum

class TipoOrganizador(str, Enum):
    principal = "principal"
    secundario = "secundario"

class UsuarioOrganizador(BaseModel):
    id_usuario_organizador: PydanticObjectId
    tipo_organizador: TipoOrganizador
    nombre_usuario_organizador: str