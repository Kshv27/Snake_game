a = input("Enter the value of A:")
b = input("Enter the value of B:")
c = input("Enter the value of C:")

if a>b:
    if a>c:
        print(a,"is greatest")
    else:
        print(c,"is greatest")
elif b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")                