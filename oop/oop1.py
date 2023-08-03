class Dog:
    def __init__(self, my_name, my_gender, my_age):
        self.name = my_name
        self.gender = my_gender
        self.age = my_age

    def eat(self):
        if self.gender == "male":
            print(f"{self.name} + Good Boy! Eat up.")
        else:
            print(f"{self.name} + Good Girl! Eat up.")

    def bark(self, is_loud):
        if is_loud:
            print("WOOF WOOF WOOF ")
        else:
            print("WOOOF")


class German(Dog):

    def __init__(self, my_name, my_gender, my_age, sleepy):
        super().__init__(my_name, my_gender, my_age)
        self.sleepy = sleepy

    def hunt(self):
        if not self.sleepy:
            self.bark(True)
            print(f"{self.name} is hunting")
        else:
            print(f"{self.name} is not good in hunting")


g1 = German("rex", "female", 10, False)
g1.hunt()
