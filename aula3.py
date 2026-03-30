# controle de fluxo
# Exemplos práticos: if, while, for, break, continue, pass, else, elif

print("-" * 30)
print("1. EXEMPLO COM: if, elif e else")
idade = 18

if idade < 18: # if - se
    print("Você é menor de idade.")
elif idade == 18: # elif - se não se
    print("Você tem exatamente 18 anos. Bem-vindo à maioridade!")
else: # else - se não
    print("Você é maior de idade.")


print("\n" + "-" * 30)
print("2. EXEMPLO COM: while (enquanto)")
contador = 0

while contador < 3:
    print(f"Contador do while: {contador}")
    contador += 1 # contador = contador + 1


print("\n" + "-" * 30)
print("3. EXEMPLO COM: for (para)")
frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")

print("\nUsando 'for' com 'range' (intervalo):")
for i in range(4): # Vai de 0 a 3
    print(f"Número gerado: {i}")


print("\n" + "-" * 30)
print("4. EXEMPLO COM: break (parar o loop imediatamente)")
for numero in range(10):
    if numero == 4:
        print("Achei o número 4, parando o for com 'break'!")
        break # Sai do ciclo for completamente
    print(f"Analisando número: {numero}")


print("\n" + "-" * 30)
print("5. EXEMPLO COM: continue (pular etapa atual e continuar)")
for numero in range(5):
    if numero == 2:
        print("O número é 2, pulando ele com 'continue'!")
        continue # Ignora o restante do código e vai para a próxima repetição
    print(f"Analisando número: {numero}")


print("\n" + "-" * 30)
print("6. EXEMPLO COM: pass (passar - não faz nada)")
# O pass é ótimo de usar quando você cria uma estrutura (ex: um 'if' ou uma função), mas ainda vai escrever o código depois. Ele evita erros de sintaxe.
numero_teste = 10
if numero_teste > 5:
    # Ainda vou escrever esse código no futuro, deixo o pass para não dar erro
    pass
else:
    print("Número é menor ou igual a 5")
print("O código passou sem erros graças ao 'pass'.")


print("\n" + "=" * 40)
print("             LISTAS E DICIONÁRIOS")
print("=" * 40)

print("\n--- 7. LISTAS ---")
# Listas servem para guardar vários valores (itens) em ordem numa única variável. Posicionamento começa no zero.
minha_lista_de_compras = ["Maçã", "Pão", "Leite", "Café"]

print(f"Lista completa: {minha_lista_de_compras}")
print(f"Primeiro item (posição 0): {minha_lista_de_compras[0]}")
print(f"Último item: {minha_lista_de_compras[-1]}")

# Adicionando um novo item no final da lista usando .append():
minha_lista_de_compras.append("Biscoito")
print(f"Lista após adicionar 'Biscoito': {minha_lista_de_compras}")

# Removendo um item usando .remove():
minha_lista_de_compras.remove("Pão")
print(f"Lista após remover 'Pão': {minha_lista_de_compras}")


print("\n--- 8. DICIONÁRIOS ---")
# Dicionários guardam informações em pares chamados "Chave" e "Valor". Em outras linguagens são chamados de JSON ou Objetos.
# Ao invés de acessar por números (0, 1, 2) como nas listas, você usa os "nomes" (chaves) para consultar os valores.
meu_carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "cor": "Prata"
}

print(f"Dicionário completo: {meu_carro}")

# Acessando um valor específico do dicionário usando sua chave (entre colchetes ou aspas):
print(f"A marca do carro é: {meu_carro['marca']}")
print(f"O ano do carro é: {meu_carro['ano']}")

# Adicionando uma nova informação (uma nova chave e valor) no dicionário:
meu_carro["placa"] = "ABC-1234"
print(f"Dicionário após adicionar a placa: {meu_carro}")

# Alterando um valor que já existe:
meu_carro["cor"] = "Preto"
print(f"Dicionário após pintar o carro (mudamos a cor): {meu_carro}")


