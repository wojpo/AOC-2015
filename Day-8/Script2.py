from get_input import get_input

def calc_difference(s):
    raw = len(s)
    encoded = 2
    i = 0
    while i < len(s):
        if s[i] == '"':
            encoded += 2
            i += 1
        elif s[i] == '\\':
            encoded += 2
            i += 1
        else:
            encoded += 1
            i += 1
    return encoded - raw

def summarize():
    return sum(calc_difference(i) for i in get_input("input"))

if __name__ == "__main__":
    print(summarize())