import requests
import time

API_BOT = 'https://api.telegram.org/bot'
TOKEN_BOT = '6182115604:AAFHordDBdMYAMAe4H3ImY-S8DaZlI6EDzE'
API_CAT = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'Здесь должен была быть картинка, но что-то пошло не так'
SUCCESS_TEXT = 'это конечно хорошо, но как насчет котика?'

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str
user_text: str

while counter < 100:
    print('attempt=', counter)
    updates = requests.get(f'{API_BOT}{TOKEN_BOT}/getUpdates?offset={offset + 1}').json()

    for result in updates['result']:
        offset = result['update_id']
        chat_id = result['message']['from']['id']
        user_text = result['message']['text']

        cat_response = requests.get(f'{API_CAT}')

        if cat_response.status_code == 200:
            cat_link = cat_response.json()[0]['url']
            requests.get(f'{API_BOT}{TOKEN_BOT}/sendMessage?chat_id={chat_id}&text="{user_text}" {SUCCESS_TEXT}')
            requests.get(f'{API_BOT}{TOKEN_BOT}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
        else:
            requests.get(f'{API_BOT}{TOKEN_BOT}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1

