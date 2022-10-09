# @Сделайте так, чтобы число
# секунд отображалось в виде дни: часы: минуты: секунды.

new_time = 3672112


def replace_time(seconds: int) -> str:
    days = seconds // 86400
    seconds -= days*86400
    hours = seconds // 3600
    seconds -= hours*3600
    minute = seconds // 60
    seconds -= minute*60

    print("Days:{:.55f} Hours:{:.1f} Minute::{:.2f}:{:.2f}".format(
        days, hours, minute, seconds))


print(replace_time(new_time))
