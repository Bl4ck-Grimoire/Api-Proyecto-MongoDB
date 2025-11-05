from fastapi import HTTPException,status
from beanie import PydanticObjectId
from typing import List, Optional

async def crear_evento(evento_model, EventoModel):
    evento = EventoModel(**evento_model.dict())
    await evento.insert()
    return evento