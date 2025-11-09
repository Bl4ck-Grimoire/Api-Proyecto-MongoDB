from fastapi import APIRouter, Path, status
from typing import List
from app.crud import usuarios as crud
from app.schemas.usuarios import UsuarioBase, CrearUsuario, ActualizarUsuario, Usuario

router = APIRouter()

@router.post("/", summary="Crear Usuario", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: CrearUsuario):
    return await crud.crear_usuario(usuario)

@router.put("/{usuario_id}", summary="Actualizar Usuario", response_model=Usuario, status_code=status.HTTP_200_OK)
async def actualizar_usuario(
    usuario_id: str = Path(..., description="ID del usuario a actualizar"), usuario: ActualizarUsuario = ...):
    return await crud.actualizar_usuario(usuario_id, usuario)

@router.get("/{usuario_id}", summary="Obtener Usuario", response_model=Usuario, status_code=status.HTTP_200_OK)
async def obtener_usuario(usuario_id: str = Path(..., description="ID del usuario a obtener")):
    return await crud.obtener_usuario_por_id(usuario_id)

@router.get("/", summary="Obetener todos los Usuarios", response_model=List[Usuario], status_code=status.HTTP_200_OK)
async def listar_usuarios():
    return await crud.obtener_usuarios()

@router.delete("/{usuario_id}", summary="Eliminar Usuario", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(usuario_id: str = Path(..., description="ID del usuario a eliminar")):
    await crud.eliminar_usuario(usuario_id)
    return None