numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

for i in range(numero2):
    nu = (i+1)
    multiplo = numero1 * nu
    print(f"{numero1} x {nu} = {multiplo}")