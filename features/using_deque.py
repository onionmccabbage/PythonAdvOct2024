# a double-ended queue les us work on BOTH ends (rather than just the last member)
from collections import deque

def checkPalindrome(word):
    '''check to see if the word is a palindrome (reads the same in both directions)'''
    dq = deque(word) # we now have a double ended queue
    while len(dq) > 1:
        left = dq.popleft()
        right = dq.pop()
        if left != right:
            return False
    return True

if __name__ == '__main__':
    result = checkPalindrome('madam')
    print(result)
    result = checkPalindrome('tenet')
    print(result)
    result = checkPalindrome('racecar')
    print(result)
    result = checkPalindrome('oops')
    print(result)