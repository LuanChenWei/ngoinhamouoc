for i in range(0,6,):
    print("*" * i )
else:
    print("\n")

for i in range(5,0,-1):
    print("*" * i )
else:
    print("\n")

for i in range(0,6):
    print(' '*(5-i) + i*"*" )
else:
    print("\n")

for i in range(0,5):
    print(i*" " + "*"*(5-i))
