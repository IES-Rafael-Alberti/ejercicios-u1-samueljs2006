import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej11_dep  import calcular_suma

def test_calcular_suma():
    assert calcular_suma(7) == "Resultado: 28.00"
    assert calcular_suma(9) == "Resultado: 45.00"