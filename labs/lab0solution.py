def same(word):
    if word[0].casefold()==word[-1].casefold():
        return True
    else:
        return False

def consecutiveSum(x, y):
    return (x+y)/2*(y-x-1)
