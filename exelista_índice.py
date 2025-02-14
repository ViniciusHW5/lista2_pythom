produtos = ['tv','celular','tablet','mouse','teclado','geladeira','forno']
estoque = [100,150,250,70,80 ]
produto = input ('Insira o nome do produto e letra minuscula ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('temos {} unidades de {} no estoque'.format(qtde_estoque,produto))
else:
    print('{} não existe no estoque'.format(produto))


#produtos = ['tv','celular','mouse','teclado','tablet']
#vendas = [1000, 1500, 350, 270, 900 ]
#print('as vendas de {} foram de {}'.format(produtos[1],vendas[2]))
#produtos = ['tv','celular','mouse','teclado','tablet']
#i= produtos.index('mouse')
#print('O valor de i é '+ str(i))
#print('O produto da posição i é '+ str(produtos[i]))

#O valor de i é 2
#o valor da posição i é mouse