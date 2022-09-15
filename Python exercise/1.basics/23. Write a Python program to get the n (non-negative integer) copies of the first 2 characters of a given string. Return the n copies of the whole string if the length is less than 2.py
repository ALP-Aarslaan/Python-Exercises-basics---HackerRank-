string = input("enter a string : ")
n = int(input("enter how many copy you want : "))
if len(string) < 2:
    print(string*n)
else:
    print(string[:2]*n)