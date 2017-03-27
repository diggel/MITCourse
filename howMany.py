animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def howMany(aDict):
    count = sum(len(v) for v in animals.values())
    return count


print(howMany(animals))

element = {}
for k in animals:
    element[k] = element.get(k, 0) + 4
print(element)

# def howMany(aDict):
#     myDict = {}
#     for animal in aDict:
#         if animal in myDict:
#             myDict[animal] += 1
#         else:
#             myDict[animal] = 1
#     return myDict


# sum(map(len, animals.values()))
