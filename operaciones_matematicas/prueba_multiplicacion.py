def multiplicar(filas,Matriz1,Matriz2,Matriz0):
    Matriz3=[]
    for i in range(int(filas)):
        i=[]
        Matriz3.append(i)


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
    return Matriz0