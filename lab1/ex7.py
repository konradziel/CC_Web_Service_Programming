import asyncio


async def przygotowywanie_etap(danie, etap, czas):
    print(f"Rozpoczęcie: {danie} - {etap}")
    await asyncio.sleep(czas)
    print(f"Zakończenie: {danie} - {etap}")


async def przygotowywanie_danie(danie, etapy):
    for etap, czas in etapy:
        await przygotowywanie_etap(danie, etap, czas)
    print(f"Zakończono przygotowanie dania: {danie}")


async def main():
    dania = [
        ("Danie 1", [("Krojenie warzyw", 2), ("Gotowanie makaronu", 5), ("Smażenie mięsa", 3)]),
        ("Danie 2", [("Krojenie warzyw", 3), ("Gotowanie ziemniaków", 4), ("Smażenie ryby", 6)]),
        ("Danie 3", [("Krojenie mięsa", 2), ("Gotowanie ryżu", 7), ("Smażenie warzyw", 4)])
    ]

    tasks = [przygotowywanie_danie(danie, etap) for danie, etap in dania]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
