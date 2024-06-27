calls = 0
def  count_calls():
    global calls
    calls += 1
    print(f"{calls}")

def string_info(string):
    upper_ = string.upper()
    lower_ = string.lower()
    return len(string), upper_, lower_


def is_contains(string, list_to_search):
    for string_ in list_to_search:
        if string_ == string:
            return True
    return False


print(string_info('Хозяйство'))

print(is_contains('Fox', ['Fox', 'Weather', 'lesson']))

print(string_info('Sunny'))

print(is_contains('Black', ['brown', 'grey', 'yellow']))

print(string_info('Good morning'))

print(is_contains('grey', ['brown', 'grey', 'yellow']))

print(calls)