import requests
from bs4 import BeautifulSoup
from http import HTTPStatus


# get_list_news()
# print(get_list_news())

def get_list_news(parse_data: tuple) -> str:
    url, class_entry_title, class_entry_date = parse_data
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.findAll('article')

    status = page.status_code
    list_news = ''
    if status == HTTPStatus.OK:
        for article in articles:
            data_news = article.find_all(attrs={'class': class_entry_title})
            data_published = article.find_all(
                attrs={'class': class_entry_date})
            for news, pub_date in zip(data_news, data_published):
                list_news += f'{pub_date.text}\n{news.text}\n{news.find("a").get("href")}\n'
                list_news += '-' * 100 + '\n'
        return list_news
    return f'The site {url} has returned the status {status}.'
