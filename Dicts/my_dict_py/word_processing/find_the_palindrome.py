#find out if an input string is a palindrome
def palindrome(s):
    test = False
    l = len(s)
    ordeal = ""
    pali = 0
    if l % 2 == 0:
        ordeal = "even"
    elif l % 2 == 1:
        ordeal = "odd"
    for i in range(l):
        d = ""
        if s[i] != l:
            if i+1 != l and s[i] == s[i+1]:
                d = s[i] + s[i+1]
                print(i,l,s[i],"I have found a palindrome to the right, " + d)
                truth = True
                pali += 1
            elif i != 0 and s[i] == s[i-1]:
                d = s[i] + s[i-1]
                print(i,l,s[i],"I have found a palindrome to the left, " + d)
                truth = True
                pali += 1
            else:
                print(i,l,s[i],"else")        
    if truth == True:
        print ("there is at least one palindrome, " + str(pali))
    else:
        print ("there are no palindromes") 
                    
palindrome(input())


##############
####unfinished. can only find the amount of twin characters nearby####
##############
