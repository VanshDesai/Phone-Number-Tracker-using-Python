import random

indian_names = ["Aarav", "Vihaan", "Ananya", "Pari", "Arnav", "Kabir", "Advik", "Aadhya", "Vivaan", "Aaradhya", "Aryan", "Ishaan", "Reyansh", "Saanvi", "Aarush", "Anika", "Yuvan", "Angel", "Prisha", "Advika", "Shaurya", "Kaira", "Veer", "Myra", "Anaisha"]

l=[]
time = []
current_hour = 0

while len(time) < 25:
    if current_hour == 24:
        current_hour = 0
    current_min = 0
    current_hour += random.randint(0, 3)
    current_min += random.randint(0, 59)
    time.append(str(current_hour).zfill(2) + ":" + str(current_min).zfill(2))

for i in range(25):
    minutes=random.randint(0,60)
    seconds=random.randint(0,60)
    l.append(indian_names[random.randint(0,24)] + "   -->    " + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))

with open("call_record.txt", 'w') as f:
    f.write("|   Name   Duration        Time    |\n")
    for i in range(len(l)):
        f.write("{:<10}{:<20}mintues  -->  {}\n".format(str(i+1), l[i], time[i]))
