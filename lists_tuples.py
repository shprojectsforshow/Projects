users = ['Dave','John','Sara']
#Alt+shift+R
data = ['Dave',42,True]

emptylist=[]

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:3])
print(users[0:])

print(len(data))

users.append('Scooter')

users += ['jason']
print(users)

users.extend(['robert','jimmy'])
print(users)

#users.extend(data)
#print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ["eddie",'Alex']
print(users)

users[1:3] = ['robert','jpj']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)


users.sort(key=str.lower) #key needed if lower/upper case included
print(users)

nums = [4,42,78,1,5]
nums.reverse() #just flips list not sorting
print(nums)

#nums.sort(reverse=True)
#print(nums)

print(sorted(nums,reverse=True)) #global sorted function
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Niel",True])
print(mylist)

#Tuples (data cant change and order cant change)

mytuple = tuple(('Dave',42,True))

anothertuple = (1,4,2,8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

#Used to change tuple workaround 
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

#unpack tuple

(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)