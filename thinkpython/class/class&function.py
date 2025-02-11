##class and function
#Time
class Time:
    """Time of day
    attributes:hour,minute,second
    """
def print_Time(t):
    print("%0.2d:%0.2d:%0.2d"%(t.hour,t.minute,t.second))

t1  = Time()
t1.hour = 12
t1.minute = 43
t1.second = 9
print_Time(t1)
t2 = Time()
t2.hour = 12
t2.minute = 13
t2.second = 55

#Prototype原型（纯函数）
def add_time(t1,t2):
    sum = Time()
    sum.second = (t1.second+t2.second)%60
    sum.minute = ((t1.second+t2.second)//60 + (t1.minute+t2.minute))%60
    sum.hour = (((t1.second+t2.second)//60 + (t1.minute+t2.minute))//60 + (t1.hour+t2.hour))%24
    return sum
print_Time(add_time(t1,t2))

#modifier修改器(补丁)
def time_to_int(t):
    return t.hour*3600+t.minute*60+t.second
def int_to_time(seconds):
    if seconds<0:
        seconds = 86400-seconds
    t=Time()
    t.second = seconds%60
    t.minute = (seconds//60)%60
    t.hour = (seconds//3600)%24
    return t
def Add_time(t,seconds):
    return int_to_time(time_to_int(t)+seconds)
def Sub_time(t,seconds):
    return int_to_time(time_to_int(t)-seconds)

print_Time(Add_time(t1,time_to_int(t2)))
print_Time(Sub_time(t2,time_to_int(t1)))

#调试
def valid_time(time):
    if time.hour<0 or time.hour>=24:
        return False
    elif time.minute< 0 or time.minute>=60:
        return False
    elif time.second<0 or time.second>=60:
        return False
    return True
 #assert添加在函数中以检查错误，在错误时抛出异常
def Add_Time(t,seconds):
    assert valid_time(t)
    return int_to_time(time_to_int(t1)+seconds)

t3 = Time()
t3.hour = 23
t3.minute = 50
#t3.second = 60
t3.second =59
print_Time(Add_Time(t3,5666))

#Practice
def mul_time(t,n):
    """时间*整数n"""
    seconds = time_to_int(t)*n
    return int_to_time(seconds)

def time_per_mile(t,miles):
    """计算每英里所花费的时间"""
    seconds = time_to_int(t)//miles
    return int_to_time(seconds)

t4 = Time()
t4.hour = 10
t4.minute = 20
t4.second = 15
miles = 139
print_Time(time_per_mile(t4,miles))

import datetime
date = datetime.datetime.now()
print(date)
datetoday = datetime.date.today()
print(datetoday)
print("星期%d" % datetoday.weekday())

(year,month,day) = map(int,input(">输入您的生日 年-月-日\n").split('-'))

birthday = datetime.date(year,month,day)
print(birthday)
def age(birth):
    datetoday = datetime.date.today()
    return datetoday.year - birth.year
print("you're %d years old." % age(birthday))
