#Primeiro, crie a função
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)


# Entrada do usuário
n = int(input("Digite o número de discos: "))

print(f"\nNúmero mínimo de movimentos: {2**n - 1}\n")
torre_hanoi(n, 'A', 'C', 'B')
