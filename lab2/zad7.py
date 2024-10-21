import aiohttp
import asyncio

async def download_file(url: str, save_path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(save_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"File saved to {save_path}")
            else:
                print(f"Failed to download file. HTTP status: {response.status}")

async def main():
    url = "https://a.allegroimg.com/original/1e2e84/8f844dc74b63ab5cc29a0a4b3fd4"
    save_path = "D:\\Repositories\\CC_Web_Service_Programming\\lab2\\zad7_file\\zad7_file.jpg"
    await download_file(url, save_path)

if __name__ == "__main__":
    asyncio.run(main())
