import phonenumbers
import folium
from geopy.distance import geodesic
import tkinter as tk
from tkinter import messagebox
import random

from phonenumbers import geocoder

def track_phone():
    number = phone_entry.get()
    root.destroy()
    if not number:
        messagebox.showerror("Error", "Please enter a phone number")
    else:
        pepnumber = phonenumbers.parse(number)
        print(pepnumber)
        location = phonenumbers.geocoder.description_for_number(pepnumber, "en")
        print(location)

        from phonenumbers import carrier
        service_provider = phonenumbers.parse(number)
        print(carrier.name_for_number(service_provider, "en"))

        from opencage.geocoder import OpenCageGeocode

        key = "09d0d101b55a4e479cb470af91ca7c45"
        geocoder = OpenCageGeocode(key)
        qurey = str(location)
        result = geocoder.geocode(qurey)

        # print(result)
        lng = result[0]['geometry']['lng']
        lat = result[0]['geometry']['lat']

        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)

        myMap.save(f"{location}_location.html")

def distance_phone():
    number = phone_entry1.get()
    number1 = phone_entry2.get()
    root.destroy()
    if not number:
        messagebox.showerror("Error", "Please enter a phone number")
    else:
        pepnumber = phonenumbers.parse(number)
        location = phonenumbers.geocoder.description_for_number(pepnumber, "en")

        from opencage.geocoder import OpenCageGeocode

        key = "09d0d101b55a4e479cb470af91ca7c45"
        geocoder = OpenCageGeocode(key)
        qurey = str(location)
        result = geocoder.geocode(qurey)

        lng = result[0]['geometry']['lng']
        lat = result[0]['geometry']['lat']

        pepnumber = phonenumbers.parse(number1)
        location1 = phonenumbers.geocoder.description_for_number(pepnumber, "en")

        from opencage.geocoder import OpenCageGeocode

        key = "09d0d101b55a4e479cb470af91ca7c45"
        geocoder = OpenCageGeocode(key)
        qurey = str(location1)
        result = geocoder.geocode(qurey)

        lng1 = result[0]['geometry']['lng']
        lat1 = result[0]['geometry']['lat']

        coord1=(lat,lng)
        coord2=(lat1,lng1)
        distance = geodesic(coord1, coord2).kilometers
        print(f"Distance between {location} and {location1} : {distance:.2f}kms")

def fetch_call_history():
    indian_names = [
        "Aarav", "Aisha", "Arjun", "Ananya", "Dev",
        "Diya", "Ishaan", "Ishika", "Kabir", "Kiara",
        "Laksh", "Maya", "Neel", "Nisha", "Om",
        "Priya", "Rahul", "Riya", "Siddharth", "Sonia",
        "Tanvi", "Vikram", "Zara", "Yash", "Natasha"
    ]

    # english_names = [
    #     "Adam", "Emily", "Benjamin", "Olivia", "Christopher",
    #     "Sophia", "Daniel", "Ava", "Ethan", "Mia",
    #     "Gabriel", "Isabella", "Henry", "Charlotte", "Isaac",
    #     "Emma", "Jack", "Lily", "James", "Grace",
    #     "Liam", "Harper", "Matthew", "Amelia", "William"
    # ]

    l=[]
    time = []
    current_hour = 0
    while len(time) < 25:
        if current_hour == 24:
            current_hour = 0
        current_min = 0
        current_hour += random.randint(0, 3)
        current_min += random.randint(0, 59)
        time.append(str(current_hour) + ":" + str(current_min))
    for i in range(0, 25):
        minutes=random.randint(0,60)
        seconds=random.randint(0,60)
        l.append(indian_names[random.randint(0,24)]+"   -->    "+str(minutes)+":"+str(seconds))
    f = open("call_record.txt", 'w')
    f.write("   Name              Duration              Time\n")
    for i in range(len(l)):
        f.write(str(i+1)+"  "+l[i]+" mintues    -->     "+time[i]+"\n")
    f.close()

def fetch_message_history():
    name=["SwiftMessage","TxtTalk","SpeedyText","RapidCom","QuickTxt","SnapChat","InstantLink","MessageMe",
          "ExpressTxt","DirectDial","InstantChat","ByteBlast","SwiftSend","SnapTxt","ZipZap","ExpressMessage",
        "QuickConnect","BlinkText","RapidRelay","FlashChat"]

    message = ["Hello, how are you today?","What's up?","Have a great day!","Good morning!",
               "Hope you're doing well.","Just checking in.","Wishing you a fantastic day!",
               "How's everything going?","Thinking of you!","Sending positive vibes your way.",
               "You're awesome!","Keep up the good work!","Hope to catch up soon.",
               "Stay strong and positive!","Sending virtual hugs!","Believe in yourself!",
               "Remember to take breaks!","You've got this!","Chin up, buttercup!","Make today amazing!"]
    l = []
    l1 = []
    for i in range(0, 25):
        l1.append(name[random.randint(0, 19)])
    for i in range(0, 25):
        l.append(message[random.randint(0, 19)])
    f=open("message_history.txt",'w')
    for i in range(len(l)):
        f.write(str(i+1)+" "+l1[i]+" -> "+l[i]+"\n")
    f.close()

while True:
    print("""
1. find location
2. find distance between 2 numbers
3. phone list
4. message list
5. exit
    """)
    try:
        choice=int(input("enter choice :"))
    except Exception as e:
        print("you enter invalid input pls enter again")
        continue
    if choice==1:
        root = tk.Tk()
        root.title("Phone Number Tracker")

        phone_label = tk.Label(root, text="Enter Phone Number:")
        phone_label.pack()

        phone_entry = tk.Entry(root)
        phone_entry.pack()

        track_button = tk.Button(root, text="Track", command=track_phone)
        track_button.pack()

        root.mainloop()
    elif choice==2:
        root = tk.Tk()
        root.title("Phone Number Tracker")

        phone_label1 = tk.Label(root, text="Enter Phone Number 1:")
        phone_label1.pack()

        phone_entry1 = tk.Entry(root)
        phone_entry1.pack()

        phone_label2 = tk.Label(root, text="Enter Phone Number 2:")
        phone_label2.pack()

        phone_entry2 = tk.Entry(root)
        phone_entry2.pack()

        track_button = tk.Button(root, text="Track", command=distance_phone)
        track_button.pack()

        root.mainloop()
    elif choice==3:
        fetch_call_history()
        print("call history fetch")
    elif choice==4:
        fetch_message_history()
        print("message history fetch")
    elif choice==5:
        break
    else:
        print("invalid choice")
