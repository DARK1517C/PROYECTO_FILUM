from crear_db import crear_bd
from usuarios import registrar_usuario, iniciar_sesion, modificar_contraseña, eliminar_usuario
from productos import agregar_producto, ver_inventario
from menu import mostrar_menu

crear_bd()

print("\nBienvenido al Sistema FILUM")
print("1. Registrarse")
print("2. Iniciar sesión")
opcion = input("Seleccione una opción (1-2): ")

usuario, usuario_id = None, None
if opcion == "1":
    usuario, usuario_id = registrar_usuario()
elif opcion == "2":
    usuario, usuario_id = iniciar_sesion()
else:
    print("❌ Opción no válida.")
    exit()

if usuario:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ")
        if opcion == "1":
            agregar_producto(usuario_id)
        elif opcion == "2":
            ver_inventario(usuario_id)
        elif opcion == "7":
            modificar_contraseña(usuario_id)
        elif opcion == "8":
            confirm = input("¿Está seguro que desea eliminar su usuario? (s/n): ")
            if confirm.lower() == "s":
                eliminar_usuario(usuario_id, usuario)
                break
        elif opcion == "9":
            print("No es un adiós, es un hasta luego")
            break
