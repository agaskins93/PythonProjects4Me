from os import supports_effective_ids

import requests as request # allows to download html
from bs4 import BeautifulSoup, ResultSet  # use data gathered to manilulate
import pprint

#ReAd terms and conditons and /robot.txt to see if dSata is able to be scrapped

def get_cetain_pages(page_list):
    hn_page_list = []
    counter = 0
    mega_links = []
    mega_subtext = []

    for page in page_list:
        if page == 1:
            res = request.get('https://news.ycombinator.com/news')
        else:
            res = request.get(f'https://news.ycombinator.com/news?p={page}')

        counter += 1
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')

        subtext = soup.select('.subtext')
        mega_links = mega_links + links
        mega_subtext = mega_subtext + subtext

        print(f'here at itereation {counter} with article: {create_custom_hn(links, subtext)}')


    return pprint.pprint(create_custom_hn(mega_links, mega_subtext))


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)




def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        votes = subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().split()[0])
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

#input the amount of page needed
#1 for page 1, #2 for page2 ....and so on

pprint.pprint(get_cetain_pages([1,2]))


