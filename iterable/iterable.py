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
        '''生成器函数, 每次生成一个值
        '''
        for i in self.sentence:
            yield i


if __name__ == '__main__':
    s = SentenceGen('hello')
    for i in s:
        print(i)

