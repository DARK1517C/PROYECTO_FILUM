import sqlite3
from datetime import datetime
from menu import elegir_categoria

def agregar_producto(usuario_id):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    print("\n--- Agregar Producto ---")
    categoria = elegir_categoria()
    if not categoria:
        print("❌ Opción inválida.")
        return

    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datos = {"color": None, "material": None, "tamaño": None, "tipo_hilo": None,
             "tipo_accesorio": None, "tipo_herramienta": None, "marca": None, "estado": None}

    if categoria == "telas":
        datos["color"] = input("Color: ")
        datos["material"] = input("Material: ")
        datos["tamaño"] = input("Tamaño: ")
    elif categoria == "hilos":
        tipo = input("Tipo de hilo (1-Nylon, 2-Calibre 120): ")
        datos["tipo_hilo"] = "nylon" if tipo == "1" else "calibre 120"
        datos["color"] = input("Color: ")
    elif categoria == "accesorios":
        tipo = input("Tipo (1-Agujas,2-Botones,3-Cremalleras,4-Cintas,5-Elásticos,6-Encajes): ")
        tipos = {"1": "aguja","2": "botón","3": "cremallera","4": "cinta","5": "elástico","6": "encaje"}
        datos["tipo_accesorio"] = tipos.get(tipo, "otro")
        datos["color"] = input("Color (opcional): ")
        datos["tamaño"] = input("Tamaño (opcional): ")
    elif categoria == "maquinas":
        tipo = input("Tipo (1-Máquina,2-Tijeras,3-Reglas,4-Marcadores): ")
        tipos = {"1": "máquina de coser","2": "tijera","3": "regla","4": "marcador"}
        datos["tipo_herramienta"] = tipos.get(tipo, "otro")
        datos["marca"] = input("Marca (opcional): ")
        estado = input("Estado (1-Nuevo,2-Usado,3-Dañado): ")
        estados = {"1": "nuevo","2": "usado","3": "dañado"}
        datos["estado"] = estados.get(estado, "desconocido")

    cursor.execute("""INSERT INTO productos 
        (usuario_id, codigo, nombre, categoria, cantidad, fecha_agregado, color, material, tamaño, tipo_hilo, tipo_accesorio, tipo_herramienta, marca, estado)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (usuario_id, codigo, nombre, categoria, cantidad, fecha, datos["color"], datos["material"], datos["tamaño"],
         datos["tipo_hilo"], datos["tipo_accesorio"], datos["tipo_herramienta"], datos["marca"], datos["estado"])
    )
    conn.commit()
    conn.close()
    print("✅ Producto agregado correctamente.")

def ver_inventario(usuario_id):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE usuario_id=?", (usuario_id,))
    productos = cursor.fetchall()
    conn.close()
    if not productos:
        print("📦 No hay productos en el inventario.")
    else:
        for p in productos:
            print("\n Producto:")
            for i, v in zip(["ID","Usuario ID","Código","Nombre","Categoría","Cantidad","Fecha","Color","Material","Tamaño","Tipo Hilo","Tipo Accesorio","Tipo Herramienta","Marca","Estado"], p):
                print(f"{i}: {v}")
