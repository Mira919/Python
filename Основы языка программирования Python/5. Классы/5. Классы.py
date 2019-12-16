# Создать обьекты: гусь Белый, гусь Серый, корова Манька, овца Барашек, овца Кудрявый, курица Ко-КО, курица Кукареку, коза Рога, коза Копыта, утка Кряква
# Со всеми животными необходимо взаимодействовать: кормить, корову и коз доить, овец стричь, собирать яйца у кур, утки и гусей.

# Необходимо посчитать общий вес всех животных (weight_all_animal);
# Вывести название самого тяжелого животного (heaviest);

class Goose:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.animal = "Гусь"

    def eat_and_egg(self):
        action = self.animal + ' ' + self.name + ' покормлен(а) и яйца собраны'
        print(action)

class Cow(Goose):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Корова"

    def eat_and_milk(self):
        action = self.animal + ' ' + self.name + ' покормлен(а) и подоена'
        print(action)

class Sheep(Goose):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Овечка"

    def eat_and_cut(self):
        action = self.animal + ' ' + self.name + ' покормлен(а) и подстрижена'
        print(action)

class Chiken(Goose):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Кура"

class Goat(Cow):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Коза"

class Duck(Goose):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.animal = "Утка"

goose_gray = Goose('Серый', 5.8)
goose_white = Goose('Белый', 6.1)
cow_manka = Cow('Манька', 500)
sheep_barashek = Sheep('Барашек', 25)
sheep_kudryavui = Sheep('Кудрявый', 26)
chiken_koko = Chiken('Ко-Ко', 1.2)
chiken_kukareku = Chiken('Кукареку', 1.1)
goat_roga = Goat('Рога', 55)
goat_kopita = Goat('Копыта', 57)
duck_kryakva = Duck('Кряква', 2.5)

goose_gray.eat_and_egg()
goose_white.eat_and_egg()
cow_manka.eat_and_milk()
sheep_barashek.eat_and_cut()
sheep_kudryavui.eat_and_cut()
chiken_koko.eat_and_egg()
chiken_kukareku.eat_and_egg()
goat_roga.eat_and_milk()
goat_kopita.eat_and_milk()
duck_kryakva.eat_and_egg()

weight_all_animal = (goose_gray.weight, goose_white.weight, cow_manka.weight, sheep_barashek.weight, sheep_kudryavui.weight, chiken_koko.weight, chiken_kukareku.weight, goat_roga.weight, goat_kopita.weight, duck_kryakva.weight)
print(f"Общий весь всех животных: {sum(weight_all_animal)} килограмм")

heaviest = max(goose_gray, goose_white, cow_manka, sheep_barashek, sheep_kudryavui, chiken_koko, chiken_kukareku, goat_roga, goat_kopita, duck_kryakva, key = lambda x: x.weight)
print(f'Самое тяжелое животное: {heaviest.animal} {heaviest.name} весом: {heaviest.weight} кг.')

