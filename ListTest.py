# x = (1, 2, (3, 'John', 4), 'Hi')
#
# print(type((1, 2, (3, 'John', 4))))
# print(x[2][-1])
# print(x[-1])
# print(x[2])
# print(x[0:1])
#
# x = [1, 2, [3, 'John', 4], 'Hi']
# print(type(x[2]))

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']




x = listA.extend([4, 1, 6, 3, 4])
y = listA.sort()
z = listA.insert(0, 100)
print(listA)

d = {'hello': 'world'}
print(d)
print(d.get('hello', 'jaja'))
if 'hello' in d:
    print(d['hello'])

L = [2, -3, -1]
L2 = [4, 6, -4]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


print(applyToEach(L, abs))


for elt in map(abs, L):
    print(elt)
