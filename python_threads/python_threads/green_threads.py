import gevent
from gevent import monkey
from icecream import ic

# Patch the standard library to replace blocking calls with asynchronous ones
monkey.patch_all()


def task1(n):
    if n % 3 == 0:
        delay = 1
    else:
        delay = 0.1

    gevent.sleep(delay)
    ic("Hello", n)


def main():
    tasks = [gevent.spawn(task1, i) for i in range(5)]
    gevent.joinall(tasks)


if __name__ == "__main__":
    main()
