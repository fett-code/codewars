# Write a function that takes an array of words and 
# smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, 
# but you should add spaces between each word. Be careful, there s
# houldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

# my solution
def smash(words):
    if len(words) == 0:
        return ''
    elif len(words) == 1:
        return words[0]
    elif len(words) >= 1:
        mystring = ' '.join(words)
        return mystring