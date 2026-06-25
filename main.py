from attendance import mark_attendance, view_attendance
from reports import display_summary, search_student, export_report
from ai import display_ai_report
from utils import clear_screen, pause, validate_menu_choice


def display_menu():
    print("=" * 50)
    print("            SMART ATTENDANCE TRACKER")
    print("=" * 50)
    print("1. Register Attendance")
    print("2. View Attendance")
    print("3. Attendance Summary")
    print("4. AI Risk Analysis")
    print("5. Search Student")
    print("6. Export Report")
    print("7. Exit")
    print("=" * 50)


def main():
    while True:
        clear_screen()
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if not validate_menu_choice(choice):
            print("\nInvalid choice. Please try again.")
            pause()
            continue

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            display_summary()

        elif choice == "4":
            display_ai_report()

        elif choice == "5":
            search_student()

        elif choice == "6":
            export_report()

        elif choice == "7":
            print("\nThank you for using Smart Attendance Tracker!")
            break

        pause()
      
