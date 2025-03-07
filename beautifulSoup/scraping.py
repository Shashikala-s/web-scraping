import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

table=soup.find('table', class_='wikitable sortable')
data=soup.findAll('table')[1].findAll('th')
print(table)
# <table class="wikitable sortable sticky-header-multi sort-under"
# <table class="wikitable sortable plainrowheaders"
