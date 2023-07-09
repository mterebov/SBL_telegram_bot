from aiogram import types
from bot import dp, bot
from handlers import keyboard
import Datapathes
from functions.info_reader import inforeader
from functions.vk_parcer_schedule import schedule


async def start(message: types.Message):
    try:
        await message.answer(inforeader(Datapathes.welcome_message), reply_markup=keyboard.mainmenu)
    except Exception as e:
        print(e)


async def keyboard_handler(message: types.Message):
    try:
        match message.text:
            case 'Помощь':
                await message.answer(inforeader(Datapathes.botoverview_path), reply_markup=keyboard.help_inline_keyboard)
            case 'О нас':
                await message.answer('что вас интересует?', reply_markup=keyboard.aboutus)
            case 'Расписание':
                await message.answer(schedule('https://vk.com/topic-20011640_49388431'))
                await message.answer('До встречи на тренировках!')
            case 'Назад':
                await message.answer('Чем могу помочь?', reply_markup=keyboard.mainmenu)
            case 'Кто мы такие?':
                await message.answer(inforeader(Datapathes.Who_are_we_path))
            case 'Где проходят тренировки?':
                await message.answer(inforeader(Datapathes.Where_are_we_path))
            case 'Со скольки лет можно заниматься?':
                await message.answer(inforeader(Datapathes.about_age_path))
            case 'Список вещей на тренировку':
                await message.answer('Еще в разработке :(')
            case 'Список вещей на сборы':
                await message.answer('Еще в разработке :(')
            case 'Контакты':
                await message.answer('Способы связи с нами:', reply_markup=keyboard.contacts)
            case _:
                await message.reply('Нет такой комманды!')
    except Exception as e:
        print(e)


async def inline__keyboard_handler(call: types.CallbackQuery):
    try:
        match call.data:
            case 'helpfunctions':
                await call.message.answer(inforeader(Datapathes.botfunctions_path))
                await bot.answer_callback_query(callback_query_id=call.id)
            case 'contactscall':
                await call.message.bot.send_contact(call.message.chat.id, '+79111630993', 'Павловская', 'Валерия')
                await bot.answer_callback_query(callback_query_id=call.id)
            case 'contactsemail':
                await call.message.answer('info@skiliberty.ru')
                await bot.answer_callback_query(callback_query_id=call.id)
    except Exception as e:
        print(e)


def register_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(keyboard_handler, state=None)
    dp.register_callback_query_handler(inline__keyboard_handler)
