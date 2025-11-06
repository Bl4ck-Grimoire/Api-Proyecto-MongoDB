from pydantic import BaseModel
from beanie import PydanticObjectId

class OrganizacionExterna(BaseModel):
    id_organizacion: PydanticObjectId
    nombre_organizacion:str
    asiste_representante_legal: str
    nombre_representante_legal: str
    nombre_representante_alterno: str