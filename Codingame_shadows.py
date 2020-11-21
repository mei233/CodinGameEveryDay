import sys
import math


'''
le site de Codingame https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()] # the starting position of Batman

# (0,0),(0,h-1),(w-1,0),(w-1,h-1)
l = 0
u = 0
r = w - 1
d = h - 1
# game loop
# U, R, L, D,
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # print(bomb_dir)
    #print(bomb_dir, file=sys.stderr, flush=True)
    if 'U' in bomb_dir:
        d = y
        y = math.ceil((y+u-1)/2)
    if 'D' in bomb_dir:
        u = y
        y = (y+d+1)//2
    if 'L' in bomb_dir:
        r = x
        x = math.ceil((x+l-1)/2)
    if 'R' in bomb_dir:
        l = x
        x = (x+r+1)//2

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
