#module模块的import
import math
#这个反而更像是引入了类似于c++中的using namespace std，或者说引入一个带有大量函数的class类
n = 10
pi = math.pi#看来这个math类中还有一些variablites可以调用
m = math.ceil(n-pi)#ceil向上取整函数
print(m)
print(math.floor(n-pi))#floor向下取整函数
print(math.sqrt(n))#求平方根函数
print(math.pow(2,3))#求2的3次方函数 
print(math.log(n))#求自然对数函数
print(math.exp(2))#求e的2次方函数

print(math.sin(math.radians(45)))

print(math.sin(pi/2))#求sin函数
print(math.cos(pi/2))#求cos函数&&&神奇的结果，并非0而是一个极小的数字
print(math.tan(pi/4))#求tan函数
print(math.asin(1))#求asin函数
print(math.acos(1))#求acos函数
print(math.atan(1))#求atan函数
print(math.degrees(pi/2))#角度制转弧度制函数
print(math.radians(180))#弧度制转角度制函数

#def写入新的函数
def divides(messsage):
    print("-----------------",messsage,"-------------------")

divides("def function")

def get_sum(n):
    return fibinacci(n)+1

def fibinacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibinacci(n-1)+fibinacci(n-2)
    
n = 12
print(fibinacci(n))
print(n)#这个n是全局变量，所以在函数中修改了值，但是外部的n并没有改变,这样调用函数不会改变外部变量的值

print(get_sum(12))#看来函数的定义次序好像没啥影响，但是调用必须在定义之后（不懂python有没有声明这一说）
#print(fibinacci("2"))     #最后报错原因竟然是str类型没减法，而不是函数调用不允许str类型
#由此发现函数不指定传入参数的类型，只要能运行就允许传入任何类型,但是c++需要用template <typename T>实现多类型参数
def print_twice(message):
    print(message)
    print(message)    
print_twice("hello world")
print_twice(123)

print(print_twice("5"))#没有返回值的函数返回的实际是NONE
print(type(print_twice('5')))#None的类型是NoneType

divides("Practice")

def right_justify(meessage):
    print(" "*(30-len(meessage))+meessage)
    
right_justify("Lrics")
#这还能用函数作为函数的参数(高阶函数，函数嵌套?)
def Do_twice(function,args):
    function(args)
    function(args)
    
Do_twice(print_twice,"I LOVE YOU!")

print("-"*30,end=" ")#修改print的默认结束符（默认是换行符）
print("+")

#递归
divides("Recursion")
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
    
print(f(5))

print("Please input a number:")

num = int(input())
print("The factorial of",num,"is",f(num))

#布尔函数
divides("Boolean Function")
def is_prime(n):
    for i in range(2,int(n**0.5)):#what！python 可以用**0.5取平方根
        if n%i==0:
            return False
        return True

print(is_prime(17))
print(is_prime(12))

#Practice
divides("Practice")

import time
print(time.time())#获取当前时间戳
print(type(time.time()))#时间戳的类型是float
Time = int(time.time())
seconds = Time%60
minutes = Time//60%60
hours = Time//3600%24 + 8 #北京时间比utc时间早8小时
days = Time//38400
print("Current time is",days,"days",hours,":",minutes,":",seconds)

print("Plesae input four numbers:")
#input不够智能看起来，不能在同一行输入多个值，只能分开输入
a,b,c,n= map(int,input().split())
#a=int(input())
#b=int(input())
#c=int(input())
#n=int(input())
def check_Fermat(a,b,c,n):
    if(n>2 and a**n+b**n==c**n):
        print("Oh,Fermat is wrong!")
    elif(n<=2):
        print("Please input a number greater than 2")
    else:
        print("No,This is invalid")

check_Fermat(a,b,c,n)

def ack(m,n):
    if m==0:
        return n+1
    elif n==0 and m>0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    else:
        return "Invalid input"
    
print(ack(3,4))

def is_palindrome(str):
    for i in range(int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("python"))

def is_power(m,n):
    if m==n:
        return True
    elif m%n==0:
        return is_power(m//n,n)
    else:
        return False
    
print(is_power(16,2))
#这种求最大公约数的方法叫 辗转相除法
def gcd(a,b):
    if b==0:
        return a
    elif a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)
    
print(gcd(24,1568))
