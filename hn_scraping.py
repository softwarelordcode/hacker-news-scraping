'''
A simple web scraper to fetch titles and points from Hacker News.
'''

import requests
from bs4 import BeautifulSoup

def create_custom_hn(links, subtexts):
    '''
    Create a custom Hacker News object with title and points.
    '''
    hn = []
    for link, subtext in zip(links, subtexts):
        title = link.getText()
        href = link.get('href', None)
        points = (subtext.find('span', class_='score').getText(
        ) if subtext.find('span', class_='score') else '0 points').removesuffix(' points')
        hn.append({'title': title, 'href': href, 'points': points})
    return hn

def main():
    '''
    Main function to scrape Hacker News.
    '''
    res = requests.get('https://news.ycombinator.com', timeout=5)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.athing.submission .title .titleline > a')
    subtexts = soup.select('.subtext')

    custom_hn = create_custom_hn(links, subtexts)

    print(custom_hn)

if __name__ == '__main__':
    main()
