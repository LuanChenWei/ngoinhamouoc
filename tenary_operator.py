import random


num = random.uniform(0,100)
intnum = int(num)

num_check = intnum % 2 == 0
if num_check :
    print('{} is even number'.format(intnum))
else:
    print('{} is odd number'.format(intnum))

