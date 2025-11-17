productos = {}

def crear_producto(id, nombre, descripcion, precio, cantidad):
    if id in productos:
        return "Error, el producto ya existe"
    productos[id] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad
    }
    return f"Producto creado {productos[id]['nombre']}"

def leer_producto(id):
    if id not in productos:
        return "Error, el producto no fue encontrado"
    return f"Producto consultado {productos[id]['nombre'], productos[id]['descripcion'], productos[id]['precio'], productos[id]['cantidad']}"

def actualizar_producto(id, nombre=None, descripcion=None, precio=None, cantidad=None):
    if id not in productos:
        return "Error, el producto no fue encontrado"

    if nombre is not None:
        productos[id]["nombre"] = nombre
    if descripcion is not None:
        productos[id]["descripcion"] = descripcion
    if precio is not None:
        productos[id]["precio"] = precio
    if cantidad is not None:
        productos[id]["cantidad"] = cantidad

    return f"Producto actualizado {productos[id]['nombre']}"

def eliminar_producto(id):
    if id not in productos:
        return "Error, el producto no fue encontrado"
    del productos[id]
    return f"Producto eliminado {id}"

if __name__ == "__main__":
    print(crear_producto(1, "Mouse", "Mouse óptico", 50.0, 10))
    print(leer_producto(1))
    print(actualizar_producto(1, precio=60.0))
    print(eliminar_producto(1))