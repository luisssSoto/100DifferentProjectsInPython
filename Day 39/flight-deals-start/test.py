import datetime

departure_date = datetime.datetime.now() + datetime.timedelta(days = 1)
departure_date.strftime("%Y-%m-%d")
return_date = departure_date + datetime.timedelta(days = 30 * 6)
return_date = return_date.strftime("%Y-%m-%d")
departure_date = str(departure_date)[:10]

print(type(departure_date))
print(type(return_date))