import requests
from bs4 import BeautifulSoup as BS


#Парсинг расписания, возвращает вложенный список с разбиением на дни(условно строки того, что написано в расписании)
def schedule(url):
    #Парсинг поста в вк
    req = requests.get(url)
    html = BS(req.content, 'html.parser')
    finded = html.find_all("div", {"class": "pi_text"})

    #Переменные, необходимые для выполнения скрипта
    ras = finded[1].text.split(' ')
    raspisanie = ''
    find_finish_debug = []
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    num_days = 0
    fl = []
    output = []
    output_str = '------------' + '\n'

    #Разделение слепленных слов(почти всех)
    for part in range(len(ras)):
        for sym in range(len(ras[part])):
            if str(ras[part])[sym].isupper():
                delta = str(ras[part])[:sym] + ' ' + str(ras[part])[sym:]
                ras[part] = delta

    #Склейка в строку
    for i in range(len(ras)):
        raspisanie += ' ' + ras[i]

    #Дебаг строки и удаление лишних образовавшихся пробелов
    find_finish = raspisanie.split(' ')
    for el in range(len(find_finish)):
        if len(find_finish[el]) != 0:
            find_finish_debug.append(find_finish[el])

    #Выборка по дням недели
    for el in range(len(find_finish_debug)):
        if find_finish_debug[el] in days:
            num_days += 1
            fl.append(el)

    for ind in range(len(fl)):
        time_land = []
        if ind != (len(fl) - 1):
            for el in range(fl[ind], fl[ind + 1]):
                time_land.append(find_finish_debug[el])
            output.append(time_land)
        else:
            for el in range(fl[ind], len(find_finish_debug)):
                time_land.append(find_finish_debug[el])
            output.append(time_land)

    for dep in range(4):
        output[-1].pop(-1)

    for sot in range(len(output)):
        for wd in range(len(output[sot])):
            output_str += output[sot][wd] + ' '
        output_str += '\n' + '------------' + '\n'

    return output_str

#Пример вызова функции
'''schedule('https://vk.com/topic-20011640_49388431')'''