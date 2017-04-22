def bottles(x):
    x = int(x)
    for i in range(x):
        print ("")
        print ("%d bottles of beer on the wall, %d bottles of beer." % (x,x))
        x -= 1
        print ("Take one down, pass it around, %s bottles of beer on the wall." % (x))
bottles(input())
