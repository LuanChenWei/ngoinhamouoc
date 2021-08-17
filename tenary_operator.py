import random


num_check = random.uniform(0,100)
intnum = int(num_check)
if intnum % 2 == 0:
    print('{} is even number'.format(intnum))
else:
    print('{} is odd number'.format(intnum))

