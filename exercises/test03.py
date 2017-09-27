
# 前向引用

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

# 函数属性

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

# 内部/内嵌函数

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

# 变量生存周期

'''函数foo的命名空间随着函数调用开始而开始，结束而销毁'''

# def foo():
#      x = 1
# foo()
# print x # SyntaxError: Missing parentheses in call to 'print'

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

# 闭包函数

'''
闭包存在有什么意义呢？为什么需要闭包？
个人认为，闭包存在的意义就是它夹带了外部变量(私货)，如果它不夹带私货，它和普通的函数就没有任何区别。同一个的函数夹带了不同的私货，就实现了不同的功能。
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

# print(another.__closure__)
# (<cell at 0x0000025F94C75708: str object at 0x0000025F94D09298>,)

# # __closure__ 对象返回一个由 cell 对象组成的元组，cell 对象记录了定义在外围作用域的变量信息。
# 对于那些不是闭包的函数对象来说，__closure__ 属性值为 None

# print(another.__closure__[0].cell_contents) # Hello

# 闭包的应用

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
# dog = make_sing("dog")
# print(dog("wong"))

# 什么是装饰器？

''' 
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。

装饰器的功能是将被装饰的函数a()当作参数传递给与装饰器@a对应的函数b()(与@a名称相同的函数)，并返回包装后的被装饰的函数。
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

# 习题：装饰器有一个参数

# def w1(func):
#     def inner(arg):
#         # 验证1
#         # 验证2
#         # 验证3
#         return func(arg)
#     return inner

# @w1
# def f1(arg):
#     print('f1')

# f1(3)

# 习题：N个参数
# def w1(func):
#     def inner(*args, **kwargs):
#         # 验证1
#         # 验证2
#         # 验证3
#         return func(*args, **kwargs)
#     return inner

# @w1
# def f1(arg1, arg2, arg3):
#     print('f1')

# f1(3, 4, 5)

# 习题：被多个装饰器装饰

# def make_wrap(func):
#     def wrapper(*args):
#         print("before function")
#         func(*args)
#         print("after function")
#     return wrapper

# def make_another(func):
#     def wrapper(*args):
#         print("another begin")
#         func(*args)
#         print("another end")
#     return wrapper

# @make_another     # 等同于 print_msg = make_another(make_wrap(print_msg))
# @make_wrap        # 等同于 print_msg = make_wrap(print_msg)
# def print_msg(msg):
#     print(msg) # msg = "Hello"

# print_msg("Hello")

# 习题：

# def logging(level):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             print(
#                 "[{level}]: enter function {func}()".format(
#                 level=level,
#                 func=func.__name__)
#                 )
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return wrapper

# @logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))

# # 如果没有使用@语法，等同于
# # say = logging(level='INFO')(say)

# @logging(level='DEBUG')
# def do(something):
#     print("do {}...".format(something))

# if __name__ == '__main__':
#     say('hello')
#     do("my work")

''' 当带参数的装饰器被打在某个函数上时，比如@logging(level='DEBUG')，它其实是一个函数，会马上被执行，只要这个它返回的结果是一个装饰器时，那就没问题 '''

# 习题：很屌的装饰器

# def Before(request, kargs):
#     print('before')

# def After(request, kargs):
#     print('after')

# def Filter(before_func, after_func):
#     def outer(main_func):
#         def wrapper(request, kargs):

#             before_result = before_func(request, kargs)
#             if(before_result != None):
#                 return before_result

#             main_result = main_func(request, kargs)
#             if(main_result != None):
#                 return main_result

#             after_result = after_func(request, kargs)
#             if(after_result != None):
#                 return after_result
#         return wrapper
#     return outer

# @Filter(Before, After)
# def Index(request, kargs):
#     print('index')

# Index('Hello', 'World')
