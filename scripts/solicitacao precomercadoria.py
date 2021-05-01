preco = float(input('Digite o preço: '))
perc = float(input('Digite uma porcentagem de desconto: '))
novoPreco = preco - (preco * perc / 100)
desconto = preco - novoPreco
print('Preço com desconto: R$ {}'.format(novoPreco))
print('Desconto de : R$ {}'.format(desconto))
