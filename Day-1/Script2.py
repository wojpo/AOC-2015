from get_input import get_input

def get_basement_char(string):
    floors = 0
    for i, val in enumerate(string):
        if val == ')':
            floors -= 1
            if floors == -1:
                return i + 1
        else:
            floors += 1

if __name__ == '__main__':
    input_str = get_input("input")
    ans = get_basement_char(input_str)
    print(ans)