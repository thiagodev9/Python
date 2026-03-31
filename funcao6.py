"""
4. Funções
Importância na Engenharia de Dados
Funções permitem modularizar e reutilizar código, essencial para processar e analisar 
grandes conjuntos de dados. Na engenharia de dados, funções são usadas para encapsular 
lógicas de transformação, limpeza, agregação e análise de dados, tornando o código mais
organizado e mantendo a qualidade do código.

As funções em programação são abstrações poderosas que permitem encapsular blocos de código
para realizar tarefas específicas. Elas servem não apenas para organizar o código e torná-lo mais legível,
mas também para abstrair complexidades, permitindo que os programadores pensem em problemas em um nível mais alto.
Uma função bem projetada pode ser vista como um "mini-programa" dentro de um programa maior,
com sua própria lógica e dados de entrada e saída.

Um exemplo clássico dessa abstração é a ordenação de uma lista.
Vamos primeiro desenvolver uma função simples em Python que ordena uma lista
usando o algoritmo de ordenação por seleção, um método simples mas eficaz para listas pequenas e médias.
Em seguida, mostraremos como essa tarefa pode ser realizada de forma mais direta usando o método sort()
 built-in do Python, que é uma abstração fornecida pela linguagem para realizar a mesma tarefa.
"""

# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)


"""
Usando o Método Built-in sort()
O Python fornece uma abstração poderosa através do método sort(), 
que pode ordenar listas in-place de maneira eficiente
 e com uma sintaxe simples.
"""
# Lista de exemplo
lista_exemplo = [64, 34, 25, 12, 22, 11, 90]

# Ordenando a lista com sort()
lista_exemplo.sort()

print("Lista ordenada com método built-in:", lista_exemplo)