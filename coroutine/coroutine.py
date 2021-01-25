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

if __name__ == '__main__':
    main()
    