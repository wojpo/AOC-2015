#from get_input import get_input
#
#def light_action(instructions, grid):
#    if instructions[0] == True or instructions[0] == False:
#        for i in range(instructions[1][0], instructions[2][0] + 1):
#            for j in range(instructions[1][1], instructions[2][1] + 1):
#                grid[i][j] = instructions[0]
#    else:
#        for i in range(instructions[1][0], instructions[2][0] + 1):
#            for j in range(instructions[1][1], instructions[2][1] + 1):
#                if grid[i][j]:
#                    grid[i][j] = False
#                else:
#                    grid[i][j] = True
#    return grid
#
#def summarize_lights(list_of_instructions, grid):
#    for i in range(len(list_of_instructions)):
#        grid = light_action(list_of_instructions[i], grid)
#    return grid
#
#def check_lights(grid):
#    ans = 0
#    for i in grid:
#        ans += sum(1 for j in i if j)
#    return ans
#
#if __name__ == '__main__':
#    print(check_lights(summarize_lights(get_input("input"), [[False] * 1000 for _ in range(1000)])))


def process_instruction(instruction, grid):
    """Process a single instruction to modify the brightness of the grid."""
    # Parse the instruction
    parts = instruction.split()
    print(parts)
    # Extract coordinates for the affected lights
    if parts[0] == "turn":
        action = parts[1]  # 'on' or 'off'
        start_x, start_y = map(int, parts[2].split(','))
        end_x, end_y = map(int, parts[4].split(','))

        # Apply the instruction on the grid
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == "on":
                    grid[x][y] += 1
                elif action == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)

    elif parts[0] == "toggle":
        start_x, start_y = map(int, parts[1].split(','))
        end_x, end_y = map(int, parts[3].split(','))

        # Apply the toggle instruction
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                grid[x][y] += 2


def calculate_total_brightness(grid):
    """Calculate the total brightness of all lights in the grid."""
    return sum(sum(row) for row in grid)


def main(file_path):
    # Define the size of the grid
    grid_size = 1000  # 1000x1000 grid

    # Initialize the grid with zeros (all lights are off)
    grid = [[0] * grid_size for _ in range(grid_size)]

    # Read instructions from the file
    with open(file_path, 'r') as file:
        instructions = file.readlines()

    # Process each instruction
    for instruction in instructions:
        process_instruction(instruction.strip(), grid)

    # Calculate the total brightness
    total_brightness = calculate_total_brightness(grid)
    print(f"Total brightness: {total_brightness}")


if __name__ == "__main__":
    # Replace 'instructions.txt' with the path to your instructions file
    main('input')
