
# def fn(x, n):
#     result = 1
#     while n > 0:
#         result = result * x
#         n = n - 1
#     return result

# print(fn(2, 3))


# def sum(*args):
#     # print(type(args)) # tuple
#     print(args)
#     ret = 0
#     # print(type(ret)) # int
#     for i in args: 
#         print(i)
#         print(type(i))
#         ret += i
#     return ret
# print(sum([1,2,3]))

# def add_end(L=[]):
#     print(add_end.__defaults__)
#     L.append('END')
#     return L
# print(add_end([1, 2, 3]))
# # print(add_end(['x', 'y', 'z']))

# print(add_end())
# print(add_end())
# print(dir(add_end))

# def fn(x=5, *args):
#     print(x,end=",")
#     print(args)
# fn(1, 2, 3, 4) 

# def fn(*args, x=5):
#     print(x)
#     print(args)
# fn(1, 2, 3, 4)

# def add(x,y):
#     ret = x + y
#     print("{}+{}".format(x,y,ret))
#     return ret
# # add(x = 1, y = 2)
# # print(add(x = 1, y = 2)) 

# d = {'x': 1, 'y': 2}
# print(add(**d))

def person(name, age, *, city, job):
    # if 'city' in kw:
    #     # 有city参数
    #     print("有city参数")
    # if 'job' in kw:
    #     # 有job参数
    #     print("有job参数")
    print('name:', name, 'age:', age, 'city:', city, "job:",job)
person('Jack', 24, city='Beijing', job='Chaoyang')
# print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))