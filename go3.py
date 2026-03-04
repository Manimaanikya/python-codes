num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
num3=int(input('enter 3rd number'))
if num2>=num1 and num1>=num3:
    print('greater',num1)
elif num2>=num1 and num2>=num3:
    print("greater",num2)
else:
    print("grater",num3)
