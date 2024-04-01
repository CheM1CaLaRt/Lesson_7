import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "курлык!"

    def fly(self):
        return f"{self.name} летает."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Гррр!"

    def run(self):
        return f"{self.name} бежит."


class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        return "Ссссс!"

    def crawl(self):
        return f"{self.name} ползает."

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_to_text_file(self, filename):
        with open(filename, 'w') as f:
            f.write("Животные:\n")
            for animal in self.animals:
                f.write(f"{type(animal).__name__}: {animal.name}, Возраст: {animal.age}\n")

            f.write("\nПерсонал:\n")
            for staff_member in self.staff:
                f.write(f"{type(staff_member).__name__}: {staff_member}\n")

    def load_from_text_file(self, filename):
        with open(filename, 'r') as f:
            current_section = None
            for line in f:
                line = line.strip()
                if line == "Животные:":
                    current_section = "Животные"
                elif line == "Персонал:":
                    current_section = "Персонал"
                elif current_section == "Животные":
                    animal_parts = line.split(":")
                    if len(animal_parts) >= 2:
                        animal_type = animal_parts[0]
                        animal_info = ":".join(animal_parts[1:]).strip().split(", ")
                        if len(animal_info) >= 2:
                            name = animal_info[0]
                            age = int(animal_info[1].split(":")[1])
                            if animal_type == "Bird" and len(animal_info) >= 3:
                                wingspan = animal_info[2].split(":")[1]
                                self.add_animal(Bird(name, age, wingspan))
                            elif animal_type == "Mammal" and len(animal_info) >= 3:
                                fur_color = animal_info[2].split(":")[1]
                                self.add_animal(Mammal(name, age, fur_color))
                            elif animal_type == "Reptile" and len(animal_info) >= 3:
                                scale_pattern = animal_info[2].split(":")[1]
                                self.add_animal(Reptile(name, age, scale_pattern))
                elif current_section == "Персонал":
                    staff_parts = line.split(":")
                    if len(staff_parts) >= 2:
                        staff_type = staff_parts[0]
                        staff_name = staff_parts[1].strip()
                        if staff_type == "ZooKeeper":
                            self.add_staff(ZooKeeper(staff_name))
                        elif staff_type == "Veterinarian":
                            self.add_staff(Veterinarian(staff_name))

class ZooKeeper:
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        return f"{animal.name} кормит работник зоопарка."


class Veterinarian:
    def __init__(self, name):
        self.name = name
    def heal_animal(self, animal):
        return f"{animal.name} лечит ветеринар."

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Пример использования
zoo1 = Zoo("Зоопарк №1")
bird = Bird("Воробей", 2, "маленькие")
mammal = Mammal("Лев", 5, "рыжый")
reptile = Reptile("Змея", 3, "полосатая")
zoo1.add_animal(bird)
zoo1.add_animal(mammal)
zoo1.add_animal(reptile)
zoo1.add_staff(ZooKeeper("Вася"))
zoo1.add_staff(Veterinarian("Петя"))

animal_sound([bird, mammal, reptile])

zoo1.save_to_text_file("my_zoo_list.txt")
zoo1.load_from_text_file("my_zoo_list.txt")