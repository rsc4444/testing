START_YEAR = 1970
SECONDS_PER_DAY = 86400


def getNumberOfLeapYears(startYear,endYear):
    count = 0
    for y in range(startYear,endYear):
        if y % 4 == 0:
            count += 1
    return count


def unixToDate(year,month,day,hour,minute,second):
    if int(year) < START_YEAR:
        return year
    unixTime = 0
    years = year - START_YEAR
    yearsInSeconds = (years*365 + getNumberOfLeapYears(START_YEAR,year)) * SECONDS_PER_DAY
    
    
    
    
print(unixToDate(int("2022"),int("05"),int("13"),int("15"),int("17"),int("28")))