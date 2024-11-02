tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

escolha = input("Digite pedra, papel ou tisoura: ")
if escolha == 'pedra':
    print(pedra)
elif escolha == 'papel':
    print(papel)
else:
    print(tesoura)
lista =[pedra, papel, tesoura]
listarandom =random.choice(lista)
print(listarandom)

if escolha == 'pedra' and listarandom == tesoura:
    print("voce perdeu")
elif escolha == 'pedra' and listarandom == pedra:
    print ("Empate")
elif escolha == 'pedra' and listarandom == papel:
    print('Você ganhou')
elif escolha == 'tesoura' and listarandom == tesoura:
    print ("Empate")
elif escolha == 'tesoura' and listarandom == papel:
    print('Você ganhou')
elif escolha == 'tesoura' and listarandom == pedra:
    print ("voce perdeu")
elif escolha == 'papel' and listarandom == papel:
    print ("Empate")
elif escolha == 'papel' and listarandom == pedra:
    print('Você ganhou')
elif escolha == 'papel' and listarandom == tesoura:
    print ("voce perdeu")