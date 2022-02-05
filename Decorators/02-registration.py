
registry = []


def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

# 作为模块导入会自动执行函数装饰器


if __name__ == "__main__":
    main()
