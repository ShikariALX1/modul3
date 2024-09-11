calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    print((len(list(string)), string.upper(), string.lower()))


def is_contains(string, list_to_search):
    count_calls()
    list_to = [x.lower() for x in list_to_search]
    if list_to.count(string.lower()):
        print(True)
    else:
        print(False)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
