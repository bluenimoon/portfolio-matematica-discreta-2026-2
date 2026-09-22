# ==================================================
# PORTFÓLIO DE ESTRUTURAS MATEMÁTICAS
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 2 - Divisibilidade, MDC e MMC
# ==================================================

nome = input("Nome: ")
matricula = input("Matrícula: ")
turno = input("Turno: ")

print("\n==============================================")
print("PORTFÓLIO DE ESTRUTURAS MATEMÁTICAS")
print("ATIVIDADE 2 - DIVISIBILIDADE, MDC E MMC")
print("==============================================")
print("Aluno:", nome)
print("Matrícula:", matricula)
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno:", turno)
print("==============================================")

# Entrada de dois números inteiros positivos
a = int(input("\nDigite o primeiro número inteiro positivo: "))

while a <= 0:
    print("O número deve ser maior que zero.")
    a = int(input("Digite novamente o primeiro número: "))

b = int(input("\nDigite o segundo número inteiro positivo: "))

while b <= 0:
    print("O número deve ser maior que zero.")
    b = int(input("Digite novamente o segundo número: "))

print("\n==============================================")
print("NÚMEROS INFORMADOS")
print("==============================================")
print("Primeiro número:", a)
print("Segundo número:", b)

# ==================================================
# DIVISÃO INTEIRA E RESTO DA DIVISÃO
# ==================================================

quociente = a // b
resto = a % b

print("\n==============================================")
print("DIVISÃO INTEIRA E RESTO")
print("==============================================")
print("DIV =", quociente)
print("MOD =", resto)
print(a, "=", b, "*", quociente, "+", resto)

# ==================================================
# MDC PELO ALGORITMO DE EUCLIDES
# ==================================================

# Cópias para preservar os números originais
x = a
y = b

print("\n==============================================")
print("ALGORITMO DE EUCLIDES")
print("==============================================")

while y != 0:
    quociente = x // y
    resto = x % y

    print(x, "=", y, "*", quociente, "+", resto)

    x = y
    y = resto

mdc = x

print("\nMDC =", mdc)

# ==================================================
# MÍNIMO MÚLTIPLO COMUM
# ==================================================

mmc = (a * b) // mdc

print("\n==============================================")
print("MÍNIMO MÚLTIPLO COMUM")
print("==============================================")
print("MMC =", mmc)

print("\n==============================================")
print("RESUMO DOS RESULTADOS")
print("==============================================")
print("Números informados:", a, "e", b)
print("MDC =", mdc)
print("MMC =", mmc)