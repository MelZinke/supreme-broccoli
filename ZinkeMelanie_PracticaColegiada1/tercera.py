PRECIO = 100

while True:
    cantidadNoches = 0
    descuento = 0
    montoTotal = 0

    cantidadNoches = int(input('Ingrese la cantidad de noches: '))

    if cantidadNoches > 3:
        descuento = 0.05

    montoTotal = (PRECIO * cantidadNoches) - \
        (PRECIO * cantidadNoches) * descuento

    print('El costo total del hospedaje ses:  ' + str(montoTotal))
