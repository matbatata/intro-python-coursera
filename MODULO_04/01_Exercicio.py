n = int(input("Digite um número natural: "))
fatorial = 1
contador = 1 
while contador <= n:
    fatorial *= contador
    contador += 1

print(n, "! =",fatorial, sep='')
