from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from randomAnimal import getRandomAnimal
from jokes import getRandomJoke
from address import get_address_from_coords
from keyboards import KEYBOARD, INLINE_KB_AHAHA
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def start_bot(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! Я бот, зацени, чё могу")
    await message.answer("Чё хочешь то от жизни??", reply_markup=KEYBOARD)

# пока не работает
# @dp.message_handler(text = 'загадай число')
# async def process_guess_int_command(message: types.Message):
#     await message.reply('Блин, этому пока что только учусь', reply_markup=inline_kb2)
#     #await bot.send_message(message.from_user.id, guessInt(), reply_markup=inline_kb2)

def get_address_keyboard():
    get_keyboard = types.ReplyKeyboardMarkup(
        input_field_placeholder="Тыкни",
        one_time_keyboard=True
    )
    button = types.KeyboardButton(
        "тык сюда",
        request_location=True,
        one_time_keyboard = True)
    get_keyboard.add(button)
    return get_keyboard

@dp.message_handler(content_types=["location"])
async def process_address_command(message: types.Location):
    # вытаскиваем из геопозиции долготу и ширину
    current_position = (message.location.longitude, message.location.latitude)
    lon = message.location.longitude
    lat = message.location.latitude
    # создаем строку в виде ДОЛГОТА,ШИРИНА
    coords = f"{current_position[0]},{current_position[1]}"

    await bot.send_message(message.from_user.id, get_address_from_coords(coords, lon, lat), reply_markup=KEYBOARD)

@dp.message_handler(text = 'где я')
async def process_locate_me_command(message: types.Message):
    reply = "Тыкни, чтобы зашарить своё местоположение"
    await message.answer(reply, reply_markup=get_address_keyboard())

@dp.message_handler(text = 'расскажи шутку')
async def process_get_joke_command(message: types.Message):
    await bot.send_message(message.from_user.id, getRandomJoke(), reply_markup=INLINE_KB_AHAHA)

@dp.message_handler(text = 'животных знаешь каких-нибудь?')
async def process_get_word_command(message: types.Message):
    await bot.send_message(message.from_user.id, getRandomAnimal())

@dp.message_handler(text = 'о боте')
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "https://github.com/Alexandr100RB")

@dp.callback_query_handler(text="button1")
async def send_answer(message: types.Message):
    await bot.send_message(message.from_user.id, 'ахахахаха в карман не положишь, лучше скинь денег на карту')

@dp.callback_query_handler(text="button2")
async def send_answer(message: types.Message):
    await bot.send_message(message.from_user.id, 'что есть, то есть')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
