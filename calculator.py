import datetime
import locale

year = raw_input("What year were you born? ")
month = raw_input("What month were you born? ")
day = raw_input("What day were you born? ")

death = raw_input("How old do you expect to be when you die? ")

today = datetime.datetime.now()

birthday = datetime.datetime(int(year), int(month), int(day), 0, 0)
deathday = birthday + datetime.timedelta(days=int(death)*365)

savings = raw_input("How much do you have saved? ")
budget = raw_input("How much money do you need a day to live? ")

networth_retirement = int(savings)
amount_needed_per_day = int(budget)

datetime.timedelta(7)
days_left = (deathday - today).days

total_amount_needed_from_retirement = days_left * amount_needed_per_day

rate = raw_input("What is your expected intrest rate? ")
annual_rate = float(rate)
if annual_rate >= 1:
    annual_rate = float(rate)/100

daily_rate = (annual_rate/12.0/4.0/7.0) + 1.0

number_additional_days = 0

while total_amount_needed_from_retirement - networth_retirement > 0 and days_left > 1:
    number_additional_days = number_additional_days + 1
    days_left = days_left - 1
    networth_retirement = networth_retirement * daily_rate
    total_amount_needed_from_retirement = total_amount_needed_from_retirement - amount_needed_per_day


print
locale.setlocale( locale.LC_ALL, '' )
print "You can retire on %s with %s in savings." % ((today + datetime.timedelta(days = number_additional_days)).strftime('%B %d, %Y'), locale.currency(networth_retirement, grouping=True))
