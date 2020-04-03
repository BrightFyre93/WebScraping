import requests
from bs4 import BeautifulSoup
import pprint


final_list = []


def sort_stories_by_votes(list_of_links):
    return sorted(list_of_links, key=lambda k: k['votes'], reverse=True)


def create_custom__hn(link, subtext):
    hn = []
    for index, item in enumerate(link):
        title = item.getText()
        href = item.get('href', None)
        vote_temp = subtext[index].select('.score')
        if len(vote_temp):
            points = int(vote_temp[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


for page in range(10):
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = (soup.select('.storylink'))
    subtexts = (soup.select('.subtext'))
    final_list += (create_custom__hn(links, subtexts))
    final_list = sort_stories_by_votes(final_list)


pprint.pprint(final_list)