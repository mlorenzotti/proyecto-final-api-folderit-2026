"""Modelos de datos: describen qué campos tiene cada elemento y cómo se validan."""
from pydantic import BaseModel, Field

class LibroNuevo(BaseModel):
    titulo: str = Field(min_length=1)
    descripcion: str = ""
    numero_copias: int = Field(ge=0)
    isbn: int = Field(ge=0)
    anio: int = Field(ge=0)
    activo: bool 

class LibroUpdate(BaseModel):
    titulo: str | None = None
    isbn: int | None = None
    descripcion: str | None = None
    anio: int | None = None
    numero_copias: int | None = None
    activo: bool | None = None