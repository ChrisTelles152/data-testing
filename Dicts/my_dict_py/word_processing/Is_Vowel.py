#check if an input letter is a vowel
def is_vowel(string):
    if len(string) == 1:
        if string in ("a","e","i","o","u"):
            return True
        else:
            return False
    else:
        return "Please enter only one character"
is_vowel(input())
