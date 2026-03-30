#erros são comuns em programação
#tratar erros é importante para que o programa não pare de funcionar
#try e except são usados para tratar erros
#try é usado para tentar executar um bloco de codigo
#except é usado para tratar um erro
#else é usado para executar um bloco de codigo se não houver erro
#finally é usado para executar um bloco de codigo sempre    

#exemplo de try e except
try:
    numero = int(input("Digite um numero: "))
except ValueError:
    print("Numero invalido")    
else:
    print("Numero valido")
finally:
    print("Fim do programa")
  
#type check é usado para verificar se os tipos de dados estão corretos
#type conversion é usado para converter tipos de dados  

#metodos de operação    
# + adição
# - subtração
# * multiplicação
# / divisão
# % módulo
# ** potenciação
# // divisão inteira

#exemplo de metodos de operação
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(1 % 1)
print(1 ** 1)
print(1 // 1)

#metodos operação
# .upper() - converte para maiúsculo
# .lower() - converte para minúsculo
# .title() - converte para título
# .strip() - remove espaços em branco
# .replace() - substitui uma string por outra
# .split() - divide uma string em uma lista
# .join() - une uma lista em uma string
# .find() - encontra a posição de uma string
# .count() - conta o número de ocorrências de uma string
# .startswith() - verifica se a string começa com uma string
# .endswith() - verifica se a string termina com uma string
# .replace() - substitui uma string por outra
# .split() - divide uma string em uma lista
# .join() - une uma lista em uma string
# .find() - encontra a posição de uma string
# .count() - conta o número de ocorrências de uma string
# .startswith() - verifica se a string começa com uma string
# .endswith() - verifica se a string termina com uma string 

#exemplo de metodos de operação
print("Hello World".upper())
print("Hello World".lower())
print("Hello World".title())
print("Hello World".strip())
print("Hello World".replace("World", "Python"))
print("Hello World".split())
print("Hello World".join(["Hello", "World"]))
print("Hello World".find("World"))
print("Hello World".count("World"))
print("Hello World".startswith("Hello"))
print("Hello World".endswith("World"))
print("Hello World".replace("World", "Python"))
print("Hello World".split())
print("Hello World".join(["Hello", "World"]))
print("Hello World".find("World"))
print("Hello World".count("World"))
print("Hello World".startswith("Hello"))
print("Hello World".endswith("World"))

# operação logica   
# and - e
# or - ou
# not - não
# xor - ou exclusivo
# in - dentro
# not in - não dentro

#exemplo de operação logica
print(1 and 1)
print(1 or 1)
print(not 1)
print(1 ^ 1)
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

# Faça um programa que peça dois numeros inteiros e imprima a divisão inteira do primeiro pelo segundo
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
res = print("Divisão inteira: ", num1 // num2)
print(res)


# Escreva um programa que calcule area de um circulo, recebendo o raio como entrada
# Area = pi * raio^2    
raio = float(input("Digite o raio do circulo: "))
area = 3.14159 * raio ** 2
print("A area do circulo é: ", area)

# Escreva um programa que calcule o quadrado de um numero
numero = int(input("Digite um numero: "))
quadrado = numero ** 2
print("O quadrado do numero é: ", quadrado)

# Escreva um programa que calcule o cubo de um numero
numero = int(input("Digite um numero: "))
cubo = numero ** 3
print("O cubo do numero é: ", cubo) 

# Escreva um programa que calcule a raiz quadrada de um numero
numero = int(input("Digite um numero: "))
raiz_quadrada = numero ** 0.5
print("A raiz quadrada do numero é: ", raiz_quadrada)

# Escreva um programa que calcule a raiz cúbica de um numero
numero = int(input("Digite um numero: "))
raiz_cubica = numero ** (1/3)
print("A raiz cúbica do numero é: ", raiz_cubica)

# Escreva um programa que calcule a potencia de um numero
numero = int(input("Digite um numero: "))
potencia = numero ** 2
print("A potencia do numero é: ", potencia)

#biblioteca são conjuntos de funções que podem ser usadas em um programa
#biblioteca math é uma biblioteca que contém funções matemáticas
#biblioteca random é uma biblioteca que contém funções aleatórias
#biblioteca datetime é uma biblioteca que contém funções de data e hora
#biblioteca os é uma biblioteca que contém funções de sistema operacional
#biblioteca sys é uma biblioteca que contém funções de sistema
#biblioteca time é uma biblioteca que contém funções de tempo

#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mes e o ano separadamente
#exemplo: 
#Digite uma data: 25/12/2024
#Dia: 25
#Mes: 12
#Ano: 2024

data = input("Digite uma data no formato dd/mm/aaaa: ")
dataseparada = data.split("/")
print("Dia: ", dataseparada[0])
print("Mes: ", dataseparada[1])
print("Ano: ", dataseparada[2]) 

#isintance() verifica se uma variavel é do tipo especificado
#exemplo: 
#isintance(1, int) - True
#isintance(1, float) - False
#isintance(1, str) - False
#isintance(1, bool) - False
#isintance(1, list) - False
#isintance(1, tuple) - False
#isintance(1, dict) - False

#Exercicios
#Conversor de temperatura
#Faça um programa que converta temperatura de Celsius para Fahrenheit
#Fahrenheit = (Celsius * 9/5) + 32

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print("A temperatura em Fahrenheit é: ", temp_fahrenheit)

#Verificador de palindromo
#Faça um programa que verifique se uma palavra é um palindromo
#exemplo: 
#Digite uma palavra: arara
#A palavra é um palindromo

palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
    print("A palavra é um palindromo")
else:
    print("A palavra não é um palindromo")

#calculadora simples
#Faça um programa que calcule a soma, subtração, multiplicação e divisão de dois numeros
#exemplo: 
#Digite um numero: 10
#Digite outro numero: 2
#Soma: 12
#Subtração: 8
#Multiplicação: 20
#Divisão: 5

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
print("Soma: ", num1 + num2)
print("Subtração: ", num1 - num2)
print("Multiplicação: ", num1 * num2)
print("Divisão: ", num1 / num2)

#Classificador de numeros
#Faça um programa que classifique um numero como par ou impar
#exemplo: 
#Digite um numero: 10
#O numero é par

numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")

#Conversão de tipo com validação
#Faça um programa que converta uma string para inteiro
#exemplo: 
#Digite um numero: 10
#O numero é 10

numero = input("Digite um numero: ")
try:
    numero = int(numero)
    print("O numero é ", numero)
except ValueError:
    print("Numero invalido")


