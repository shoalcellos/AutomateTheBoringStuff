# Solution to the first practise problem in:
# https://automatetheboringstuff.com/chapter4/

def CommaCode(inputList):
    """Takes a list value as an argument and returns \
        a string with all the items separated by a comma \
        and a space, with and inserted before the last item."""

    inputList[-1] = 'and ' + str(inputList[-1])
    return ", ".join(inputList)

if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats', 1]
    print(CommaCode(spam))