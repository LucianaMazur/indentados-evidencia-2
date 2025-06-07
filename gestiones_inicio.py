def iniciar_sesion(usuarios):
    if not usuarios:
        print("Aún no hay usuarios registrados.")
        return None
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["email"] == email and usuario["contraseña"] == contraseña:
            print(f"🔓 Bienvenido/a {usuario['nombre']}!")
            return usuario
    print("❌ Email o contraseña incorrectos.")
    return None




