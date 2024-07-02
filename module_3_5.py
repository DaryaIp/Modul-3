def get_multiplied_digits(number):

    str_number = str(number)
    int_number = int(number)
    str_number = str(int_number)
    first = int(str_number[0])
    if len(str(number)) >= 2:
        return first * get_multiplied_digits(int(str_number[1:]))

    else:
        return first

result = get_multiplied_digits('00040203')
print(result)