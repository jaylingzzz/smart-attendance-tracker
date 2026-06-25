import pandas as pd
from attendance import load_attendance


def calculate_summary():
    """
    Calculate attendance summary for each student.
    """
    attendance = load_attendance()

    if attendance.empty:
        print("\nNo attendance records found.")
        return pd.DataFrame()

    summary = attendance.pivot_table(
        index=["StudentID", "Name"],
        columns="Status",
        aggfunc="size",
        fill_value=0
    ).reset_index()

    if "Present" not in summary.columns:
        summary["Present"] = 0

    if "Absent" not in summary.columns:
        summary["Absent"] = 0

    summary["Total Classes"] = summary["Present"] + summary["Absent"]

    summary["Attendance %"] = (
            summary["Present"] /
            summary["Total Classes"] * 100
    ).round(2)

    summary = summary[
        [
            "StudentID",
            "Name",
            "Present",
            "Absent",
            "Total Classes",
            "Attendance %"
        ]
    ]

    return summary


def display_summary():
    """
    Display attendance summary.
    """
    summary = calculate_summary()

    if summary.empty:
        return

    print("\n========== ATTENDANCE SUMMARY ==========\n")
    print(summary.to_string(index=False))


def search_student():
    """
    Search for a student by name or ID.
    """
    summary = calculate_summary()

    if summary.empty:
        return

    keyword = input("\nEnter Student Name or ID: ").strip().lower()

    result = summary[
        summary["Name"].astype(str).str.lower().str.contains(keyword) |
        summary["StudentID"].astype(str).str.contains(keyword)
        ]

    if result.empty:
        print("\nStudent not found.")
    else:
        print("\n")
    print(result.to_string(index=False))


def export_report():
    """
    Export attendance summary to report.csv.
    """
    summary = calculate_summary()

    if summary.empty:
        return

    summary.to_csv("report.csv", index=False)

    print("\nReport exported successfully as report.csv")
