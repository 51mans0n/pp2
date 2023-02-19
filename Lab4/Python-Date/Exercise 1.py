import datetime
date = datetime.datetime.today()
date = date - datetime.timedelta(5)
print(date.strftime("%c"))