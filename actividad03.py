DESCUENTO_ESTUDIANTE = 0.15
DESCUENTO_CLIENTE_FRECUENTE = 0.10
DESCUENTO_PRIMERA_COMPRA = 0.05
precio_original = float(input("Ingrese el precio del artículo: $"))
es_estudiante = input("¿Es usted estudiante? (s/n): ").lower() == 's'
es_cliente_frecuente = input("¿Es usted cliente frecuente? (s/n): ").lower() == 's'
es_primera_compra = input("¿Es su primera compra? (s/n): ").lower() == 's'
descuento = 0
if es_estudiante:
    descuento = DESCUENTO_ESTUDIANTE
elif es_cliente_frecuente:
    descuento = DESCUENTO_CLIENTE_FRECUENTE
elif es_primera_compra:
    descuento = DESCUENTO_PRIMERA_COMPRA
monto_descuento = precio_original * descuento
precio_final = precio_original - monto_descuento
print(f"El precio final con descuento es: ${precio_final:.2f}")