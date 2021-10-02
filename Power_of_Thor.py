# Rules
# Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".

#Once the program starts you are given:

#   the variable lightX: the X position of the light of power that Thor must reach.
#    the variable lightY: the Y position of the light of power that Thor must reach.
#    the variable initialTX: the starting X position of Thor.
#    the variable initialTY: the starting Y position of Thor.

# At the end of the game turn, you must output the direction in which you want Thor to go among:
# N (North)
# NE (North-East)
# E (East)
# SE (South-East)
# S (South)
# SW (South-West)
# W (West)
# NW (North-West)
# Each movement makes Thor move by 1 cell in the chosen direction.
 

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    command = ''
    if initial_ty < light_y:
        command += 'S'
        initial_ty += 1
    if initial_ty > light_y:
        command += 'N'
        initial_ty -= 1

    if initial_tx < light_x:
        command += 'E'
        initial_tx += 1
    if initial_tx > light_x:
        command += 'W'
        initial_tx -= 1
    
    
   
    # A single line providing the move to be made: N NE E SE S SW W or NW
    [print(command)]
