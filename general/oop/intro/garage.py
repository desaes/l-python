class Garage:
    def __init__(self) -> None:
        self.cars = []

    # allows you to count the number of items from an object
    def __len__(self) -> int:
        return len(self.cars)
    
    # allows you to get an item from an object by it index
    def __getitem__(self, index) -> str:
        return self.cars[int(index)]
    
    # repr() is mainly used for debugging and development. Repr’s goal is to be unambiguous. Should be choose over str.
    def __repr__(self):
        return f"<Garage {self.cars}>"
    
    # str() is used for creating output for end user. Str’s is to be readable. Optional.
    def __str__(self):
        return f"Garage with {len(self.cars)} cars."
    
ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0])

# for needs __getitem__
for car in ford:
    print(car)

# will call __repr__ if __str__ is not defined, otherwise will call __str__
print(ford)
print(repr(ford))
print(str(ford))

