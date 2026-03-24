users = [
    {"name": "Anna", "is_active": True},
    {"name": "Jan", "is_active": False},
    {"name": "Maria", "is_active": True}
]
active_user_names_func = list(
    map(lambda u: u["name"], filter(lambda u: u["is_active"], users))
)

print("Wynik funkcyjny:", active_user_names_func) # ['Anna', 'Maria']