
# The program must first read the initialization data from standard input. Then, within an infinite loop, read the device data from the standard input and provide to the standard output the next movement instruction.
# Initialization input

# Line 1 : 2 integers W H. The (W, H) couple represents the width and height of the building as a number of windows.

# Line 2 : 1 integer N, which represents the number of jumps Batman can make before the bombs go off.

# Line 3 : 2 integers X0 Y0, representing the starting position of Batman.
# Input for one game turn
# The direction indicating where the bomb is.
# Output for one game turn
# A single line with 2 integers X Y separated by a space character. (X, Y) represents the location of the next window Batman should jump to. X represents the index along the horizontal axis, Y represents the index along the vertical axis. (0,0) is located in the top-left corner of the building.









import sys

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
left_x = 0
right_x = w
top_y = 0
bottom_y = h

# game loop
while True:
    # the direction of the bombs from batman's current location:
    # U, UR, R, DR, D, DL, L or UL
    direction = input()
    # we crate he string to get the direction #
    if 'U' in direction:
        bottom_y = y - 1
        # set the new bottom boundarie #
    elif 'D' in direction:
        # set the new top boundarie #
        top_y = y + 1
    if 'L' in direction:
        right_x = x - 1
        # same for the left and right #
    elif 'R' in direction:
        left_x = x + 1
    # caclcuate the new location of batman #
    x = (left_x + right_x) // 2
    y = (top_y + bottom_y) // 2
    print(x,y) 