#list of letter counts using for loop
def jay():
    num = int(input("How many words? "))
    string = []
    total = []
    print("Please enter %s words: " % (num))
    for i in range(0,num,1):
        new = input()
        string.append(new)
    for i in range(len(string)):
        total.append(len(string[i]))
    print (total)
jay()
