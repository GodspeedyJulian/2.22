def FindRepeats():
    
    Repeats = 0
    for i in range(0, len(UserNameArray)-1):
        FirstID = (UserNameArray[i])[:6]
        SecondID = (UserNameArray[i+1])[:6]
        if FirstID == SecondID:
            print(UserNameArray[i+1])
            Repeats = Repeats +
        if Repeats == 0:
            print("The array contains no repeated UserIDs")
        else:
            print(“There are “, Repeats, " repeated UserIDs")

