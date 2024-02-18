from random import randint
from time import sleep
from operator import itemgetter

jogo = {'David': randint(1,6),
        'Neymar': randint(1,6),
        'Aline': randint(1,6),
        'Edna': randint(1,6)}

print('== Resultado do jogo == ')

for k , v in jogo.items():
    print(f'{k} tirou {v} no dado')

raking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('-='*30)

for i, v in enumerate(raking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

