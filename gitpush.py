import os
while True:
    print('//////////////////////////////////////////////////////')
    print(' ')
    inputUsuario = int(input('Qual ação é desejada? 1 - Git Status  2 - Git add/commit/push 3 - Visualizar arquivos no repositorio  4 - Git rm' ))
    if inputUsuario == 1:
      print(os.system("git status"))
    elif inputUsuario == 2:  
          nomeArquivo = str(input('Insira o nome do arquivo/pasta desejado: '))
          commit = str(input('Insira o comentario do commit: '))

          os.system('git add '+ nomeArquivo)
          os.system('git commit -m '+ commit )
          os.system('git push')
    elif inputUsuario == 3:
          os.system('dir')
    elif inputUsuario == 4:
          nomeArquivoRemov = str(input('Insira o nome do arquivo/pasta desejado para remoção: '))
          commit = str(input('Insira o comentario do commit: '))
          os.system('git rm -r ' + nomeArquivoRemov)
          os.system('git commit -m '+ commit )
          os.system('git push')
    else:
        print('Ação inválida!')    

        