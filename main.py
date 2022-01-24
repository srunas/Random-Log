import random
import logging

logging.basicConfig(filename="info30.log", level=logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s" )

logging.info("Начался ввод количества бочек")
while True:
    try:
        n = int(input("Введите количество боченков: "))
        if  n < 1:
            logging.error("Ошибка некорректного ввода")
            print("Количество бочек должно быть положительным числом")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Некорректный ввод")
        pass

l = list(range(1, n + 1))
random.shuffle(l)
logging.info("Начался вывод чисел")
for i in l:
    input("Нажмите Enter для появления бочки.")
    print(i)
logging.info("Вывод чисел закончился")
input("Программа завершена, для закрытия нажмите Enter.")
logging.info("Программа завершилась")
