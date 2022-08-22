for num in [1, 2, 3, 4, 5]:
    print(num)

for letter in 'Crocodile':
    print(letter)

def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    
my_for('Crocodile')    

numbers = [1, 2, 3, 4, 5]

my_for(numbers)