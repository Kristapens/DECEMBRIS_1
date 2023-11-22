import datetime

pašreizējā_stunda = datetime.datetime.now().hour

if 6 <= pašreizējā_stunda < 12:
    sveiciens = "Labrīt!"
elif 12 <= pašreizējā_stunda < 18:
    sveiciens = "Labdien!"
else:
    sveiciens = "Labvakar!"

print(sveiciens)
