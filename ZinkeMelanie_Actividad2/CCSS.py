# Variables globales
cantidadAltas = 0
cantidadVerdes = 0
cantidadAmarillos = 0
cantidadRojos = 0

for n in range(1, 11):
    # Variables internas
    nombrePaciente = ''
    cedulaPaciente = ''
    cantidadSintomas = 0
    clasificacion = ''

    nombrePaciente = input('Ingrese el nombre del paciente ' + str(n))
    cedulaPaciente = input('Ingrese la cedula del paciente ' + str(n))
    cantidadSintomas = int(
        input('Ingrese la cantidad de sintomas que presenta el paciente ' + str(n)))

    if cantidadSintomas == 0:
        clasificacion = 'Alta'
        cantidadAltas += 1

    elif cantidadSintomas >= 1 and cantidadSintomas < 5:
        clasificacion = 'Verde'
        cantidadVerdes += 1

    elif cantidadSintomas >= 5 and cantidadSintomas < 10:
        clasificacion = 'Amarillo'
        cantidadAmarillos += 1

    elif cantidadSintomas >= 10:
        clasificacion = 'Rojo'
        cantidadRojos += 1

    print('Informacion del paciente ' + str(n))
    print('Nombre:' + nombrePaciente)
    print('Cedula:' + cedulaPaciente)
    print('Cant. Sintomas:' + str(cantidadSintomas))
    print('Clasificacion Grevedad:' + clasificacion)
    print()

print('Resultado de clasificaciones.')
print('Pacientes en Alta: ' + str(cantidadAltas))
print('Pacientes en Verde: ' + str(cantidadVerdes))
print('Pacientes en Amarillos: ' + str(cantidadAmarillos))
print('Pacientes en Rojos: ' + str(cantidadRojos))
