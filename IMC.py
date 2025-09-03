print("CALCULADOR DE IMC!")

peso = float(input("Digite seu peso em kg (ex: 55.6): "))
altura = float(input("Digite sua altura em metros (ex: 1.62): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f} ")

if imc < 18.5:
    classificacao = "Magreza"
elif 18.5 <= imc < 25:
    classificacao = "Normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 40:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade Grave"
    
print(f"Sua classificação é: {classificacao}")