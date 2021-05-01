#valor do produto
preco = float(input('Qual o valor do produto?' ))

#Desconto que sera concedido.
desconto = float(input('Desconto (em %) para este produto: '))

#Transformando a porcentagem em número real.
desconto = desconto / 100

#Exibir tudo
print('Valor original: R$ ', preco)
print('Desconto ganho: R$ ', preco * desconto)
print('Valor com desconto: R$ ', preco * (1 - desconto))

      
