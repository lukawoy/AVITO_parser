import logging
import os
import sys
import time
from http import HTTPStatus
from json import decoder

import requests
from dotenv import load_dotenv
from exceptions import EndpointError, ResponsCompositionError
from telebot import TeleBot, apihelper

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



TELEGRAM_TOKEN = os.getenv('TG_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TG_CHAT_ID')


RETRY_PERIOD = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'







def check_tokens():
    """Проверка доступности переменных окружения."""
    tokens = {
        'TELEGRAM_TOKEN': TELEGRAM_TOKEN,
        'TELEGRAM_CHAT_ID': TELEGRAM_CHAT_ID
    }
    unavailable_tokens = []
    for token_name, token in tokens.items():
        if token is None:
            unavailable_tokens.append(token_name)

    if unavailable_tokens:
        logger.critical(
            f'Переменные окружения {unavailable_tokens} недоступны.')
        sys.exit()


def send_message(bot, message):
    """Отправка сообщения в Telegram-чат."""
    try:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
        )
        logger.debug('Сообщение успешно отправлено.')
    except apihelper.ApiException as error:
        logger.exception(f'Ошибка отправки сообщения. {error}')


def get_api_answer(timestamp):
    """Запрос к API Практикум.Домашка."""
    pass





def parse_status(homework):
    """Получение информации о статусе домашней работы."""
    pass


def main():
    """Основная логика работы бота."""
    bot = TeleBot(token=TELEGRAM_TOKEN)
    timestamp = int(time.time()) - SECONDS_AGO
    last_message_error = ''

    while True:
        try:
            check_tokens()
            answer_api = get_api_answer(timestamp)
            check_response(answer_api)
            list_of_homeworks = answer_api.get('homeworks')
            if list_of_homeworks:
                message = parse_status(list_of_homeworks[NUMBER_HOMEWORK])
                send_message(bot, message)

            timestamp = answer_api.get('current_date', timestamp)
            last_message_error = ''

        except Exception as error:
            logger.exception(error)
            message = f'Сбой в работе программы: {error}'
            if message != last_message_error:
                send_message(bot, message)
                last_message_error = message

        time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    main()
