a = float(input('nhap so bat ky: '))

if a % 2 == 0:
    print('{} la so chan'.format(a))
elif a % 2 == 1:
    print('{} la so le'.format(a))
else:
    print('{} khong phai so tu nhien'.format(a))

