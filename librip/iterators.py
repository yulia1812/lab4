# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.data = items
        self.counter = 0
        if kwargs.get("ignore_case") != None:
            self.ignore_case = kwargs.get("ignore_case")
        else:
            self.ignore_case = False

    def __next__(self):
        # Нужно реализовать __next__

        if self.counter < len(self.data):
            if self.ignore_case == False:
                for i in range(self.counter, len(self.data)):
                    if (self.data.index(self.data[i]) >= i):
                        self.counter = i + 1
                        return self.data[i]
                raise StopIteration
            else:
                a = []
                for i in self.data:
                    a.append(i.lower())
                for i in range(self.counter, len(self.data)):
                    if (a.index(a[i]) >= i):
                        self.counter = i + 1
                        return self.data[i]
                raise StopIteration
        else:
            raise StopIteration

    def __iter__(self):
        return self
