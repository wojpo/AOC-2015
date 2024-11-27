def get_input(file):
    with open(file) as f:
        ans = {}
        for line in f:
            meow = line.strip().split(" -> ")
            ans[meow[1]] = meow[0]
        return ans

