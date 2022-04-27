"""Ejercicio1:
Dado el valor de venta de producto, calcular su IVA (19%)
y el precio final de venta."""

print("-------------------------------")
print("----IVA PRECIO DE VENTA -------")
print("-------------------------------")

# input
precio = int(input("Digite el precio del producto: "))

# processing
iva = 0.19*precio
precio_venta = precio + iva

# output
print("\n\nRESULTADOS:\n")
print("Precio: " + str(precio))
print("IVA: " +  str(iva))
print("Precio de venta: " + str(precio_venta))