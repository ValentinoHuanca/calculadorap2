operacion=input("eliga el tipo de operacion que desea(sumar,restar,multiplicar):")
operacion_igualado_letras=operacion.lower()
Sumar="sumar"
Restar="restar"
Multiplicar="multiplicar"
Tipo_de_Matriz = "2x2" #input("decime que tipo de matriz es, EJ:2x2,3x3,etc: ")
cadena_sepa=Tipo_de_Matriz.split("x")
filas=cadena_sepa[0]
columnas=cadena_sepa[1]
Matriz1=[]
for i0 in range(int(filas)):
    contador1=i0+1
    Numeros="23 45"#input(f"por favor introduzca la linea nuemro {contador1} de la matriz(use espacios para separar los numeros): ")
    nuemros_separados=Numeros.split(" ")
    cantidad_de_indices=len(nuemros_separados)
    if cantidad_de_indices ==2+1:
        print("introduzca la cantidad de numeros correctos, se iniciara el pedido de datos desde el inicio")
        break
    numeros_combretidos=[]
    for i in nuemros_separados:
        nuemro_comber=int(i)
        numeros_combretidos.append(nuemro_comber)
    Matriz1.append(numeros_combretidos)

Matriz2=[]
for i0 in range(int(filas)):
    contador1=i0+1
    Numeros="23 45"#input(f"por favor introduzca la linea nuemro {contador1} de la segunda matriz(use espacios para separar los numeros): ")
    nuemros_separados=Numeros.split(" ")
    cantidad_de_indices=len(nuemros_separados)
    if cantidad_de_indices ==2+1:
        print("introduzca la cantidad de numeros correctos, se iniciara el pedido de datos desde la linea 1° de la matriz numero uno")
        break
    numeros_combretidos=[]
    for i in nuemros_separados:
        nuemro_comber=int(i)
        numeros_combretidos.append(nuemro_comber)
    Matriz2.append(numeros_combretidos)

Matriz0=[]
for i in range(int(filas)):
    i=[]
    Matriz0.append(i)

for i in [Sumar,Restar,Multiplicar]:
    if Sumar==operacion_igualado_letras:
        import operaciones_matematicas.prueba_suma as suma
        uno=suma.suma(int(filas),Matriz1,Matriz2,Matriz0)
        print(uno)
        break
    elif Restar==operacion_igualado_letras:
        import operaciones_matematicas.prueba_resta as resta
        dos=resta.resta(int(filas),Matriz1,Matriz2,Matriz0)
        print(dos)
        break
    elif Multiplicar==operacion_igualado_letras:
        import operaciones_matematicas.prueba_multiplicacion as multiplicacion
        tres=multiplicacion.multiplicar(int(filas),Matriz1,Matriz2,Matriz0)
        print(tres)
        break