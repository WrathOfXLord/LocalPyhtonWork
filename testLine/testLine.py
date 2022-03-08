import sys


def ioTest():
    my_file = open("test.txt", "r")
    lines = my_file.readlines()
    i = 0
    List = []
    for l in lines:
        splitCount = len(l.split(" "))
        splitted_l = l.split(" ")
        print("split count is : " + str(splitCount))
        i += 1
    


ioTest()
