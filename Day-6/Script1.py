from get_input import get_input

def light_action(instructions, grid):
    if instructions[0] == True or instructions[0] == False:
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for j in range(instructions[1][1], instructions[2][1] + 1):
                grid[i][j] = instructions[0]
    else:
        for i in range(instructions[1][0], instructions[2][0] + 1):
            for j in range(instructions[1][1], instructions[2][1] + 1):
                if grid[i][j]:
                    grid[i][j] = False
                else:
                    grid[i][j] = True
    return grid

def summarize_lights(list_of_instructions, grid):
    for i in range(len(list_of_instructions)):
        grid = light_action(list_of_instructions[i], grid)
    return grid

def check_lights(grid):
    ans = 0
    for i in grid:
        ans += sum(1 for j in i if j)
    return ans

if __name__ == '__main__':
    print(check_lights(summarize_lights(get_input("input"), [[False] * 1000 for _ in range(1000)])))
