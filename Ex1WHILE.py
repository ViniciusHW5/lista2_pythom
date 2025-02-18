venda = input ('registre um produtos. Para cancelar o registro de um novo produto, basta apreter entre sem digitar nada: ')
vendas = []
#CRIE AQUI O PROGRAMA
while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar entre sem digitar nada: ')
print('Registros Finalizado. As vendas cadastradas foram: {}'.format(vendas))