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
    id_facultad: Optional[str] = None
    id_unidad_academica: Optional[str] = None
    id_programa_academico: Optional[str] = None

    class Settings:
        name = "usuarios"