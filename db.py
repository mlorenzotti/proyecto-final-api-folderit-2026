"""Base de datos simulada: guarda los datos en un archivo JSON.

Todo el acceso a los datos está en este archivo. Los endpoints de main.py solo
llaman a estas funciones, sin saber dónde ni cómo se guardan. Más adelante se
puede reemplazar este archivo por una base de datos real sin tocar main.py.
"""
import json
from pathlib import Path

import os
from dotenv import load_dotenv
from supabase import create_client

from models import LibroNuevo
load_dotenv()
supabase = create_client(
 os.getenv("SUPABASE_URL"),
 os.getenv("SUPABASE_SECRET_KEY"),
)


def listar_libros():
    """Lee la base de datos y devuelve la lista de libros."""
    res = supabase.table("libros").select("*").execute()
    return res.data

def obtener_libro(id_libro):
    res = supabase.table("libros").select("*").eq("id_libro", id_libro).execute()
    return res.data

def agregar_libro(libro):
    respuesta = supabase.table("libros").insert(libro.model_dump()).execute()
    return respuesta

def actualizar_libro(id_libro, libro):
    respuesta = supabase.table("libros").update(
    libro.model_dump()
     ).eq("id_libro", id_libro).execute()
    return respuesta

def eliminar_libro(id_libro):
    respuesta = supabase.table("libros").delete().eq("id_libro", id_libro).execute()
    return respuesta

