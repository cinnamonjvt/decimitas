duracion = float(input("Ingrese la duración de la canción en minutos: "))
genero = input("Ingrese el género de la canción: ").lower()
anio = int(input("Ingrese el año de lanzamiento: "))
duracion_adecuada = 2.5 <= duracion <= 4.5
genero_adecuado = genero in ["kpop", "jazz", "ranxeras"]
anio_adecuado = anio > 2010
if duracion_adecuada and genero_adecuado and anio_adecuado:
print("\n¡La canción es perfecta para tu playlist!")
else:
print("\nLa canción no cumple con todos los criterios para la playlist:")
if not duracion_adecuada:
print(f"- La duración ({duracion} min) está fuera del rango ideal (2.5-4.5
min)")
if not genero_adecuado:
print(f"- El género '{genero}' no está entre los preferidos (kpop, jazz,
ranxeras)")
if not anio_adecuado:
print(f"- El año {anio} es anterior a 2010"
