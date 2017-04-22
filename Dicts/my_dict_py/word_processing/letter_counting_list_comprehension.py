#list of letter counts using list comprehension
def lay():
    num = int(input("How many words? "))
    print("Please enter %s words: " % (num))
    total = [list(len(x) for x in input().split()) for i in range(num)]
    print (total)
    
lay()
