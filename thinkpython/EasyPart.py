print("Hello World")
message = "This is a message."
intiger = 39
print(message)
print(intiger)
#显然虽然pi的赋值小数位数极长，但是print的输出长度有限
pi=3.141459265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097
print(pi)
#python的字符串竟然可以用+和*，离散和python真NB
another_message = "This is another message."
new_message = message + another_message
print(new_message)
anther_newmessage = "Fxxk!"*3
print(anther_newmessage)
#python可以连续声明并赋值变量，神奇，c++好像也行？
x=y=1
#print(x,y)连续print x和y，中间会有 空格 间隔
print(x,y)
#print(xy) 显然x*y不能简写成xy
print(message,intiger,new_message)#自动识别变量类型太酷了

#----Functions----#
type_message = type(message)
print(type_message)

N = int(pi)
print(N)
message=pi#啊，竟然可以给字符串类型的变量赋值一个浮点数,好吧，它变成浮点数了
#message=str(pi)
type_message = type(message)
print(type_message)

#向下取整的除法 //
print(5//2)
print(5/2)#直接使用除法会得到一个浮点数

#取模运算 %
print(18%7)

#Bool类型
print(True)
print(5>=5)
print(5==5)
print(5<5)

# and or not 与 或 非
print(True and True)
print(True and False) 
print(True or False)
print(not True)
print(not True or False)

#if
a = 5 
if a>0:
    print("a is positive")

if a<0:
    pass #pass语句什么都不做，可以用作占位符
else:
    print("a is zero or negative")
    
if a>0:
    print("a is positive")
elif a==0:
    print("a is zero")
else:
    print("a is negative")


if a>0:
    if a%2==0:
        print("a is even and positive")
    else:
        print("a is odd and positive")
else:
    pass

if a>0 and a%2==0:
    print("a is even and positive")
elif a>0 and a%2!=0:
    print("a is odd and positive")
else:
    pass

