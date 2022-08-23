# Date : Aug 23 2022
# Author : Kanghoon
# #

'''
Input :
이동을 위한 W,A,S,D 입력 /
Output :
현재 중심 물체를 이동하여 움직임을 표현 / 물체가 사과위치에 다다랐을 경우 사과를 먹은 것으로 간주
Object :
사용자(2)가 모든 사과(3)을 다 먹으면 게임 종료
경로는 (0)으로 표시, 지나갈 수 없는 경로는 (1)로 표시

'''

import tkinter as tk

root = tk.Tk()
WIDTH = 800
HEIGHT = 800
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
x0 = (WIDTH * 5) / 10
y0 = (HEIGHT * 5) / 12
x1 = (WIDTH) / 2
y1 = (HEIGHT) / 2
text = canvas.create_text(x0, y0*2-20, text="Keys to move = a,d,w,s")

class plum() :
    def __init__(self) -> None:
        super().__init__()


# 기본 이중 리스트 생성
board1010 = [[0 for col in range(5)] for row in range(5)]
print(board1010)
ME = 2
# 기본 맵 설정
board1010[1][1] = ME
for i in range (5):
    board1010[0][i] = 1
    board1010[4][i] = 1
    board1010[i][0] = 1
    board1010[i][4] = 1
print(board1010)

player = canvas.create_rectangle
def draw_rect():
    player((x1, y1, x1 + 10, y1 + 10), fill="green")
def del_rect():
    player(x1, y1, x1 + 10, y1 + 10, fill="white")
def move(event):
    global x1, y1
    print(event.char)
    if event.char == "a":
        del_rect()
        x1 -= 10
    elif event.char == "d":
        del_rect()
        x1 += 10
    elif event.char == "w":
        del_rect()
        y1 -= 10
    elif event.char == "s":
        del_rect()
        y1 += 10
    draw_rect()
root.bind("<Key>", move)
root.mainloop()
keyinput = ''

'''
board1010 = [20][20]
'''

while() :
    exit




