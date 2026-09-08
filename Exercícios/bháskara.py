#calculando a formula de bhaskara
print("Vamos calcular a fórmula de bhaskara")
a=float(input("Qual o valor de a?"))
b=float(input("Qual o valor de b?"))
c=float(input("Qual o valor de c?"))
delta=b**2-4*a*c
print("O valor de delta é:", delta)
x=float(input("qual o valor de x?"))
x=-b+delta**(1/2)/(2*a)
print("O valor de x é:", x)
x=-b-delta**(1/2)/(2*a)
print("o valor de x é:",x)
