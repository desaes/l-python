def create_gen():
    mylist = range(3)
    for i in mylist:
        yield i

mygen01 = create_gen()
mygen02 = create_gen()
try:
    while True:
        print(next(mygen01))
        print(next(mygen02))
except StopIteration:
    pass
