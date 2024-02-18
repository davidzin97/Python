times = ('Flamengo','Palmeiras','São Paulo','Santos','Corinthians','Fluminense','Botafogo','Vasco da Gama',
'Grêmio','Internacional','Atlético Mineiro','Cruzeiro','Atlético Paranaense','Bahia','Sport Recife','Ceará','Fortaleza','Chapecoense','Avaí','Goiás' )

print(35*'=-=')
print(sorted(times))
print(35*'=-=')

print(35*'=-=')
libertadores = times[0:6]
print('Os 5 times que vão pra libertadores são: {}'.format(libertadores))
print(35*'=-=')

rebaixamento = times[16:20]
print('Os 4 times que vão ser rebaixados são: {}'.format(rebaixamento))

posicao = times.index("Chapecoense")
print('A Chapeconse esta na posição',posicao)

print(35*'=-=')
print('FIM DO PROGAMA')