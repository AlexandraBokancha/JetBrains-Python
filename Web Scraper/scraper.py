import os
import requests
import string
from bs4 import BeautifulSoup

number_of_pages = int(input())
type_of_article = input()

for i in range(1, number_of_pages + 1):
    url = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    current_dir = os.getcwd()
    directory_name = 'Page_' + str(i)
    path = os.path.join(current_dir, directory_name)
    os.mkdir(path)

    for article in articles:
        article_type = article.find('span', {'class': 'c-meta__type'}).text
        if type_of_article == article_type:
            article_title = article.find('a', {'data-track-action': 'view article'}).text.strip()
            new_url = 'https://www.nature.com' + article.find('a').get('href')
            r2 = requests.get(new_url)
            new_soup = BeautifulSoup(r2.content, 'html.parser')
            title = new_soup.find('h1', {'class': 'c-article-magazine-title'}).text.strip().translate(
                str.maketrans('', '', string.punctuation)).replace(' ', '_') + '.txt'
            description = new_soup.find('p', {'class': 'article__teaser'}).text.strip()
            with open(os.path.join(path, title), 'w', encoding='utf-8') as f:
                f.write(description)
