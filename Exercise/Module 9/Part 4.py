import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def race():
    cars = []
    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(license_plate, max_speed))

    race_finished = False
    while not race_finished:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_finished = True
                break

    return sorted(cars, key=lambda c: c.travelled_distance, reverse=True)
