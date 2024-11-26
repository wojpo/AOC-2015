def get_input(file):
    with open(file) as f:
        ans = []
        for line in f:
            meow = line.strip()
            meow = meow.split()
            if meow[0] == 'turn':
                meow.pop(0)
                if meow[0] == 'on':
                    meow[0] = True
                else:
                    meow[0] = False
            else:
                meow[0] = 2
            meow.pop(2)
            meow[1], meow[2] = meow[1].split(','), meow[2].split(',')
            meow[1], meow[2] = [int(meow[1][0]), int(meow[1][1])], [int(meow[2][0]), int(meow[2][1])]
            ans.append(meow)
        return ans
