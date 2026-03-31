#Funções

#Funções são blocos de código que realizam uma tarefa específica.
#Elas são definidas usando a palavra-chave def.
#Elas podem receber parâmetros e retornar valores.

#Exemplo de função
def soma(a, b):
    return a + b

#Exemplo de uso
print(soma(1, 2))


# Mais exemplos de funções
def subtrai(a, b):
    return a - b

print(subtrai(1, 2))
     
#Multiplicação
def multiplica(a, b):
    return a * b

print(multiplica(1, 2))

#Divisão
def divide(a, b):
    return a / b

print(divide(1, 2))

#Chamando funções com parâmetros diferentes
print(soma(1, 2))
print(subtrai(1, 2))
print(multiplica(1, 2))
print(divide(1, 2))


#Exemplo de função tipadas 
def soma(a: int, b: int) -> int:
    return a + b

print(soma(1, 2))

#Chamando a função com parâmetros diferentes
print(soma(1, 2))

"""
Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos,
o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim,
calcular e reportar as vendas totais por categoria de produto.
"""

#Exemplo de arquivo CSV
"""
produto,categoria,preco,quantidade
camiseta,roupas,29.99,10
calca,roupas,59.99,5
tenia,calcados,129.99,3
"""     
import csv
#Lendo o arquivo CSV
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            print(linha)

#Processando o arquivo CSV      
def processar_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            print(linha)

#Calculando as vendas totais por categoria
def calcular_vendas(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            print(linha)

#Reportando as vendas totais por categoria
def reportar_vendas(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            print(linha)

#Chamando as funções
ler_csv('vendas.csv')
processar_csv('vendas.csv')
calcular_vendas('vendas.csv')
reportar_vendas('vendas.csv')            