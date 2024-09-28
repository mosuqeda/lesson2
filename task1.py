username = ["juan", "pedro", "James", "sagaad","fuego"]
age = [-12,13,-14,15,-16]

for userdata in username:
    if userdata == "James":
        print("james cute")
        break
    else:
        print("james none")
        break

for agedata in age:
    if agedata > 0:
        print(str(agedata) + "positive")
    elif agedata < 0:
        print(str(agedata) + "negative")