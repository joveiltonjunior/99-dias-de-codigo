#Password Generator Project
# nesse projeto vai ser gerado senhas aleatorias 
import random
# essas 3 linhas abaixos estão as letras simbolos e numeros que serão usado para criar a senha 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

''' Para começar, vai ser informada uma frase de bem-vindo para o usuário. Logo após, vai ser perguntado quantas
letras ele deseja usar na senha. Após informar o número de letras que ele quer na senha dele, vai ser perguntado o número de 
números e símbolos, cada número, vai ser armazenado em suas respectivas variáveis.  ''' 
print("Bem vindo ao gerador de senha!")
letras = int(input("Digite a quantidade de letras que você quer na sua senha: "))
simbolos = int(input("Digite a quantidade de simbolos que você quer na sua senha: "))
numeros = int(input("Digite a quantidade de numeros que você quer na sua senha: "))

#Eazy Level - Order not randomised:
# começando no modulo mais fácil foi criado uma variavel senha vazia 
senha = ''

'''Usando a função for, vai ser percorrido o range de 1 ao número que foi armazenado na variável "letras" (na função range
se você digitar de 1 , 10 ela vai mostrar de 1 a  9 por isso foi adicionado +1 ) após escolher o range, é preciso escolher as letras
que vai compor a senha. Para isso, foi utilizada a função random.choice() onde vai escolher aleatoriamente a quantidade de 
letras digitadas pelo usuário.'''
for i in range(1, letras+1):
    senha += random.choice(letters)

# no codigo a abixo foi feito o mesmo passo no codigo a cima 
for i in range(1, simbolos+1):
    senha+= random.choice(symbols)

# no codigo a abixo foi feito o mesmo passo no codigo a cima 
for i in range(1,numeros +1):
    senha+= random.choice(numbers)
print(senha)


#Hard Level - Order of characters randomised:
''' No módulo Hard, a senha após ser criada vai ser ordenada aleatoriamente. Para fazer isso, é preciso criar uma variável 
como a função de lista vazia vai ser feita, o mesmo processo feito acima. '''
senhadificil = []
senhafinal = ''
for i in range(1, letras+1):
    senhadificil += random.choice(letters)

for i in range(1, simbolos+1):
    senhadificil+= random.choice(symbols)

for i in range(1,numeros +1):
    senhadificil+= random.choice(numbers)

'''Até aqui, foi feito o mesmo processo feito no código anterior.'''
#abaixo vai ser misturado os caracters da senha 
random.shuffle(senhadificil)

''' Temos uma lista de caracteres, porém vamos transformar essa lista em uma 'palavra'. Para isso, vai ser utilizada a função for
onde nessa função vai ser percorrido a lista e cada vez que é percorrido a lista é adicionado na variável senha final formando
uma string que pode ser copiada e colada no login.'''
for i in senhadificil:
    senhafinal += i
print(senhafinal)
