secret=9
i=0
while i<3:
    g=int(input("Enter Guess"))
    if g==secret:
        print("U Guessed Correct!!!")
        break
    i+=1
    #if i==3:
     #print("U ran out of guesses")
else:
    print("Sorry, U failed")
