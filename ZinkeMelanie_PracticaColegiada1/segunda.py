precio = 10000  # constante, no se especificó el precio en el problema.
cantidad = 0
descuento = 0
montoCompra = 0
montoDescuento = 0
montoTotal = 0

while True:
    cantidad = int(input('Ingrese la cantidad de pantalones: '))

    if cantidad >= 1 and cantidad <= 5:
        descuento = 0.125

    elif cantidad >= 5 and cantidad <= 8:
        descuento = 0.20

    elif cantidad > 0:
        descuento = 0.315

    montoCompra = precio * cantidad

    montoDescuento = montoCompra * descuento

    montoTotal = montoCompra - montoDescuento

    print('Monto de Compra ' + str(montoCompra))
    print('Descuento ' + str(descuento * 100))
    print('Monto de descuento ' + str(montoDescuento))
    print('Monto total ' + str(montoTotal))
