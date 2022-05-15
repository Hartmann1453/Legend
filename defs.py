import random
import pyautogui
import finder


def check_fight():
    res_x, res_y = finder.element('img/default/vs.png', 15)
    print(f'Элемент найден [VS в бою]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Я не в бою'


def click_hunt():
    res_x, res_y = finder.element('img/default/hunt.png', 3)
    print(f'Элемент найден [Кнопка Охоты]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Моб не найден'

    # Выделяем область клика
    x = random.randint(res_x, res_x + 25)
    y = random.randint(res_y, res_y + 25)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка Охоты]')
