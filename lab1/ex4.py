import asyncio


async def ex4(numer):
    await asyncio.sleep(numer)
    print(numer)

async def main() -> None:
    task1 = asyncio.create_task(ex4(1))
    task2 = asyncio.create_task(ex4(2))
    task3 = asyncio.create_task(ex4(3))
    task4 = asyncio.create_task(ex4(4))
    task5 = asyncio.create_task(ex4(5))

    await task1
    await task2
    await task3
    await task4
    await task5
    
if __name__ == "__main__":
    asyncio.run(main())