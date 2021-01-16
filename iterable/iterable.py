# coding=utf8


s = 'andigsodighjdf'

# 直接运行会报错，因为 s 是一个可迭代对象，但不是一个迭代器
# TypeError: 'str' object is not an iterator
# print(next(s))

# 利用 iter 函数生成一个迭代器, 此时直接输出一个 a
# s_iter = iter(s)
# print(next(s_iter))

# --------------------------------------------------------------------
# 1. 手动实现一个迭代器, 结果输出一个 h
# --------------------------------------------------------------------

class SentenceIterator():
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0

    def __next__(self):
        try:
            value = self.sentence[self.index]
        except:
            raise IndexError("迭代器已经没有数据，请重新构建迭代器")

        self.index += 1
        return value


# --------------------------------------------------------------------
# 2. 手动实现一个 yield 生成器
# --------------------------------------------------------------------


class SentenceGen():
    def __init__(self, sentence):
        self.sentence = sentence

    def __iter__(self):
        '''生成器函数, 每次生成一个值, 和直接 return self 的区别在于，每次返回的是一个生成器
        '''
        for i in self.sentence:
            yield i


# --------------------------------------------------------------------
# 3. 手动实现一个 yield 函数，即生成器函数
# --------------------------------------------------------------------

def gen_fun():
    for i in [1,2,3]:
        yield i


# --------------------------------------------------------------------
# 4. 手动实现一个等差生成器函数
# --------------------------------------------------------------------

def aritprog_gen(begin, step, end=None):
    forever = False
    if not end:
        forever = True

    result = begin
    yield result

    while forever or result <= end:
        result = begin + step
        yield result


if __name__ == '__main__':
    g = aritprog_gen(10, 10, 100)
    print(next(g))
    print(next(g))