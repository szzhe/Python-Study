
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

# def person(name, age, *, city, job):
#     # if 'city' in kw:
#     #     # 有city参数
#     #     print("有city参数")
#     # if 'job' in kw:
#     #     # 有job参数
#     #     print("有job参数")
#     print('name:', name, 'age:', age, 'city:', city, "job:",job)
# person('Jack', 24, city='Beijing', job='Chaoyang')
# # print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# def a ():
#     def b (name='hlf'):
#         def c():
#             print('name: %s' % name)
#             return 'name: %s' % name
#         return c
#     return b
# a()
# print(a())
# print(a()()())

import sys
import struct
def f():
    def f1():
        x = 3
        print("目前在函数f1()中：x = ", x)

        def f2():
            print("目前在函数f2()中，x = ", x)
        f2()
    # print("目前在函数f()中，x = ",x) # 说明内部函数可以引用外部函数中定义的变量，但是外部函数却不能引用内部函数定义的变量
    f1()
# f()

'''局部作用域对应于函数本身，外部作用域对应于外部函数（如果有的话），全局作用域对应于模块（或文件），Python内建的作用域对应于Python解释程序'''
# print(dir(f))
# 查看内置函数
# print("内置函数为: ",dir(__builtins__) )
# print("内置函数为: ",dir(sys.struct['__builtins__']))

# def f():
# 	x = 0
# 	def f1():
# 		x = 1
# 		def f2():
# 			x = 2
# 			def f3():
# 				x = 3
# 				print('目前在函数f3（）中，变量x的值为：',x)
# 			print('目前在函数f2（）中，变量x的值为：',x)
# 			f3()
# 		print('目前在函数f1（）中，变量x的值为：',x) 
# 		f2()
# 	print('目前在函数f（）中，变量x的值为：',x) 
# 	f1()
# f()

# def f():
#     x = 0
#     def f1():
#         x = 1
#         def f2():
#             # x = 2
#             def f3():
#                 # x = 3
#                 print('目前在函数f3（）中，变量x的值为：',x)
#             print('目前在函数f2（）中，变量x的值为：',x)
#             f3()
#         print('目前在函数f1（）中，变量x的值为：',x) 
#         f2()
#     print('目前在函数f（）中，变量x的值为：',x) 
#     f1()
# f()

# x = 8
# def f():
#     x = 0
#     print('目前在函数f()中，变量x的值为：',x) 
#     def f1():
#         global x
#         x = 1
#         print('目前在函数f1()中，变量x的值为：',x)
#     f1()
# print('现在函数f()中，变量x的值为 ',x)
# f()


# def f():
# 	x = 0
# 	print('当前正在执行函数f（），其变量x的值为：',x)
# 	def f1():
# 		x = 1
# 		print('当前正在执行函数f1（）中，其变量x的值为：',x) 
# 		def f2():
# 			x = 2
# 			print('当前正在执行函数f2（）中，其变量x的值为：',x)
# 			def f3():
# 				x = 3
# 				print('当前正在执行函数f3（）中，其变量x的值为：',x)
# 			f3()
# 		f2()
# 	f1()
# f()

def f():
    x = 8
    def f1():
        print(x)
    return f1
# f()
fun = f()
print(fun())
print(f())