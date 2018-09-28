
from cs50 import get_int

#Get user input for height of the blocks
height = -1
while height<0 or height>23:
    height = get_int("Height: ")

#What row are we on?
for row in range(height):
    #First spaces
    for spaces in range(height-row-1):
        print(end=" ")

    #First Blocks
    for first in range(row+1):
        print(end="#")

    #Gap
    print(end="  ")

    #2nd Blocks
    for second in range(row+1):
        print(end="#")

    #Next line
    print()