def divide(message):
    print("-----------------------------",message,"---------------------------",sep="")

divide("Dictionary")
#dictionary字典，类似于list，由键值对组成(key-value pair),是key->value的映射
empty_dict = dict()#新建一个空的字典{}，用{}表示字典
print(empty_dict)
dict_1 = {'one':1}#新建并初始化一个非空的字典
print(dict_1)
dict_1['two'] = 2
dict_1['three'] = 3
print(dict_1)
print(dict_1['two'])
#字典的len返回它的键值对个数
print(len(dict_1))
#in用在字典时只检测key（键）中有没有
print('one' in dict_1)
print(1 in dict_1)
#values方法返回一个value组成的list
values = dict_1.values()
print(values)#这个结果让人意外
print(1 in values)

divide("Counter")
#counter
def histogram(word):
    dic = dict()
    for letter in word:
        if letter in dic:
            dic[letter]+=1
        else:
            dic[letter]=1
    return dic

test_word_1 = "PythonApplication"
dict_2 = histogram(test_word_1)
print(dict_2)
#get方法 dict.get(key,None->value)接受一个target键，和一个如果找不到时会返回的默认值
print(dict_2.get('o',0))
print(dict_2.get('Z',0))

#遍历
def traversal(dic):
    for key in dic:
        print(key,dic[key],sep="->")
        
traversal(dict_2)
print()
def traversalInOrder(dic):
    for key in sorted(dic):#sorted也可以对字典使用，按key排序后返回一个新的字典
        print(key,dic[key],sep="->")

traversalInOrder(dict_2)

#反向查找(搜索)
def reverse_lookup(value,dic):
    for key in dic:
        if value == dic[key]:
            return key
    raise LookupError("value does not appear in the dictionary!")#python的抛出异常，类似c++的throw，可选参数可以使其更加详细
#print(reverse_lookup(3,dict_2))
print(reverse_lookup(2,dict_2))

#反转字典
def invert_dic(dic):
    res = dict()
    for key in dic:
        if dic[key] in res:
            res[dic[key]].append(key)
        else:
            res[dic[key]] = [key]
    return res
print(invert_dic(dict_2))#list可以作为dict的value，但是不能作key

#memo备忘[c++的bp？]
divide("memo")
known = {0:0,1:1}
def Fibonacci(n):#一般情况下，python在函数中出现的变量都是局部变量尽管它与外面的全局变量同名,但是本身就可以修改的字典和列表除外
    if n in known:
        return known[n]
    else:
        res = Fibonacci(n-1)+Fibonacci(n-2)
        known[n] = res
        return res
    
print(Fibonacci(56))
    
#全局变量声明
number = 0
def plusplus():
    number+=1
#plusplus()
print(number)#可见尽管外部已有number，但是不在函数内声明，函数内就无法调用它，声明不使用global那也只是开了一个新的局部变量，不会影响外部的全局变量
def PlusPlus():
    global number
    number+=2
PlusPlus()
print(number)

#Practice
divide("Pratice")#有点超纲的用到了元组
ack_known = {(0,0):1,(0,1):2,(1,1):3}

def ack_plus(m,n):
    if (m,n) in ack_known:
        return ack_known[(m,n)]
    else:
        if m == 0:
            res = n+1
            ack_known[(m,n)] = n+1
        elif n==0 and m>0:
            res = ack_plus(m-1,1)
            ack_known[(m,n)] = res
        elif m>0 and n>0:
            res = ack_plus(m-1,ack_plus(m,n-1))
            ack_known[(m,n)]=res
        return res
print(ack_plus(3,4))

def has_duplicates(string):
    dic = {}
    for c in string:
        if c in dic:
            return True
        else:
            dic[c]=1
    return False
print(has_duplicates("acbzeiknsaligwgskilgsd"))
