
num = 1

while num <= 10:
    for i in range(10):
        print("{} * {} = {}".format(num, i, (num * i)))
    print()
    num += 1
