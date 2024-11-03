class B:
    #function with no argument and no return value
    def sampleFunction(self):
        print("Hello Ganesh")

    # function with 2 arguments and no return value
    def argumentFunction(self, val1, val2):
        val3 = val1 + val2
        print(val3)

    # function with 2 arguments and returning value
    def argumentandretunFunction(self, val1, val2):
        val3 = val1 + val2
        return val3


#Creating object for class A
test = B()

#Calling function which has no argument and no return value
test.sampleFunction()

#Calling function which has 2 arguments and no return value
test.argumentFunction(15,20)

#Calling function which has 2 arguments and returning value
res = test.argumentandretunFunction(40,40)
print(res)