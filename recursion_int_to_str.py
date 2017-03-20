def tostr(number,base):
    convert_string='0123456789ABCDEF'
    # base condition
    if number<base:
        return convert_string[number]

    else:
        return tostr(number // base, base) + convert_string[number%base]


print tostr(233,16)
