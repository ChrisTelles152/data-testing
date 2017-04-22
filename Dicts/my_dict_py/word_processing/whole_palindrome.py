def reverse_string(string):
    length = len(string)
    full = list(string)
    new = ""
    if length != 0:        
        for i in range(length):
            full[i] = string[length-(1+i)]
        new = "".join(full)
        return new
    else:
        return "Please input a string."

def palindrome(s):
    reverse_string(s)
    reverse = reverse_string(s)
    if s == reverse:
        print ("success")
    else: 
        print ("failure")

palindrome(input())
