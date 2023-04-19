from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import tokens
from aiogram import F


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = tokens.tokens['tg']

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

#@dp.message(F.voice)
#async def send_voice_echo(message: Message):
#    await message.reply_voice(message.voice.file_id)
#
## Этот хэндлер будет срабатывать на отправку боту фото
#@dp.message(F.photo)
#async def send_photo_echo(message: Message):
#    print(message)
#    await message.reply_photo(message.photo[0].file_id)
#
#@dp.message(F.sticker)
#async def send_sticker_echo(message: Message):
#    await message.reply_sticker(message.sticker.file_id)
## Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
## кроме команд "/start" и "/help"
#
#@dp.message()
#async def send_echo(message: Message):
#    await message.reply(text=message.text)

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(message.chat.id)
    except:
        await message.answer('Упс')

if __name__ == '__main__':
    dp.run_polling(bot)