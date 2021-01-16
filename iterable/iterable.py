# coding=utf8


s = 'andigsodighjdf'

# 直接运行会报错，因为 s 是一个可迭代对象，但不是一个迭代器
# TypeError: 'str' object is not an iterator
# print(next(s))

# 利用 iter 函数生成一个迭代器, 此时直接输出一个 a
# s_iter = iter(s)
# print(next(s_iter))

# --------------------------------------------------------------------
# 1. 手动实现一个迭代器
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


if __name__ == '__main__':
    s = SentenceIterator('hello')
    print(next(s))
