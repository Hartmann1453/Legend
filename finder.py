import cv2
import numpy as np
from mss import mss
from transliterate import translit

def element(template, iteration):
    # Переводим кириллицу в латиницу
    template = translit(template, language_code='ru', reversed=True)

    # Загружаем образец
    template = cv2.imread(template, 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1365, 'height': 767}
    sct = mss()
    for i in range(iteration):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.95)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            return x, y
    return 'Элемент не найден.', 0

def pixel_coord(template, iteration):

    # Область поиска
    bounding_box = {'top': 225, 'left': 75, 'width': 1210, 'height': 290}
    m = mss()

    # Берем цвет с шаблона
    color = grabcolor(template)

    for i in range(iteration):
        # Переводим картинку в матрицу
        img = m.grab(bounding_box)
        img_arr = np.array(img)

        # Поиск цвета ( b, g, r, alpha)
        our_map = (color[2], color[1], color[0], 255)
        indexes = np.where(np.all(img_arr == our_map, axis=-1))
        our_crd = np.transpose(indexes)

        # Возвращаем координаты пикселя, иначе возвращаем заглушку
        if len(our_crd) > 0:
            our_crd[0][0] += 225 # Координата Y
            our_crd[0][1] += 75 # Координата X
            return our_crd[0]
    return [-1, -1]


def grabcolor(template):
    # Переводим кириллицу в латиницу
    template = translit(template, language_code='ru', reversed=True)

    # Загружаем образец пикселя
    img = cv2.imread(f'img/resourse/{template}/res.png', flags=6)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Переводим картинку в массив пикселей
    img_arr = np.array(img)
    return img_arr[0][0]