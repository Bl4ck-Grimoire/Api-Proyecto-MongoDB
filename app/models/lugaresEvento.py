from beanie import PydanticObjectId
from pydantic import BaseModel

class lugaresEvento(BaseModel):
    id_lugar: PydanticObjectId
    nombre_lugar: str