def vacuum_cleaner(location, room_status):
    if room_status[location] == "Dirty":
        print(f"Room {location} is Dirty")
        print("Action: SUCK")
        room_status[location] = "Clean"
    else:
        if location == "A":
            print("Room A is Clean")
            print("Action: Move Right to Room B")
            location = "B"
        else:
            print("Room B is Clean")
            print("Action: Move Left to Room A")
            location = "A"

    return location, room_status

room_status = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:
    location, room_status = vacuum_cleaner(location, room_status)

    if room_status["A"] == "Clean" and room_status["B"] == "Clean":
        print("\nAll rooms are clean.")
        break

print("Final Room Status:", room_status)
