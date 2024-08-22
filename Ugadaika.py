from random import*
from math import*
 

def is_valid(n, x, y):

    return n.isdigit() and x <= int(n) <= y


def ugadaika():
    print("Добро пожаловать в числовую угадайку")

    while True:
        print("Выберите диапозон чисел")
        x = int(input("Начало: "))
        y = int(input("Конец: "))
        diapozon = (y - x) + 1
        # Используем бинарный поиск, чтобы найти минимальное количество попыток
        attempts = ceil(log2(diapozon + 1))  # Добавляем 1 к n
        print(f"Я загадаю число от {x} до {y}, а вы попробуйте его отгадать. на угадывание вам будет даваться {attempts} попыток")
        print("Загадал...")
        cnt = 0
        digit = randint(x, y)
 
        while cnt < attempts:
            n = input(f"Введите ваше число (от {x} до {y}): ")
            # Проверяем на валидность, если не валидно, запрашиваем снова
            while not is_valid(n, x, y):
                print("А может быть всё-таки введем целое число от {x} до {y}?")
                n = input(f"Введите ваше число (от {x} до {y}): ")

            n = int(n)  # Преобразуем введенное значение в целое число
            cnt += 1  # Увеличиваем счетчик попыток
            if n < digit:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                print()
            if n > digit:
                print("Ваше число больше загаданного, попробуйте еще разок")
                print()
            if n == digit:
                print("Вы угадали, поздравляем!")
                print("Вам потребовалось", cnt, "попытки")
                break
        if cnt == attempts and n != digit:
            print("Попытки кончились. Выпроиграли")
            print("Загаданное число было:", digit)

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            print("Спасибо за игру! До свидания!")
            return False  
 

ugadaika()  