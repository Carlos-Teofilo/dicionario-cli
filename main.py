import sys

from bs4 import BeautifulSoup
import requests

URL = 'https://www.dicio.com.br/' + sys.argv[1]

r = requests.get(URL)
r.raise_for_status()

soup = BeautifulSoup(r.text, 'html.parser')
titulo_sig = soup.select_one('.tit-significado')
significado = soup.select_one('.significado').select('span')
subs = significado.pop(0)

print(titulo_sig.text, f'({subs.text})')
print('----------------------------------------------------------------------')
for tag in significado:
    print(tag.text)
    print('----------------------------------------------------------------------')
