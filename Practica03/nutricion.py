caloriasSemana = [0] * 7
dias = [
    'Lunes',
    'Martes',
    'Miercoles',
    'Jueves',
    'Viernes',
    'Sabado',
    'Domingo',
]

for i in range(7):
    caloriasSemana[i] = int(
        input("Ingrese las calorías consumidas en el día " + str(i+1) + ": "))


def diaMasCalorias(calorias):
    return calorias.index(max(calorias))


def diaMenosCalorias(calorias):
    return calorias.index(min(calorias))


def totalCalorias(calorias):
    return sum(calorias)


def imprimirCalorias(calorias):
    for i in range(7):
        print("Calorías consumidas en el día " +
              dias[i] + ": " + str(calorias[i]))


while True:
    print("\nMenú:")
    print("1. Estimar el día que más calorías se consumieron")
    print("2. Estimar el día que menos calorías se consumieron")
    print("3. Sumar el total de calorías consumidas durante la semana")
    print("4. Imprimir las calorías consumidas cada día")
    print("5. Salir")
    opcion = input("Seleccione una opción del menú: ")

    if opcion == '1':
        indiceDia = diaMasCalorias(caloriasSemana)
        print("El día con más calorías fue el día", dias[indiceDia])
    elif opcion == '2':
        indiceDia = diaMenosCalorias(caloriasSemana)
        print("El día con menos calorías fue el día", dias[indiceDia])
    elif opcion == '3':
        print("El total de calorías consumidas durante la semana fue:",
              totalCalorias(caloriasSemana))
    elif opcion == '4':
        imprimirCalorias(caloriasSemana)
    elif opcion == '5':
        break
    else:
        print("Opción inválida. Por favor seleccione una opción del menú.")
