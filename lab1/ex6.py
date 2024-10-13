import asyncio


async def fetch(delay: int):
    await asyncio.sleep(delay)
    return(delay*2)


async def main() -> None:
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(fetch(i*2+3)))

    result = await asyncio.gather(*tasks, return_exceptions=True);
    print(result)

if __name__ == "__main__":
    asyncio.run(main())