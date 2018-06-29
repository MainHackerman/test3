string = input('Zadej text: ')
words = 0
spaces = 0
chars = 0
souhlasky = 0
samohlasky = 0
prevchar = ''

a = 'aeiuoy'
b = 'qwrtpsdfghjklxcvbnm'

for char in string:
    if char in a:
        samohlasky += 1

    elif char in b:
        souhlasky += 1

    elif char == ' ':
        if prevchar in a + b:
            words += 1
        spaces += 1
    prevchar = char

chars = len(string) - spaces

print(string)
print('Slova', words)
print('Mezery', spaces)
print('Znaky', chars)
print('Souhlasky', souhlasky)
print('Samohlasky', samohlasky)
