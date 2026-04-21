def format_name(name):
    if type(name) != str:
        raise TypeError("Input must be a string")

    return name.capitalize()


print(format_name("ARjun"))