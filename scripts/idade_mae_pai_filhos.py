#Programa que define idade dos pais e a idade que eles tinham quando os filhos nasceram.
anoAtual = int(input('Ano atual: '))
nascMae = int(input('Ano de nascimento Mãe: '))
nascPai = int(input('Ano de nascimento Pai: '))
idFilho = int(input('Idade do filho: '))
idMae = anoAtual - nascMae
idPai = anoAtual - nascPai
idMaepart = idMae - idFilho
idPaipart = idPai - idFilho
print('A idade da mãe é {} anos e a idade do pai é {} anos, a mãe tinha {} anos no nascimento do filho(a) e o pai tinha {} anos.'.format(idMae, idPai, idMaepart, idPaipart))
