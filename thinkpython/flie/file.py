#file
#只读打开文件
file_1 = open("words.txt")

def Is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
palindrome_words = []
counter = 0
for line in file_1:
    word = line.strip()
    if Is_palindrome(word):
        #print(word)
        palindrome_words.append(word)
        counter+=1
        
file_1.close()

#写入write
file_2 = open("book.txt",'w')#在没有对应文件时新建，有对应文件覆写
for word in palindrome_words:
    file_2.write(word+'\n')
    #write返回值是写入的字符个数，而文件对象记录写入到位置（即下一个要写的位置）
file_2.write("Totally it has "+str(counter)+" palindrome words")#write的参数只能是字符串
file_2.write("\npattern")
file_2.close()

#格式操作符%
#用法接近于c++的%
line = "Totally it has %d palindrome words" %counter
print(line)
n = 20
w = 50.6
line = "My name is %s,and i am %d years old.My weight is %.2f kg." %("Zxh",n,w)
print(line)

#文件名和路径
import os      #os 是operating system操作系统
cwd = os.getcwd() #cwd 是current working directory当前工作目录
cwd = "d:\GCC\code\pyhton"#绝对路径,之前用文件名打开，如book.txt是相对路径，\GCC\code\pyhton\book.txt是完整的绝对路径
print(os.path.exists("book.txt"))#检验某一个文件或者路径是否存在
print(os.path.exists("\GCC\code\c++"))
print(os.listdir(cwd))#返回指定路径的文件以及其他目录的列表
print(os.listdir("\GCC\code\c++"))
    #目录的遍历
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
walk(cwd)
#try and except捕获异常
try:
    fin = open("book.cpp")
except:
    print("Something went wrong.")
#python首先尝试try内的语句，如果没用报错则跳过except内的语句，否则运行except内的语句

#数据库
import dbm
db = dbm.open("caption",'c') 
db["cless.png"] = "Photo of sunbreak"
db["cless.png"]#输出的是b'Photo of sunbreak',b表示字节组对象(bytes object)
#用起来像是字典，但是不用到字典方法keys和items
#dbm限制key和value(items)都是字符串

#封存
#使用pickle模块可以将大多数类型转换成字符串类型或是翻译回来
import pickle
list = [1,2,3,5]
str = pickle.dumps(list)#输出是b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x05e.'
another_list = pickle.loads(str)

db["LIST_A"] = str
print(pickle.loads(db["LIST_A"]))
db.close()

#编写模块module --> My_module.py
import My_module#发现输出了over correctly说明import模块时相当于运行了一遍My_module
My_module.divide("module")

#调试好帮手repr
#接受任何对象，并转化为相应的字符串.如换行变成\n
s = "1\t 55 6\n"
print(s)
print(repr(s))

#管道pipe object代表一个正在运行的程序

#Practice
My_module.divide("Practice")

def sed(pattern,replace,source,dest):
    """Reads a source file and writes the destination file.
    pattern:string
    replace:string
    source:filename,txt comes from
    dest:filename,result write into
    """
    fin = open(source,'r')
    fout = open(dest,'w')
    for line in fin:
        line = line.replace(pattern,replace)
        fout.write(line)
    fin.close()
    fout.close()

source = "book.txt"
dest = "newbook.txt"
pattern = "pattern"
replace = "replaced!"
sed(pattern,replace,source,dest)
