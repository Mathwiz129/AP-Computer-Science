def square(num1):
    return num1*num1

def greater(num1, num2):
    if num1 > num2:
        return print(str(num1) + " is greater than " + str(num2))
    else:
        return print(str(num2) + " is greater than " + str(num1))

def char(str, index):
    if index > len(str):
        return print("Index out of range")
    else:
        return print(str[index])

newlist =[]
def sort(list, num1, num2):
    for x in list:
        if x > num1 and x < num2:
            newlist.append(x)
    return print(newlist)

newlist2 = []
def common(list1, list2):
    for x in list1:
        if x in list2:
            newlist2.append(x)
    return print(newlist2)
