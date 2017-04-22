def bottles ():
    for i in range(99,0,-1):
        many = ""
        if i > 1:
            many = "bottles"
        elif i == 1:
            many = "bottle"
        print("%s %s of beer" % (i,many))

bottles()
