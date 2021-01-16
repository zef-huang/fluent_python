# --------------------------------------------------------------------
# 1. 手动实现一个上下文管理器
# --------------------------------------------------------------------

from contextlib import contextmanager


@contextmanager
def reverse_output():
    import sys
    std_write = sys.stdout.write

    def reverse_write(text):
        std_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 
    sys.stdout.write = std_write


if __name__ == '__main__':
    with reverse_output() as f:
        print("hello world")

    print('hello world')
    