'''
This is a madlibs generator, by having the story in story.txt with placeholders between brackets <>.
'''

from re import findall, sub

with open('./story.txt') as file:
    story = file.read()

print(story)

new_story = story

placeholders = findall(r'<\w+>', story)
placeholder_list = []

for word in placeholders:
    w1 = sub('<','', word)
    w2 = sub('>','', w1)
    w3 = sub('_',' ',w2)
    if w3 not in placeholder_list: placeholder_list.append(w3)

print(placeholders)
print(placeholder_list)

inputs = []

placeholders_unique = []

for bracket in placeholders:
    if bracket not in placeholders_unique:
        placeholders_unique.append(bracket)

print(placeholders_unique)

for bracket in placeholder_list:
    new_word = input(f'Please enter a {bracket}:')
    inputs.append(new_word)

for i in range(0,len(placeholders_unique)):

    new_story = new_story.replace(placeholders_unique[i],inputs[i])

print(new_story)
