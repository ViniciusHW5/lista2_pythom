#faça um programa que receba uma nota do aluno e se for SUPERIOR ou IGUAL a 7 (sete) apareça mensagem que ele está Aprovado, se for INFERIOR a 
#5 (cinco) ele está "não aprovado/ reprovado dirito" e se estiver entre 5 (cinco) e 7(sete) apareça mensagem "não aprovado/Recuperação".
num1 =  int(input('digite uma nota: '))
if num1 >=7:
    print("aluno aprovado:")
else:    
    if num1 >=5:
        print("não aprovado/Recuperação:")
    else:
         print("não aprovado/reprovado direto:")    
