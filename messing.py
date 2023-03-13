

def letterfrequency(filename, letter):
    file = open(filename, 'r')
    text = file.read()
    return text.count(letter)

if _name_=='_main_':
    if len(sys.argv) < 3:
        print('usage: python letter_frequency.py filename letter')
else:
    filename = sys.argv[1]
    letter = sys.argv[2]
    count = letter_frequency(filename, letter)

print(f'the letter "{letter}" appears {count} times in "{filename}"')

    