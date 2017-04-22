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
reverse_string(input())
