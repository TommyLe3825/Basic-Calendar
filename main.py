import calendar

print("Check your month according to the year: ")
# ask for year input
yy = int(input("Enter the year (yyyy): "))

# ask for month input
mm = int(input("Enter the month (1-12): "))

# displays calendar
print(calendar.month(yy, mm))
