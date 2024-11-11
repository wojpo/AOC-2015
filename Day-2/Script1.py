class Present:
    def __init__(self, dimensions):
        self.l = dimensions[0]
        self.w = dimensions[1]
        self.h = dimensions[2]

    def get_square_foots_of_paper(self):
        a = self.l * self.w * 2
        b = self.w * self.h * 2
        c = self.h * self.l * 2
        return a + b + c + min(a,b,c) / 2

def get_input(file):
    with open(file) as f:
        dimensions = []
        for line in f:
            UwU = line.replace('\n', '').split('x')
            for i in range(len(UwU)):
                UwU[i] = int(UwU[i])
            dimensions.append(UwU)
        return dimensions

def calc(inp):
    ans = 0
    for i in inp:
        ans += Present(i).get_square_foots_of_paper()
    return ans

if __name__ == '__main__':
    dims = get_input('input')
    print(calc(dims))
