
def days_in_year(year):
    if year/4!=0:
        return 365;
    else:
        if year/100!=0:
            return 366;
        else:
            if year/400!=0:
                return 365;
            else:
                return 366;

def daysOfMonths(month):
    if month==1:
        return 31;
    if month==2:
        return 28;
    if month==3:
        return 31;
    if month==4:
        return 30;
    if month==5:
        return 31;
    if month==6:
        return 30;
    if month==7:
        return 31;
    if month==8:
        return 31;
    if month==9:
        return 30;
    if month==10:
        return 31;
    if month==11:
        return 30;
    if month==12:
        return 31;

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total=0
    
    while day1!=day2:
        total=total+1
        day1=day1+1;
        if day1>daysOfMonths(month1):
            day1=day1%daysOfMonths(month1)
            month1=month1+1
    while month1!=month2:
        total=total+daysOfMonths(month1)
        month1=month1+1;
        if month1>12:
            month1=month1%12
            year1=year1+1
    while year1<year2:
        total=total+days_in_year(year1)
        year1=year1+1
    return total
        


