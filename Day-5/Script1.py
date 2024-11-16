from get_input import get_input

def check_if_nice_string(string):
    vowels = 0
    twice = False
    for i in string:
        if i in 'aeiou':
            vowels += 1
    for i in range(len(string) - 1):
        if string[i] + string[i+1] in ['ab', 'cd', 'pq', 'xy']:
            return False
        if string[i] == string[i+1]:
            twice = True
    if twice and vowels >= 3:
        return True
    return False

def calc_nice_string(list_of_strings):
    return sum(1 for i in list_of_strings if check_if_nice_string(i))

if __name__ == '__main__':
    ans = calc_nice_string(get_input("input"))
    print(ans)
