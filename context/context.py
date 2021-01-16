# --------------------------------------------------------------------
# 1. 手动实现一个上下文管理器
# contextmanager 和 yield 搭配使用
# --------------------------------------------------------------------

from contextlib import contextmanager


@contextmanager
def reverse_output():
    import sys
    std_write = sys.stdout.write

    def reverse_write(text):
        std_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield
    except Exception as e:
        print(e)

    sys.stdout.write = std_write


if __name__ == '__main__':
    with reverse_output() as f:
        print("hello world")
        print(2/0)

    print('hello world')
    