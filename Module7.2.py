def posts():
    num = input("Enter a number: ")
    largernum = input("Enter a larger number: ")
    if num > largernum:
        print(num + " is less than " + largernum)
        posts()
    for x in range(int(num), int(largernum)+1):
        print(x)

posts()