#You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
#Array can contain numbers or strings. X can be either.
#Return true if the array contains the value, false if not.
#my solution`
def check(seq, elem):
    for num in range(len(seq)):
        if seq[num]==elem:
            return True
    return False
    pass
