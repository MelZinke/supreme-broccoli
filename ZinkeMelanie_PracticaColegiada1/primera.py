# variables
nuevoSalario = 0
salarioActual = 0
tiempoLaborado = 0
aumento = 0

for n in range(5):
    salarioActual = float(input('Ingresar el salario actual:'))
    tiempoLaborado = float(input('Ingresar el tiempo laborado:'))

    if tiempoLaborado >= 0 and tiempoLaborado < 6:
        aumento = 0.1

    elif tiempoLaborado >= 6 and tiempoLaborado < 10:
        aumento = 0.15

    elif tiempoLaborado >= 10 and tiempoLaborado < 15:
        aumento = 0.25

    else:
        aumento = 0.30

    nuevoSalario = salarioActual * aumento + salarioActual

    print('Nuevo Salario: ' + str(nuevoSalario))
    print('Aumento:' + str(aumento))
