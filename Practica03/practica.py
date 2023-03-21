def problemaA():
    a = float(input('ingrese el valor de A: '))
    b = float(input('ingrese el valor de B: '))
    c = float(input('ingrese el valor de C: '))
    e = float(input('ingrese el valor de E: '))
    f = float(input('ingrese el valor de F: '))
    
    resultado = (((a-b)*e**(c-1)*c) / ((f*b)-(c*a))) * a
    return resultado 

def problemaB():
    numero1 = float(input('ingrese el valor de numero 1: '))
    numero2 = float(input('ingrese el valor de numero 2: '))

    resultado = numero1 + numero2
    return resultado

def problemaC():
     numero1 = float(input('ingrese el valor de numero 1: '))
     numero2 = float(input('ingrese el valor de numero 2: '))
     numero3 = float(input('ingrese el valor de numero 3: '))

     resultado = numero1 * numero2 * numero3
     return resultado

def problemaD():
    a = float(input('ingrese el valor de A: '))
    b = float(input('ingrese el valor de B: '))
    c = float(input('ingrese el valor de C: '))
    d = float(input('ingrese el valor de D: '))
    e = float(input('ingrese el valor de E: '))
    f = float(input('ingrese el valor de F: '))
    
    resultado = ((c<e) and not (d * c/f == a)) or ((f < a/c) and (e* (c - b) != f) > d**b)
    return resultado

def problemaE():
    numero1 = int(input('ingrese el valor de numero 1: '))
    numero2 = int(input('ingrese el valor de numero 2: '))
   
    resultado = numero1 // numero2
    return resultado

def problemaF():
    a = int(input('ingrese el valor de A: '))
    b = int(input('ingrese el valor de B: '))

    resultado = b // a
    return resultado 

def problemaG():
     numero1 = float(input('ingrese el valor de numero 1: '))
     numero2 = float(input('ingrese el valor de numero 2: '))
     numero3 = float(input('ingrese el valor de numero 3: '))

     resultado = numero1 - numero2 - numero3
     return resultado


while True: 
    print('--------- MENU ---------')
    print("a. ((𝐴−𝐵∗𝐸^𝐶−1)*C/(𝐹∗𝐵−𝐶∗𝐴)) * A")
    print("b. Suma de dos números")
    print("c. Multiplicación de tres números en formato flotante")
    print("d. (𝐶 < 𝐸) 𝑎𝑛𝑑 𝑛𝑜𝑡 (𝐷 ∗𝐶𝐹== 𝐴) 𝑜𝑟 ((𝐹 <𝐴𝐶) 𝑎𝑛𝑑 ((𝐸 ∗ 𝐶 − 𝐵)! = 𝐹) > 𝐷𝐵))")
    print("e. División de dos números en formato entero")
    print("f. Dados dos números A y B, calcule la división entera donde A es el divisor y B es el dividendo.")
    print("g. Resta de tres números")
    print("h. Apagar la calculadora (salir)")
    print("------------------------------------")
    
    opcion = input('Seleccione una opcion: ')

    if opcion == 'a':
        print('\n ----> El resultado es: ', problemaA(), '\n')

    elif opcion == 'b':
        print('\n ----> El resultado es: ', problemaB(), '\n')        
        
    elif opcion == 'c':
        print('\n ----> El resultado es: ', problemaC(), '\n') 

    elif opcion == 'd':
        print('\n ----> El resultado es: ', problemaD(), '\n') 

    elif opcion == 'e':
        print('\n ----> El resultado es: ', problemaE(), '\n')  

    elif opcion == 'f':
        print('\n ----> El resultado es: ', problemaF(), '\n')   

    elif opcion == 'g':
        print('\n ----> El resultado es: ', problemaG(), '\n')                      
                               
    elif opcion == 'h':
        break
    else:
        print('La opcion es invalida')

    input('Presione cualquier tecla para continuar...')