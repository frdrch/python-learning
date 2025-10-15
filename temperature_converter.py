print("Конвертер температуры")

choice = input("Выбери направление перевода (C->F или F->C): ")

if choice.lower() == "c->f":
    c = float(input("Введите температуру в °C: "))
    f = c * 9/5 + 32
    print(f"Температура в °F: {f:.2f}")

elif choice.lower() == "f->c":
    f = float(input("Введите температуру в °F: "))
    c = (f - 32) * 5/9
    print(f"Температура в °C: {c:.2f}")

else:
    print("Неверный выбор. Используй 'C->F' или 'F->C'.")
