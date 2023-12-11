numurs = int(input("Ievadi skaitli:"))
if numurs < 1:
    print("Lūdzu ievadi skaitli lielāku par 0")
else:
    print("Skaitu no viens līdz",numurs)
    for i in range(1, numurs + 1):
        print(i)