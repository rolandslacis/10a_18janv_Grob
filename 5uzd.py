ievade=input("Ievadi savu vārdu!:")

def galvena_funkcija():
    try:
        with open("darbs.txt","w", encoding="utf-8") as b:
            b.write(ievade)
            if ievade in b:
                print("Ir izveidots fails!")
            
    except SyntaxError:
        print("Nav pareizi ievadīts!")

if __name__ == "__main__":
    galvena_funkcija()
