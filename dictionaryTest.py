animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

myDict = {}

grades = {'anna': '8', 'piet': '6', 'klaas': '7', 'karin': '4'}
grades['anna'] = '8.5'

print(len(grades))

print(len(animals['a']))

for i in grades:
    if 'ann' in grades:
        print('ja')
        break
    else:
        print('nop')
        break

print(grades.get(''))

# grade = grades.keys()
# print(grade)

for grade in grades:
    temp = grades[grade]
print(temp)

count = {}
for k in grades:
    count[k] = count.get(k, 0) + 1
print(count)

print(min(grades))


for k in grades:
    big = min(grades.keys())
print(big)
