"""
pip install requests
pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions?tab=Frequent'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')

    if titulo:
        if data:
            print(data.text, titulo.text, votos.text, sep='\t')
        else:
            print("None", titulo.text, votos.text, sep='\t')
