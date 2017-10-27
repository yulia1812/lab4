# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

def print_result(function_to_decorate):
# Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
# получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function(*a):
        otv = function_to_decorate(*a) # Сама функция
        print(function_to_decorate.__name__)
        if type(otv) == list:
            for i in otv:
                print(i)
        elif type(otv) == dict:
            for i, j in otv.items():
                print(i, '=', j)
        else:
            print(otv)
        return otv
        # Вернём эту функцию
    return the_wrapper_around_the_original_function