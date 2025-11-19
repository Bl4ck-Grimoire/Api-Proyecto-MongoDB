from enum import Enum
from pydantic import BaseModel
from beanie import PydanticObjectId

class TipoRepresentante(str, Enum):
    legal = "legal"
    alterno = "alterno"

class OrganizacionExterna(BaseModel):
    id_organizacion: PydanticObjectId
    nombre_organizacion: str
    tipo_representante: TipoRepresentante
    nombre_representante: str
    certificado_participacion_url: str