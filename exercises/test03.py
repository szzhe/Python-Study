
### 闭包函数

'''
闭包存在有什么意义呢？为什么需要闭包？
个人认为，闭包存在的意义就是它夹带了外部变量（私货），如果它不夹带私货，它和普通的函数就没有任何区别。同一个的函数夹带了不同的私货，就实现了不同的功能。
其实你也可以这么理解，闭包和面向接口编程的概念很像，可以把闭包理解成轻量级的接口封装。

Nonlocal variable是相对于某个函数来说的，指的是这个函数所调用的在本函数作用域之外的变量。
Nested function指的被定义在一个函数(outer enclosing function)中的函数，这个nested function可以调用包围它的作用域中的变量。
'''

# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer

# another = print_msg("Hello")
# another()

# 在这个例子中函数printer就是一个nested function，而变量msg就是一个nonlocal variable。这里需要注意的是，printer虽然可以访问msg，但是不可以改变它。
# 如果必须要更改这个变量的值，，在Python3中新引入的nonlocal语句可以解决。
# Nonlocal 与 global 的区别在于 nonlocal 语句会去搜寻本地变量与全局变量之间的变量，其会优先寻找层级关系与闭包作用域最近的外部变量。
# 将print_msg("Hello")返回的函数赋值给another，再调用another函数时，发现已经离开了print_msg函数的作用域，但是"Hello"已经被绑定给another,所以仍然能够正常调用。
# 删除print_msg之后，another仍然能够正常调用。

# del print_msg
# # print_msg("Hello") # NameError: name 'print_msg' is not defined
# another() # Hello

# 支持将函数当成对象使用的编程语言，一般都支持闭包。比如Python, JavaScript

### 闭包的应用

'''当符合下面几个条件时就形成了闭包：
1.有一个Nested function
2.这个Nested function访问了父函数作用域中的变量
3.父函数返回了这个Nested function
'''

# 闭包主要运用在需要讲父函数作用域中的变量绑定到子函数的场景之中，在释放掉父函数之后子函数也不会受到影响。
# 运用闭包可以避免对全局变量的使用。对于一个只有需要实现少数方法的类我们也可以用闭包来替代，这样做可以减少资源的使用。

# 案例：用闭包函数定义不同动物的叫声

# def make_sing(animal):
#     def make_voice(voice):
#         return "{} sings {}".format(animal,voice)
#     return make_voice
# dog = make_sing("dog") # dog = make_voice()；animal = "dog"
# print(dog("wong")) # make_voice("wong") -> animal = "dog"；voice = "wong"

### 什么是装饰器？

''' 
装饰器的功能是将被装饰的函数a()当作参数传递给与装饰器@a对应的函数b()(名称相同的函数)，并返回包装后的被装饰的函数。
简而言之：@a 就是将 b 传递给 a()，并返回新的 b = a(b)
'''

# def dobi(qf):
#     return qf()
# @dobi
# def qifeng():
#     print("dobi")

'''
解析过程是这样子的：
1.python 解释器发现@dobi，就去调用与其对应的函数(dobi 函数)
2.dobi 函数调用前要指定一个参数，传入的就是@dobi下面修饰的函数，也就是qinfeng()。
3.dobi()函数执行，调用qinfeng()，qinfeng()打印“dobi”
'''

### 闭包与装饰器

# 闭包通常用来实现一个通用的功能，Python中的装饰器就是对闭包的一种应用，只不过装饰器中父函数的参数是一个函数。

def make_wrap(func):
    def wrapper(*args):
        print("before function")
        func(*args)
        print("after function")
    return wrapper

def make_another(func):
    def wrapper(*args):
        print("another begin")
        func(*args)
        print("another end")
    return wrapper

@make_another     # 等同于 print_msg = make_another(make_wrap(print_msg))
@make_wrap        # 等同于 print_msg = make_wrap(print_msg)
def print_msg(msg): 
    print(msg) # msg = "Hello"

print_msg("Hello")

'''
转换成闭包的形式：
print_msg = make_wrap(print_msg)
print_msg = make_another(print_msg)

'''

''' https://segmentfault.com/a/1190000008955952  '''

