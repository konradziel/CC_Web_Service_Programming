import aiohttp
import asyncio


async def fetch_weather(city: dict) -> dict:
    base_url = "https://api.open-meteo.com/v1/forecast"
    lat, lon = city['latitude'], city['longitude']
    url = f"{base_url}?latitude={lat}&longitude={lon}&hourly=temperature_2m&forecast_days=2"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    'city': city['name'],
                    'temperatures': data['hourly']['temperature_2m'][24:48]  # Następny dzień
                }
            else:
                return None


def calculate_average_temperature(temperatures: list) -> float:
    return round(sum(temperatures) / len(temperatures), 2)


async def main(cities: list) -> dict:
    tasks = [fetch_weather(city) for city in cities]
    results = await asyncio.gather(*tasks)

    # Filtruj wyniki i oblicz średnią temperaturę
    city_weather = []
    for result in results:
        if result:
            avg_temp = calculate_average_temperature(result['temperatures'])
            city_weather.append({
                'city': result['city'],
                'avg_temp': avg_temp,
                'temperatures': result['temperatures']
            })

    # Sortowanie miast według średniej temperatury malejąco
    city_weather_sorted = sorted(city_weather, key=lambda x: x['avg_temp'], reverse=True)

    # Tworzenie słownika wyników
    sorted_weather_dict = {city['city']: city for city in city_weather_sorted}

    return sorted_weather_dict


cities = [
    {'name': 'Zakopane', 'latitude': 49.299, 'longitude': 19.9489},
    {'name': 'Warszawa', 'latitude': 52.2297, 'longitude': 21.0122},
    {'name': 'Berlin', 'latitude': 52.52, 'longitude': 13.4050},
    {'name': 'Nowy Jork', 'latitude': 40.7128, 'longitude': -74.0060},
    {'name': 'Tokio', 'latitude': 35.6762, 'longitude': 139.6503},
]

if __name__ == "__main__":
    sorted_weather = asyncio.run(main(cities))
    for city, weather in sorted_weather.items():
        print(f"City: {city}, Average Temp: {weather['avg_temp']}°C")
