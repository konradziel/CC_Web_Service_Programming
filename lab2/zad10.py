import aiofiles
import aiohttp
import asyncio


async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to fetch data: {response.status}")
                return None


def process_data(data: dict) -> str:
    processed_data = f"Title: {data['title']}\nBody: {data['body']}\n\n"
    return processed_data


async def save_to_file(file_path: str, data: str):
    async with aiofiles.open(file_path, mode='a') as f:
        await f.write(data)


async def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Przykładowe API
    file_path = "D:\\Repositories\\CC_Web_Service_Programming\\lab2\\zad10_file\\zad10_file.json"

    data = await fetch_data(url)

    if data:
        processed_data = process_data(data)

        await save_to_file(file_path, processed_data)
        print(f"Data saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
