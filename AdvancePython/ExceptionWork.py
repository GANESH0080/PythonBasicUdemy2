
try:
    #Enter first value as alphanumber so that you will get Exception
    user_input1 = input("Please enter first number : ")
    user_input2 = input("Please enter second number : ")
    c = int(user_input1 ) +  int(user_input2)
    print(c)
except:
    print("Please enter correct numbers, you have entered incorrect number")

finally:
    print("Finally will execute even after execption or not")