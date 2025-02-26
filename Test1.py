#Task 1
print("TASK 1:")
string = input("Enter a string that contains both letters and numbers: ")

def test1(str1):
    new_str = ""
    for i in str1:
        if i.isalpha():
            new_str += i
    return new_str

def test2(list1):
    return max(list1) - min(list1)

def test3(list1, list2):
    if test2(list1) > test2(list2):
        print("The list, "+ str(list1) + " has the largest range of "+ str(test2(list1))+".")
        return list1
    else:
        print("The list, "+ str(list2) + " has the largest range of "+ str(test2(list2))+".")
        return list2