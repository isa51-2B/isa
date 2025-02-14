class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет действие.")

    def attack(self):
        print(f"{self.name} атакует!")
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 50:
                print(f"{self.name} стреляет и попадает! Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} стреляет, но промахивается! Осталось стрел: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать, стрелы закончились!")
    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и восстанавливает стрелы. Текущий запас стрел: {self.arrows}")
    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"
archer1 = Archer("Лучник", 100, 10, 75)
print(archer1.status())
archer1.attack()
archer1.attack()
archer1.rest()
archer1.attack()

