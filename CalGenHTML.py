# This is a sample Python script.
from datetime import date, timedelta
import sys
import traceback

def month(a):
    bulans = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember","[]"]
    bulans = ["Jan.", "Feb.", "Mar.", "April", "Mei", "Juni", "Juli", "Agus.", "Sept.", "Okto.", "Nov.", "Des.","[]"]

    return bulans[a-1]


def isHoliday(day):
    for holiday_start, holiday_end in holidays:
        if day >= holiday_start and day < holiday_end:
            return True
    return False

    

days = 90

now = date.today()

data =[]
daysFR = ["Lundi", "Mardi", "Mercredi", "Jeudi","Vendredi", "Samedi", "Dimanche"]
daysID = ["Senin ", "Selasa", "Rabu  ", "Kamis ","Jumat ", "Sabtu ", "Minggu"]
sepID = ["------", "------","------","------","------","------","------"]
sepID = ["______","______","______","______","______","______","______"]
sepID = ["======","======","======","======","======","======","======"]
print(" | ".join(daysFR))

holidays = [(date(2025,10,18), date(2025,11,3)), 
            (date(2025,12,20), date(2026,1,5)),
            (date(2026,2,7), date(2026,2,23)),
            (date(2026,4,4), date(2026,4,20))]
            
holiday_start = date(2025,10,18)
holiday_end = date(2025,11,3)

start = date.today() - timedelta(days= date.today().weekday())
print(start)
print("|  " +"  |  ".join(daysID)+"  |")
print("|==" +"==|==".join(sepID)+"==|")
#data.append(days)
line = []
lines = []
today = start
yesterday = start
# start_month = today.month
# end_month  = today.month

endMonthLine = False
classes = []
lineC = []
isLastMonthLine = False

aaaa = []
colMonthA = {}
colMonthZ = {}
aaa = 0
aaMonth = ""
zzz = 0
zzMonth = ""

weeks=14
week_nums = []
for n in range(0, weeks*7):
    aaaa.append(str(n))
    try:
        today = start + timedelta(days=n)
        nextLineDay = today+timedelta(days=7)
        todayClasses = "day"

        day = today.day
        week = today.isocalendar().week
        #print(today, week)
        day = str(day)
        line.append(day)
        if len(line) % 7 == 0 :
        
            week_nums.append(week)

    
        dayC = ["day"]
        if isHoliday(today):
            dayC.append("holiday")
        dayC.append("dow"+str(today.weekday()))
        dayC.append("mn"+str(today.month))
        if not today.month == yesterday.month:
            dayC.append("firstDay")
        if today.month != nextLineDay.month:
            dayC.append("lastWeek")
        lineC.append(" ".join(dayC ))

        if len(line) == 7:
            # end of week line
            a = (today+timedelta(days=-7)).month
            b = today.month
            aa = a
            bb = b

            if n > 6 and a == (today+timedelta(days=-14)).month:
                #
                aa = 13
                aaa += 1
            else:
                aaa = 1
            if n > 6 and b == (today+timedelta(days=-7)).month:
                bb = 13
                zzz += 1
            else:
                zzz = 1

            colMonthA[month(a)] = aaa
            colMonthZ[month(b)] = zzz

            line = [month(aa)] + line + [month(bb)]
            lineC = [" ".join(["month", f"mn{aa}"])] + lineC + [" ".join(["month", f"mn{bb}"])]

            print(">>>>>>>>", len(lineC))
            lines.append(line)
            classes.append(lineC)
            # print("|  "+"  |  ".join(line)+"  |")
            # print("#  ".join(lineC))
            aaaa = []
            line = []#print(start + timedelta(days=n))
            lineC=[]
        yesterday = today
    except Exception as ex:
        print(traceback.format_exc())

print("week nums: ", week_nums)
print("|==" + "==|==".join(sepID) + "==|")
print(colMonthA)
print("------")
print(colMonthZ)
print(len(classes))
with open("cal.html", 'w') as cal:
    print("<html><head><link rel=\"stylesheet\" href=\"cal.css\"></head><body>", file=cal)
    print("<table>", file=cal)
    print("<tr><th></th><th class=\"dName\">"+"</th><th class=\"dName\">".join(daysID)+"</th><th></th><tr>", file=cal)
    row = 0
    for line in lines:
        print("--------------------------")
        print("<tr>", file=cal)
        rowSpanAA = colMonthA[line[0]] if line[0] != "[]" else None
        rowSpanZZ = colMonthZ[line[-1]] if line[-1] != "[]" else None
        if rowSpanAA:
            print(f"<td rowspan=\"{rowSpanAA}\" class=\"{classes[row][0]}\"><span class=\'left\'>{line[0]}</span></td>", file=cal)

        rowCells = []
        for n in range(1, 8):
            # print(n)
            # print(f"{row} - {classes[row]}  - {n}")
            cell = ""
            if n == 1:
                cell = f"<td class=\"{classes[row][n]}\"><span class=\"week_num\">{week_nums[row]}</span><span>{line[n]}</span></td>"
            else:
                cell = f"<td class=\"{classes[row][n]}\"><span>{line[n]}</span></td>"
            rowCells.append(cell)

        print("".join(rowCells), file=cal)

        if rowSpanZZ:
            print(f"<td rowspan=\"{rowSpanZZ}\" class=\"{classes[row][-1]}\"><span class=\'right\'>{line[-1]}</span></td>", file=cal)
        print("</tr>", file=cal)
        row += 1

    print("</table></body></html>", file=cal)
