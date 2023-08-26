print("---------------------------------------------")
print("----------------CALCULADORA------------------")
print("---------------------------------------------")

s1=int(input("Digite o primeiro valor......: "))
s2=int(input("Digite o segundo valor.......: "))

soma=s1+s2
print("\nSoma dos valores: ",soma)

subtração=s1-s2
print("\nDiferença entre os valores: ",subtração)

multiplicação=s1*s2
print("\nMultiplicação entre os valores: ",multiplicação)

if s2!=0:
    print("\nA divisão entre os valores é: ",s1/s2)
else:
    print("\n>>>Impossível !")

