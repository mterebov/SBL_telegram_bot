from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

#Клавиатура главного меню
mainmenu_aboutus = KeyboardButton('О нас')
mainmenu_help = KeyboardButton('Помощь')
mainmenu_schedule = KeyboardButton('Расписание')
mainmenu_contacts = KeyboardButton('Контакты')
mainmenu_list_camp = KeyboardButton('Список вещей на сборы')
mainmenu_list_training = KeyboardButton('Список вещей на тренировку')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(mainmenu_schedule)\
    .row(mainmenu_list_training, mainmenu_list_camp)\
    .row(mainmenu_help, mainmenu_aboutus, mainmenu_contacts)

#Клавиатура раздела "О нас"
aboutus_who_we_are = KeyboardButton('Кто мы такие?')
aboutus_where_we_are = KeyboardButton('Где проходят тренировки?')
aboutus_about_age = KeyboardButton('Со скольки лет можно заниматься?')
aboutus_go_back = ('Назад')
aboutus = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(aboutus_who_we_are)\
    .row(aboutus_where_we_are)\
    .row(aboutus_about_age)\
    .row(aboutus_go_back)

#Клавиатура раздела ""
camp_summer = KeyboardButton('Летний сбор')
camp_winter = KeyboardButton('Зимний сбор')
camp_spring = KeyboardButton('Весенний сбор')
camp_autumn = KeyboardButton('Осенний сбор')
camp = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(camp_winter, camp_spring)\
    .row(camp_summer, camp_autumn)

#Инлайн клавиатура раздела "Контакты"
contacts = InlineKeyboardMarkup(row_width=1)
contacts_vk = InlineKeyboardButton(text='Наша группа в вк', url='https://vk.com/club20011640')
contacts_inst = InlineKeyboardButton(text='Наш инстаграмм', url='https://instagram.com/ski.board.liberty')
contacts_call = InlineKeyboardButton(text='Позвонить нам', callback_data='contactscall')
contacts_email = InlineKeyboardButton(text='Наша электронная почта', callback_data='contactsemail')
contacts_site = InlineKeyboardButton(text='Наш сайт', url='http://ski-board-liberty.tilda.ws/')
contacts.insert(contacts_call)
contacts.insert(contacts_email)
contacts.insert(contacts_site)
contacts.insert(contacts_vk)
contacts.insert(contacts_inst)

#Клавиатура раздела "Помощь"
help_inline_keyboard = InlineKeyboardMarkup(row_width=1)
help_github = InlineKeyboardButton(text='Код проекта на GIT', url='https://github.com/mterebov/SBL_telegram_bot/tree/main')
help_functions = InlineKeyboardButton(text='Доступные функции', callback_data='helpfunctions')
help_inline_keyboard.insert(help_functions)
help_inline_keyboard.insert(help_github)
