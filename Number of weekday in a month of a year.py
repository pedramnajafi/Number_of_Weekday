import calendar
from operator import countOf
import re
import sys
from datetime import date
from datetime import timedelta
from datetime import datetime

cal = calendar.TextCalendar(calendar.MONDAY)

while True:
    print("\n ----------------------------------------- \n Which day of the week you want to count? or type (e) to exit")
    day_of_week = input(" 0 : Monday \n 1 : Tuesday \n 2 : Wednesday \n 3 : Thursday \n 4 : Friday \n 5 : Saturday \n 6 : Sunday \n - \n e : EXIT \n")

    if day_of_week == 'e':
        sys.exit()
    else:
        if (int(day_of_week) > 6) or (int(day_of_week) < 0):
            print("XXX You have entered a wrong number. Choose only between 0 to 6")
        else:
            year_str = input("\nWhich YEAR you want to check? \n")
            try:
                year_int = int(year_str)
                if (year_int < 1000) or (year_int > 9999):
                    print("XXX You have not entered a valid YEAR. Try Again")
                else:
                    month_str = input("\nWhich MONTH you want to check? \n")
                    try:
                        month_int = int(month_str)
                        if (month_int < 1) or (month_int > 12):
                            print("XXX You have not entered a valid MONTH. Choose only between 1 to 12")
                        else:
                            created_calendar = cal.formatmonth(year_int, month_int, 0, 0)
                            week_list = calendar.monthcalendar(year_int, month_int)
                            day_count = 0
                            for week in week_list:
                                if week[int(day_of_week)] !=0:
                                    day_count += 1
                            print('')
                            if int(day_of_week) == 0:
                                day_name = "Monday"
                            elif int(day_of_week) == 1:
                                day_name = "Tuesday"
                            elif int(day_of_week) == 2:
                                day_name = "Wednesday"
                            elif int(day_of_week) == 3:
                                day_name = "Thursday"
                            elif int(day_of_week) == 4:
                                day_name = "Friday"
                            elif int(day_of_week) == 5:
                                day_name = "Saturday"
                            elif int(day_of_week) == 6:
                                day_name = "Sunday"
                            print("The number of", day_name, "in", year_str, "/", month_str, "is :", day_count)

                                
                    except:
                        print("XXX You have not entered a number. Choose only between 1 to 12")
            except:
                print("XXX You have not entered a number. Choose only between 1000 to 9999")


