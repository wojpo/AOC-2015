from Present import Present
from get_input import get_input

def calc(inp):
    ans = 0
    for i in inp:
        ans += Present(i).get_ribbon()
    return ans

if __name__ == '__main__':
    dims = get_input('input')
    print(calc(dims))