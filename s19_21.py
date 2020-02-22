TotalValue=0
ZeroCount=0
for i in range (1,100):
    TotalValue +=Result[i]
    if Result[Index]=0:
        ZeroCount+=1
print("The average is " + str(TotalValue/100))
print("the number of elements with a zero value is " + str(ZeroCount))
