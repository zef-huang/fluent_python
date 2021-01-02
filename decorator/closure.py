# coding=utf-8

def make_avg():
    num_list = []

    def avg(num):
        num_list.append(num)
        print(num_list)

    return avg


avg = make_avg() # 外部函数使用了内部 num_list 的作用域，所以 num_list 一直被引用，不会被垃圾回收
avg(12)
avg(18)

print('cell_contents:', avg.__closure__[0].cell_contents)
avg(25)




