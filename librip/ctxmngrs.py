# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
import time
class timer:
    def __enter__(self):
        self.t = time.clock()


    def __exit__(self, exp_type, exp_value, traceback):
        print(time.clock() - self.t)
