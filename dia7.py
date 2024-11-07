# Esse programa vai codificar suas mensagens.

letras =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Para começar o programa, foi feita uma função onde nela vai estar o código.
def funcao(a, b, c):
    texto_codificado = ''# Variável onde vai ser armazenado o texto codificado.
    for letra in texto:# Esse for vai fazer um loop pelas letras do texto digitado.
        if direcao == 'codificar':# Nesse if vai ser checado se o usuário precisa codificar ou descodificar a mensagem.
            letras_alteradas = letras.index(letra) + desvio# as letras das palavras digitadas vão ser checadas com o índice da
            #lista letras Após ser checada, o índice vai ser somado ao número digitado no desvio (onde vai ser codificado) e com 
            #sso vai retornar uma nova letra 
            letras_alteradas %= len(letras)# Caso a palavra tenha uma letra z e o usuário digite 3 no desvio, o programa vai
            #retornar o índex erro para corrigir isso foi adicionado essa linha. 
            texto_codificado += letras[letras_alteradas] # Vai ser armazenado todas as letras nessa variável.
        else:# Nesse else foi feito o mesmo explicado anteriormente, o diferente e ao invés de
            # somar vai ser subtraído, nesse caso aqui vai ser feita a descodificação do texto codificado.
            letras_alteradas = letras.index(letra) - desvio
            letras_alteradas %= len(letras)
            texto_codificado += letras[letras_alteradas]
        
        
    print(f'Aqui esta a sua mensagem {direcao} {texto_codificado}')

while True:# Enquanto o usuário não digitar n o programa vai continuar rodando.
    direcao = input('Digite se você quer "codificar" ou "descodificar": ').lower()
    texto = input('Digite o texto: ').lower()
    desvio = int(input('Digite o número de desvio que você deseja: '))
    
    funcao (a= direcao, b= texto, c= desvio)

    continuar = input('Digite s para continuar e n para sair ').lower
    if continuar == 'n':
        break