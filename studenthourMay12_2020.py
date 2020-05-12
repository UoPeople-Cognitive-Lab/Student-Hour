vowels = ['a', 'e', 'i', 'o', 'u']

name = 'zamzam'
nameLen = len(name)
# print(nameLen)
name2 = ''

for i in range(nameLen):  # For loop
    if name[i] in vowels:
        name2 = name2 + name[i] + 'u'  # String Concatenation
    else:
        name2 = name2 + name[i]

print(name2)  # zaumzaum

# x = 5
# school = 'uopeople'
# print(school[x])
