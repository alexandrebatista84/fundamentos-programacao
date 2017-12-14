
n=float(input("Introduza uma quantia em Euros? "))

notas50=0
notas20=0
notas10=0
notas5=0
moeda2=0
moeda1=0
moeda50c=0
moeda20c=0
moeda10c=0
moeda5c=0
moeda2c=0
moeda1c=0

notas50=n//50
notas20=(n-notas50*50)//20
notas10=(n-notas50*50-notas20*20)//10
notas5=(n-notas50*50-notas20*20-notas10*10)//5
moeda2=(n-notas50*50-notas20*20-notas10*10-notas5*5)//2
moeda1=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2)//1
moeda50c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1)//0.5
moeda20c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1-moeda50c*0.5)//0.2
moeda10c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1-moeda50c*0.5-moeda20c*0.2)//0.1
moeda5c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1-moeda50c*0.5-moeda20c*0.2-moeda10c*0.1)//0.05
moeda2c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1-moeda50c*0.5-moeda20c*0.2-moeda10c*0.1-moeda5c*0.05)//0.02
moeda1c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moeda2*2-moeda1-moeda50c*0.5-moeda20c*0.2-moeda10c*0.1-moeda5c*0.05-moeda2c*0.02)//0.01

print("A quantia em Euros é composta por:")
print(notas50,"notas de 50€")
print(notas20,"notas de 20€")
print(notas10,"notas de 10€")
print(notas5,"notas de 5€")
print(moeda2,"moedas de 2€")
print(moeda1,"moedas de 1€")
print(moeda50c,"moedas de 0.50€")
print(moeda20c,"moedas de 0.20€")
print(moeda10c,"moedas de 0.10€")
print(moeda5c,"moedas de 0.05€")
print(moeda2c,"moedas de 0.02€")
print(moeda1c,"moedas de 0.01€")