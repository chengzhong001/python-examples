import datetime


def test1():
    str_value = "hello，python coders"
    print(f"{str_value = }")


def test2():
    num_value = 123
    print(f"{num_value % 2 = }")


def test3():
    today = datetime.date.today()
    print(f"{today: %Y%m%d}")
    # 20211019
    print(f"{today =: %Y%m%d}")


def test4():
    a = 42
    print(f"{a:b}")  # 2进制
    print(f"{a:o}")  # 8进制
    print(f"{a:x}")  # 16进制，小写字母
    print(f"{a:X}")  # 16进制，大写字母
    print(f"{a:c}")  # ascii 码


def test5():
    num_value = 123.456
    print(f'{num_value = :.2f}')    # 保留 2 位小数
    nested_format = ".2f"           # 可以作为变量
    print(f'{num_value:{nested_format}}')


def test6():
    x, n = 'test', 10
    print(f'{x:>10}')   # 右对齐，左边补空格
    print(f'{x:*<10}')  # 左对齐，右边补*
    print(f'{x:=^10}')  # 居中，左右补=
    print(f'{x:~^{n}}') # 可以传入变量 n


def test7():
    x = '中'
    print(f"{x!s}")  # 相当于 str(x)
    print(f"{x!r}")  # 相当于 repr(x)


def test8():
    class MyClass:
        def __format__(self, format_spec) -> str:
            print(f'MyClass __format__ called with {format_spec=!r}')
            return "MyClass()"

    print(f'{MyClass():bala bala  %%MYFORMAT%%}')


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
