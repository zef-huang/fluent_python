# coding=utf8


s = 'andigsodighjdf'

# 直接运行会报错，因为 s 是一个可迭代对象，但不是一个迭代器
# TypeError: 'str' object is not an iterator
# print(next(s))

# 利用 iter 函数生成一个迭代器, 此时直接输出一个 a
s_iter = iter(s)
print(next(s_iter))