import turtle as t

def green_color():
    t.color("greenyellow")

def pink_color():
    t.color("pink")
    
def black_color():
    t.color("black")

def white_color():
    t.color("white")

def red_color():
    t.color("red")

def penup():
    t.up()   

def pendown():
    t.down()

def begin_fill():
    t.begin_fill()

def end_fill():
    t.end_fill()  

def draw_ondrag(x,y):
    t.ondrag(None)
    t.goto(x,y)
    t.ondrag(draw_ondrag)

# t.shape("turtle") #모양 거북이로 바꾸기
t.bgcolor("lightblue") # 배경색깔

t.onscreenclick(draw_ondrag) 
t.onkeypress(green_color,"g") #listen이랑 같이 써야가능
t.onkeypress(pink_color,"p")
t.onkeypress(black_color,"b")
t.onkeypress(white_color,"w")
t.onkeypress(red_color,"r")
t.onkeypress(penup,"Up")
t.onkeypress(pendown,"Down")
t.onkeypress(begin_fill,"Left") #그리기전에 누르고 그리고 난 뒤에 오른쪽 누르면 채워짐
t.onkeypress(end_fill,"Right")
t.listen()

t.done()