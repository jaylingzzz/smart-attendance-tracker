from reports import calculate_summary


def risk_level(percentage):
    """
    Determine attendance risk level.
    """
    if percentage >= 90:
        return "Excellent"

    elif percentage >= 80:
        return "Very Good"

    elif percentage >= 70:
        return "Monitor"

    elif percentage >= 60:
        return "Warning"

    return "High Risk"


def ai_suggestion(percentage):
    """
    Generate AI suggestion.
    """
    if percentage >= 90:
        return "Excellent attendance. Keep it up."

    elif percentage >= 80:
        return "Attendance is good. Stay consistent."

    elif percentage >= 70:
        return "Attendance is dropping. Monitor closely."

    elif percentage >= 60:
        return "Improve attendance immediately."

    return "Immediate intervention recommended."


def display_ai_report():
    """
    Display AI attendance analysis.
    """
    summary = calculate_summary()

    if summary.empty:
        return

    summary["Risk Level"] = summary["Attendance %"].apply(risk_level)

    summary["AI Suggestion"] = summary["Attendance %"].apply(ai_suggestion)

    print("\n========== AI RISK ANALYSIS ==========\n")

    print(
        summary[
            [
                "StudentID",
                "Name",
                "Attendance %",
                "Risk Level",
                "AI Suggestion"
            ]
        ].to_string(index=False)
    )
