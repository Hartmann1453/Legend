import random
import time

import pyautogui

import finder

def check_puzzle():
    # Ищем якорь
    res_x, res_y = finder.element('img/default/puzzle/1/venchor.png', 3)
    print(f'Элемент найден [Пазл]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return False
    else:
        return True

def start_puzzle():

    # Получаем координаты клика по кусочку
    # Перетягиваем пазл на его место
    #
    # Первые два атррибута это отступ от якоря в пикселях.
    puzzle_x, puzzle_y = puzzle(1)
    move_puzzle(-10, 55, puzzle_x, puzzle_y)
    time.sleep(1)

    # Для 2 кусочка
    puzzle_x, puzzle_y = puzzle(2)
    move_puzzle(140, 55, puzzle_x, puzzle_y)
    time.sleep(1)

    # Для 3 кусочка
    puzzle_x, puzzle_y = puzzle(3)
    move_puzzle(290, 55, puzzle_x, puzzle_y)
    time.sleep(1)

    # Для 4 кусочка
    puzzle_x, puzzle_y = puzzle(4)
    move_puzzle(-10, 190, puzzle_x, puzzle_y)
    time.sleep(1)

    # Для 5 кусочка
    puzzle_x, puzzle_y = puzzle(5)
    move_puzzle(140, 190, puzzle_x, puzzle_y)
    time.sleep(1)

    # Для 6 кусочка
    puzzle_x, puzzle_y = puzzle(6)
    move_puzzle(290, 190, puzzle_x, puzzle_y)
    time.sleep(1)

def move_puzzle(x, y, puzzle_x, puzzle_y):
    # Ищем координаты якоря
    venchor_x, venchor_y = finder.element('img/default/puzzle/1/venchor.png', 30)
    if venchor_x == 'Элемент не найден.':
        venchor_x, venchor_y = finder.element('img/default/puzzle/2/venchor.png', 30)
        if venchor_x == 'Элемент не найден.':
            venchor_x, venchor_y = finder.element('img/default/puzzle/3/venchor.png', 30)
            if venchor_x == 'Элемент не найден.':
                return

    move_x = random.randint(venchor_x + x, venchor_x + x + 50)
    move_y = random.randint(venchor_y + y, venchor_y + y + 50)

    pyautogui.mouseDown(x=puzzle_x, y=puzzle_y)
    time.sleep(1)
    pyautogui.mouseUp(x=move_x, y=move_y)

def puzzle(number):


    # Ищем кусочек с соответствующим номером.
    if number == 1:
        # Ищем верхне-левую часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz1.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz1.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz1.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [1-ый кусочек]. x: {res_x} | y: {res_y}')
    if number == 2:
        # Ищем верхне-среднюю часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz2.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz2.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz2.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [2-ой кусочек]. x: {res_x} | y: {res_y}')
    if number == 3:
        # Ищем верхне-правую часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz3.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz3.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz3.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [3-ий кусочек]. x: {res_x} | y: {res_y}')
    if number == 4:
        # Ищем нижне-левую часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz4.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz4.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz4.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [4-ый кусочек]. x: {res_x} | y: {res_y}')
    if number == 5:
        # Ищем нижне-среднюю часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz5.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz5.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz5.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [5-ый кусочек]. x: {res_x} | y: {res_y}')
    if number == 6:
        # Ищем нижне-правую часть.
        res_x, res_y = finder.element('img/default/puzzle/1/puz6.png', 30)
        if res_x == 'Элемент не найден.':
            res_x, res_y = finder.element('img/default/puzzle/2/puz6.png', 30)
            if res_x == 'Элемент не найден.':
                res_x, res_y = finder.element('img/default/puzzle/3/puz6.png', 30)
                if res_x == 'Элемент не найден.':
                    return
        print(f'Элемент найден [6-ой кусочек]. x: {res_x} | y: {res_y}')

    # Выделяем область клика по кусочку пазла.
    puzzle_x = random.randint(res_x, res_x + 80)
    puzzle_y = random.randint(res_y, res_y + 80)

    return puzzle_x, puzzle_y
