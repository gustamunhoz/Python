T= float(input("Quantas horas você trabalha por dia?"))
totalH=T*45.00
ttlH2= T*37.50
if totalH >= 1:
    print("O valor que você irá receber por dia é:", totalH)
else: ttlH2= T*37.50
print("Caso não complete as horas, receberá o valor descontado :", ttlH2)
