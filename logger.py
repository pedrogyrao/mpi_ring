import datetime


def log(message):
    n = datetime.datetime.now()
    now = datetime.datetime(
        day=n.day, month=n.month, year=n.year,
        hour=n.hour, minute=n.minute, second=n.second,
        microsecond=n.microsecond)
    print(f"[{now.isoformat().replace('T', ' ')}] {message}")
