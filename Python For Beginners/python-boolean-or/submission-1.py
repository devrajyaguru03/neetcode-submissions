a, b, c, d = False, False, True, True
first = (a or b)
second = (b or c)
third = (c or d)
fourth = (a or b or c or d)


print(first)
print(second)
print(third)
print(fourth)
