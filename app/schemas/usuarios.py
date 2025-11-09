from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import date

class UsuarioBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    apellido: str
    correo: str
    rol: str
    id_facultad: Optional[str] = None
    id_unidad_academica: Optional[str] = None
    id_programa_academico: Optional[str] = None

class CrearUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    apellido: str
    correo: str
    rol: str
    id_facultad: Optional[str] = None
    id_unidad_academica: Optional[str] = None
    id_programa_academico: Optional[str] = None

class ActualizarUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[str] = None
    rol: Optional[str] = None
    id_facultad: Optional[str] = None
    id_unidad_academica: Optional[str] = None
    id_programa_academico: Optional[str] = None

class Usuario(CrearUsuario):
    id: str = Field(..., description="ID único del usuario")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True
    )