#!python2

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


def biggest(aDict):
    for k in animals:
        big = max(animals.keys())
        return big


print(biggest(animals))




# print(biggest(animals))
