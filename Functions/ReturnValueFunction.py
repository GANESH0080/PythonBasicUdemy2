
#Function taking some argument and returning value
def returnMultiply(a,b) :
    "This is function"
    c = a * b
    return c

multiply2number = returnMultiply(10,30)
print(multiply2number)

print("____________________________________________")

#Function taking some argument but not returning any value
def noreturn(a,b) :
    "This is function"
    c = a + b
    print(c)

noreturn(10,30)

print("____________________________________________")

# Function without argument but return type
def returndata():
    "This is function"
    c = 100
    return c


returnvalue = returndata()
print(returnvalue)
