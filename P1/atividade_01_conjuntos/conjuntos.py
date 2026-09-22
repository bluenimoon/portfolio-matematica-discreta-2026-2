# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# ==================================================

nome = input("Nome: ")
matricula = input("Matrícula: ")
turno = input("Turno: ")

print("\n==============================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("==============================================")
print("Aluno:", nome)
print("Matrícula:", matricula)
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno:", turno)
print("==============================================")

# Entrada dos elementos dos conjuntos
entrada_a = input("\nDigite os elementos do conjunto A separados por espaço: ")
entrada_b = input("Digite os elementos do conjunto B separados por espaço: ")

# Converte os valores digitados para números inteiros
valores_a = entrada_a.split()
valores_b = entrada_b.split()

A = []
B = []

# Montagem do conjunto A sem elementos repetidos
for valor in valores_a:
    numero = int(valor)

    if numero not in A:
        A.append(numero)

# Montagem do conjunto B sem elementos repetidos
for valor in valores_b:
    numero = int(valor)

    if numero not in B:
        B.append(numero)

print("\n==============================================")
print("CONJUNTOS INFORMADOS")
print("==============================================")
print("A =", A)
print("B =", B)

# ==================================================
# OPERAÇÕES ENTRE OS CONJUNTOS
# ==================================================

# União de A e B
uniao = []

for elemento in A:
    if elemento not in uniao:
        uniao.append(elemento)

for elemento in B:
    if elemento not in uniao:
        uniao.append(elemento)

# Interseção de A e B
intersecao = []

for elemento in A:
    if elemento in B:
        intersecao.append(elemento)

# Diferença A - B
diferenca_a_b = []

for elemento in A:
    if elemento not in B:
        diferenca_a_b.append(elemento)

# Diferença B - A
diferenca_b_a = []

for elemento in B:
    if elemento not in A:
        diferenca_b_a.append(elemento)

print("\n==============================================")
print("OPERAÇÕES ENTRE OS CONJUNTOS")
print("==============================================")
print("A ∪ B =", uniao)
print("A ∩ B =", intersecao)
print("A - B =", diferenca_a_b)
print("B - A =", diferenca_b_a)

# ==================================================
# CARDINALIDADES
# ==================================================

cardinalidade_a = 0

for elemento in A:
    cardinalidade_a += 1

cardinalidade_b = 0

for elemento in B:
    cardinalidade_b += 1

cardinalidade_uniao = 0

for elemento in uniao:
    cardinalidade_uniao += 1

cardinalidade_intersecao = 0

for elemento in intersecao:
    cardinalidade_intersecao += 1

print("\n==============================================")
print("CARDINALIDADES")
print("==============================================")
print("|A| =", cardinalidade_a)
print("|B| =", cardinalidade_b)
print("|A ∪ B| =", cardinalidade_uniao)
print("|A ∩ B| =", cardinalidade_intersecao)

# ==================================================
# CONJUNTO DAS PARTES
# ==================================================

# Conjunto das partes de A
partes_a = [[]]

for elemento in A:
    novos_subconjuntos = []

    for subconjunto in partes_a:
        novo_subconjunto = subconjunto + [elemento]
        novos_subconjuntos.append(novo_subconjunto)

    for subconjunto in novos_subconjuntos:
        partes_a.append(subconjunto)


# Conjunto das partes de B
partes_b = [[]]

for elemento in B:
    novos_subconjuntos = []

    for subconjunto in partes_b:
        novo_subconjunto = subconjunto + [elemento]
        novos_subconjuntos.append(novo_subconjunto)

    for subconjunto in novos_subconjuntos:
        partes_b.append(subconjunto)


# Cardinalidade dos conjuntos das partes
cardinalidade_partes_a = 0

for subconjunto in partes_a:
    cardinalidade_partes_a += 1


cardinalidade_partes_b = 0

for subconjunto in partes_b:
    cardinalidade_partes_b += 1


print("\n==============================================")
print("CONJUNTO DAS PARTES")
print("==============================================")

print("P(A) =", partes_a)
print("|P(A)| =", cardinalidade_partes_a)

print("\nP(B) =", partes_b)
print("|P(B)| =", cardinalidade_partes_b)

# ==================================================
# EXEMPLO DE PARTIÇÃO DO CONJUNTO A
# ==================================================

pares = []
impares = []

for elemento in A:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)

particao_a = []

if pares:
    particao_a.append(pares)

if impares:
    particao_a.append(impares)

print("\n==============================================")
print("EXEMPLO DE PARTIÇÃO DO CONJUNTO A")
print("==============================================")

print("Partição de A =", particao_a)

# ==================================================
# PRODUTO CARTESIANO A x B
# ==================================================

produto_cartesiano = []

for elemento_a in A:
    for elemento_b in B:
        par = (elemento_a, elemento_b)
        produto_cartesiano.append(par)

print("\n==============================================")
print("PRODUTO CARTESIANO")
print("==============================================")

print("A x B =", produto_cartesiano)

# ==================================================
# VERIFICAÇÃO DE INCLUSÃO
# ==================================================

a_contido_em_b = True

for elemento in A:
    if elemento not in B:
        a_contido_em_b = False


b_contido_em_a = True

for elemento in B:
    if elemento not in A:
        b_contido_em_a = False


print("\n==============================================")
print("INCLUSÃO ENTRE OS CONJUNTOS")
print("==============================================")

if a_contido_em_b:
    print("A é subconjunto de B.")
else:
    print("A não é subconjunto de B.")

if b_contido_em_a:
    print("B é subconjunto de A.")
else:
    print("B não é subconjunto de A.")