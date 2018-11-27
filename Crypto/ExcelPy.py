import xlrd
import xlwt

#initiallazing

wb = xlrd.open_workbook("STDPY.xlsx")
ws = wb.sheet_by_name("BOLTS")
wRows = ws.nrows
wCol = ws.ncols

wbOut = xlwt.Workbook(encoding="utf-8")
wsOut = wbOut.add_sheet("Sheet 1")


#Filling the lists
boltNA = list()
boltLen = list()
boltTH = list()
boltSL = list()
boltSD = list()
boltM = list()
boltCo = list()

for i in range(1, wRows):
    boltNA.append(ws.cell(i, 0).value)
    boltLen.append(ws.cell(i, 9).value)
    boltTH.append(ws.cell(i, 10).value)
    boltSL.append(ws.cell(i, 15).value)
    boltSD.append(ws.cell(i, 16).value)
    boltM.append(ws.cell(i, 17).value)
    boltCo.append(ws.cell(i, 22).value)

print("Numero de parte {}".format(boltNA))
print("Las longitudes por bolt son {}".format(boltLen))
print("Las longitudes de TH {}".format(boltTH))
print("Las longitudes de SL {}".format(boltSL))
print("Las longitudes de SD {}".format(boltSD))
print("Material del bolt {}".format(boltM))
print("Precio por bolt: {}".format(boltCo))

#Bolt tuples

boltsT = [() for i in range(1, wRows)]

for i in range(wRows-1):
    boltsT[i] = boltNA[i], boltLen[i], boltTH[i], boltSL[i], boltSD[i], boltM[i], boltCo[i]


j = 0
i = 0
for i in range(len(boltsT)):
    n = boltsT[i][0]
    si = boltsT[i][1]
    t = float(boltsT[i][2])
    sl = float(boltsT[i][3])
    sd = float(boltsT[i][4])
    m = boltsT[i][5]
    c = boltsT[i][6]

    for item in boltsT:
        n2 = str(item[0])
        si2 = item[1]
        t2 = item[2]
        sl2 = item[3]
        sd2 = item[4]
        m2 = item[5]
        c2 = item[6]
        # print(si)
        # print(si2)
        if si != 0 and n != n2:
            if (si -.05 <= si2 <= si+.05 and t-.05 <= t2 <= t+.05 and sl-.05 <= sl2 <= sl+.05 and sd <= sd2 <= sd and m == boltsT[j][5]):
                boltsT[i] = (boltsT[i] + (("Similar to: " + n2),))

for item in boltsT:
    print(item)

# for i in range(len(boltsT)):
#     if boltsT[i][7] is None:
#         boltsT[i][7] = ''
#     if boltsT[i][8] is None:
#         boltsT[i][8] = ''
#     if boltsT[i][9] is None:
#         boltsT[i][9] = ''
#     if boltsT[i][10] is None:
#         boltsT[i][10] = ''

#
# for i in range(len(boltsT)):
#     wsOut.write(i, 0, boltsT[i][0])
#     wsOut.write(i, 1, boltsT[i][1])
#     wsOut.write(i, 2, boltsT[i][2])
#     wsOut.write(i, 3, boltsT[i][3])
#     wsOut.write(i, 4, boltsT[i][4])
#     wsOut.write(i, 5, boltsT[i][5])
#     wsOut.write(i, 6, boltsT[i][6])


counter = 0
for item in boltsT:
    h = 0
    for huevos in item:
        # print(counter, h, huevos)
        wsOut.write(counter, h, huevos)
        h += 1
    counter += 1


wbOut.save("Recommendations.xls")
