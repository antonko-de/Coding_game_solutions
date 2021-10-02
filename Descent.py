#At the start of each game turn, you are given the height of the 8 mountains from left to right.
# By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).
# Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass. 





# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    # a list to append all mountains in #
    mountains = []
    for i in range(8):
        mountain_h = int(input())
        mountains.append(mountain_h)
        # find the highest mountain #
        max_m = max(mountains)
    
    # The index of the mountain to fire on.
    print(mountains.index(max_m))
