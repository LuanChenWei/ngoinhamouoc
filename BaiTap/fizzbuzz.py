

a = int(input('nhap vao so dau tien: '))

b = int(input('nhap vao so thu hai: '))

c = range(a, b+1)

for y in c:
    if y % 3 == 0 and y % 5 == 0:
        print('lizzbuzz')
    elif y % 3 == 0:
        print('lizz')
    elif y % 5 == 0:
        print('buzz')

    else:
        print(y)
