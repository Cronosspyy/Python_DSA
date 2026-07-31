num1 = 112
num2 = num1
print("before update")
print("num 1 =",num1)
print("num 2 =",num2)

print("num1 points to : ",id(num1))
print("num1 points to : ",id(num2))

num2=22

print("after update")
print("num 1 = ",num1)
print("num 2 =", num2)

print("num1 points to : ",id(num1))
print("num1 points to : ",id(num2))