def calc_coords(ch, coord):
    if ch == ">":
        coord[0] += 1
    elif ch == "<":
        coord[0] -= 1
    elif ch == "^":
        coord[1] += 1
    else:
        coord[1] -= 1
    return coord