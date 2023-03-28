numero1= float(input('primeiro numero: '))
numero2= float(input('segundo numero: '))

print('1-soma')
print('2-subtração')
print('3-multipiplicação')
print('4-divisão')

opcao= int(input('escolha uma opção: '))

if opcao ==1 :
    resultado= numero1 + numero2
    print(f'a soma de {numero1} e {numero2} é {resultado}')
elif opcao ==2:
    resultado= numero1-numero2
    print(f'a subtração de {numero1} e {numero2} é {resultado}')
elif opcao== 3:
    resultado= numero1 * numero2
    print(f'a multiplicação de {numero1} e {numero2} é {resultado}')
elif opcao== 4:
    if numero2 != 0:
     resultado= numero1 / numero2
     print(f'a a divisão de {numero1} e {numero2} é {resultado}')
    else:
        print('não é possivel fazer uma divisão por zero')
else:
    print('opção invalida! ')