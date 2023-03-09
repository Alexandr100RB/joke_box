from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from randomAnimal import getRandomAnimal, words
from jokes import jokes, getRandomJoke
from randomInt import guessInt
from address import get_address_from_coords

from config import TOKEN

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, update

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start_bot(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! Я бот, зацени, чё могу")
    kb = [
            [
                # types.KeyboardButton(text="загадай число"),
                types.KeyboardButton(text="где я"),
                types.KeyboardButton(text="расскажи шутку")],
            [
                types.KeyboardButton(text="животных знаешь каких-нибудь?")
                ],
            [
                types.KeyboardButton(text="памагити!!!!!")
            ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ну выбери уже что-нибудь"
    )

    await message.answer("Чё хочешь то от жизни??", reply_markup=keyboard)


@dp.message_handler(text = 'загадай число')
async def process_guess_int_command(message: types.Message):
    #await message.reply('Блин, этому пока что только учусь', reply_markup=inline_kb2)
    await bot.send_message(message.from_user.id, guessInt(), reply_markup=inline_kb2)

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Поделиться местоположением", request_location=True)
    keyboard.add(button)
    # получаем обьект сообщения (локации)
    message = update.message
    # вытаскиваем из него долготу и ширину
    current_position = (message.location.longitude, message.location.latitude)
    # создаем строку в виде ДОЛГОТА,ШИРИНА
    coords = f"{current_position[0]},{current_position[1]}"
    print(coords)
    # отправляем координаты в нашу функцию получения адреса
    address_str = get_address_from_coords(coords)
    print(address_str)
    # вовщращаем результат пользователю в боте
    update.message.reply_text(address_str)
    return keyboard

def location(update, context):
    #получаем обьект сообщения (локации)
    message = update.message
    #вытаскиваем из него долготу и ширину
    current_position = (message.location.longitude, message.location.latitude)
    #создаем строку в виде ДОЛГОТА,ШИРИНА
    coords = f"{current_position[0]},{current_position[1]}"
    #отправляем координаты в нашу функцию получения адреса
    address_str = get_address_from_coords(coords)
    #вовщращаем результат пользователю в боте
    update.message.reply_text(address_str)


@dp.message_handler(text = 'где я')
async def process_locate_me_command(message: types.Message):
        reply = "Тыкни чтобы поделиться"
        await message.reply(reply, reply_markup=get_keyboard())


@dp.message_handler(text = 'расскажи шутку')
async def process_get_joke_command(message: types.Message):
    await bot.send_message(message.from_user.id, getRandomJoke(jokes), reply_markup=inline_kb1)

@dp.message_handler(text = 'животных знаешь каких-нибудь?')
async def process_get_word_command(message: types.Message):
    await bot.send_message(message.from_user.id, getRandomAnimal(words))

@dp.message_handler(text = 'памагити!!!!!')
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Здесь был список команд, но теперь всё на кнопках")


# keyboards.py
inline_btn_1 = InlineKeyboardButton('ахахахаха', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_btn_2 = InlineKeyboardButton('отстой(((', callback_data='button2')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)

@dp.callback_query_handler(text="button1")
async def send_answer(message: types.Message):
    await bot.send_message(message.from_user.id, 'ахахахаха в карман не положишь, лучше скинь денег на карту')

@dp.callback_query_handler(text="button2")
async def send_answer(message: types.Message):
    await bot.send_message(message.from_user.id, 'что есть, то есть')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

my_cords = "37.603716,55.543578"

# даем запрос на получение адреса с координатами
address_str = get_address_from_coords(my_cords)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
