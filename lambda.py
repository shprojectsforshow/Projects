squared = lambda num :  num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(8))

sum = lambda a, b  : a + b

print(sum(2,2))

##############

def funcBuilder(x):
    return lambda num : num +  x

addTen = funcBuilder(10)
addTwenty = funcbuilder(20)