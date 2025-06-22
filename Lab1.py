# قائمة المقاعد المحجوزة
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

def check_and_book_seat():
    row = int(input("🎫 Enter row number (1-10): "))
    seat = int(input("🎫 Enter seat number (1-20): "))

    if (row, seat) in booked_seats:
        print(f"❌ Seat Row {row}, Seat {seat} is already booked.")
    else:
        print(f"✅ Seat Row {row}, Seat {seat} is available.")
        choice = input("Do you want to book it? (yes/no): ").lower()
        if choice == "yes":
            booked_seats.append((row, seat))
            print("✅ Seat booked successfully!")
        else:
            print("❎ Booking canceled.")

def display_booked_seats():
    print("\n📋 All Booked Seats:")
    for seat in booked_seats:
        print(f"Row {seat[0]}, Seat {seat[1]}")

def show_summary():
    print(f"\n🎟 Total Booked Seats: {len(booked_seats)}")
    row_counts = [0] * 10
    for seat in booked_seats:
        row_counts[seat[0] - 1] += 1
    for i in range(10):
        print(f"Row {i+1}: {row_counts[i]} seats booked")

# قائمة أوامر المستخدم
while True:
    print("\n==== Cinema Booking Menu ====")
    print("1. Check and Book a Seat")
    print("2. View All Booked Seats")
    print("3. Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_and_book_seat()
    elif choice == "2":
        display_booked_seats()
    elif choice == "3":
        show_summary()
    elif choice == "4" or choice.lower() == "exit":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠ Invalid option. Please choose 1-4.")

