print("Yaer to Second Converter")
print("------------------------")
print()

NumberOfTotalYear = int(input("Enter the number of Total years: "))
NumberOfLeapyear = int(input("Enter the number of leap years in it: "))

if NumberOfTotalYear >= NumberOfLeapyear:
  NumberOfNonLeapyear = NumberOfTotalYear - NumberOfLeapyear
  print()
  
  DaysInYear = 365
  DaysInLeapyear= 366
  HoursInDay = 24
  MinutesInHour = 60
  SecondsInMinute = 60
  
  SecondsInYear = DaysInYear * HoursInDay * MinutesInHour * SecondsInMinute
  TotalSecondsInYear = NumberOfNonLeapyear * DaysInYear * HoursInDay * MinutesInHour * SecondsInMinute
  
  SecondsInLeapyear = DaysInLeapyear * HoursInDay * MinutesInHour * SecondsInMinute
  TotalSecondsInLeapyear = NumberOfLeapyear * DaysInLeapyear * HoursInDay * MinutesInHour * SecondsInMinute
  
  print("Total Seconds in a year: ", SecondsInYear)
  print("Totla Seconds in a leap year: ", SecondsInLeapyear)
  
  print("Total Seconds in", NumberOfTotalYear, "years is", TotalSecondsInYear + TotalSecondsInLeapyear)

else:
  print("Number of leap years cannot be more than the total years")
