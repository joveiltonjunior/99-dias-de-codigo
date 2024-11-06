forca = [
    r'''
      _______
     |/      |
     |      
     |      
     |       
     |       
     |
    _|___      ''',
    r'''    
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
    _|___      ''',
    r'''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___       ''',
    r'''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
    _|___      ''',
    r'''  
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___        ''',
    r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
    _|___          ''',
    
    r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___      ''',
    r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___           '''
]


'''Na primeira parte do código, foi importada a função random para escolher uma palavra aleatória da lista, foi criada uma nova
Variável palvra_secreta para armazenar a palavra que foi aleatoriamente escolhida, também foi criada uma variável para armazenar
as letras acertadas e a quantidade de vidas que o usuário tem.'''
import random

lista_palavra = ['caderno', 'caneta', 'papel']
palavra_secreta = random.choice(lista_palavra)
letras_acertadas = ''
vidas = 0 

'''Para criar o jogo, foi preciso usar a função while onde ela vai ficar rodando enquanto o usuário tiver uma quantidade de 
vidas ou acertas as letras, quando o usuário atingir o número máximo de erro, vai chegar na função break e terminar o jogo ou
o usuário digita todas as letras corretas antes de acabar as suas tentativas.'''

while True:
    # O usuário vai digitar uma letra, que será convertida para minúscula
    letras = input('Digite uma letra: ').lower()

    # Verifica se a letra já foi acertada antes de adicionar
    if letras in palavra_secreta and letras not in letras_acertadas:
        letras_acertadas += letras

    # Nessa variável, vai ser armazenada cada letra correta para formar a palavra secreta.
    palavra_formada = ''
    '''Nesse for vai ser analisado a letra digita confere com as letras que estão na variável palavra_secreta
    e vai checar essa lógica usando o if a baixo. Caso a letra esteja na palavra secreta, ela vai ser armazenada na variável 
    palavra_formada caso não esteja vai ser mostrad "_"  ''' 
    for letra in palavra_secreta:        
        if letra in letras_acertadas:
            palavra_formada += letra
            print(vidas)
        else:
            palavra_formada += '_'
    '''Caso a letra digitada pelo usuário não esteja na palavra secreta, vai ser utilizado o if abaixo e cada vez que for digitado
    uma letra que não tem na palavra secreta vai ser adicionado 1 o usuário tem 8 possibilidades de errar, cada vez que ele errar
    vai ser mostrado o boneco sendo enforcado.'''
    if letras not in palavra_secreta:
        vidas += 1
        print (forca[vidas])
        if vidas == 8:
            print ('Você não acertou a palvra: GAME OVER ')
            break
    print("Vidas perdidas :", vidas)  
    
    ''' Por fim, caso o usuário digite tudo certo, vai ser mostrada a mensagem e o jogo acaba.'''
    if palavra_formada == palavra_secreta:
        print("Parabéns! Você descobriu a palavra secreta:", palavra_secreta)
        break