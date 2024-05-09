fails = input("darbs")

try:
    with open(fails, 'r') as f:
        saturs = f.read()
    print("Faila saturs:")
    print(saturs)
except FileNotFoundError:
    print("Failu nevar atrast.")
