#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            if i < 8:
                print("{:02}, ".format(int(str(i) + str(j))), end="")
            else:
                print("{:02}".format(int(str(i) + str(j))))
