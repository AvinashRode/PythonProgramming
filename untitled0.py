
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

num=5
if num > 2: 
    print(num) 
    num -= 1 
else: 
    print(num)
    

num=2
while num>10:
    print(num)
    num+=2
else:
   print("Goodbye!")
   
print("Hello!")
for n in range (10,0,-2):
    print(n)
 
    
print("Hello")    
num=10
while num>=2:
    print(num)
    num-=2
    
    
total = 0
current = 1
while current <= 6:
    total += current
    current += 1

print(total)


n=0
i=1
while i<=6:
    n+=i
    i+=1
    
print(n)

x=2
ans=0
itersleft=x
while (itersleft!=0):
    ans+=x
    itersleft-=1
print(str(x)+'*'+str(x)+'='+str(ans))
    

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
        
for letter in 'AVINASH':
    print(letter)
          