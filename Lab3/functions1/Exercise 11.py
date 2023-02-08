def palindrome(string):
    str = string[::-1]
    if(str == string):
        return True
    return False