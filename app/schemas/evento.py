from datetime import date
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from app.models.evento import OrganizadoPor, TipoEvento, EstadoEvento, TipoAval
from app.models.lugaresEvento import lugaresEvento
from app.models.organizacionesExternas import OrganizacionExterna
from app.models.usuariosOrganizadores import UsuarioOrganizador


class EventoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    tipo_evento: TipoEvento
    descripcion_evento: str
    fecha_evento: date
    hora_inicio: str
    hora_fin: str
    estado_evento: EstadoEvento
    organizado_por: OrganizadoPor
    tipo_aval: TipoAval
    lugares_evento: Optional[List[lugaresEvento]] = []
    organizaciones_externas: Optional[List[OrganizacionExterna]] = []
    usuarios_organizadores: Optional[List[UsuarioOrganizador]] = []
    evento_aval_url: str

class CrearEvento(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    tipo_evento: TipoEvento
    descripcion_evento: str
    fecha_evento: date
    hora_inicio: str
    hora_fin: str
    estado_evento: EstadoEvento
    organizado_por: OrganizadoPor
    tipo_aval: TipoAval
    lugares_evento: Optional[List[lugaresEvento]] = []
    organizaciones_externas: Optional[List[OrganizacionExterna]] = []
    usuarios_organizadores: Optional[List[UsuarioOrganizador]] = []
    evento_aval_url: str

class ActualizarEvento(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: Optional[str] = None
    tipo_evento: Optional[TipoEvento] = None
    descripcion_evento: Optional[str] = None
    fecha_evento: Optional[date] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    estado_evento: Optional[EstadoEvento] = None
    organizado_por: Optional[OrganizadoPor] = None
    tipo_aval: Optional[TipoAval] = None
    lugares_evento: Optional[List[lugaresEvento]] = None
    organizaciones_externas: Optional[List[OrganizacionExterna]] = None
    usuarios_organizadores: Optional[List[UsuarioOrganizador]] = None
    evento_aval_url: Optional[str] = None

class Evento(CrearEvento):
    id: str = Field(..., description="ID único del evento")
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True
    )