class Counter:
    def __init__(self, lower, higher) -> None:
        self.lower = lower
        self.higher = higher

    def __iter__(self):
        return self

    def __next__(self):
        if self.lower < self.higher:
            number = self.lower
            self.lower = self.lower + 1
            return number
        raise StopIteration


con = Counter(1,61)
print(con)
it = iter(con)
print(next(it))
print(next(it))
print(next(it))