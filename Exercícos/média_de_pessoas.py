qtd = int(input("quantas pessoas? "))

homem = 0
mulher = 0
soma_h = 0
soma_m = 0

for i in range(qtd):
    sexo = input("digite o sexo (M/F): ")
    altura = float(input("digite a altura: "))

    if sexo == "M":
        homem = homem + 1
        soma_h = soma_h + altura

    else:
        mulher = mulher + 1
        soma_m = soma_m + altura

print()

if homem > 0:
    print("media dos homens:", soma_h / homem)

if mulher > 0:
    print("media das mulheres:", soma_m / mulher)
