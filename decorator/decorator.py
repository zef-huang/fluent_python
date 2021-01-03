# coding=utf-8
# 手写一个装饰器


def training_decorator(func):
    def wrapper(*args, **kwargs):
        print("training 3 hours ...")
        print("training done")

        func(*args, **kwargs)
    
    return wrapper


# 案例二：实现一个简单的装饰器，用于打印函数的执行时间
from  time import time
def run_time_decorator(func_name):
    def rerord_func_run_time(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            func(*args, **kwargs)
            print('函数 %s 执行时间：%s' % (func_name, time() - start_time))
        return wrapper
    return rerord_func_run_time


@run_time_decorator("eat_something")
@training_decorator
def eat_something(something):
    print("you can eat %s now" % something)


if __name__ == '__main__':
    # eat_something = training_decorator(eat_something)
    eat_something('two eggs')
