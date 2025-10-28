import sqlite3

def registrar_usuario():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    print("\n--- REGISTRAR USUARIO ---")
    usuario = input("Elija un nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")
    try:
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
        conn.commit()
        print("✅ Usuario registrado con éxito.")
        return usuario, cursor.lastrowid
    except sqlite3.IntegrityError:
        print("❌ Ese nombre de usuario ya existe.")
        return None, None
    finally:
        conn.close()

def iniciar_sesion():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    print("\n--- INICIAR SESIÓN ---")
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña))
        resultado = cursor.fetchone()
        if resultado:
            print(f"✅ Bienvenido/a, {usuario}!")
            conn.close()
            return usuario, resultado[0]
        else:
            intentos -= 1
            print(f" Datos incorrectos. Intentos restantes: {intentos}")
    conn.close()
    print(" Demasiados intentos.")
    return None, None

def modificar_contraseña(usuario_id):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    nueva_contraseña = input("Ingrese su nueva contraseña: ")
    cursor.execute("UPDATE usuarios SET contraseña=? WHERE id=?", (nueva_contraseña, usuario_id))
    conn.commit()
    conn.close()
    print(" Contraseña modificada con éxito.")

def eliminar_usuario(usuario_id, usuario_nombre):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE usuario_id=?", (usuario_id,))
    cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
    conn.commit()
    conn.close()
    print(f" Usuario '{usuario_nombre}' y su inventario fueron eliminados.")
