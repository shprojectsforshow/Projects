name = "dave" #global scope
count = 1


# def greeting(name):
#     color = "blue" #local scope only
#     print(color)
#     print(name)



def another():
    color = "blue"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()