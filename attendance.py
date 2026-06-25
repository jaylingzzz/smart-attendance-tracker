import os
import pandas as pd
from utils import get_today_date


STUDENTS_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"


def load_students():
    """
    Load students from students.csv.
    """
    if not os.path.exists(STUDENTS_FILE):
        print("Error: students.csv not found.")
        return pd.DataFrame()

    return pd.read_csv(STUDENTS_FILE)


def load_attendance():
    """
    Load attendance records. If the file doesn't exist,
    create an empty DataFrame with the correct columns.
    """
    if not os.path.exists(ATTENDANCE_FILE):
        return pd.DataFrame(
            columns=["Date", "StudentID", "Name", "Status"]
        )

    return pd.read_csv(ATTENDANCE_FILE)


def save_attendance(attendance_df):
    """
    Save attendance records to CSV.
    """
    attendance_df.to_csv(ATTENDANCE_FILE, index=False)


def attendance_exists(attendance_df, date):
    """
    Check whether attendance has already been taken today.
    """
    if attendance_df.empty:
        return False

    return date in attendance_df["Date"].values


def mark_attendance():
    """
    Record attendance for today's class.
    """
    students = load_students()

    if students.empty:
        return

    attendance = load_attendance()

    today = get_today_date()

    if attendance_exists(attendance, today):
        print(f"\nAttendance has already been recorded for {today}.")
        return

    print(f"\nRecording attendance for {today}\n")

    new_records = []

    for _, student in students.iterrows():

        while True:

            status = input(
                f"{student['StudentID']} - {student['Name']} (P/A): "
            ).strip().upper()

            if status == "P":
                status = "Present"
                break

            elif status == "A":
                status = "Absent"
                break

            else:
                print("Invalid input. Enter P or A.")

        new_records.append(
            {
                "Date": today,
                "StudentID": student["StudentID"],
                "Name": student["Name"],
                "Status": status,
            }
        )

    new_df = pd.DataFrame(new_records)

    attendance = pd.concat(
        [attendance, new_df],
        ignore_index=True
    )

    save_attendance(attendance)

    print("\nAttendance saved successfully.")


def view_attendance():
    """
    Display all attendance records.
    """
    attendance = load_attendance()

    if attendance.empty:
        print("\nNo attendance records found.")
        return

    print("\n========== ATTENDANCE RECORDS ==========\n")

    print(attendance.to_string(index=False))
