names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names):
    print(f"{counter}. {name}")
# 0. Harry
# 1. Rachel
# 2. Brian    

names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")
# 1. Harry
# 2. Rachel
# 3. Brian

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for counter, movie in enumerate(movies, start=1):
    print(f"{counter}. {movie[0]} ({movie[2]}), by {movie[1]}")

# (1, ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004)),
# (2, ("Memento", "Christopher Nolan", 2000)),
# (3, ("Requiem for a Dream", "Darren Aronofsky", 2000))    