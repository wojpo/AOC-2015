from get_input import get_input

def calc_difference(s):
    raw = len(s)
    i = 1
    not_raw = 0
    while i < len(s) - 1:
        if s[i] == "\\":
            if s[i + 1] == "\\" or s[i + 1] == '"':
                not_raw += 1
                i += 2
            elif s[i + 1] == "x":
                not_raw += 1
                i += 4
        else:
            not_raw += 1
            i += 1
    return raw - not_raw

def summarize():
    return sum(calc_difference(i) for i in get_input("input"))

if __name__ == "__main__":
    print(summarize())
