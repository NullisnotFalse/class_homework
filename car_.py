class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, up_speed):
        self.speed += up_speed
        if self.speed > 150:
            self.speed = 150

    def brake(self, down_speed):
        self.speed -= down_speed
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


car1 = Car("a", "red", 20)
print(car1.get_speed())
car1.accelerate(20)
print(car1.get_speed())
car1.brake(20)
print(car1.get_speed())
