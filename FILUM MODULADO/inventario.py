from crear_db import conectar
from datetime import datetime

def agregar_producto():
    conexion = conectar()
    cursor = conexion.cursor()

    nombre = input(" Nombre del producto: ")
    categoria = input(" Categoría: ")
    cantidad = int(input(" Cantidad: "))
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO productos (nombre, categoria, cantidad, fecha_agregado) VALUES (?, ?, ?, ?)",
                   (nombre, categoria, cantidad, fecha))
    conexion.commit()
    conexion.close()
    print("✅ Producto agregado con éxito.")

def ver_inventario():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("\n INVENTARIO:")
        for p in productos:
            print(f"ID: {p[0]} | {p[1]} | {p[2]} | Cantidad: {p[3]} | Fecha: {p[4]}")
    else:
        print(" No hay productos en el inventario.")

    conexion.close()
