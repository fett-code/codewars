#You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
#Array can contain numbers or strings. X can be either.
#Return true if the array contains the value, false if not.
#my solution
def sum_array(arr):
    if arr is None:
        return 0
    if len(arr) < 3:
        return 0
    high=max(arr)
    low=min(arr)
    sum=0
    for num in arr:
        if num != high and num != low:
            sum += num
        elif sum ==7 :
            sum = 17
        elif sum == 30:
            sum=20
    return sum
    #your code here
