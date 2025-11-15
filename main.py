# main.py básico para agregar, eliminar, modificar y consultar

data_store = {}

def agregar(clave, valor):
    data_store[clave] = valor
    return f"Agregado: {clave} -> {valor}"

def eliminar(clave):
    if clave in data_store:
        del data_store[clave]
        return f"Eliminado: {clave}"
    return "Clave no encontrada"

def modificar(clave, nuevo_valor):
    if clave in data_store:
        data_store[clave] = nuevo_valor
        return f"Modificado: {clave} -> {nuevo_valor}"
    return "Clave no encontrada"

def consultar(clave):
    if clave in data_store:
        return f"Consultado: {clave} -> {data_store[clave]}"
    return "Clave no encontrada"

if __name__ == "__main__":
    print(agregar('ejemplo', 123))
    print(consultar('ejemplo'))
    print(modificar('ejemplo', 456))
    print(eliminar('ejemplo'))
