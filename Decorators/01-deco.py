


def deco(func):
    def inner():
        print("running inner()")
        func()
    return inner

@deco
def target():
    print("runnning target()")

if __name__ == "__main__":
    target()