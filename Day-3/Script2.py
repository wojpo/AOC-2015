from get_input import get_input
from coords import calc_coords

def calc_how_many_houses_at_least_one_present_robosanta(string):
    l = [[0, 0]]
    santa_coords = [0, 0]
    robo_coords = [0, 0]
    for i in range(len(string)):
        if i % 2 == 0:
            santa_coords = calc_coords(string[i], santa_coords)
            if santa_coords not in l:
                l.append([santa_coords[0], santa_coords[1]])
        if i % 2 == 1:
            robo_coords = calc_coords(string[i], robo_coords)
            if robo_coords not in l:
                l.append([robo_coords[0], robo_coords[1]])
    return len(l)

if __name__ == "__main__":
    inp = get_input("input")
    ans = calc_how_many_houses_at_least_one_present_robosanta(inp)
    print(ans)