from fastapi import APIRouter, Path, status
from typing import List
from app.crud import evento as crud
from app.schemas.evento import EventoBase, CrearEvento, ActualizarEvento, Evento

router = APIRouter()

@router.post("/", response_model=Evento, status_code=status.HTTP_201_CREATED)
async def crearEvento(evento: CrearEvento):
    return await crud.crear_evento(evento)

@router.put("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def actualizarEvento(
    evento_id: str = Path(..., description="ID del evento a actualizar"), evento: ActualizarEvento = ...):
    return await crud.actualizar_evento(evento_id, evento)

@router.get("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def obtenerEvento(evento_id: str = Path(..., description="ID del evento a obtener")):
    return await crud.obtener_evento_por_id(evento_id)

@router.get("/", response_model=List[Evento], status_code=status.HTTP_200_OK)
async def listarEventos():
    return await crud.obtener_eventos()

@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminarEvento(evento_id: str = Path(..., description="ID del evento a eliminar")):
    await crud.eliminar_evento(evento_id)
    return None