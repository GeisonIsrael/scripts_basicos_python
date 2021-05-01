# Calcular o preço de um produto com % de desconto para pagamento a vista e % de juros para pagamento parcelado.
print('x=' * 80)

# AQUI FICA O VALOR DO PRODUTO.
preco = float(input('Qual o valor do produto ?R$ '))

# VALOR DO DESCONTO OU ACREŚIMO.
porcentagem = float(input('Desconto ou acréscimo para este produto em (%) ? '))

# QUANTIDADE DE PARCELAS.
prestacoes = float(input('Número de parcelas: '))

# CALCULO PARA COMPRA A VISTA.
avista = preco - (preco * porcentagem / 100)

# CALCULO PARA COMPRA PARCELADA.
parcelado = preco + (preco * porcentagem / 100)

# VALOR POR PARCELAS.
parcelas = parcelado / prestacoes

# VALOR A VISTA.
print('O valor do produto é R$ {:.2f}, se o pagamento for a vista tera um desconto de {}% ficando o valor em R$ {:.2f}.'.format(preco, porcentagem, avista))

# VALOR PARCELADO.
print('Se o pagamento for parcelado tera um acréscimo {}% ficando o valor em R$ {:.2f}.'.format(porcentagem, parcelado))

# PARCELAS.
print('Com {:.0f} parcelas de {:.2f}.'.format(prestacoes, parcelas))

print('x=' * 80)
