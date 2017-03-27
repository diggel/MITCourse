testList = [1, -4, 8, -9]

# >>> print(testList)
# [5, -20, 40, -45]


def applyToEach(L, f):
        for i in range(len(L)):
            L[i] = f(L[i])


def timesFive(a):
    return a * 5


# applyToEach(testList, timesFive)

print(testList)

""" >>> print(testList)
  [1, 4, 8, 9]
"""

# applyToEach(testList, abs)

print(testList)

"""
  >>> print testList
  [2, -3, 9, -8]

"""


def add1(a):
    return a + 1


# applyToEach(testList, add1)
print(testList)

"""
  [1, 16, 64, 81]

"""


def square(a):
    return a * a


applyToEach(testList, square)
print(testList)
