import asyncio

async def machine_work(machine_name, cycle_time, total_time):
    elapsed_time = 0
    while elapsed_time < total_time:
        print(f"{machine_name} - Start cyklu")
        await asyncio.sleep(cycle_time)
        elapsed_time += cycle_time
        print(f"{machine_name} - Koniec cyklu, czas: {elapsed_time} s")
    print(f"{machine_name} zakończyła pracę po {total_time} sekundach.\n")

async def main():
    total_time = 15

    tasks = [
        machine_work("Maszyna A", 2, total_time),  # Maszyna A działa co 2 sekundy
        machine_work("Maszyna B", 3, total_time),  # Maszyna B działa co 3 sekundy
        machine_work("Maszyna C", 5, total_time)   # Maszyna C działa co 5 sekund
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())