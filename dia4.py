"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
 - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
 - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta. 
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
''' Fazer uma variável onde vai ser armazenada a palavra secreta, criar uma variável para armazenar as letras digitadas pelo usuário
e outra para armazenar o número de tentativas.''' 
palavra = 'perfume'
letras_acertadas = ''
contador =0
'''Utilizando a função while para True para verificar se o usuário conseguiu digitar a palavra secreta quando o usuário digitou a
todas as letras da palavra secreta, o while vai se tornar False e o jogo termina.'''
while True:
#Para começar o jogo, o usuário tem que digitar uma letra. Caso o usuário digite mais de uma letra, o programa vai informar que e 
#permitido digitar somente uma letra, a função len vai contar quantas letras foram digitadas.

    letra_digitada = input('Digite uma letra: ')
    contador +=1
    # Verifica se mais de uma letra foi digitada
    if len(letra_digitada) > 1:
        print("Você digitou mais de uma letra.")
        continue

# Nesse if vai ser checada se a letra digitada está na palavra. Caso esteja, a letra digitada vai ser adicionada na variável
# letras_acertadas e essa variável vai acumulando todas as letras acertadas.
    if letra_digitada in palavra:
        letras_acertadas += letra_digitada

#Nessa parte do código foi declarada uma nova variável onde vai ser armazenado todas as letras digitadas. Cada letra vai ser
#checada com variável palavra Caso a letra esteja na variável palavra ela será armazenada na variável palavra_formada, quando o
# usuário acertar a letra, ela vai ser mostrada na tela e as demais letras estarão com um * como está declarado no else. 
    palavra_formada = ''
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(f"Palavra formada: {palavra_formada}")
# Depois que o usuário digitou todas as letras certas vai aparecer uma mensagem de parabéns e uma mensagem informado quantas 
# tentativas ele tentativas foram feitas  
    # Condição de vitória
    if palavra_formada == palavra:
        print("Parabéns! Você acertou a palavra!")
        print(f'o número de tentativas foi : {contador}')
        break
