try:
    fails = input("darbs")
    paplasinajums = input("txt")
    with open(f"{fails}.{paplasinajums}", 'r') as f:
        print("Faila saturs:")
        print(f.read())
except FileNotFoundError:
    print(f"Faila nevar atrast.")
except Exception as e:
    print(f"Radās kļūda: {e}")
