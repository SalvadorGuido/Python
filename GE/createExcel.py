import xlwt

x=1
y=2
z=3

list1=[2.34,4.346,4.234]

wbOut = xlwt.Workbook(encoding="utf-8")

wsOut = wbOut.add_sheet("Sheet 1")

wsOut.write(0, 0, "Display")
wsOut.write(1, 0, "Dominance")
wsOut.write(2, 0, "Test")

wsOut.write(0, 1, x)
wsOut.write(1, 1, y)
wsOut.write(2, 1, z)

wsOut.write(4, 0, "Stimulus Time")
wsOut.write(4, 1, "Reaction Time")

i=4

for n in list1:
    i = i+1
    wsOut.write(i, 0, n)

wbOut.save("trial.xls")