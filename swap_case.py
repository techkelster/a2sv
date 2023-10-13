def swap_case(s):
    res = ''
    for i in s:
        if i.islower():
            res += i.upper()
        elif i.isupper():
            res += i.lower()
        else:
            res += i
    return res
