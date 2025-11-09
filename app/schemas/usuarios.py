from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from beanie import PydanticObjectId
from app.models.usuarios import RolUsuario

class UsuarioBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    apellido: str
    correo: str
    rol: RolUsuario
    id_facultad: Optional[PydanticObjectId] = None
    id_unidad_academica: Optional[PydanticObjectId] = None
    id_programa_academico: Optional[PydanticObjectId] = None

class CrearUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    apellido: str
    correo: str
    rol: RolUsuario
    id_facultad: Optional[PydanticObjectId] = None
    id_unidad_academica: Optional[PydanticObjectId] = None
    id_programa_academico: Optional[PydanticObjectId] = None

class ActualizarUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    rol: Optional[RolUsuario] = None
    id_facultad: Optional[PydanticObjectId] = None
    id_unidad_academica: Optional[PydanticObjectId] = None
    id_programa_academico: Optional[PydanticObjectId] = None

class Usuario(CrearUsuario):
    id: str = Field(..., description="ID único del usuario")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True
    )