from fastapi import HTTPException,status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.evento import EventoModel
from app.schemas.evento import EventoBase, CrearEvento, ActualizarEvento, Evento

async def crear_evento(nuevo_evento: EventoModel) -> Evento:
    evento = EventoModel(**nuevo_evento.model_dump())
    await evento.insert()
    return Evento(id=str(evento.id), **nuevo_evento.model_dump())