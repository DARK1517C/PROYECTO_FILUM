def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL FILUM ---")
    print("1. Agregar producto")
    print("2. Ver inventario completo")
    print("3. Ver productos por categoría")
    print("4. Buscar producto por código")
    print("5. Actualizar cantidad de un producto")
    print("6. Eliminar producto")
    print("7. Modificar mi contraseña")
    print("8. Eliminar mi usuario")
    print("9. Salir")

def elegir_categoria():
    print("\nSeleccione la categoría:")
    print("1. Telas")
    print("2. Hilos")
    print("3. Accesorios")
    print("4. Máquinas y herramientas")
    categorias = {
        "1": "telas",
        "2": "hilos",
        "3": "accesorios",
        "4": "maquinas"
    }
    opcion = input("Ingrese el número de la categoría: ")
    return categorias.get(opcion)
