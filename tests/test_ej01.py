import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej01_dep import saludo

def test_saludo():
    assert saludo ("oscar") == "hola,oscar."
    assert saludo("jesus") == "hola,jesus."
    assert saludo("juan") == "hola,juan."

