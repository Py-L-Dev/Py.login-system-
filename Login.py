# Py.login-system-
I started yesterday, soo, don't expect things from me/comecei ontem... Então não espere muito sobre mim.

print("Bem vindo ao nosso site!")
nome = input("insira seu nome para começar por favor")
print("seja bem vindo!",nome,)
email = input("insira seu email para iniciar o registro!")
print("muito bem! agora crie uma senha para logar!")
input("insira sua senha")
print("otimo!")
input("insira novamente para confirmar-la!")
print("muito obrigado" ,nome)
try:
   idade = int(input("informe sua idade por gentileza!"))   
   if idade >= 16:
    print("otimo!")
    print("sua conta foi criada com sucesso!")
   else:
        print("infelizmente não é possivel autorizar seu cadastro! :(")
        
except ValueError:
        print("digite um numero, não uma letra")
        idade = int(input("informe sua idade"))
        if idade >= 16:
          print("otimo!", nome, "sua conta foi criada com sucesso!")
        else:
          print("não foi possivel concluir seu cadastro")

