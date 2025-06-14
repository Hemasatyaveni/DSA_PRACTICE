def separateofalpha(arr):
    letterslist = "abcdefghijklmnopqrstuvwxyz"
    digitslist = "1234567890"
    letters = ""
    digits = ""
    for char in arr:
        for letter in letterslist:
            if char == letter:
                letters+=char
                break
        for digit in digitslist:
            if char == digit:
                digits+=char
                break
    return letters,digits
arr = "sa2ty4a6"
