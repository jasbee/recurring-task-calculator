def recurringTask(firstDate, k, daysOfTheWeek, n):
    days = []
    iday = 1
    imonth = 1
    iyear = 1900
    imonth_length = 31
    diff = 0
    x = 0
    total = 0
    k = (k * 7) - 7
    m1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_names = ["Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday"]

    day = int(firstDate[0:2])
    month = int(firstDate[3:5])
    year = int(firstDate[-4:])

    while x == 0:
        if (iyear % 4 == 0 and iyear % 100 != 0) or iyear % 400 == 0:
            month_lengths = m1
        else:
            month_lengths = m2
        imonth_length = month_lengths[imonth - 1]
        if iday < imonth_length:
            iday = iday + 1
            diff = diff + 1
        elif iday == imonth_length:
            if imonth < 12:
                imonth = imonth + 1
                iday = 1
                diff = diff + 1
            else:
                iday = 1
                imonth = 1
                iyear = iyear + 1
                diff = diff + 1
        if iday == day and imonth == month and iyear == year:
            x = 1

    while total < n:
        for p in range(7):
            if (week_names[((diff + 1) % 7)]) in daysOfTheWeek:
                if iday < 10:
                    a = str(iday)
                    a = '0' + a
                else:
                    a = str(iday)
                if imonth < 10:
                    b = str(imonth)
                    b = '0' + b
                else:
                    b = str(imonth)
                if total < n:
                    days.append(a + '/' + b + '/' + str(iyear))
                    total = total + 1
            if (iyear % 4 == 0 and iyear % 100 != 0) or iyear % 400 == 0:
                month_lengths = m1
            else:
                month_lengths = m2
            imonth_length = month_lengths[imonth - 1]

            if iday < imonth_length:
                iday = iday + 1
                diff = diff + 1
            elif iday == imonth_length:
                if imonth < 12:
                    imonth = imonth + 1
                    iday = 1
                    diff = diff + 1
                else:
                    iday = 1
                    imonth = 1
                    iyear = iyear + 1
                    diff = diff + 1

        for q in range(k):
            if (iyear % 4 == 0 and iyear % 100 != 0) or iyear % 400 == 0:
                month_lengths = m1
            else:
                month_lengths = m2
            imonth_length = month_lengths[imonth - 1]

            if iday < imonth_length:
                iday = iday + 1
                diff = diff + 1
            elif iday == imonth_length:
                if imonth < 12:
                    imonth = imonth + 1
                    iday = 1
                    diff = diff + 1
                else:
                    iday = 1
                    imonth = 1
                    iyear = iyear + 1
                    diff = diff + 1
    return days

firstDate = "31/08/2106"
k = 5
daysOfTheWeek = ["Monday", "Thursday"]
n = 10

print('Based on the information received these are ', end='')
print('the dates of the recurring tasks: ')
print(recurringTask(firstDate, k, daysOfTheWeek, n))
print('')
print('firstDate = ' + firstDate + ' | k = ' + str(k), end='')
print(' | daysOfTheWeek =' + str(daysOfTheWeek) + ' | n = ' + str(n))