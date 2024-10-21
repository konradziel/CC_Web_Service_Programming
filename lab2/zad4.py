import aiohttp
import asyncio
from datetime import datetime

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&forecast_days=1"
    data = await fetch(url)

    temperatures = data['hourly']['temperature_2m']
    times = data['hourly']['time']

    fullDatetime = datetime.now()
    for i in range(24):
        if(i>fullDatetime.hour):
            next_temperature = temperatures[i]
            next_time = times[i]
            break;

    print(f"Temperature for {next_time}: {next_temperature}°C")


if __name__ == "__main__":
    asyncio.run(main())
