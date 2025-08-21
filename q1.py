def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using list indexing
    values = [x, y]
    values[0], values[1] = values[1], values[0]

    x, y = values
    print("Swapped values:", x, y)
    return x, y


# Task 2
print(swap("AI", 10))
print(swap(8, 14)) 
