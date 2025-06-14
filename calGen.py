# This is a sample Python script.
import reportlab
from macholib.mach_o import nlist
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import calendar
from datetime import date, timedelta
import sys


days = 90

now = date.today()

def printLines():
    line  = []#'-','-','-','-','-','-','-']

    for n in range(0, now.weekday()):
        line.append("-")
    for n in range(now.weekday(), 7):
        if n == now.weekday():
            line.append("["+str(n+1)+"]")
        else:
            line.append(str(n+1))

    print(line)




#document = SimpleDocTemplate("table.pdf", pagesize=A4)
#items = []

data =[]
daysFR = ["Lundi", "Mardi", "Mercredi", "Jeudi","Vendredi", "Samedi", "Dimanche"]
daysID = ["Senin ", "Selasa", "Rabu  ", "Kamis ","Jumat ", "Sabtu ", "Minggu"]
sepID = ["------", "------","------","------","------","------","------"]
sepID = ["______","______","______","______","______","______","______"]
sepID = ["======","======","======","======","======","======","======"]
print(" | ".join(daysFR))

from datetime import date
date.today()
start = date.today() - timedelta(days= date.today().weekday())
print(start)
print("|  " +"  |  ".join(daysID)+"  |")
print("|==" +"==|==".join(sepID)+"==|")
#data.append(days)
line  = []
today = start
yesterday = start
for n in range(0, 13*7):
    today = start + timedelta(days=n)
    day = today.day
    if day < 10:
        day = "0"+str(day)
    else:
        day = str(day)
    if today.month == yesterday.month:
        line.append("         "+day+"  ")
    else:
        line.append("       * "+day+"  ")
    if len(line) == 7:

        print("|"+"|".join(line)+"|")
        line = []#print(start + timedelta(days=n))
    yesterday = today
sys.exit(0)

rows = 13

for i in range(1,rows):
    n = [0,1,2,3,4,5,6]

    row = [i * 7 + x for x in n]
    data.append(row)

t=Table(data,len(days)*[25*mm], rows*[25*mm])
t.setStyle(
    TableStyle([
        ('ALIGN',(-1,-1),(-2,-2),'RIGHT'),
        ('VALIGN',(-1,-1),(-1,-1),'RIGHT'),
        ('ALIGN',(-1,-1),(-1,-1),'RIGHT'),
        ('VALIGN',(-1,-1),(-1,-1),'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),]
    ))
items.append(t)
document.build(items)
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

