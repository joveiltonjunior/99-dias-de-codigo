# Foi criada 4 funções, cada uma foi utilizada uma operação matemática.
def soma (n1, n2):
    return n1 + n2

def subtracao (n1, n2):
    return n1- n2

def multiplicacao (n1, n2):
    return n1 * n2

def divisao (n1, n2):
    return n1/ n2 

operacoes = {
     '+': soma,
      '-' :subtracao,
      '*': multiplicacao,
      '/':divisao
}# Dicionário para armazenar cada operação. Quando o usuário digitar o símbolo, vai ser chamada a função atribuída ao símbolo.

print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|    ''')

def calculadora() : # Função calculadora 
    continuar = True # Caso a variável se torne falsa, o usuário sai do loop.
    primeiro_numero = float(input('Digite o primeiro numero: '))
    while continuar:    
        for simbolo in operacoes:# vai imprimir os símbolos das 4 operações. 
            print (simbolo)
        operador = input('digite qual operação deseja fazer: ')
        segundo_numero = float(input('Digite o segundo numero: '))

        resposta = operacoes[operador](primeiro_numero, segundo_numero)# Vai ser feito o cálculo e o resultado vai ser armazenado nessa variável.
        print(f'{primeiro_numero} {operador} {segundo_numero} {resposta}')# vai ser mostrado a operação e o resultado
        
        '''Caso o usuário deseja fazer mais uma operação, será perguntado se deseja utilizar o resultado, caso a resposta seja sim
         o primeiro número vai ser a resposta e o segundo número o usuário vai digitar e escolher o operador. '''
        segunda_opereracao = input (f'Deseja utilizar o resultado da operação anterior {resposta}: [s] para utilizar e [n] para não utilizar: ')
        if segunda_opereracao == 's':
            primeiro_numero = resposta
        # Usuário não vai utilizar a resposta para fazer outro cálculo, nesse caso terá que digitar os 2 números e a operação
        else:
            continuar = False
            print('\n'*20)
            calculadora()
        # Essa opção é para o usuário encerrar o programa.
        sair = input("deseja sair: [s] sim, [n] não: ")
        if sair == 's':
            break

calculadora()# Foi chamada a função para iniciar a calculadora.