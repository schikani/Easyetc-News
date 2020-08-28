import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Here we go to the Urls of first two pages of Hacker News
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Here we parse the html using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Here we select links and subtexts using .select
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

# Here we combine links and subtexts of first two pages
mega_links = links + links2
mega_subtext = subtext + subtext2

# Here we make an empty list to append later
hn = []


# This function is used to sort_stories_by_votes in ascending order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# This function is used to create custom links. Keeping more than 30 votes only in mind.
def create_custom_hn(links, subtext):
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        if href[-1] == "/":
            href = href[:-1]
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 30:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


# Dictionaries divided into the groups of 10 to be later used in the GUI version
dictionary = create_custom_hn(mega_links, mega_subtext)
d1to10 = dictionary[:10]
d11to20 = dictionary[10:20]
d21to30 = dictionary[20:30]

# Here we print in terminal the dictionaries containing our news with links and votes.
pprint(d1to10)
pprint(d11to20)
pprint(d21to30)
