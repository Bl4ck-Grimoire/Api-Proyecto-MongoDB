from fastapi import HTTPException,status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.evento import EventoModel
from app.schemas.evento import EventoBase, CrearEvento, ActualizarEvento, Evento

async def crear_evento(nuevo_evento: EventoModel) -> Evento:
    evento = EventoModel(**nuevo_evento.model_dump())
    await evento.insert()
    return Evento(id=str(evento.id), **nuevo_evento.model_dump())

async def actualizar_evento(evento_id: PydanticObjectId, evento_actualizado: ActualizarEvento) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {evento_id} no es válido"
            )
    evento = await EventoModel.get(object_id)
    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el evento con ID {evento_id}"
            )
    evento_data = evento_actualizado.model_dump(exclude_unset=True)
    for key, value in evento_data.items():
        setattr(evento, key, value)
    await evento.save()
    return Evento(
        id=str(evento.id), 
        nombre=evento.nombre,
        tipo_evento=evento.tipo_evento,
        descripcion_evento=evento.descripcion_evento,
        fecha_evento=evento.fecha_evento,
        hora_inicio=evento.hora_inicio,
        hora_fin=evento.hora_fin,
        estado_evento=evento.estado_evento,
        organizado_por=evento.organizado_por,
        tipo_aval=evento.tipo_aval,
        lugares_evento=evento.lugares_evento,
        organizaciones_externas=evento.organizaciones_externas,
        usuarios_organizadores=evento.usuarios_organizadores,
        evento_aval_url=evento.evento_aval_url
        )

async def obtener_evento_por_id(evento_id: PydanticObjectId) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {evento_id} no es válido"
            )
    evento = await EventoModel.get(object_id)
    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el evento con ID {evento_id}"
            )
    return Evento(
        id=str(evento.id), 
        nombre=evento.nombre,
        tipo_evento=evento.tipo_evento,
        descripcion_evento=evento.descripcion_evento,
        fecha_evento=evento.fecha_evento,
        hora_inicio=evento.hora_inicio,
        hora_fin=evento.hora_fin,
        estado_evento=evento.estado_evento,
        organizado_por=evento.organizado_por,
        tipo_aval=evento.tipo_aval,
        lugares_evento=evento.lugares_evento,
        organizaciones_externas=evento.organizaciones_externas,
        usuarios_organizadores=evento.usuarios_organizadores,
        evento_aval_url=evento.evento_aval_url
        )

async def eliminar_evento(evento_id: PydanticObjectId) -> None:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {evento_id} no es válido"
            )
    evento = await EventoModel.get(object_id)
    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el evento con ID {evento_id}"
            )
    await evento.delete()