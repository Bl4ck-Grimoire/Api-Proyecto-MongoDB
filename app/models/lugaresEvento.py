from pydantic import BaseModel
from beanie import PydanticObjectId

class lugaresEvento(BaseModel):
    id_lugar: PydanticObjectId
    nombre_lugar: str