from get_input import get_input

def calc_floors(string):
    floors = len(string)
    for i in string:
        if i == ')':
            floors -= 2
    return floors

if __name__ == '__main__':
    input_str = get_input("input")
    ans = calc_floors(input_str)
    print(ans)