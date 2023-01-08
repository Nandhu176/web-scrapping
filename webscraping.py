import requests
import re
from bs4 import BeautifulSoup
url="https://www.cricbuzz.com/"
data = requests.get(url).text
soup=BeautifulSoup(data,"html.parser")
print(soup.prettify())