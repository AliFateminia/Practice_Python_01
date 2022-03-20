# Practice four >>> Calculate the average
name = input("Enter name : ")
LastName = input("Enter LastName : ")
n = int(input("Enter the number of lessons : "))
lst = []
x = average = 0
for i in range(n):
    print("Enter the number of lesson ", i, ":")
    lst.insert(i, (float(input())))
    x += lst[i]
    if i == n - 1:
        average = round(x / n, 2)
        print("average = ", average)
        if average >= 17:
            print(name, LastName, "is a Great student")
        if 12 <= average < 17:
            print(name, LastName, "is a Normal student")
        if average < 12:
            print(name, LastName, "is a Fail student")

