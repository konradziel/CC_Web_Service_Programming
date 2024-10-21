import aiohttp
import asyncio

async def fetch(url: str, session) -> str:
    async with session.get(url) as response:
        return await response.text()

async def fetch_all_content(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)

async def main() -> None:
    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://httpbin.org/get",
        "https://www.github.com"
    ]

    content = await fetch_all_content(urls)

    for i, page_content in enumerate(content):
        print(f"--- Content from {urls[i]} ---\n{page_content[:200]}...\n")


if __name__ == "__main__":
    asyncio.run(main())