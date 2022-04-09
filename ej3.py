numeroestudiantes = 10
minus50 = 0
between57 = 0
between78 = 0
most8 = 0

for i in range(numeroestudiantes):
    vari= int(input(f"Digite la nota para el estudiante {(i+1)}: "))
    if (vari < 50):
        minus50 += 1
        print(f"Hay {minus50} estudiante(s) con nota por debajo de 50")
    elif (vari >= 50 and vari < 70):
        between57 += 1
        print(f"Hay {between57} estudiante(s) con nota entre 50 y 70")
    elif (vari >= 70 and vari < 80):
        between78 += 1
        print(f"Hay {between78} estudiante(s) con nota entre 70 y 80")
    else:
        most8 += 1
        print(f"Hay {most8} estudiante(s) con nota mayor o igual a 80")