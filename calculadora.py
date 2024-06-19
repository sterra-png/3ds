print('adição +')
print('subtração -')
print('mutiplicação *')
print('divisão /')



o1 = input('qual a operaçao aritimetica')
n1 = float(input('digite um valor !'))
n2 = float(input('digite outro valor !'))

lista_operadores = ['+','-','*','/']

if n1 > 0 and n2 > 0 and o1 in lista_operadores:


    match o1 :
        case '+':
            print(n1 + n2)

        case '-':
            print(n1 - n2)

        case '*' :
            print(n1 * n2)

        case '/' :
            print(n1 / n2)
else:
    print('erro')