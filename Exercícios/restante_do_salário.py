Salário = float (input("Quanto você ganha no mês?"))
a= float (input("Qual o valor da conta de água?"))
l= float (input("Qual o valor da conta de luz?"))
t= float (input("Qual o valor da conta de telefone?"))
total = a + l + t
if Salário >= 900.00:
    print ("Você tem dinheiro o suficiente para pagar as contas")
else:
    print ("Você não tem dinheiro o suficiente para pagar as contas")
Sobrou = Salário - total
print ("O valor que sobrou do seu salário é de R$ %.2f" % Sobrou)
