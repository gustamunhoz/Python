VC= float (input("Qual foi o valor da compra?"))
if VC >=200:
    print("Você tem direito a um desconto de 20%")
    VC= VC*0.8
    print("O valor da compra com desconto é R$ %.2f" % VC)
else:
    print("Como o valor não foi igual ou superior a 200, você não tem direito a desconto")