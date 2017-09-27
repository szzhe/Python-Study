
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

# import logging

# def foo():
#     print('i am foo')
#     logging.info("foo is running")
# foo()


def Before(request, kargs):
    print('before')


def After(request, kargs):
    print('after')


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):

            before_result = before_func(request, kargs)
            if(before_result != None):
                return before_result

            main_result = main_func(request, kargs)
            if(main_result != None):
                return main_result

            after_result = after_func(request, kargs)
            if(after_result != None):
                return after_result

        return wrapper
    return outer


@Filter(Before, After)
def Index(request, kargs):
    print('index')


Index('Hello', 'World')
