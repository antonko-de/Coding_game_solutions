#  Write a program that prints the temperature closest to 0 among input data. 
# If two numbers are equally close to zero, 
# positive integer has to be considered closest to zero 
# (for instance, if the temperatures are -5 and 5, then display 5)


n = int(input())  # the number of temperatures to analyse1
if n == 0:
    print(0)
    exit()
# the corner case where we will receive no string #
closest = 5526
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    a = abs(t)
    if a < abs(closest):
        closest = t
    # main statement check #
    elif t == closest and closest < 0:
        closest = t
    # corner case where we have same two negativies #
    elif a == abs(closest) and closest < 0:
    # corner case where we have same absolute values #
        closest = a

print(closest)