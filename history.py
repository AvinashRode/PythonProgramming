        p += s[x+1] 
        x += 1 
        
        print(l)
s = 'azcbobobegghakl'
bobs = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        bobs += 1

print('Number of times bob occurs is:', bobs)
s = 'azcbobobegghakl'
cur = lng = s[0]
for c in s[1:] + ' ':
    if c < cur[-1]:
        if len(cur) > len(lng):
            lng = cur
        cur = c
    else:
        cur += c

print("Longest substring in alphabetical order is:", lng)
s = 'azcbobobegghakl'
cur = lng = s[0]
for c in s[1:] + ' ':
    if c < cur[-1]:
        if len(cur) > len(lng):
            lng = cur
        cur = c
    else:
        cur += c

print("Longest substring in alphabetical order is:", lng)

prev = ' '
start = size = l_start = l_size = 0
for c in s:
    if c >= prev:
        size += 1
    else:
        if size > l_size:
            l_size = size
            l_start = start
        start += size
        size = 1
    prev = c

if size > l_size:
    l_size = size
    l_start = start

print('Longest substring in alphabetical order is:', s[l_start: l_size+l_start])
n=10
for n in range(1:5)
for n in range(1,5)
for n in range(1:5): 
    print(n)
for n in range(1,5): 
    print(n)
    
s = 'azcbobobegghakl'
for c in s[1:]:
    print(c)
    
for c in s[1:]:
    if c=="b":
    print(c)
s = 'azcbobobegghakl'
for c in s[1:]:
    if c=="b":
    print(c)
for c in s[1:]:
    if c=="b":

        print(c)
        
for c in s[7:]:
    if c=="b":

        print(c)
        
for c in s[5:9]:

        print(c)
        
for c in s[-1]:

        print(c)
        
for c in s[-2]:

        print(c)
        
for c in s[1:15:-2]:

        print(c)
        
for c in s[15:1:-2]:

        print(c)
        

## ---(Thu Apr  9 17:57:05 2020)---
num=2
while num>10:
    print(num)
    num+=2

else:
   print("Goodbye!")
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1

print('Outside of loop')
print("Hello!")
for n in range (10,0,-2):
    print(n)
print("Hello")    
num=10
while num>=2:
    print(num)
    num-=2
n=0
i=1
while i<=6:
    n+=i
    i+=1


print(n)
n=0
i=1
while i<=6:
    n+=i
    i+=1


print("sum"+n)
x=0
ans=0
itersleft=x
while (itersleft!=0):
    ans+=x
    itersleft-=1

print(str(x)+'*'+str(x)+'='+str(ans))
x=2
ans=0
itersleft=x
while (itersleft!=0):
    ans+=x
    itersleft-=1

print(str(x)+'*'+str(x)+'='+str(ans))
str1 = 'hello'
str2 = ','
str3 = 'world'
print(str1 + str2 + str3)