import aiohttp
import asyncio
from datetime import datetime

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def process_weather_data(url: str) -> None:
    data = await fetch(url)

    temperatures = data['hourly']['temperature_2m']
    times = data['hourly']['time']

    fullDatetime = datetime.now()

    next_temperature = None
    next_time = None

    for i in range(24):
        if i > fullDatetime.hour:
            next_temperature = temperatures[i]
            next_time = times[i]
            break

    if next_temperature and next_time:
        print(f"Temperature for {next_time}: {next_temperature}°C (URL: {url})")
    else:
        print(f"No valid data found for {url}")

async def main() -> None:
    urls = [
        "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=60.1695&longitude=24.9354&hourly=temperature_2m&forecast_days=1",
    ]

    tasks = [process_weather_data(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
