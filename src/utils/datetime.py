from datetime import datetime
import re


def cast(string_date, format='%d%m%Y'):
    return datetime.strptime(string_date, format).date()


def validate(text_date, pattern=r'^\d{1,2}\/\d{1,2}\/\d{4}$'):
    return re.match(f"{pattern}", text_date)
