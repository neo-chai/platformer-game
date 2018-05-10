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

def copy(grid):
	return [row.copy() for row in grid]

def valid_move(grid, move):
	grid2 = copy(grid)
	move(grid2)
	if grid2 != grid:
		return True
	return False

def is_lose(grid):
	if not valid_move(grid,left) and not valid_move(grid,right) and not valid_move(grid,up) and not valid_move(grid,down):
		return True
	else :
		return False




def left (grid):
	for y in range (4):
		for x in range (4): 
			if grid [y][x]=='': continue
			pickedup = grid [y][x]
			grid [y][x] =''
			for spot in range (x,-2,-1) :
				if spot==-1:
					grid [y][0]=pickedup
					break
				if grid [y][spot]=='': continue
				if pickedup==grid[y][spot]:
					grid [y][spot]*=2
					break
				else:
					grid[y][spot+1]=pickedup
					break

def right (grid):
	for y in range (4):
		for x in range (3,-1,-1): 
			if grid [y][x]=='': continue
			pickedup = grid [y][x]
			grid [y][x] =''
			for spot in range (x,5) :
				if spot==4:
					grid [y][3]=pickedup
					break
				if grid [y][spot]=='': continue
				if pickedup==grid[y][spot]:
					grid [y][spot]*=2
					break
				else:
					grid[y][spot-1]=pickedup
					break

def up (grid):
	for x in range (4):
		for y in range (4): 
			if grid [y][x]=='': continue
			pickedup = grid [y][x]
			grid [y][x] =''
			for spot in range (y,-2,-1) :
				if spot==-1:
					grid [0][x]=pickedup
					break
				if grid [spot][x]=='': continue
				if pickedup==grid[spot][x]:
					grid [spot][x]*=2
					break
				else:
					grid[spot+1][x]=pickedup
					break

def down (grid):
	for x in range (4):
		for y in range (3,-1,-1): 
			if grid [y][x]=='': continue
			pickedup = grid [y][x]
			grid [y][x] =''
			for spot in range (y,5) :
				if spot==4:
					grid [3][x]=pickedup
					break
				if grid [spot][x]=='': continue
				if pickedup==grid[spot][x]:
					grid [spot][x]*=2
					break
				else:
					grid[spot-1][x]=pickedup
					break






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

def tile(pos, number):
	if number in tilecolors:
		square(100,pos,tilecolors[number], tilecolors[number])
	else:
		square(100,pos,tilecolors["default"], tilecolors["default"])
	t.goto((pos [0]+50,pos [1]-85))
	t.color ("black")
	t.write(number,align="center",font=("Times New Roman",48,"normal"))


def drawgrid(grid):
	for x in range (4):
		for y in range (4):
			if grid [y][x] != "":
				tile((-300+40+140*x,300-40-140*y),grid[y][x])
 

def display():
	t.clear()
	background()
	drawgrid(grid)
	t.update()

def handleleft ():
	if valid_move(grid,left):
		left (grid)
		insertnumber(grid)
		display()
		if is_lose(grid):
			t.penup()
			t.goto((0,0))
			t.pendown()
			t.write("you lose", align="center", font=("Arial", 48, "bold"))
			t.update()

def handleright():
	if valid_move(grid,right):
		right (grid)
		insertnumber(grid)
		display() 
		if is_lose(grid):
			t.penup()
			t.goto((0,0))
			t.pendown()
			t.write("you lose", align="center", font=("Arial", 48, "bold"))
			t.update()


def handleup ():
	if valid_move(grid,up):
		up(grid)
		insertnumber(grid)
		display()
		if is_lose(grid):
			t.penup()
			t.goto((0,0))
			t.pendown()
			t.write("you lose", align="center", font=("Arial", 48, "bold"))
			t.update()

def handledown ():
	if valid_move(grid,down):
		down (grid)
		insertnumber(grid)
		display()
		if is_lose(grid):
			t.penup()
			t.goto((0,0))
			t.pendown()
			t.write("you lose", align="center", font=("Arial", 48, "bold"))
			t.update()

t.onkey(handleleft,"Left")
t.onkey(handleright,"Right")
t.onkey(handleup,"Up")
t.onkey(handledown,"Down")




insertnumber(grid)
insertnumber(grid)
t.tracer(0,0)
t.hideturtle()
display()
t.listen()
t.mainloop()