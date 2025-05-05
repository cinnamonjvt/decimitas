# Definimos las credenciales correctas
usuario_correcto = "cinamon"
contrasena_correcta = "roll2007"

# Solicitamos credenciales al usuario
usuario_ingresado = input("Ingrese su nombre de usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

# Verificamos las credenciales
if usuario_ingresado == usuario_correcto and contrasena_ingresada == contrasena_correcta:
    print(f"¡Bienvenido/a {usuario_ingresado}! Acceso concedido.")
elif usuario_ingresado == usuario_correcto:
    # El usuario es correcto pero la contraseña no
    print("Contraseña incorrecta.")
    print(f"Pista: la contraseña comienza con '{contrasena_correcta[0]}'")
else:
    print("Usuario no registrado. Por favor, verifica tus credenciales.")