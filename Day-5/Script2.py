from get_input import get_input

def check_if_nice_string(string):
    twice = False
    pair = False
    for i in range(len(string) - 1):
        if string[i:i+2] in string[i+2:]:
            pair = True
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            twice = True
    if twice and pair:
        return True
    return False


def calc_nice_string(list_of_strings):
    return sum(1 for i in list_of_strings if check_if_nice_string(i))

if __name__ == '__main__':
    ans = calc_nice_string(get_input("input"))
    print(ans)