from fastapi import HTTPException,status
from beanie import PydanticObjectId
from app.models.usuarios import UsuarioModel
from app.schemas.usuarios import UsuarioBase, CrearUsuario, ActualizarUsuario, Usuario

async def crear_usuario(nuevo_usuario: CrearUsuario) -> Usuario:
    usuario = UsuarioModel(**nuevo_usuario.model_dump())
    await usuario.insert()
    return Usuario(
        id=str(usuario.id),
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        correo=usuario.correo,
        rol=usuario.rol,
        id_facultad=str(usuario.id_facultad) if usuario.id_facultad else None,
        id_unidad_academica=str(usuario.id_unidad_academica) if usuario.id_unidad_academica else None,
        id_programa_academico=str(usuario.id_programa_academico) if usuario.id_programa_academico else None
    )

async def actualizar_usuario(usuario_id: PydanticObjectId, usuario_actualizado: ActualizarUsuario) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {usuario_id} no es válido"
            )
    usuario = await UsuarioModel.get(object_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el usuario con ID {usuario_id}"
            )
    usuario_data = usuario_actualizado.model_dump(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(usuario, key, value)
    await usuario.save()
    return Usuario(
        id=str(usuario.id), 
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        correo=usuario.correo,
        rol=usuario.rol,
        id_facultad=str(usuario.id_facultad) if usuario.id_facultad else None,
        id_unidad_academica=str(usuario.id_unidad_academica) if usuario.id_unidad_academica else None,
        id_programa_academico=str(usuario.id_programa_academico) if usuario.id_programa_academico else None
        )

async def obtener_usuario_por_id(usuario_id: PydanticObjectId) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {usuario_id} no es válido"
            )
    usuario = await UsuarioModel.get(object_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el usuario con ID {usuario_id}"
            )
    return Usuario(
        id=str(usuario.id), 
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        correo=usuario.correo,
        rol=usuario.rol,
        id_facultad=str(usuario.id_facultad) if usuario.id_facultad else None,
        id_unidad_academica=str(usuario.id_unidad_academica) if usuario.id_unidad_academica else None,
        id_programa_academico=str(usuario.id_programa_academico) if usuario.id_programa_academico else None
        )

async def obtener_usuarios() -> list[Usuario]:
    usuarios = await UsuarioModel.find_all().to_list()
    return [
        Usuario(
            id=str(usuario.id), 
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            correo=usuario.correo,
            rol=usuario.rol,
            id_facultad=str(usuario.id_facultad) if usuario.id_facultad else None,
            id_unidad_academica=str(usuario.id_unidad_academica) if usuario.id_unidad_academica else None,
            id_programa_academico=str(usuario.id_programa_academico) if usuario.id_programa_academico else None
            ) 
        for usuario in usuarios
        ]

async def eliminar_usuario(usuario_id: PydanticObjectId) -> None:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"El ID {usuario_id} no es válido"
            )
    usuario = await UsuarioModel.get(object_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se encontró el usuario con ID {usuario_id}"
            )
    await usuario.delete()