def divide(messsage):
    print("-----------------------",messsage,"-----------------------------")
#while
divide("while loop")
def countdown(n):
    while n!=0:#zero is the base case（停止条件）
        print(n)
        n -= 1#n=n-1

countdown(10)

for i in range(10):
    print(i)

print(len("message"))
for i in range(len("message")):
    print(i,":", "message"[i])

def is_palindrome(str):
    for i in range(int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True

while True:
    message = input("> ")#有趣的写法，在input中写入message，相当于省去了一个print，这真是，太酷了
    if(message=="Done"):
        break
    elif is_palindrome(message):
        print("The word",message,"is palindrome")
    else:
        print("your input isn't palindrome")
        
def Sqrt(n):
    x = n/2
    while True:
       y = (x+n/x)/2
       e = abs(x-y)
       x=y
       if e<0.000001:
           break
    return x

print(Sqrt(2))

#Pratice
divide("Practice")
while True:
    polyon = input("> ")
    if polyon == "Done":
        break
    print(eval(polyon))#python内置的计算字符串类型的计算式的函数eval（evaluate的缩写）
    
def Sqrt(n):
    x = n/2
    while True:
       y = (x+n/x)/2
       e = abs(x-y)
       x=y
       if e<0.000001:
           break
    return x
