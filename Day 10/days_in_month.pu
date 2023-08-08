def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(in_year,in_month):
  if in_month> 12 or in_month < 1 or in_year < 0 :
      return "invalid input"  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  #if is_leap(in_year):
  #    month_days[1] = 29
  
  if is_leap(in_year) and month == 2:
      return 29
  
  return month_days[in_month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
