import time
from datetime import datetime

def now(format='%d/%m/%Y'):
    return datetime.now().strftime(format)

def datetime_convert(date_string, current_format="%d/%m/%Y", new_format="%b, %Y"):

    current_date =  datetime(*(time.strptime(date_string, current_format)[0:6]))
    return current_date.strftime(new_format)
