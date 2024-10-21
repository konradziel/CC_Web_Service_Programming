import aiohttp
import asyncio


async def fetch(url: str, session: aiohttp.ClientSession, retries: int = 3) -> dict:
    for attempt in range(retries + 1):
        try:
            async with session.get(url) as response:
                if 200 <= response.status < 300:
                    return await response.json()  # Zwróć odpowiedź w przypadku sukcesu
                elif 500 <= response.status < 600:
                    print(f"Server error {response.status}. Retrying... (attempt {attempt + 1})")
                    continue  # Spróbuj ponownie w przypadku błędu serwera
                else:
                    print(f"Received unexpected status code: {response.status}")
                    return None
        except Exception as e:
            print(f"Request failed: {e}. Retrying... (attempt {attempt + 1})")
            continue
    return None  # Zwróć None, jeśli wszystkie próby nie powiodły się


async def main(url: str, num_requests: int) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)

    # Filtruj odpowiedzi, aby zachować tylko te z kodem 200-299
    successful_responses = [response for response in responses if response is not None]

    return successful_responses


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    num_requests = 100

    successful_responses = asyncio.run(main(url, num_requests))

    print(f"Received {len(successful_responses)} successful responses.")
