n=eval(input("Introduza um valor monetário: "))

notas50=0
notas50=n//50
print("São necessárias",notas50,"notas de 50€.")

notas20=0
notas20=(n-notas50*50)//20
print("São necessárias",notas20,"notas de 20€.")

notas10=0
notas10=(n-notas50*50-notas20*20)//10
print("São necessárias",notas10,"notas de 10€.")

notas5=0
notas5=(n-notas50*50-notas20*20-notas10*10)//5
print("São necessárias",notas5,"notas de 5€.")

moedas2=0
moedas2=(n-notas50*50-notas20*20-notas10*10-notas5*5)//2
print("São necessárias",moedas2,"moedas de 2€.")

moedas1=0
moedas1=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2)//1
print("São necessárias",moedas1,"moedas de 1€.")

moedas50c=0
moedas50c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1)//0.50
print("São necessárias",moedas50c,"moedas de 0.50€.")

moedas20c=0
moedas20c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1-moedas50c*0.5)//0.20
print("São necessárias",moedas20c,"moedas de 0.20€.")

moedas10c=0
moedas10c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1-moedas50c*0.5-moedas20c*0.20)//0.10
print("São necessárias",moedas10c,"moedas de 0.10€.")

moedas5c=0
moedas5c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1-moedas50c*0.5-moedas20c*0.20-moedas10c*0.10)//0.05
print("São necessárias",moedas5c,"moedas de 0.05€.")

moedas2c=0
moedas2c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1-moedas50c*0.5-moedas20c*0.20-moedas10c*0.10-moedas5c*0.05)//0.02
print("São necessárias",moedas2c,"moedas de 0.02€.")

moedas1c=0
moedas1c=(n-notas50*50-notas20*20-notas10*10-notas5*5-moedas2*2-moedas1-moedas50c*0.5-moedas20c*0.20-moedas10c*0.10-moedas5c*0.05-moedas2c*0.02)//0.01
print("São necessárias",moedas1c,"moedas de 0.01€.")
