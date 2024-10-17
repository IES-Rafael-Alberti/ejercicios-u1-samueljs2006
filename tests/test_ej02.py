import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej02_dep import calcular_importe_total

def test_calcular_importe_total():
    assert calcular_importe_total(5, 2) == 10
    assert calcular_importe_total(4, 2) == 8
    assert calcular_importe_total(7, 2) == 14
    