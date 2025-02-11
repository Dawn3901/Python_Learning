import math
#class 类
class Point:
    """represents a point in 2-d space"""
    
entity =  Point()
##属性attribute
entity.x = 3.0
entity.y = 4.0

def Print_Point(p):
    print("(%g,%g)" % (p.x,p.y)) #%g运算符能够自动简化输出中多余的0与小数点,常用于不指定输出格式的输出中
    p.x+=1#看来p是c++中类似于引用的写法，会改变传入的参数的值
    p.y+=1
    
Print_Point(entity)
Print_Point(entity)

def distance_between(A,B):
    distance = math.sqrt((A.x-B.x)**2+(A.y-B.y)**2)
    return distance

entity_2 = Point()
entity_2.x = -1.0
entity_2.y = 5.0
print(distance_between(entity_2,entity))

##矩形
class Rectangle:
    """Represnet a rectangle
    attributes:width,length,corner(矩形的左下角)    
    """
    
Rectangle_1 = Rectangle()
Rectangle_1.length = 10
Rectangle_1.width = 5
Rectangle_1.corner = Point()
Rectangle_1.corner.x = 2.0
Rectangle_1.corner.y = -1.0

def area_of_rectangle(rect):
    area = rect.width * rect.length
    return area

print(area_of_rectangle(Rectangle_1))

def find_center(rect):
    center = Point()
    center.x = rect.corner.x+rect.length/2
    center.y = rect.corner.y+rect.width/2
    return center

entity_3 = find_center(Rectangle_1)
Print_Point(entity_3)

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy

move_rectangle(Rectangle_1,-5,2.5)
Print_Point(find_center(Rectangle_1))

##copy
import copy

box_1 = Rectangle()
box_1.width = 500
box_1.length = 888
box_1.corner = Point()
box_1.corner.x = -550
box_1.corner.y = -400
box_2 = copy.copy(box_1)

print(box_1 is box_2,"意味着自定义的对象的复制不是“引用”，即不是同一的")
print(box_1 == box_2,"意外的尽管两者的所有value都相等但是不是==，因为python不知道两个对象相等的条件")

print(box_2.corner is box_2.corner,"简单的copy的内嵌还是同一的")

box_3 = copy.deepcopy(box_1)
print(box_3.corner is box_1.corner,"deepcopy的复制是真正的新开一个实例，并且实例的value都于被复制的相同")

#调试
isinstance(entity,Point)
isinstance(entity_3,Rectangle)
hasattr(Point,'width')
hasattr(Rectangle,'x')#内嵌也是false

#Practice
class Circle:
    """Represent a circle
    Atrributes:center,radius    
    """

circle = Circle()
circle.center = Point()
circle.center.x = 150
circle.center.y = 100
circle.radius = 75

def point_in_circle(p,c):
    if distance_between(p,c.center) <= c.radius:
        return True
    return False
print(point_in_circle(entity,circle))


def draw_rect(turtle,rect):
    turtle.penup()
    turtle.goto(rect.corner.x,rect.corner.y)
    turtle.pendown()
    for i in range(2):
        turtle.fd(rect.length)
        turtle.lt(90)
        turtle.fd(rect.width)
        turtle.lt(90)

import turtle
t = turtle.Turtle()
turtle.delay(10)
draw_rect(t,box_1)
turtle.mainloop()
