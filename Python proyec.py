
from bs4 import BeautifulSoup
import requests
import pandas as pd


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

def get_partidos(year):