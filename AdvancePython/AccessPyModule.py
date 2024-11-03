#Whenever we are importing any module that module executable code will run
import PyModule


#We are calling module functions (Without class fucntions) using file name
#We can call parameterised functions, Return functions etc
PyModule.testingmodulefucntion()
PyModule.sum(10,20)
result = PyModule.returnmethod(10 ,40)
print(result)

# We are calling class functions as well using object
test= PyModule.Abc()
test.testing()