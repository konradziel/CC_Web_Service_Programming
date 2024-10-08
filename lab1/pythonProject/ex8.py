import asyncio


async def przetwarzanie_etap(plik, etap, czas):
    print(f"Rozpoczęcie: {plik} - {etap}")
    await asyncio.sleep(czas)
    print(f"Zakończenie: {plik} - {etap}")


async def przetwarzanie_plik(plik, etapy):
    for etap, czas in etapy:
        await przetwarzanie_etap(plik, etap, czas)
    print(f"Zakończono przetwarzanie pliku: {plik}")


async def main():
    pliki = [
        ("Plik 1", [("Wczytanie", 2), ("Analiza", 5), ("Zapis", 3)]),
        ("Plik 2", [("Wczytanie", 3), ("Analiza", 4), ("Zapis", 6)]),
        ("Plik 3", [("Wczytanie", 2), ("Analiza", 7), ("Zapis", 4)])
    ]

    tasks = [przetwarzanie_plik(plik, etap) for plik, etap in pliki]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
