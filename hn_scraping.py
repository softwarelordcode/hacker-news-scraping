'''
A simple web scraper to fetch titles and points from Hacker News.
'''
import sys
import pprint
import time
import requests
from bs4 import BeautifulSoup

def sort_stories_by_points(hn):
    '''
    Sort the Hacker News stories by points in descending order.
    '''
    return sorted(hn, key=lambda x: x['points'], reverse=True)

def create_custom_hn(links, subtexts):
    '''
    Create a custom Hacker News object with title and points.
    '''
    hn = []
    for link, subtext in zip(links, subtexts):
        title = link.getText()
        href = link.get('href', None)
        points = int((subtext.find('span', class_='score').getText(
        ) if subtext.find('span', class_='score') else '0 points').removesuffix(' points'))

        if points > 99:
            hn.append({'title': title, 'href': href, 'points': points})

    return sort_stories_by_points(hn)

def main(args):
    '''
    Main function to scrape Hacker News.
    '''

    try:
        if len(args) > 1 and args[1] == '-p':
            pages_num = int(args[2])
        else:
            pages_num = 1
    except IndexError:
        print("Usage: python hn_scraping.py")
        print("or")
        print("Usage: python hn_scraping.py -p <pages>")
        print("Example: python hn_scraping.py -p 1")
        sys.exit(1)
    except ValueError:
        print("Invalid number of pages. Please provide a valid integer.")
        sys.exit(1)

    pages = [f'https://news.ycombinator.com/news?p={i}' for i in range(1, pages_num + 1)]

    custom_hn = []

    for page in pages:
        res = requests.get(page, timeout=5)
        time.sleep(2)

        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.athing.submission .title .titleline > a')
        subtexts = soup.select('.subtext')

        custom_hn.extend(create_custom_hn(links, subtexts))

    pprint.pp(custom_hn)

if __name__ == '__main__':
    main(sys.argv)
