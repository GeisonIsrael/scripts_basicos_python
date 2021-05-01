print('x=' * 40)
preco = float(input('Valor do produto:R$ '))
print()

dec = float(input('Valor do desconto em (%): '))
print()

avista = preco - (preco * dec / 100)
print()

parcelado = float(input('Valor do acréscimo (%): '))
print()

noValor = preco + (preco * parcelado / 100)
print()

parcelas = float(input('Número de parcelas: '))
print()

valParcelas = noValor / parcelas

print('O valor do produto é R$ {:.2f}, com desconto de {:.0f}% fica por R$ {:.2f}.'.format(preco, dec, avista))
print()
print('O valor do produto com {:.0f}% de acréscimo sera de R$ {:.2f}.'.format(parcelado, noValor))
print()
print('Em {:.0f} parcelas de R$ {:.2f}.'.format(parcelas, valParcelas))
print('x=' * 40)
