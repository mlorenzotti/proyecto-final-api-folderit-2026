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


def agregar_libro(libro):
    respuesta = supabase.table("libros").insert(libro.model_dump()).execute()
    return respuesta

"""def buscar_item(item_id):
   
    for item in cargar_items():
        if item["id"] == item_id:
            return item
    return None


def agregar_item(datos):
   
    items = cargar_items()
    nuevo_id = max((i["id"] for i in items), default=0) + 1
    item = {"id": nuevo_id, **datos}
    items.append(item)
    guardar_items(items)
    return item"""

