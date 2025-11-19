from beanie import Document, PydanticObjectId
from typing import Optional
from enum import Enum

class RolUsuario(str, Enum):
    estudiante = "estudiante"
    docente = "docente"
    seceretrio_academico = "secretario academico"

class UsuarioModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    apellido: str
    correo: str
    rol: RolUsuario
    id_facultad: Optional[PydanticObjectId] = None
    id_unidad_academica: Optional[PydanticObjectId] = None
    id_programa_academico: Optional[PydanticObjectId] = None

    class Settings:
        name = "usuarios"