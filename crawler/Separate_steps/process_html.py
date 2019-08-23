# Gets all hyperlinks from the website
import json, re
from bs4 import BeautifulSoup

html = None
with open('response.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
all_href = soup.find_all('a')

href_list = []
for href in all_href:
    href_str = href.string
    if re.match(r'\n', href_str):
        href_str = re.split(r'\n', href_str)[-1]
    href_list.append({'Name': href_str, 'href': href['href']})

with open('all_href.txt', 'w') as f:
    f.write(json.dumps(href_list))