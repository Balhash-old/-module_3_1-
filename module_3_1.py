cals = 0


def count_cals():
    global cals
    cals += 1


def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_cals()
    return result


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list_to_search
    count_cals()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]) == string:
            result = True
        else:
            result = False
            continue
    return result


print(string_info('Hunter'))
print(string_info('Astronaut'))
print(is_contains('Omega', ['OmeGA', 'Hotel', 'Astra'])) # Urban ~ urBan
print(is_contains('sckorpion', ['Stop', 'exit']))
print(cals)