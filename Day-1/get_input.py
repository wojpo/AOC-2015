def get_input(file):
    with open(file) as f:
        for i in f.readlines():
            return i
