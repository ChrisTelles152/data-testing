#list of letter counts using mapping
def kay():
    num = int(input("How many words? "))
    print("Please enter %s words: " % (num))
    letters = [""] * num
    this = list(map(stringappender,letters))
    print (this)

def stringappender(string):
    string = []
    total = []
    new = input()
    string.append(new)
    total.append(len(string[0]))
    return total

kay()
