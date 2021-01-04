# 测试 __repr__ 魔法方法

class Test():
    def __repr__(self):
        return "this is repr"

t = Test()
print(t)