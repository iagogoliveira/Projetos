import sys

def senha ():
  senUser = int(input('Senha: '))
  return senUser

codUser = int(input('Insira o codigo de usuario: '))
if codUser != 1234:
    print('Numero de usuario invalido!')
    sys.exit()
else:
    if senha() != 9999:
        print('Senha invalida')
        op = int(input('1 - Tentar novamente  2 - Finalizar programa : '))
        if op == 2:
            sys.exit()
        elif op == 1:
            senha()
        else:
            print('Opcao invalida')
            sys.exit()
    else:
        print('Acesso Permitido')



