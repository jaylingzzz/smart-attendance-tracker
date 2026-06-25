from datetime import datetime


def clear_screen():
    pass


def pause():
    """
    Waits for the user before continuing.
    """
    input("\nPress Enter to continue...")


def get_today_date():
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return datetime.now().strftime("%Y-%m-%d")


def validate_menu_choice(choice):
    """
    Checks if the menu choice is valid.
    """
    return choice in ["1", "2", "3", "4", "5", "6", "7"]
  
