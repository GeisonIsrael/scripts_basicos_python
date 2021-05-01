# BASEADO NOS EXECÍCIOS 12 E 13.
# Calcular o preço de um produto com 10% de desconto para pagamento a vista e 10% de juros para pagamento parcelado.
preco = float(input('Qual o valor do produto ?R$ '))
avista = preco - (preco * 10 / 100)
parcelado = preco + (preco * 10 / 100)
parcelas = parcelado / 12
print('O valor do produto é R$ {:.2f}, se o pagamento for a vista tera um desconto de 10% ficando o valor em R$ {:.2f},'.format(preco, avista))
print('se o pagamento for parcelado tera um acréscimo 10% ficando o valor em R$ {:.2f}, com 12 parcelas de R$ {:.2f}'.format(parcelado, parcelas))

