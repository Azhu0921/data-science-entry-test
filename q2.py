def find_and_replace(lst, find_val, replace_val):

    for i in range(len(lst)):

        if lst[i] == find_val:

          lst[i] = replace_val

    return lst


# Task 2:
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
