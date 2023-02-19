class MercedezBenz:
    doors = 2
    wheels = 4

print(MercedezBenz.__dict__)

MercedezBenz.model = 'G'

print(MercedezBenz.__dict__)