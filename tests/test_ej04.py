import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej04_def2 import convertir_temperatura

def test_convertir_temperatura():
    assert convertir_temperatura(100) == 37.78 
    assert convertir_temperatura(5) == -15.00