Boundary=99
while NoSwaps == True:
    NoSwaps=True
    for j in range (1,Boundary):
        FirstID=UserNameArray[j]
        SecondID=UserNameArray[j+1]
        if FirstID>SecondID:
            Temp=UserNameArray[j]
            UserNameArray[j]=UserNameArray[j+1]
            UserNameArray[j+1]=Temp
            NoSwaps=False
    Boundary-=1
    
    
