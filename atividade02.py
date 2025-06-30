#Conversor de moedas
real = 100
dolar = 5.20
euro = 6.10

ConverterDolar = real / dolar
ConverterEuro = real / euro

print(f"O valor do real convertido para dolar é: {ConverterDolar:.2f}")
print(f"O valor do real convertido para Euro é: {ConverterEuro:.2f}")

# Calculadora de Desconto

NomeProduto = "Camiseta Preta"
PrecoOriginal = 50.00
Desconto = 20

ValorDesconto = PrecoOriginal * (Desconto / 100)

PrecoFinal = PrecoOriginal - ValorDesconto

print(f"Nome do Produto: {NomeProduto}")
print(f"Preço Original: R$ {PrecoOriginal:.2f}")
print(f"Desconto Original: R$ {Desconto:.2f}")
print(f"Valor do Desconto: R$ {ValorDesconto:.2f}")
print(f"Preço Final: R$ {PrecoFinal:.2f}")

# Define as notas do aluno
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("------BOletim do Aluno")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média Final: {media: .2f}")

#Calculadora de Consumo de Combustível
DistanciaPercorrida = 300
CombustivelGasto = 25

ConsumoMedio =  DistanciaPercorrida / CombustivelGasto

print(f"Distância Percorrida: {DistanciaPercorrida} ")
print(f"Combustível Gasto: {CombustivelGasto}")
print(f"Consumo Medio: {ConsumoMedio} km/l")

# Calculadora de Soma com entrada do Usuário

A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))

X = A + B

print(f"X = {X}")

NumeroFuncionario = int(input("Digite o número do funcionario: "))
HorasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
ValorHora = float(input("Digite o valor da hora: "))

salario = HorasTrabalhadas * ValorHora

print(f"Salário do Funcionário: R$ {salario:.2f}")