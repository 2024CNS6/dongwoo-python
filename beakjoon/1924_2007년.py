import calendar
m,d=map(int,input().split())
day=calendar.day_abbr[calendar.weekday(2007,m,d)]
print(day.upper())