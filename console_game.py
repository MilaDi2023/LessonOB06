# ЗАДАНИЕ: Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями
# с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди
# наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 2. Игра должна быть реализована как консольное приложение.
#
# Классы:
#
# Класс `Hero`:
#
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
#
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
#
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
#
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f'{self.player.name} атакует {self.computer.name}, у {self.computer.name} осталось {self.computer.health} здоровья.')
            else:
                self.computer.attack(self.player)
                print(f'{self.computer.name} атакует {self.player.name}, у {self.player.name} осталось {self.player.health} здоровья.')
            turn += 1

        winner = self.player if self.player.is_alive() else self.computer
        print(f'\nПОБЕДИТЕЛЬ: {winner.name}')


# Создание игры и запуск
print("\nЗДОРОВЬЕ ИГРОКА - 100")
print("ЗДОРОВЬЕ КОМПЬЮТЕРА - 100")
print()


game = Game('Игрок', 'Компьютер')
game.start()