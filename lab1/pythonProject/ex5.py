import asyncio



def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

async def fibonacci_sequence_for_n_seconds(n):
    fib_numbers = fibonacci(n)
    for number in fib_numbers:
        print(number)
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(fibonacci_sequence_for_n_seconds(5))