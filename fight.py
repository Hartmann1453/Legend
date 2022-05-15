import random
import time
import pyautogui
import finder

def start():
    while True:

        # Отлавливаем промежуточную ошибку "Обновить".
        check_refresh()

        # Рандомизируем направление атаки и наносим удар.
        rand = random.randint(1, 3)
        if rand == 1:
            click_dd_up()
        elif rand == 2:
            click_dd_mid()
        else:
            click_dd_down()

        # Проверяем окончание боя. Сценарий победы.
        if check_win():
            click_exit()
            time.sleep(2) # Пауза необходима. Иначе возвращает программу в бой.
            return

        # Проверяем окончание боя. Сценарий поражения.
        if check_retreat():
            click_exit()
            click_inloc()
            click_reborn()
            time.sleep(20) # Пауза для восстановления хп после поражения. Можно удалить, если не требуется.
            return

def click_dd_down():
    # Ищем кнопку удара
    res_x, res_y = finder.element('img/default/dd_down.png', 3)
    print(f'Элемент найден [Удар вниз]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return

    # Выделяем область клика
    x = random.randint(res_x, res_x + 20)
    y = random.randint(res_y, res_y + 20)

    # Кликаем
    pyautogui.click(x, y) # Клик на удар
    print('Нажали на элемент [Удар вниз]')

def click_dd_mid():
    # Ищем кнопку удара
    res_x, res_y = finder.element('img/default/dd_mid.png', 3)
    print(f'Элемент найден [Удар центр]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return

    # Выделяем область клика
    x = random.randint(res_x, res_x + 20)
    y = random.randint(res_y, res_y + 20)

    # Кликаем
    pyautogui.click(x, y) # Клик на удар
    print('Нажали на элемент [Удар центр]')

def click_dd_up():
    # Ищем кнопку удара
    res_x, res_y = finder.element('img/default/dd_up.png', 3)
    print(f'Элемент найден [Удар Вверх]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return

    # Выделяем область клика
    x = random.randint(res_x, res_x + 20)
    y = random.randint(res_y, res_y + 20)

    # Кликаем
    pyautogui.click(x, y) # Клик на удар
    print('Нажали на элемент [Удар Вверх]')

def click_exit():
    # Ищем кнопку победы
    res_x, res_y = finder.element('img/default/exit.png', 30)
    print(f'Элемент найден [Кнопка Выход]. x: {res_x} | y: {res_y}')

    # Выделяем область клика
    x = random.randint(res_x, res_x + 70)
    y = random.randint(res_y, res_y + 10)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка Выход]')

def click_inloc():
    # Ищем кнопку перехода в локацию
    res_x, res_y = finder.element('img/default/inloc.png', 200)
    print(f'Элемент найден [Кнопка В локацию]. x: {res_x} | y: {res_y}')

    # Выделяем область клика
    x = random.randint(res_x, res_x + 155)
    y = random.randint(res_y, res_y + 15)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка В локацию]')

def click_reborn():
    # Ищем кнопку воскреснуть
    res_x, res_y = finder.element('img/default/reborn.png', 200)
    print(f'Элемент найден [Кнопка Воскреснуть]. x: {res_x} | y: {res_y}')

    # Выделяем область клика
    x = random.randint(res_x, res_x + 140)
    y = random.randint(res_y, res_y + 15)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка Воскреснуть]')

def check_refresh():
    # Ищем кнопку обновить
    res_x, res_y = finder.element('img/default/refresh.png', 2)
    print(f'Элемент найден [Кнопка Обновить]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Ошибки нет.'

    # Выделяем область клика
    x = random.randint(res_x, res_x + 70)
    y = random.randint(res_y, res_y + 15)

    # Кликаем
    pyautogui.click(x, y)
    print('Нажали на элемент [Кнопка Обновить]')


def check_retreat():
    res_x, res_y = finder.element('img/default/retreat.png', 3)
    print(f'Элемент найден [Поражение]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else: return True

def check_win():
    res_x, res_y = finder.element('img/default/win.png', 3)
    print(f'Элемент найден [Победа]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else: return True