
# def foo():
# 	print('in foo()')
# 	bar()

# def bar():
# 	print("in bar()")

# foo()

'''
这段代码是正确的因为即使 （在foo()中） 对bar()进行的调用出现在bar()的定义之前， 但foo()
本身不是在bar()声明之前被调用的。 换句话说， 我们声明foo()， 然后再声明bar()， 接着调用foo()，
但是到那时，bar()已经存在了，所以调用成功。 
'''

def foo():
    '''foo() -- properly created doc string:szzhe'''

def bar():
    pass

# 在函数声明外定义一个文档字串
bar.__doc__ = 'Oops,forgot the doc above'
bar.version = 0.1

help(foo)
print(bar.version)
print("bar.__doc__:", bar.__doc__)
print("foo.__doc__:", foo.__doc__)
