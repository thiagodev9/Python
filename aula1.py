#tudo em python é um objeto
#funções são blocos de codigo que executam uma tarefa   
#constantes são valores que não mudam
#variaveis são valores que mudam    
#variavel secreta __variavel    

print("Hello World" )

#Pede usuario digitar o nome e mostra na tela
input ("Digite seu nome: "  )

# Crie um programa que usuario digita o nome e retorna numero de letras
#variavel é um espaco na memoria que guarda um valor
nome = input ("Digite novamente seu nome: "  )   

#len() conta o numero de caracteres
nome = print (len(nome ))

# Crie um programa que soma dois numeros
#int() converte o valor para inteiro
#float() converte o valor para float
#str() converte o valor para string
#type() mostra o tipo da variavel
#true e false são valores booleanos
n1= int(input("Digite um numero: "))
n2= int(input("Digite outro numero: "))
print ("SOMA", n1 + n2) 


# Desafios
#Faça um programa digita nome, salario, porcentagem do bonus e valor do bonus +1000
#mostra na tela uma mensagem com o nome, salario, porcentagem do bonus e valor do bonus 
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
porcentagem_bonus = float(input("Digite a porcentagem do bonus: "))
valor_bonus = salario * (porcentagem_bonus / 100)
print("Nome: ", nome)
print("Salario: ", salario)
print("Porcentagem do bonus: ", porcentagem_bonus)
print("Valor do bonus: ", valor_bonus)
