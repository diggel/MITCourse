x = ('I', 'am', 'a', 'test', 'tuple');


def oddTupples(aTuple):
    odd = ()
    for t in range(0, len(aTuple), 2):
        odd = odd + (aTuple[t],)
    return odd



print(oddTupples(x))
