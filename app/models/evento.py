from app.models.lugaresEvento import lugaresEvento
from app.models.organizacionesExternas import OrganizacionExterna
from app.models.usuariosOrganizadores import UsuarioOrganizador
from beanie import Document, PydanticObjectId
from typing import Optional, List
from datetime import date

class EventoModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    tipo_evento: str
    descripcion_evento: str
    fecha_evento: date
    hora_inicio: str
    hora_fin: str
    estado_evento: str
    organizado_por: str
    tipo_aval: str
    lugares_evento: Optional[List[lugaresEvento]] = []
    organizaciones_externas: Optional[List[OrganizacionExterna]] = []
    usuarios_organizadores: Optional[List[UsuarioOrganizador]] = []
    evento_aval_url: str

    class Settings:
        name = "eventos"