'''
A simple web scraper to fetch titles and points from Hacker News.
'''

import requests
from bs4 import BeautifulSoup

def create_custom_hn(links, subtexts):
    '''
    Create a custom Hacker News object with title and points.
    '''
    for link, subtext in zip(links, subtexts):
        points = subtext.find('span', class_='score').getText(
        ) if subtext.find('span', class_='score') else '0 points'
        print(link.getText(), points)

def main():
    '''
    Main function to scrape Hacker News.
    '''
    res = requests.get('https://news.ycombinator.com', timeout=5)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.athing.submission .title .titleline > a')
    subtexts = soup.select('.subtext')

    create_custom_hn(links, subtexts)

if __name__ == '__main__':
    main()
