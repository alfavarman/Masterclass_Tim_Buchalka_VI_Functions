# write def with 2 parameters: str(t) and int(n)
# for t's value e function return sum of all even numbers in range upto N
# for t's value o function return sum of all odds in range upto n
# for t's spam return -1


def sum_eo(n, t):
    if t.casefold() == 'e':
        result = 0
        for x in range(0, n)[::2]:
            result += x
        return result
    elif t.casefold() == 'o':
        result = 0
        for x in range(0, n)[1::2]:
            result += x
        return result
    else:
        return -1


print(sum_eo(10, 'e'))
print(sum_eo(6, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(6, 'o'))
print(sum_eo(6, 'u'))
