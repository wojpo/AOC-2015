from hashlib import md5
from get_input import get_input


def find_lowest_with_x_zeros(string, x):
    a = 1
    while True:
        encoded = md5((string + str(a)).encode()).hexdigest()
        for i in range(len(encoded)):
            if i == x:
                return a
            if encoded[i] != '0':
                a += 1
                break


if __name__ == "__main__":
    res1 = find_lowest_with_x_zeros(get_input("input"), 5)
    print(res1)
    res2 = find_lowest_with_x_zeros(get_input("input"), 6)
    print(res2)
