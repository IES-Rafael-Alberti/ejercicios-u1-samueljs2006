import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prueba1 import numero

def test_mayor():
    assert numero(9, 4) == 9

def test_igual():
    assert numero(2, 2) == 0

def test_otro_numero():
    assert numero(4, 8) == 8