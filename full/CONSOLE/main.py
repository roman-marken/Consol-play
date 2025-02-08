import random
import time
from colorama import init, Fore, Back, Style
import keyboard

# Ініціалізація
init()

with open("statik.txt", "r") as file:
    content = file.read()

wins = int(content)

player = '@'  # має бути довжина не більше 1 символа


def generate_maze(width, height):
    # Ініціалізація сітки
    maze = [["#" for _ in range(width)] for _ in range(height)]  # 2D лабіринт
    visited = [[False for _ in range(width)] for _ in
               range(height)]  # Той самий лабіринт але для відстеження вільних клітинок

    # Початкова точка
    start_x, start_y = 1, 1
    maze[start_y][start_x] = " "  # початкова позиція
    visited[start_y][start_x] = True

    # Напрямки руху: (dx, dy)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # можливі напрямки вгору, вниз, вперед, назад

    def is_valid(x, y):
        return 0 < x < width - 1 and 0 < y < height - 1 and not visited[y][x]

    def carve_path(x, y):  # перевіряє чи відвідана клітинка x, y
        random.shuffle(directions)
        for dx, dy in directions:  # nx, ny координати до яких прямує алгоритм
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[y + dy // 2][x + dx // 2] = " "  # Відкриваємо стіну між клітинками він ніби прорізає шлях
                maze[ny][nx] = " "  # Відкриваємо нову клітинку
                visited[ny][nx] = True  # позначається як відвідана
                carve_path(nx, ny)

    # Запуск генерації лабіринту
    carve_path(start_x, start_y)

    return maze  # виводимо лабіринт


def print_maze(maze):
    for row in maze:
        print("".join(row))


# Параметри лабіринту
width, height = 41, 21  # Розміри лабіринту (мають бути непарними)

# Мапа (двовимірний список)
simple_map = generate_maze(width, height)
simple_map[19][39] = '$'
# Початкова позиція
x, y = 1, 1  # Позиція на карті (x, y)

initial_map = [row.copy() for row in simple_map]


def Game():
    global x, y, simple_map, initial_map, wins
    # Очищаємо консоль
    print("\033c", end="")  # ANSI escape code для очищення екрану

    # Основний цикл гри
    while True:
        print("\033c", end="")  # Очищаємо екран кожен раз
        print("Натисніть 'q' для виходу...")

        # Управління персонажем
        if keyboard.is_pressed('right') and x < len(simple_map[0]) - 1:  # Перевірка меж карти
            if simple_map[y][x + 1] != '#':  # Якщо справа немає стіни
                x += 1  # Рух вправо
        elif keyboard.is_pressed('left') and x > 0:  # Перевірка меж карти
            if simple_map[y][x - 1] != '#':  # Якщо зліва немає стіни
                x -= 1  # Рух вліво
        elif keyboard.is_pressed('up') and y > 0:  # Перевірка меж карти
            if simple_map[y - 1][x] != '#':  # Якщо зверху немає стіни
                y -= 1  # Рух вгору
        elif keyboard.is_pressed('down') and y < len(simple_map) - 1:  # Перевірка меж карти
            if simple_map[y + 1][x] != '#':  # Якщо знизу немає стіни
                y += 1  # Рух вниз

        # Перевіряємо натискання клавіші 'q' для виходу
        if keyboard.is_pressed('q'):
            print("\033c", end="")  # Очистка консолі перед виходом
            return  # Завершити гру

        # Копіюємо початкову мапу для відновлення її стану
        current_map = [row.copy() for row in initial_map]

        # Встановлюємо поточну позицію гравця як '@'
        current_map[y][x] = player

        # Виводимо нову мапу
        for row in current_map:
            print(''.join(row))  # Виводимо кожен рядок карти як рядок символів

        # Вивести координати для перевірки
        print(f'position -\n x = {x}\n y = {y}')

        # Перевірка досягнення фінішу
        if x == 39 and y == 19:  # Ваші координати фінішу
            print("Вітаємо, ви досягли фінішу!")
            wins += 1

            with open("statik.txt", "w") as file:
                file.write(str(wins))

            x, y = 1, 1  # Скидаємо початкові координати

            # Вивести опції після досягнення фінішу
            print('\n "q" - вихід\n "c" - продовжити')

            # Цикл вибору дії після завершення гри
            while True:
                if keyboard.is_pressed('q'):
                    simple_map = generate_maze(width, height)
                    simple_map[19][39] = '$'
                    initial_map = [row.copy() for row in simple_map]

                    print("\033c", end="")  # Очистка консолі перед виходом
                    main()
                    break
                if keyboard.is_pressed('c'):
                    simple_map = generate_maze(width, height)
                    simple_map[19][39] = '$'
                    initial_map = [row.copy() for row in simple_map]

                    print("\033c", end="")  # Очистка консолі перед виходом
                    Game()  # Перезапускаємо гру
                    break

        # Затримка для чутливості
        time.sleep(0.1)


def statik():
    global wins

    print("\033c", end="")  # Очищення екрану

    print("Натисніть 'q' для виходу...")

    with open("statik.txt", "r") as file:
        content = file.read()

    print('\n----Статистика----\n')
    print(f'\nпройдених лабіринтів - {content}')
    while True:

        if keyboard.is_pressed('q'):
            print("\033c", end="")  # Очистка консолі перед виходом
            main()
            break


def main():
    current_option = 1  # Початковий вибір меню
    options = 3  # Кількість пунктів меню

    print("\033c", end="")  # Очищення консолі

    while True:
        print("\033c", end="")  # Очищення екрану
        print('   ____     _____   ___    __   _____    _____     _        ______ ')
        print('  / ___|   /  _  \  ||\\    ||  / ____|  /  _  \   | |      |  ____|')
        print(' | |      |  | |  | || \\   || | |____  |  | |  |  | |      | |__   ')
        print(' | |      |  | |  | ||  \\  ||  \___  | |  | |  |  | |      |  __|  ')
        print(' | |___   |  |_|  | ||   \\ ||   ___| | |  |_|  |  | |____  | |____ ')
        print('  \____|   \_____/  ||    \\||  /_____/  \_____/   |______| |______|\n')

        # Відображення пунктів меню
        print("> play" if current_option == 1 else "  play")
        print(
            "> statistics                                                   ↑   " if current_option == 2 else "  statistics                                                   ↑   ")
        print(
            "> exit                                                       ← ↓ →" if current_option == 3 else "  exit                                                       ← ↓ →")

        # Обробка натискань клавіш
        if keyboard.is_pressed('up'):
            current_option -= 1
            if current_option < 1:
                current_option = options  # Переходить до останнього пункту
            time.sleep(0.1)  # Затримка для стабільності

        elif keyboard.is_pressed('down'):
            current_option += 1
            if current_option > options:
                current_option = 1  # Переходить до першого пункту
            time.sleep(0.1)  # Затримка для стабільності

        elif keyboard.is_pressed('enter'):  # Вибір пункту меню
            if current_option == 1:
                print("Запуск гри...")
                time.sleep(1)
                print("\033c", end="")
                Game()
                break
            elif current_option == 2:
                print("Відкриття статистики...")
                print("\033c", end="")
                statik()
                time.sleep(1)
                break
            elif current_option == 3:
                print("Вихід з програми...")
                time.sleep(1)
                exit()
                exit()

        time.sleep(0.1)


if __name__ == "__main__":
    main()

