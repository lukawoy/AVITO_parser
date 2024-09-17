LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\nЭто команда старт.',
    '/help': 'Это команда хелп.',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy'

}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Привет!\nЭто команда старт.',
    '/help': 'Это команда хелп.',
    '/info': 'Информация с сайта'
}

INLINE_LEXICON_RU: dict[str, str] = {
    'button_news_FG': 'Узнать последние новости от Frictional Games.',
    'button_news_FS': 'Узнать последние новости от Firefly Studios.',
}

GAMING_SITES_URLS: dict[str, tuple] = {
    'Frictional_Games_url': ('https://frictionalgames.com/', 'entry-title', 'entry-date published'),
    'Firefly_Studios_url': ('https://fireflyworlds.com/news/', 'blog-title', 'entry-date'),
}
