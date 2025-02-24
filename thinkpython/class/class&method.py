#class and method 类和方法


def int_to_time(seconds):
    if seconds<0:
        seconds = 86400-seconds
    t=Time()
    t.second = seconds%60
    t.minute = (seconds//60)%60
    t.hour = (seconds//3600)%24
    return t

class Time:
    """respresent time"""
    #init
    def __init__(self,hour=0,minute=0,second=0):#这样写，不传入对应参数时默认值是0，传入参数则替换
        self.hour = hour
        self.minute = minute
        self.second = second
    #str
    def __str__(self):#返回字符串类型，一般用于打印对象，检查是否出错
        return "%.2d-%.2d-%.2d" % (self.hour,self.minute,self.second)

    #def print_Time(self):
        #print("%.2d-%.2d-%.2d" % (self.hour,self.minute,self.second))
        
    def time_to_int(self):
        return self.hour*3600+self.minute*60+self.second
    def increment(self,seconds):
        return int_to_time(self.time_to_int()+seconds)
    def is_after(self,another):
        return self.time_to_int() > another.time_to_int()
    #操作符重构
    def __add__(self,another):
        #基于类型分发 type-based dispatch
        if isinstance(another,Time):#time+time
            seconds = self.time_to_int() + another.time_to_int()
        else:#time+ int 但是不满足交换律，即int+time会报错，解决有__radd__
            seconds = self.time_to_int() + another
        return int_to_time(seconds)
    def __radd__(self,another):
        return self.__add__(another)
    
now = Time()
now.hour = 17
now.minute = 56
now.second = 55
#now.str() X
print(now)
end = now.increment(360)
print(end)
print(end.is_after(now))

t1 = Time()
print(t1)
t2 = Time(15,6)#没有传入第三个参数second,默认为0
print(t2)
t3= Time()
t3 = t1+t2
print(t3)
t4 = Time()
t4 =t3+506
print(t4)
t5 = Time()
t5 = 506 + t3
print(t5)


#Point
class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%g,%g)" % (self.x,self.y)
    def __add__(self,another):
        if isinstance(another,Point):
            result = Point(self.x + another.x,self.y + another.y)
        else:
            result = Point(self.x+another[0],self.y+another[1])
        return result
    def __radd__(self,another):
        return self.__add__(another)
A = Point(5,-2)
B = Point(-2.4,3.9)
C = Point()
C = A+B
print(C)
print(A)
D = Point()
D =(2.7,-1) + C
print(D)

#多态(以sum为例)
    #sum基于 + 实现，所有提供 +(__add__) 的对象都可以使用，例如point
    #sum第一个参数是list,dict,tuple，第二个参数是 零元 （默认是0）
E = sum([A,B,C,D],Point(0,0))
print(E)

#调试
def print_attributes(obj):#函数会将对象的全部属性和属性值打印出来
    for attr in vars(obj):#vars函数接受一个对象，并将返回对象的属性名称和值组成的字典
        print(attr,getattr(obj,attr))#getattr函数接受一个对象和属性名称，返回属性的值

#print_attributes(Point)

#Practice
class Kangaroo:
    def __init__(self,name,pouch_contents = None):
        self.name = name
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents
        
    def put_in_pouch(self,item):
        self.pouch_contents.append(item)
        
    def __str__(self):
        t = [self.name + 'has pouch contents:']
        for items in self.pouch_contents:
            s = ' '+ object.__str__(items)
            t.append(s)
        return '\n'.join(t)
    
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
#感觉怪怪的，这里为啥输出的是含有"kangaroo object"而不是 roo
print(kanga)
print(roo)
