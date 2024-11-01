
print ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print ("Bem-vindo à ilha do tesouro, a sua missão é encontrar o tesouro: ")
bifurcacao = input('Você está à procura do tesouro e se encontra em uma bifurcação. Você vai pela direita ou pela esquerda. ')
if bifurcacao.lower() =='direita':
    print("Você caiu em um buraco GAME OVER")
elif bifurcacao.lower() == 'esquerda':
    print('Você chegou em um lago.')
    barco = input('você espera por um barco ou nadar. Digite: espera ou nadar. ')
    if barco.lower() == 'nadar':
        print('Você foi atacado por piranhas assassinas. GAME OVER')
    elif barco.lower() == 'espera' :
        print('Você atravessou o rio: ')    
        porta = input ("Ao sair do barco, você encontra três portas: azul, amarela, vermelha, qual você abre? ")
        if porta.lower() == 'azul':
            print ('você foi comido por um urso: GAME OVER')
        elif porta.lower() == 'vermelho':
            print(" Várias cobras mortais te atacaram. Você morreu GAME OVER")
        elif porta.lower() == "amarela":
            print ( "Você achou o tesouro")
        else :
            print ( "você so pode escolher entre azul, amarela, vermelha: ")
    else:
        print ("você so pode escolher entre nadar ou esperar: ")
else:
    print( "você so pode escolher entre direita ou esquerda: ")
