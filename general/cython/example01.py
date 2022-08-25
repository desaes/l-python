import greeting

def main():
    name: str = input("What's your name: ")
    greeting.greet(name)

if __name__ == '__main__':
    main()