import pprint

import requests
import time



API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6182115604:AAFHordDBdMYAMAe4H3ImY-S8DaZlI6EDzE'
offset: int = -2
timeout: int = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}&allowed_updates=message').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()
            date_message = updates['result'][0]['message']['date']
        pprint.pprint(updates)
        pprint.pprint(time.ctime(date_message))

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {round((end_time - start_time))}')