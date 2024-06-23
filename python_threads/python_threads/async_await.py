import asyncio
from icecream import ic


async def task1(n):
    if n % 3 == 0:
        delay = 1
    else:
        delay = 0.1

    await asyncio.sleep(delay)
    ic("Hello", n)


async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(task1(i)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
