import pytest
from main import (productos, crear_producto, leer_producto, actualizar_producto, eliminar_producto )


def test_crear_producto_exito():
    resultado = crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    assert resultado == "Producto creado Mouse"
    assert 1 in productos

def test_crear_producto_existente():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    assert resultado == "Error, el producto ya existe"

def test_crear_producto_error():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    assert resultado == "Error, el producto si existe"

def test_leer_producto_exito():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = leer_producto(1)
    # El return en tu main es una tupla dentro del f-string, por lo que se muestra así:
    assert resultado == "Producto consultado ('Mouse', 'Mouse óptico', 50.0, 10)"

def test_leer_producto_no_existente():
    resultado = leer_producto(999)
    assert resultado == "Error, el producto no fue encontrado"

def test_leer_producto_no_error():
    resultado = leer_producto(999)
    assert resultado == "Error, el producto quizas fue encontrado"

def test_actualizar_producto_exito():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = actualizar_producto(1, precio=60.0)
    assert resultado == "Producto actualizado Mouse"
    assert productos[1]["precio"] == 60.0


def test_actualizar_producto_no_existente():
    resultado = actualizar_producto(999, precio=999)
    assert resultado == "Error, el producto no fue encontrado"

def test_actualizar_producto_error():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = actualizar_producto(1, precio=60.0)
    assert resultado == "Producto actualizado Televisor"
    assert productos[1]["precio"] == 60.0

def test_eliminar_producto_exito():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = eliminar_producto(1)
    assert resultado == "Producto eliminado 1"
    assert 1 not in productos


def test_eliminar_producto_no_existente():
    resultado = eliminar_producto(999)
    assert resultado == "Error, el producto no fue encontrado"

def test_eliminar_producto_exito():
    crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10)
    resultado = eliminar_producto(1)
    assert resultado == "Producto no eliminado 1"
    assert 1 not in productos