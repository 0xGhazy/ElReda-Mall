
from win10toast import ToastNotifier

def win10_display_notification(title: str, message: str) -> None:
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration = 3)

def change_whours() -> None:
    hours_count = int(input("Enter Hours Number>>  "))
    with open("data center\hours.txt", "w") as file_obj:
        file_obj.write(str(hours_count))
