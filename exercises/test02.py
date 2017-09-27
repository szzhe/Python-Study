
# 11.3.3 前向引用

# def foo():
#   print('in foo()')
#   bar()

# def bar():
#   print("in bar()")

# foo()

'''
这段代码是正确的因为即使(在foo()中)对bar()进行的调用出现在bar()的定义之前，但foo()本身不是在bar()声明之前被调用的。 换句话说，我们声明foo()，然后再声明bar()，接着调用foo()，
但是到那时，bar()已经存在了，所以调用成功。 
'''
# 11.3.4 函数属性

# def foo():
#     '''foo() -- properly created doc string:szzhe'''

# def bar():
#     pass

# # 在函数声明外定义一个文档字串
# bar.__doc__ = 'Oops,forgot the doc above'
# bar.version = 0.1

# help(foo)
# print(bar.version)
# print("bar.__doc__:", bar.__doc__)
# print("foo.__doc__:", foo.__doc__)


# 11.3.5 内部/内嵌函数

'''方式一：最明显的创造内部函数的方法是在外部函数的定义体内定义函数(用def关键字)'''

# def foo():
#     def bar():
#         print('bar() called')
#     print('foo() called')
#     bar()
# # foo()

# bar() # NameError: name 'bar' is not defined

'''内部函数一个有趣的地方在于整个函数体都在外部函数的作用域之内。如果没有任何对bar()的外部引用，那么除了在函数体内，任何地方都不能对其进行调用'''

'''方式二：函数体内创建函数对象的方式是使用lambda语句。
   如果内部函数的定义包含了在外部函数里定义的对象的引用(这个对象甚至可以是在外部函数之外)，内不函数会被称为闭包(closure)的特别之物
'''

# 11.3.6 *函数(与方法)装饰器

'''装饰器是在函数调用之上的装饰。这些装饰仅是当声明一个函数或者方法的时候，才会应用的额外调用
   装饰器的语法以@开头，接着是装饰器函数的名称和可选的参数。紧跟着装饰器声明的是被修饰的函数和装饰函数的可选参数。
   @decorator(dec_opt_args):
        def func2Bdecorated(func_opt_args):
            : 
'''

# import time
# def deco(func):
#     print("start")
#     startTime = time.time()
#     func()
#     endTime = time.time()
#     print("end")
#     msecs = (endTime - startTime) * 1000
#     print('->elapsed time: %fms' %(msecs))
# def myfunc():
#     print("srart myfunc")
#     time.sleep(0.6)
#     print("end myfunc")
# deco(myfunc)
# myfunc()

# 作用域
# a_string = "This is a global variable"
# def test(arg):
#     z = 1
#     a_string = "test"
#     print(locals()) # locals() 基于字典的访问局部，字典的键就是变量名，字典的值就是那些变量的值
# test(4) # {'a_string': 'test', 'z': 1, 'arg': 4}
# test('doulaixuexi') # {'a_string': 'test', 'z': 1, 'arg': 'doulaixuexi'}
# print(globals())

'''globals 函数返回一个全局变量的字典，包括所有导入的变量。 {...,'a_string': 'This is a global variable'，...}'''

# 变量生存周期

'''函数foo的命名空间随着函数调用开始而开始，结束而销毁'''

# def foo():
#      x = 1
# foo()
# print x # SyntaxError: Missing parentheses in call to 'print'

# 闭包(closure):是一种引用了外部变量的函数对象，无论该变量所处的作用域是否还存在于内存中。


def generate_power_func(n):
    print("id(n): %X" % (id(n)))  # %X 无符号十六进制

    def nth_power(x):
        return x**n
    print("id(nth_power): %X" % id(nth_power))
    return nth_power


kk = generate_power_func(4)  # 调用函数，会生成一个nth_power函数对象；且将结果返回给一个变量kk
# print(repr(kk))  # repr() 函数将对象转化为供解释器读取的形式，返回一个对象的 string 格式
'''
id(n): 7287c710
id(nth_power): 1a4715398c8
'''
del generate_power_func  # 将函数 generate_power_func 函数从全局命名空间删除
print(kk(2))  # 调用闭包函数 kk = 16
print(kk.__closure__)
print(kk.__closure__[0].cell_contents)
'''结论：函数对象nth_power是由generate_power_func产生的一个闭包，闭包会保留来自外围作用域变量的信息。'''

'''************************************************************'''
# def outer():
#     x = 1
#     def inner():
#         print(x)
#     return inner
# foo = outer()
# print(foo.__closure__)
# # __closure__ 对象返回一个由 cell 对象组成的元组，cell 对象记录了定义在外围作用域的变量信息。
# # (<cell at 0x000001F8BA898498: int object at 0x000000007287C6B0>,)
# # 对于那些不是闭包的函数对象来说，__closure__ 属性值为 None
# print(type(foo.__closure__[0]))  # <class 'cell'>
# print(foo.__closure__[0].cell_contents)  # 1

'''************************************************************'''

# def line_conf():
#     def line(x):
#         return 2 * x + 1
#     print(line(5))

# line_conf()

'''************************************************************'''
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line

# b = 5
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents)

'''************************************************************'''
# def line_conf(a, b):
#     i = a * b # 20
#     def line(x):
#     	nonlocal i
#     	i = i + x # 25
#     	return i * x + b
#     return line

# line1 = line_conf(4, 5)
# print(line1(5))


def print_msg(msg):
    '''This is the outer enclosing function'''
    def printer():
    '''This is the nested function'''
        print(msg)

# printer()
print_msg("Hello"))
