vendas = [100,50,80,190,200,210,45,37,99,105,130,111,44,25,67,93,157,25]
meta = 100
qtde_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta +=1
qtde_funionarios = len(vendas)
print('O percentual de pessoas que bateram a meta foi de {:.1%}'.format (qtde_bateu_meta/qtde_funionarios))