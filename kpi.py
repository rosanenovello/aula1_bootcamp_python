# 1) Solicita ao usuário que digite seu nome
nome= input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salario: "))
print(type(salario))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite seu bonus: "))
print(type(bonus))

# 4) Calcule o valor do bônus final
bonus_final = salario * (bonus/100)
print(f"Bonus no salario :  {bonus_final}")


# 5) Imprima cálculo do KPI para o usuário
kpi_bonus = 1000 + salario * bonus 


# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f" {nome} seu salario é de  {salario} com bonus de {bonus}% , totalizando {bonus_final} de bonus")

print(f" {nome} seu salario KPI é de  {kpi_bonus}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?