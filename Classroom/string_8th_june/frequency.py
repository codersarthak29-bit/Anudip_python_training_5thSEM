#wap to input a sentence and display the frequecy of vowels present in that sentence ignoring the case
sentence = input("Enter a sentence: ")
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0
for ch in sentence:
    if ch in "aA":
        acount += 1
    elif ch in "eE":
        ecount += 1
    elif ch in "iI":
        icount += 1
    elif ch in "oO":
        ocount += 1
    elif ch in "uU":
        ucount +=1
if acount > 0:
    print("a =", acount)
if ecount > 0:
    print("e =", ecount)
if icount > 0:
    print("i =", icount)
if ocount > 0:
    print("o =", ocount)
if ucount > 0:
    print("u =", ucount)



print("Number of vowels =", acount + ecount + icount + ocount + ucount)