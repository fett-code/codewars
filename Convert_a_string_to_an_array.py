#Write a function to split a string and convert it into an array of words.
#Examples (Input ==> Output):
#"Robin Singh" ==> ["Robin", "Singh"]
#my solution
def string_to_array(s):
    if s is None:
        return []
    elif s=="":
        return ['']
    
    arr=(s.split())
    return arr
    # your code here
