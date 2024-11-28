from get_input import get_input

def evaluate(wire, instructions, cache):
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]
    operation = instructions[wire]
    if "AND" in operation:
        x, y = operation.split(" AND ")
        value = evaluate(x, instructions, cache) & evaluate(y, instructions, cache)
    elif "OR" in operation:
        x, y = operation.split(" OR ")
        value = evaluate(x, instructions, cache) | evaluate(y, instructions, cache)
    elif "LSHIFT" in operation:
        x, n = operation.split(" LSHIFT ")
        value = evaluate(x, instructions, cache) << int(n)
    elif "RSHIFT" in operation:
        x, n = operation.split(" RSHIFT ")
        value = evaluate(x, instructions, cache) >> int(n)
    elif "NOT" in operation:
        x = operation.split()[1]
        value = ~evaluate(x, instructions, cache) & 0xFFFF
    else:
        value = evaluate(operation, instructions, cache)
    cache[wire] = value
    return value


if __name__ == "__main__":
    print(evaluate('a', get_input("input"), {}))

    meow = get_input("input")
    meow['b'] = str(evaluate('a', meow, {}))

    print(evaluate('a', meow, {}))
