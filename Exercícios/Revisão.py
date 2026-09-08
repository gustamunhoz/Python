#Uma resolução de como funcionam conceitos como variáveis, operadores, estruturas condicionais, laços de repetição, funções e arrays.

#1-Atribuição de entrada e saída
nome = "Mariana"
idade = 33

print("Meu nome é", nome, "e tenho", idade, "anos.")

#Saída
Meu nome é Mariana e tenho 33 anos.

#2-Operadores
num1 = 10
num2 = 5

print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Divisão:", num1 / num2)

#Saída
Soma: 15
Subtração: 5
Multiplicação: 50
Divisão: 2.0

#3- Estruturas condicionais
nota = 8

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


#4- Laço 'For'
for i in range(1, 11):
    print(i)

#Saída
1
2
3
4
5
6
7
8
9
10

#5-Laço 'While'
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

#Saída
10
9
8
7
6
5
4
3
2
1

#6-Funções (def)
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

resultado = calcular_media(8, 10)

print(resultado)

#Saída
9.0

#7-Arrays
numeros = [10, 20, 30, 40, 50]

soma = 0

for numero in numeros:
    soma = soma + numero

print("Soma:", soma)

#Saída
Soma: 150
