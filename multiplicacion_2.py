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
        print("introduzca la cantidad de numeros correctos")
        break
    numeros_combretidos=[]
    for i in nuemros_separados:
        nuemro_comber=int(i)
        numeros_combretidos.append(nuemro_comber)
    Matriz1.append(numeros_combretidos)

Matriz2=[]
for i0 in range(int(filas)):
    contador1=i0+1
    Numeros="23 45"#input(f"por favor introduzca la linea nuemro {contador1} de la matriz(use espacios para separar los numeros): ")
    nuemros_separados=Numeros.split(" ")
    cantidad_de_indices=len(nuemros_separados)
    if cantidad_de_indices ==2+1:
        print("introduzca la cantidad de numeros correctos")
        break
    numeros_combretidos=[]
    for i in nuemros_separados:
        nuemro_comber=int(i)
        numeros_combretidos.append(nuemro_comber)
    Matriz2.append(numeros_combretidos)
    

Matriz3=[]
for i in range(int(filas)):
    i=[]
    Matriz3.append(i)

Matriz0=[]
for i in range(int(filas)):
    i=[]
    Matriz0.append(i)


for i0 in range(int(filas)-1):
    for i in enumerate(Matriz2):
        ind=i[0]
        val=i[1]
        for i2 in enumerate(val):
            ind2=i2[0]
            val2=i2[1]
            Matriz3[ind2].append(val2)

for i0 in enumerate(Matriz1):
    ind0=i0[0]
    val0=i0[1]
    valor=0
    valorM=0
    for i in Matriz3:
        for i2,i3 in zip(val0,i):
            if valor == 0 :
                valorM = i2*i3+valor
                valor=i2*i3
            elif valor != 0 :
                valorM = i2*i3+valor
                Matriz0[ind0].append(valorM)
                valor=i2*i3
print(Matriz0)

for i0 in enumerate(Matriz0):
    indice0=i0[0]
    valor0=i0[1]
    contador = 0
    for i in enumerate(valor0):
        contador+=1
        if contador == int(filas):
            break
        elif contador != int(filas):
            valor0.pop(contador)
print(Matriz0)