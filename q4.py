def string_reverse(s):

    if not isinstance(s, str):
        return "Input must be a string"

    return s[::-1]


# Task 2:
print(string_reverse("Hello World"))
print(string_reverse("Python")) 
