def divide(message):
    print("-----------------------------",message,"---------------------------",sep="")

#list
#类似于c的数组，但是可以嵌套，元素（item）可以不同类型，很神奇
empty = []#这是一个空列表
List = [1,'c',"name",True,1.5]#列表的item可以是不同类型
Li = [1,2,3,[1.5,2.5,3.5,[1.414,1.732]]]#嵌套

list_1 = [1,2,3,4,5]
print(list_1[0])
print(list_1)#直接打印整个列表，结果为[1, 2, 3, 4, 5]

empty = []
print(empty)
#多重嵌套的print也真舒服啊，遍历都省了
TwoDem = [["apple","apple"],["rabbit","mouse"],"items"]
print(TwoDem)
print(TwoDem[1])
print(TwoDem[1][0])
print(TwoDem[-1])#下标是负数的时候倒着数
print(TwoDem[-2][-1])

#Changeable
TwoDem[0][1] = "banana"
print(TwoDem[0])
TwoDem[0] = [0,1,2,3]
print(TwoDem[0])
TwoDem = [0]
print(TwoDem)

#len数组大小(按照 广义表的定义输出 个数)
print(len(List))
print(len(Li))
print(len(Li[3]))

#遍历
for items in List:
    print(items,end=",")
print()
for index in range(len(List)):
    print(List[index],end=",")
print()
for items in Li:
    print(items,end=",")
print()

#Operate列表操作
a = [1,2,3,4,5,6,7]
b = [1,2,6,8,9,10,-1]
c = a+b
print(c)
c= c*2
print(c)

#Slice列表切片
a = [0,1,2,3,4,5,6,7,8]
print(a[5:8])#下标从5到7（看起来是不包含右边界对应的下标的）
print(a[1:])
print(a[:7])

#Function列表方法
divide("Functions")
New_list = [1,1,2,3,5,8,11]
New_list.append(13)#对应vector.push_back()
print(New_list)
New_list.pop()#对应vector.pop_back()
print(New_list)

Another_list = [-5,7,-8,5,6,7,68,3,4,29,37,2]
Another_list.sort()#默认从低到高排序
print(Another_list)

Test_list = ['abc','bcd','xyz','aaaa','aaa','AAA']
Test_list.sort()#字符串也能排序，按ASCii排序
print(Test_list)

New_list.extend(Another_list)#extend接受一个列表参数，并合并两个列表
print(New_list)
print(Another_list)

print(sum(New_list))#python内置求和函数
#累加器accumulator
def Sum(List):
    acc = 0
    for items in List:
        acc+=items
    return acc
print(Sum(New_list))

def Capitalize(string):
    res = []
    for i in string:
        res.append(i.capitalize())
    return res

test_text = "really"
print(Capitalize(test_text))
#过滤器fillter
def fillter(List):
    res = []
    for items in List:
        if items>0 and items%2==0:
            res.append(items)
    return res

print(fillter(Another_list))

#delete&pop&remove
divide("Delete")
print(New_list)
it = New_list.pop()#默认弹出最后一个元素
print(it)

it = New_list.pop(2)#可以用下标指定弹出元素
print(it)
print(New_list)
del New_list[3]#del不是函数也不是方法，写起来像是c++的delete,没有返回值
print(New_list)
del New_list[5:]#可以用slice写法一次多删
print(New_list)

New_list = [1,1,2,3,5,8,13,21]
New_list.remove(1)#remove删除指定元素(而不是下标)，emm貌似只删掉了第一个1，why？
print(New_list)

#string
divide("string")

Text = "Don't know what to write."
T_list = list(Text)#将字符串转换成列表
print(T_list)
Another_Tlist = Text.split()#默认将字符串按空格划分转换为列表
print(Another_Tlist)
Text = "Don't-know-what-to-write."
delimiter = '-'
Another_Tlist = Text.split(delimiter)#split方法还可以接受一个delimiter参数作为所需要的划分分隔符
print(Another_Tlist)
Delimiter = "->"
Text = Delimiter.join(Another_Tlist)#join是split的反函数，是delimiter的方法，接受一个列表并用delimiter连接成字符串
print(Text)

#value&object
#值相同叫 “相等=”    对象相同叫 “相同is”
divide("Value & Object")
a = "ant"
b = "ant"
print(a==b)
print(a is b)
a = [1,2,3]
b = [1,2,3]
print(a is b)#虽然值相同，但是两个列表不同
#reference
c = a
print(a is c)#这样写相同了，对应c++的引用，c是a的别名，对应的对象都是同一个


#Practice
divide("Practice")

test_list_1 = [[1,2],[3],[4,5,6]]
def nested_sum(List):
    res = 0
    for items in List:
        if type(items) == list:
            res += nested_sum(items)
        else:
            res += items
    return res    
print(nested_sum(test_list_1))


test_list_2 = [1,2,3]
def consum(List):
    res = []
    sum = 0
    for items in List:
        sum+=items
        res.append(sum)
    return res
print(consum(test_list_2))

test_list_3 = ['a','c','e','d']
def middle(List):
    res = []
    for index in range(len(List)):
        if index>0 and index<len(List)-1:
            res.append(List[index])
    return res
def Middle(List):
    res = []
    for items in List:
        if items != List[0] and items != List[-1]:
            res.append(items)
    return res
print(Middle(test_list_3))
#下面这个chop没有成功，原因不明
def chop(List):
    for index in range(len(List)):
        if index == 0 and index == len(List)-1:
            del List[index]
            
def Chop(List):
    List.pop(0)
    List.pop(-1)#这pop还真可以用-1标识倒数第一个元素
Chop(test_list_3)
print(test_list_3) 

test_list_4 = ['b','a']
def is_sorted(List):
    for index in range(len(List)-1):
        if List[index]>List[index+1]:
            return False
    return True
print(is_sorted(test_list_2))
print(is_sorted(test_list_4))

def is_anagram(word_1,word_2):
    if len(word_1)!=len(word_2):
        return False
    word_1 = sorted(word_1)#接受一个字符串或者列表
    word_2 = sorted(word_2)#返回值是一个排序后（升序）的列表
    if word_1 != word_2:
        return False
    return True
test_word_1 = "stop"
test_word_2 = "tops"

print(is_anagram(test_word_1,test_word_2))

def has_duplicates(List):
    List = sorted(List)
    for index in range(len(List)-1):
        if List[index]==List[index+1]:
            return True
    return False

def Has_duplicates(List):
    List = sorted(List)
    for items in List:
        if List.count(items)>1:#count方法返回指定元素在列表中出现的次数
            return True
    return False

test_list_5 = ['a','v','a','w']
test_list_6 = ['q','r','s']
print(has_duplicates(test_list_5))
print(has_duplicates(test_list_6))

def in_bisect(target,List):#二分查找思想（但是不能返回下标,只能返回真假)
    List = sorted(List)
    left = 0
    right = len(List)
    while True:
        index = left + (right-left)//2
        if left>=right:
            return False
        if target < List[index]:
            right = index - 1
        elif target > List[index]:
            left = index + 1
        else:
            return True

print(in_bisect('a',test_list_5))
print(in_bisect('w',test_list_5))
print(in_bisect('i',test_list_5))
