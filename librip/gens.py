import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    otv = []
    if len(args) == 1:
        for x in items:
            y = x.get(args[0])
            if y != None:
                otv.append(y)
    else:
        for x in items:
            z = []
            for y in args:
                q = []
                q.append(y)
                q.append(x.get(y))
                z.append(q)
            count = 0
            for i in z:
                if i[1] == None:
                    count += 1
            if (count != len(z)):
                for y in z:
                    if y[1] == None:
                       z.remove(y)
                otv1 = {}
                otv1.update(z)
                otv.append(otv1)
    return otv


    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):

    return [random.choice([i for i in range(begin, end+1)]) for j in range(num_count)]
    # Необходимо реализовать генератор
