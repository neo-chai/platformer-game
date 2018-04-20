import turtle as t
grid=[[""]*4,[""]*4,[""]*4,[""]*4]

def insertnumber(grid):

	emptyspace=[]

	for x in range(4):
		for y in range(4):

			if grid [x][y]=="":
				emptyspace.append((x,y))
	spot =random.choice(emptyspace)
	grid[spot[0]][spot[1]]=random.choice([2,4,2,2,2,2,2,2])
def is_win(grid):
	for x in range(4):
		for y in  range(4):
			if grid [x][y]==2048:
				return True
	return False
def left (grid):
	for y in range (4):
		for x in range (4): 
			if grid [y][x]=='': continue
			pickedup = grid [y][x]
			grid [y][x] =''
			for spot in range (x,-2,-1) :
				if grid [y][spot]=='': continue
				if spot==-1:
					grid [y][0]=pickedup
				if pickedup==grid[y][spot]:
					grid [y][spot]*=2
				else:
					grid[y][spot+1]=pickedup












def square (size,pos,color1,color2):
	t.penup()
	t.goto(pos)
	t.pendown()
	t.color(color1,color2)
	t.begin_fill()
	for i in range(4):
		t.forward(size)
		t.right(90)
	t.end_fill()

backgroundcolor="#47856c"
gridcolor="#2dd290"
tilecolors={	2:"#42d79b",
				4:"#57dba6",
				"default":"#6ce0b1"
				}

import random
def background():
	square(600,(-300,300), backgroundcolor,backgroundcolor)
	for i in range(4):
		for j in range(4):
			square(100,(-300+40+140*i,300-40-140*j),gridcolor,gridcolor)
			if random.random() < .5:
				square(100,(-300+40+140*i,300-40-140*j),tilecolors[2],tilecolors[2])

t.speed("fastest")
t.hideturtle()
background()
t.done()