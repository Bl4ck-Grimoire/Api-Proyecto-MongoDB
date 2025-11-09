from fastapi import APIRouter, Query, Path, status
from typing import List, Optional
from app.crud import evento as crud
from app.schemas.evento import EventoBase, CrearEvento, ActualizarEvento, Evento

router = APIRouter()

@router.post("/", response_model=Evento, status_code=status.HTTP_201_CREATED)
async def crearEvento(evento: CrearEvento):
    return await crud.crear_evento(evento)

@router.get("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def obtenerEvento(evento_id: str = Path(..., description="ID del evento a obtener")):
    return await crud.obtener_evento_por_id(evento_id)