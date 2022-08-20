class Car:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self) -> None:
        self.cars = []

    def __len__(self) -> int:
        return len(self.cars)

    def add_car(self, car) -> None:
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects")
        self.cars.append(car)


ford = Garage()
#ford.add_car('Fiesta')
#print(len(ford))
car = Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))

