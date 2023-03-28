import os
print ('Programa Iniciado')

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
filho = os.fork()

#pid do pai é diferente de zero, logo ele pega o arquivo do filho e exibe em tela
if(filho > 0):
    os.wait() #se não lançar o wait os concorrem juntos
    print('Sou o pai e vou imprimir o que meu filho calculou:')
    with open('resultados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

#pid do filho é zero, então ele calcula tudo
if(filho == 0):
   with open('resultados.txt', 'w') as arquivo:
       for i in range(n1, n2+1):
           if i % 2 == 0:
                arquivo.write(str(i) + ' ')
   print('Sou o filho e já calculei tudo!')
