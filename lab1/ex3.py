import asyncio

async def ex3(numer, czas):
    await asyncio.sleep(czas)
    print(f"Uruchomiła się korutyna {numer} po czasie {czas}s.")

async def main() -> None:
    task1 = asyncio.create_task(ex3(1, 3))
    task2 = asyncio.create_task(ex3(2, 1))

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())