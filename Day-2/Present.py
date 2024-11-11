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

    def get_ribbon(self):
        a = self.l * 2 + self.w * 2
        b = self.w * 2 + self.h * 2
        c = self.h * 2 + self.l * 2
        return min(a,b,c) + self.l * self.w * self.h
