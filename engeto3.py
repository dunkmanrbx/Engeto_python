

#2) Uprav kod, tak aby se dal pouzit i v nejakem rozsirenem konceptu.
from typing import SupportsFloat


sklad = ['banan', 'okurka', 'cibule', 'mango']
ovoce = []
zelenina = []
ovoce.append(sklad[0])
ovoce.append(sklad[3])
zelenina.append(sklad[1])
zelenina.append(sklad[2])
muj_kosik = input('Co chci koupit: ')
if muj_kosik in ovoce:
    print('Nakoupil jsi ovoce')
elif muj_kosik in zelenina:
    print('Nakoupil jsi zeleninu')
else:
    print('Nemame na sklade')
