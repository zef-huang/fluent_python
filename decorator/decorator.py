# coding=utf-8
# 手写一个装饰器


def training_decorator(func):
    def wrapper(*args, **kwargs):
        print("training 3 hours ...")
        print("training done")

        func(*args, **kwargs)
    
    return wrapper

@training_decorator
def eat_something(something):
    print("you can eat %s now" % something)



if __name__ == '__main__':
    # eat_something = training_decorator(eat_something)
    eat_something('two eggs')
    