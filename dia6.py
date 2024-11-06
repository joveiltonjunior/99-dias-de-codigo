'''Usando um site da internet, foi gerado um CPF fictício e foi armazenado na variável cpf, foi feito um fatiamento da strings
dos nove primeiros dígitos e foi armazenado na variável cpf_novedigito, depois declarado uma variavel contador1 onde ela recebeu
o valor 11 '''
cpf = '74682489070'
cpf_novedigito = cpf[:9]
contador1 = 11

''' Foi feito um for para fazer um desempacotamento da lista cpf_novedigito no mesmo for foi feita a contagem de 10 a 2 
com isso, vai ser multiplicado o valor do primeiro número da variavel cpf_novedigito com o primeiro valor do contador, 
vai ser seguida essa lógica até o último número, esses números serão multiplicados, somados e armazenados na variável valor1.'''
valor1 = 0
for numero in cpf_novedigito:
    contador1 -= 1
    valor1 +=(int(numero) * contador1) 

'''Após o último passo, o valor1 vai ser multiplicado por 10 e dividido por 11, o resto dessa divisão vai ser o último digito 
do CPF, caso o valor seja maior que 9, o último dígito vai ser substituído por 0 caso o valor obtido no cálculo  esteja entre 0 e 9 
vai ser mantido o número obtido no calculo.'''
digito1 = (valor1*10) % 11
digito1 = digito1 if digito1 <=9 else 0

#Para o último dígito do CPF é feito o mesmo cálculo, o diferente é que tem que ser adicionado o valor encontrado anteriormente no CPF. 
cpf_dez_digito = cpf_novedigito + str(digito1)
contador2 = 11 

valor2 = 0
for numero1 in cpf_dez_digito:
    valor2 += (int(numero1)* contador2)
    contador2 -=1

digito2 = (valor2 *10) %11
digito2 = digito2 if digito2 <= 9 else 0

'''Por fim, é necessário checar se o número do CPF calculado bate com o CPF informado. Para isso, foi feito um if onde e 
Confirmada o valor informado comparando com o valor calculado, caso sejam iguais, vai informar ao usuário que o CPF é valido 
caso não seja igual, será informado que o CPF é inválido. '''
cpf_gerado = f'{cpf_novedigito}{digito1}{digito2}'

if cpf_gerado == cpf:
    print(f'O CPF enviado {cpf} é valido')
else:
    print(f'O cpf enviado {cpf} é invalido')