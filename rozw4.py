from functools import reduce

def hr_lab_demo():
    data = [
        {"n": "A", "s": 6, "v": 15000},
        {"n": "B", "s": 2, "v": 10000},
        {"n": "C", "s": 10, "v": 30000}
    ]

    seniorzy = list(filter(lambda p: p["s"] > 5, data))
    
    premie = list(map(lambda p: p["v"] * 0.15, seniorzy))
    
    koszt_calkowity = reduce(lambda a, b: a + b, premie, 0)
    
    return seniorzy, premie, koszt_calkowity

wynik = hr_lab_demo()
print(f"Seniorzy: {wynik[0]}")
print(f"Premie: {wynik[1]}")
print(f"Całkowity koszt: {wynik[2]}")
