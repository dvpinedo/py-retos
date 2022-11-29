##Calculadora de indice de masa corporal

peso = input("Ingrese su peso en kg: ")
estatura = input("Ingrese su estatura en metros: ")
imcs = round (float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es " + str(imcs))