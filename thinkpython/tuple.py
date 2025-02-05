def divide(message):
    print("-----------------------------",message,"---------------------------",sep="")

divide("Tuple")
#新建一个tuple
tuple_1 = 1,#此处逗号不可省略
print(tuple_1,type(tuple_1))
tuple_2 = 1,2,3,4 
tuple_3 = (1,)#带上括号是好习惯,但是只要一个元素的时候逗号还是不难省略!
tuple_4 = ('a','b','c')
tuple_5 = tuple() #另一种新建一个元组的方式
print(tuple_5)
tuple_6 = tuple("water")#自行拆开了
print(tuple_6)
tuple_7 = tuple((1,2,3))
print(tuple_7)
#调用和切片
print(tuple_7[0])
print(tuple_7[1:3])#类似与列表

#元组修改
#tuple_7[0]=2 元组不支持这样修改
tuple_7 = (-1,) + tuple_7[1:] #但是可以整体修改
print(tuple_7)

#赋值
(a,b) =(1,3)#这么写元组名字都没有，只有两个有序变量，都可以单独调用
print((a,b))
(a,b) = (b,a)
print((a,b))
#使用split玩的更加 秀
addr = "username@xxx.com"
(user,address) = addr.split('@')
print((user,address))
print(user)

#元组作为函数返回值（实现多返回值函数）
def divmod(a,b):
    return (a//b,a%b)#返回的第一个值是 商，第二个值是 余数
print(divmod(7,2))

def min_max(List):
    List = sorted(List)
    return (List[0],List[-1])
min = min_max([1,2,-5,6,8,4])[0]
max = min_max([1,2,-5,6,8,4])[1]
print(min,max,sep=',')

#gather 收集 and scatter 分散 用的操作符都是*
divide("gather&scatter")
def printall(*args):
    print(args)
print(1,True,'v',"wanderland",0,-1,1.5)

#收集的一大用途是可变参数长度
def sum_all(*args):
    result = 0
    for i in args:
        result += i
    return result
print(sum_all(1,2,3))
print(sum_all(1,2,3,55,64,65,468,46,8))
tuple_8 =(7,2)
#print(divmod(tuple_8))#divmod因为接受两个参数不接受元组，所以会报错
print(divmod(*tuple_8))
#元组和列表
divide("zipper")
#zipper 多个序列按序组成元组成为新的一个序列（zip）
List = [39,0,1,27]
string = "Miku"
Zip = zip(List,string)
print(type(Zip))#zip函数返回类型是zip对象，由元组组成的序列
for items in Zip:
    print(items)
    
Zip_reverse = zip(string,List)
for items in Zip_reverse:
    print(items)
    
Zip_more = zip(List,string,['00','01','10','11'])
for items in Zip_more:
    print(items)
    
Zip_ls = zip([1,2,3],"nb")#长度不一是取最短的
print(Zip_ls)#有趣的结果
for items in Zip_ls:
    print(items)
    
#尽管zip看似是序列，但是不能通过下标访问，需要先转化为 list,list的元素为tuple类型
Ziplist = list(zip(List,string))
print(Ziplist)
print(Ziplist[0])
Zip = zip(List,string)
Ziplist_test = list(Zip)#略显诡异-->原因是Zip只能使用一次，前面遍历的时候消耗了(一次性拉链)
print(Ziplist_test)#另一种遍历方式
for (number,letter) in Ziplist:
    print(number,letter,sep='->')

def match(List_1,List_2):
    for x,y in zip(List_1,List_2):
        if x!=y:
            return False
    return True

print(match("Miku","MIku"))
#内置函数 可以得到序列的下标(从零开始)和元素组成的元组序列(zip)
for index,value in enumerate(string):
    print(index,value,sep='->')
#迭代器
#上面的zip和下面的dict_items都是一种迭代器，只能前进不能后退？    
#tulpe和dict和list
divide("")
dict_1 ={0:'M',1:'i',2:'k',3:'u'}
tuple_dic = dict_1.items()#dict的方法，将dict转换成元组组成的序列(dict_items类型,是一种迭代器)
print(type(tuple_dic))
print(tuple_dic)
for number,value in tuple_dic:
    print(number,value,sep='->')

List_tuple = [('M',0),('i',1),('k',3),('u',9)]
dict_2 = dict(List_tuple)#可以将一个元组列表转化成字典
print(dict_2)

print(type(range(5)))#range类型，相当于一个0->n-1的有序序列（list）
print(range(5))

dict_by_zip = dict(zip("Hatsune",range(7)))
print(dict_by_zip)

#dict的key可以是tuple类型(!非常好用!)
dictionary = {("xx","z"):2194939338}
def find(first,last):
    if (first,last) in dictionary:
        return dictionary[first,last]
    else:
        raise LookupError("Cannot find ",last,first)
    
print(find("xx","z"))
#print(find("z","z"))

#Practice
divide("Practice")
test_string = "PythonApplication"

def sort_by_frequency(string):
    dict_string = {}
    for i in string:
        if i in dict_string:
            dict_string[i]+=1
        else:
            dict_string[i]=1
    tuple_dict = dict_string.items()
    tuple_dict = sorted(tuple_dict,key=lambda x:x[1],reverse=True)#key函数指定排序依据，reverse=True降序排序
    return tuple_dict
print(sort_by_frequency(test_string))
    
