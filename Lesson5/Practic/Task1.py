string = 'opjjuygtKIHYTFTFFjihygytfd'
string_list_1 = ['q', 'W', 'e', 'R', 't', 'Y', ]
string_list_2 = ['q', 'W', 'e', 'R', 't', 'Y', ]


def low_str():
    return string.lower()


def upper_str():
    return string.upper()


def low(elements):
    return elements.lower()


list_lower = list(map(low, string_list_1))


def upp(elements):
    return elements.upper()


list_upper = list(map(upp, string_list_2))

print(low_str())
print(upper_str())
print(list_lower)
print(list_upper)
