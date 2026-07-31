n = 121
num= n 
new = 0 
while (num>0):
    ld = num % 10
    new = (new*10)+ld
    num = num//10
print(new)
if (new == n ):
    print("palindrome")
else:
    print("not palindrome")
    
