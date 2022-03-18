from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup


def get_info():
    data = []

    headers = {'User-Agent': 'Mozilla/5.0'}

    link = 'https://old.reddit.com/r/worldnews/'

    res = requests.get(link, headers=headers)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    reddit_post = soup.find_all('div', class_ = 'top-matter', limit=5)

    for post in reddit_post[:]:
        if len(post.p.a.attrs['href']) > 500:
            reddit_post.remove(post)
        else:
            continue
            
    for post in reddit_post:
        title = post.p.a.text
        link = post.p.a.attrs['href']
        data.append(title + "|" + link)
        data.split(", ")
    return data


print(get_info())