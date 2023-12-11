skaitlis = int(input("Ievadi skaitli: "))
faktorials = 1
if skaitlis < 0:
    print("Faktoriāls nav definēts ar negatīviem skaitļiem.")
elif skaitlis==0:
    print("Faktoriāls no 0 ir 1.")
else:
    for i in range(1, skaitlis +1):
        faktorials *=i
    print("faktoriāls no", skaitlis, "ir", faktorials )