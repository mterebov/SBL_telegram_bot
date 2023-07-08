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

#Клавиатуры разделов "Помощь", "Контакты"
go_back = KeyboardButton('Назад')
help_contacts = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(go_back)

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
contacts_vk = InlineKeyboardButton(text='Группа в вк', url='https://vk.com/club20011640')
contacts_inst = InlineKeyboardButton(text='Инстаграмм', url='https://instagram.com/ski.board.liberty')
contacts_call = InlineKeyboardButton(text='Позвонить Павловской Валерии', callback_data='contactscall')
contacts_email = InlineKeyboardButton(text='Электронная почта', url='info@skiliberty.ru')
contacts.insert(contacts_call)
contacts.insert(contacts_email)
contacts.insert(contacts_vk)
contacts.insert(contacts_inst)
