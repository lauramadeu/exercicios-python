# Faça um programa que pegue a cotação do dolar e transforme para real
cotacao_dolar = float(input("Digite a cotação atual do dolar em reais: "))

# Valor em dolar para ser convertido para real
valor_dolar = float(input("Digite o valor em dolar a ser convertido para reais: "))

# Calcule o valor em reais
valor_real = valor_dolar * cotacao_dolar

# Exibe o resultado da conversão
print("O valor em reais é:", valor_real)
