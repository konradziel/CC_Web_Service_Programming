import aiohttp
import asyncio
from datetime import datetime

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def process_weather_data(url: str, filter_mask: dict) -> dict:
    data = await fetch(url)

    temperatures = data['hourly']['temperature_2m']
    wind_speeds = data['hourly'].get('wind_speed_10m', None)
    times = data['hourly']['time']

    fullDatetime = datetime.now()

    city_result = {"url": url, "temperatures": [], "times": [], "wind_speeds": []}

    for i in range(24):
        if i > fullDatetime.hour:
            temp_ok = True
            wind_ok = True

            if "temperature_2m" in filter_mask:
                temp_ok = eval(f"{temperatures[i]} {filter_mask['temperature_2m']}")

            if wind_speeds and "wind_speed_10m" in filter_mask:
                wind_ok = eval(f"{wind_speeds[i]} {filter_mask['wind_speed_10m']}")

            if temp_ok and wind_ok:
                city_result['temperatures'].append(temperatures[i])
                city_result['times'].append(times[i])
                if wind_speeds:
                    city_result['wind_speeds'].append(wind_speeds[i])

    if city_result['temperatures']:
        return city_result
    return None

async def main() -> None:
    urls = [
        "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m,wind_speed_10m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m,wind_speed_10m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m,wind_speed_10m&forecast_days=1",
        "https://api.open-meteo.com/v1/forecast?latitude=60.1695&longitude=24.9354&hourly=temperature_2m,wind_speed_10m&forecast_days=1",
    ]

    filter_mask = {
        "wind_speed_10m": "< 20"
    }

    tasks = [process_weather_data(url, filter_mask) for url in urls]
    results = await asyncio.gather(*tasks)

    filtered_results = [result for result in results if result is not None]

    for result in filtered_results:
        print(f"--- Results for URL: {result['url']} ---")
        for time, temp, wind in zip(result['times'], result['temperatures'], result['wind_speeds']):
            print(f"Time: {time}, Temperature: {temp}°C, Wind Speed: {wind} km/h")


if __name__ == "__main__":
    asyncio.run(main())
