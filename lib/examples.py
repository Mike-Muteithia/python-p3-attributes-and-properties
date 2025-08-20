# class Human:
    # species = "Homo sapiens"
    # def __init__(self, name):
        # self.name = name

# guido = Human("Guido")
# print(guido.species)
# print(Human.species)

# print(guido.name)
# print(Human.name)

# guido.species = "Python programmer"
# print(guido.species)

# guido.name = "Guido van Rossum"
# print(guido.name)
# print(getattr(guido, "name"))

# guido.nationality = "Dutch"
# print(guido.nationality)
# setattr(guido, "nationality", "Dutch")

# my_attr = "is_a_friend"
# print(getattr(guido, my_attr, False))

# setattr(guido, my_attr, True)
# print(getattr(guido, my_attr, False))

# guido.age = False



class Human:
    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age
    
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age)

guido = Human(age=67)

guido.age = 0

guido.age = False

guido.age = 66

guido.age
print(guido.age)