
from bs4 import BeautifulSoup
import requests
import pandas as pd


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

def get_partidos(year):
    website = f'https://en.m.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    partidos = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for partido in partidos:
        home.append(partido.find('th', class_='fhome').get_text())
        score.append(partido.find('th', class_='fscore').get_text())
        away.append(partido.find('th', class_='faway').get_text())

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

#mundiales_wordcup_data
mundial =  [get_partidos(year) for year in years]
df_mundiales = pd.concat(mundial, ignore_index=True)
df_mundiales.to_csv('mundiales_wordcup_data', index=False)


df_fixture = get_partidos('2022')
df_fixture.to_csv('mundiales_wordcup_data-fixture', index=False)









