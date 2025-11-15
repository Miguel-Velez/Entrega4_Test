import pytest
from main import agregar, eliminar, modificar, consultar


def test_agregar():
    # Se agrega una clave y se verifica el retorno
    resultado = agregar('a', 1)
    assert resultado == 'Agregado: a -> 1'

def test_consultar_existente():
    agregar('b', 2)
    resultado = consultar('b')
    assert resultado == 'Consultado: b -> 2'

def test_consultar_no_existente():
    resultado = consultar('noexiste')
    assert resultado == 'Clave no encontrada'

def test_modificar_existente():
    agregar('c', 3)
    resultado = modificar('c', 33)
    assert resultado == 'Modificado: c -> 33'
    assert consultar('c') == 'Consultado: c -> 33'

def test_modificar_no_existente():
    resultado = modificar('noexiste', 99)
    assert resultado == 'Clave no encontrada'

def test_eliminar_existente():
    agregar('d', 4)
    resultado = eliminar('d')
    assert resultado == 'Eliminado: d'
    assert consultar('d') == 'Clave no encontrada'

def test_eliminar_no_existente():
    resultado = eliminar('noexiste')
    assert resultado == 'Clave no encontrada'
