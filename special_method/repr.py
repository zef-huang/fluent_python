# ------------------------------------------------------
# 1.测试 __repr__ 魔法方法
# ------------------------------------------------------
class Test():
    def __repr__(self):
        return "this is repr"

    def __str__(self):
        return "str can cover repr ??"

# t = Test()
# print(t)




# ------------------------------------------------------
# 2.构建一个类，使其具有序列器的功
# ------------------------------------------------------
class DuckSeqence():
    '''只要实现了 len 和 getitem 的魔法方法即可
    '''
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)

    def __getitem__(self, i):
        return self.array[i]


if __name__ == '__main__':
    array = [2, 6, 2, 7, 3]
    client = DuckSeqence(array)
    print(client[3])
    

