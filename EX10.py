faturamento = input('Qual foi o faturamento da loja nessa mês? ')
custo = input('Qual foi o custo da loja nesse mês? ')
if faturamento!=''and custo!='':
#if faturamento and custo:    
    lucro = int(faturamento) - int(custo)
    print('O locro da loja foi de {} R$'.format(lucro))
else:
    print('Algum valor não foi fornecido')