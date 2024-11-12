from get_input import get_input
from coords import calc_coords

def calc_how_many_houses_at_least_one_present(string):
    l = [[0, 0]]
    coords = [0, 0]
    for i in string:
        coords = calc_coords(i, coords)
        if coords not in l:
            l.append([coords[0], coords[1]])
    return len(l)

if __name__ == "__main__":
    inp = get_input("input")
    ans = calc_how_many_houses_at_least_one_present(inp)
    print(ans)
