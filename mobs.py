import random, time
import defs, finder, fight
import pyautogui
from PyQt5.QtWidgets import QMessageBox

def start(mob):
    while True:
        if defs.check_fight() != 'Я не в бою': # Проверяем в бою мы или нет
            fight.start()
        if defs.click_hunt() == 'Вкладка Охота не найдена': # Переходим к Охоте
            continue
        if click_mob(mob) == 'Моб не найден': # Ищем моба и выделяем его
            continue
        if check_mob(mob) == 'Моб не подтвержден': # Проверяем нужный ли моб выбран
            continue
        if click_attack(mob) == 'Моб не найден': # Двойной клик на моба
            continue
        fight.start() # Вступаем в бой

def guide():
    txt = "1.Авторизоваться в игре.\n2.Войти на локацию обитания требуемого моба.\n3.Раскрыть браузер на весь экран.\n4.Нажать кнопку старт.\n5. Отпустить мышку. Бот начнет работу. Требуется чтобы вкладка \"Охота\" была видна."
    guide_box = QMessageBox()

    guide_box.setWindowTitle("Подсказка")
    guide_box.setText(txt)
    guide_box.setIcon(QMessageBox.Information)

    guide_box.exec_()

def error_mob():
    txt = "Вы не выбрали моба."
    guide_box = QMessageBox()

    guide_box.setWindowTitle("Ошибка")
    guide_box.setText(txt)
    guide_box.setIcon(QMessageBox.Warning)

    guide_box.exec_()

def check_mob(mob):
    # Ищем иконку моба
    res_x, res_y = finder.element(f'img/mobs/{mob}/ico_mob.png', 3)
    print(f'Элемент найден [Иконка {mob}]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Моб не подтвержден'

def click_attack(mob):
    # Ищем кнопку атаки
    res_x, res_y = finder.element(f'img/mobs/{mob}/mob.png', 3)
    print(f'Элемент найден [Моб {mob}]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Моб не найден'

    # Создаем область клика.
    x = random.randint(res_x + 20, res_x + 30)
    y = random.randint(res_y - 35, res_y - 25)

    # Кликаем
    pyautogui.click(x, y) # Клик на моба
    time.sleep(0.3)
    pyautogui.click(x, y) # Клик на моба
    print(f'Нажали на элемент [Моб {mob}]')

def click_mob(mob):
    # Ищем моба
    res_x, res_y = finder.element(f'img/mobs/{mob}/mob.png', 300)
    print(f'Элемент найден [Моб {mob}]. x: {res_x} | y: {res_y}')
    if res_x == 'Элемент не найден.':
        return 'Моб не найден'

    # Выделяем область клика
    x = random.randint(res_x + 20, res_x + 30)
    y = random.randint(res_y - 35, res_y - 25)

    # Кликаем
    pyautogui.click(x, y) # Клик на моба
    print(f'Нажали на элемент [Моб {mob}]')