import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej05_dep2  import calcular_precio

def test_calcular_precio():
    assert calcular_precio(58) == "El precio final del artículo con IVA (21.00) es 70.18"

    