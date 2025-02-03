def divide(message):
    print("-----------------------------",message,"---------------------------",sep="")

#string字符串类型
#遍历
message = "letter"
i=0
while i < len(message):
    print(message[i],end="")#print(end修改结尾类型，sep修改间隔类型)
    i+=1

for i in range(len(message)):
    print(message[i],end="")

for letter in message:
    print(letter,end="")

def reverse(message):
    for i in range(len(message)):
        print(message[-i-1],end="")#-1标识倒数第一个，-2倒数第二，以此类推
#print("\ntest")
    #Index = 1看起来for in range不能自设置起始下标啊
    #   for Index in range(len(message)):
    #       print(message[Index],end="")
    
reverse(message)
#部分遍历？ 划分slice(切片)
print("\n",message[1:5],sep="")#下标1->5的字符
print(message[:4])#下标0->4的字符
print(message[2:])#下标2->end的字符
print(message[3:3])#将会是""
print(message[:])#完全输出
#!!!与c++不同，不能修改字符串的单个字符
    #message[0]='p'         #TypeError: 'str' object does not support item assignment
    #print(message)

#search查找
def find(letter,word):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    return -1
#看起来貌似没有类似于c++函数重载的功能，函数名不能重复，即使功能一样
def Find(letter,word,start_index):
    while start_index<len(word):
        if word[start_index] == letter:
            return start_index
        start_index+=1
    return -1
print(find('e',message))
print(Find('e',message,2))
#count 计数
def count(letter,word):
    count_result = 0
    for ch in word:
        if ch == letter:
            #count_result++ 没有自加自减
            count_result+=1
    return count_result

print(count('e',message))

#字符串类自带的函数
divide("Invocation")
word = "sequence"
print(word.upper())#大写函数
print(word.find('e'))
print(word.find('en',2))#查找子字符串也可以，后一个参数指定起始下标

#in
divide("in")
if 'e' in message:
    print(message,"has the letter 'e'.")
    
def in_both(word_1,word_2):#貌似没有客服重复出现的情况
    for letter in word_1:
        if letter in word_2:
            print(letter,end="")
            
in_both(message,word)
print()
#compare
divide("Compare")

while True:
    message = input("> ")#字符串的比较也是按ASCII码顺序比较的A在前a在后
    if message == "message":
        print("your input",message,"is same with the key_word i have set")
        break
    elif message < "message":
        print("your input is Smaller")
    else:
        print("your input is greater")
        
#Practice
divide("Practice")
def is_reverse(word_1,word_2):
    if len(word_1)!=len(word_2):
        return False
    for i in range(len(word_1)):
        if word_1[i]!=word_2[-1-i]:
            return False
    return True

print(is_reverse("stop","pots"))
print(is_reverse("boring","notfun"))

New_Test_Word = "\tDeco*27\n"
print(New_Test_Word)
New_Test_Word.strip()#delete字符串两端的特殊字符，但是不改变字符串本身，好鸡肋
#New_Test_Word.lstrip()  只删除左侧的特殊字符
#New_Test_Word.rstrip()  只删除右侧的特殊字符
print(New_Test_Word.strip("\t"))#可以指定删除的特殊字符

New_Test_Word.replace('D','d')#修改字符串的字符，修改了，但是原本的不变，也好鸡肋
print(New_Test_Word.replace('D','d'))

def is_palindrome(word):
    if word[::-1]==word:return True
    #word[a:b:c]a是起始下标，b是终止下标，c是步长，-1标识逆序
    else:return False
print(is_palindrome("pop"))

#凯撒加密
divide("caesar")
print(ord('z'),ord('Z'))
print(chr(65),chr(97))
def rotate(word,n):
    for letter in word:
        if ord(letter)<91 and ord(letter)>64:
            print(chr((ord(letter)-64+n)%24+64),end="")
        elif ord(letter)<123 and ord(letter)>96:
            print(chr((ord(letter)-97+n)%24+97),end="")
        else:
            print(letter,end="")
    print()

rotate("abc",3)
text = input("Please ipnut a setence you want to Caesar:> ")
rotate(text,3)
            
    
