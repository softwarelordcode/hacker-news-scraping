'''
A simple web scraper to fetch titles and points from Hacker News.
'''

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com', timeout=5)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.athing.submission .title .titleline > a')
subtext = soup.select('.subtext')

for link, subtext in zip(links, subtext):
    points = subtext.find('span', class_='score').getText(
    ) if subtext.find('span', class_='score') else '0 points'
    print(link.getText(), points)
