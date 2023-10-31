"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # количество попыток угадывания
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    max_num = 100  # создаем переменную с максимально возможным загаданым числом
    min_num = 1  # создаем переменную с минимально возможным загаданым числом
    
    while True:  # создаем цикл
        
        count += 1  # при каждом проходе добавляем 1 к количеству попыток
        
        if count > 100:  # если количество проходов больше 100
            break  # выходим из цикла 
        
        elif number == predict_number:  # если угадали
            break  # выход из цикла
        
        elif number > predict_number:  # если загаданое число больше чем предполагаемое
            min_num = predict_number  # то предполагаемое число становится минимально возможным
            middle_range = (max_num - predict_number) // 2  # находим середину диапазона загаданого числа
            predict_number = predict_number + middle_range  # получаем новое предполагаемое число
            
        elif number < predict_number:  # если загаданое число меньше чем предполагаемое
            max_num = predict_number  # то предполагаемое число становится максимально возможным
            middle_range = (max_num - min_num) // 2  # находим середину диапазона загаданого числа
            predict_number = max_num - middle_range  # получаем новое предполагаемое число
            
    return count  # возвращаем количество попыток


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
