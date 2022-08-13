with open('file.txt') as fd:
    contents = fd.read()
    print(contents.rstrip())