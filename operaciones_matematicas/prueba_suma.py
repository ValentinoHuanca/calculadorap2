def suma(filas,Matriz1,Matriz2,Matriz0):
    for i in range(int(filas)):
        for i2,i3 in zip(Matriz1[i],Matriz2[i]):
            i4=i2+i3
            Matriz0[i].append(i4)
    return Matriz0