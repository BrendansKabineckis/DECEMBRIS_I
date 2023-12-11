import datetime
pašreizējā_stunda = datetime.datetime.now().hour
if 6 <= pašreizējā_stunda < 12:
    print("Labrīt!")
elif 12 <= pašreizējā_stunda < 18:
    print("Labdien!")
else:
    print("Labvakar!")