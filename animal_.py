class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("멍멍멍")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("야아아아옹")


dog = Dog("탁근몬", "3")
dog.speak()

cat = Cat("Cherry", "2")
cat.speak()
