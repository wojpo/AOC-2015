def get_input(file):
    with open(file) as f:
        ans = []
        for line in f:
            ans.append(line.strip())
        return ans
