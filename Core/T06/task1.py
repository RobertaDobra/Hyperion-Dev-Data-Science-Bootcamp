num1=1
num2=2
num3=3
if num1>num2:
    print("True; num1 is larger")
else:
    print("False; num2 is larger")
if num1%2 ==0:
    print("True; num1 is even")
else:
    print("False; num1 is odd")
if num1>num2 and num1>num3 and num2<num3:
    print("num1 is the largest, desc order: num1, num3, num2")
if num1>num2 and num2>num3:
    print("num1 is the largest, desc order: num1, num2, num3")
if num1>num2 and num1<num3:
    print("num3 is the largest, desc order: num3, num1, num2")
if num1<num2 and num1<num3 and num2<num3:
    print("num3 is the largest, desc order: num3, num2, num1")
if num1<num2 and num1<num3 and num2>num3:
    print("num2 is the largest, desc order: num2, num3, num1")
if num1<num2 and num1>num3 and num2>num3:
    print("num2 is the largest, desc order: num2, num1, num3")