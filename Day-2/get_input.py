def get_input(file):
    with open(file) as f:
        dimensions = []
        for line in f:
            UwU = line.replace('\n', '').split('x')
            for i in range(len(UwU)):
                UwU[i] = int(UwU[i])
            dimensions.append(UwU)
        return dimensions