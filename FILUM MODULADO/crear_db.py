import sqlite3

def crear_bd():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Tabla usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')

    # Tabla productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            codigo TEXT UNIQUE,
            nombre TEXT,
            categoria TEXT,
            cantidad INTEGER,
            fecha_agregado TEXT,
            color TEXT,
            material TEXT,
            tamaño TEXT,
            tipo_hilo TEXT,
            tipo_accesorio TEXT,
            tipo_herramienta TEXT,
            marca TEXT,
            estado TEXT,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_bd()
    print("✅ Base de datos y tablas creadas correctamente.")
