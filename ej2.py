maximo = int(input("Digite el máximo exponente: "))

for id in range(maximo+1):
    resultado = 2**id
    print(f"2 ^ {id} = {resultado}")