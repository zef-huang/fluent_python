# coding=utf8


# =============================================================
# 1. 手动实现一个协程, 相比于生成器，多了相互交流
# =============================================================

def my_coroutine():
    for i in [1,2,4]:
        item = yield i
        print('接收到的消息为：%s' % item)


def main():
    cor = my_coroutine()
    first_resp = next(cor)
    print("see the first data", first_resp)

    # 给协程发送消息
    second = cor.send(12)
    # second = next(cor)
    print("see the first data", second)

    third = cor.send(100)
    # third = next(cor)
    print("see the first data", third)


# =============================================================
# 2. 实现一个求平均值的协程
# =============================================================


def avg_coro():
    count = 0
    sum = 0
    while True:
        recieve_number = yield
        if recieve_number:
            sum += recieve_number
            count += 1
        else:
            break
    
    return sum/count  if count else 0


def main2():
    generator = avg_coro()
    # 预激活
    next(generator)

    generator.send(3)
    generator.send(33)
    generator.send(33)
    try:
        generator.send('')
    except Exception as result:
        print("avg is ", result)


if __name__ == '__main__':
    main2()
    