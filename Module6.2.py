list = ["Alice", 27, "Bob", 14, "Charlie", 22, "David", 33, "Eve", 19, "Frank", 41, "Grace", 18, "Hank", 28, "Ivy", 37, "Jack", 25, "Kara", 31, "Liam", 24, "Mia", 30, "Noah", 29, "Olivia", 17, "Paul", 34, "Quinn", 21, "Rose", 26, "Sam", 35, "Tina", 23, "Uma", 20, "Vince", 32, "Wendy", 38, "Xander", 16, "Yara", 39, "Zane", 36]  #Used Copilot to generate list
str1 = ''
list1 = []

for x in list:
    if isinstance(x, str):
        str1 += x
    elif isinstance(x, int):
        list1.append(x)


print(str1)
print(list1)
