import requests
from bs4 import BeautifulSoup
from http import HTTPStatus

url = 'https://frictionalgames.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
news = soup.findAll('h3', class_='entry-title')


def get_list_news() -> str:
    status = page.status_code
    list_news = ''
    if status == HTTPStatus.OK:
        for data in news:
            list_news += f'{str(data.text)}\n'
        return list_news
    return f'The site FG has returned the status {status}.'
