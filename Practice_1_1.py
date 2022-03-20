# Practice one >>> Calculator application
import math

def operation1(int1, op, int2):
    if op == "+":
        rst = int1 + int2
    if op == "-":
        rst = int1 - int2
    if op == "/":
        if int2 != 0:
            rst = int1 / int2
        else:
            print("Warning: Enter the second number non-zero ")
    if op == "*":
        rst = int1 * int2
    print("result = ", rst)

def operation2(int1, op):
    if op == "radical":
        rst = math.sqrt(int1)
    if op == "factorial":
        rst = math.factorial(int1)
    print("result = ", rst)

def operation3(int1, op):
    x = math.radians(int1)
    if op == "sin":
        rst = math.sin(x)
    if op == "cot":
        rst = ((math.cos(x)) / (math.sin(x)))
    if op == "cos":
        rst = math.cos(x)
    if op == "tan":
        rst = math.tan(x)
    print("result = ", rst)

lst = ["+ ", "- ", "* ", "/ ", "radical ", "factorial ", "sin ", "cos ", "tan ", "cot "]
print("** alculator application **")
print("Supported operators >>>", lst)

int1 = float(input("Enter number 1 : "))
op = input("enter operation : ")
if (op == "+") or (op == "-") or (op == "/") or (op == "*"):
    int2 = float(input("Enter number 2 : "))
    operation1(int1, op, int2)

else:
    if (op == "radical") or (op == "factorial"):
        operation2(int1, op)
    if (op == "sin") or (op == "cos") or (op == "tan") or (op == "cot"):
        operation3(int1, op)
