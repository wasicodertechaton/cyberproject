#inout
num1=float(input("enter your first number:"))
num2=float(input("enter your second number:"))

#processing
sum=(num1+num2)
sub=(num1-num2)
mul=(num1*num2)
rem=(num1/num2)
avg=(num1*num2/2)

#output
print("sum of numbers:",sum)
print("sub of your numbers:",sub)
print("multiplication opf you rnumbers:",mul)
print("division of your numbers is:",rem)
if sub==0:
    print("try again")
else:
    print("sub",sub)