import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


url = requests.get("https://www.imdb.com/chart/top/", headers=headers)

a = url.status_code 
print(a)

soup = BeautifulSoup(url.content)