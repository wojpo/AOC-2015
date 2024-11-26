from get_input import get_input

def light_action(instructions, grid):
    if instructions[0] == True:
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for j in range(instructions[1][1], instructions[2][1] + 1):
                grid[i][j] += 1
    if instructions[0] == False:
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for j in range(instructions[1][1], instructions[2][1] + 1):
                if grid[i][j] > 0:
                    grid[i][j] -= 1
    if instructions[0] == 2:
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for j in range(instructions[1][1], instructions[2][1] + 1):
                grid[i][j] += 2
    return grid

def summarize(list_of_instructions, grid):
    for i in range(len(list_of_instructions)):
        grid = light_action(list_of_instructions[i], grid)
    return grid

def count_brightness(grid):
    ans = 0
    for i in grid:
        for j in i:
            ans += j
    return ans

if __name__ == '__main__':
    print(count_brightness(summarize(get_input("input"), [[0] * 1000 for _ in range(1000)])))