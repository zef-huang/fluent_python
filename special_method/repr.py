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
# 2.构建一个类，使其具有序列器的功能
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

    

# ------------------------------------------------------
# 3.构建一个类，使其具有切片的功能
# ------------------------------------------------------

class MySlice():
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        # 记录对象类型，使用切片后的序列重新实例化此类
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.array[index]).array
        else:
            return self.array[index]

if __name__ == '__main__':
    client = MySlice([1,2,3,4])
    print(client[1:3])
    print(tuple(client))


