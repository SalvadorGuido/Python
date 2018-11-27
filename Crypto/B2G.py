import xlrd
import xlwt

def ganancia(inv, comprar,vender):
    return inv/comprar[2]*comprar[3]/vender[2]*vender[3]

def resultados(inv, gan):
    print('Inversión Inicial: {}'.format(inv))
    print('Resultado Final: {}'.format(gan))
    print('Dolares: {:.2f}'.format(gan-inv))
    print('Ganancia: {:.2f}%'.format(((gan/inv)-1)*100))

#initiallazing

wb = xlrd.open_workbook("B2G.xlsx")
Bittrex = wb.sheet_by_name("A")
Golix = wb.sheet_by_name("B")

bRows = Bittrex.nrows
bCol = Bittrex.ncols

gRows = Golix.nrows
gCol = Golix.ncols

#Bittrex data

bDash = ("DASH", Bittrex.cell(1, 0).value)
bLtc = ("LTC", Bittrex.cell(1, 1).value)
bBcc = ("BCC", Bittrex.cell(1, 2).value)
bBtc = ("BTC", Bittrex.cell(1, 3).value)
bBtg = ("BTG,",Bittrex.cell(1, 4).value)
Bit = [bDash,bLtc,bBcc,bBtc, bBtg]


#Golix Data

gDash = ("DASH",Golix.cell(1, 0).value,Golix.cell(2, 0).value)
gLtc = ("LTC", Golix.cell(1, 1).value,Golix.cell(2, 1).value)
gBcc = ("BCC", Golix.cell(1, 2).value,Golix.cell(2, 2).value)
gBtc = ("BTC", Golix.cell(1, 3).value,Golix.cell(2, 3).value)
gBtg = ("BTG", Golix.cell(1, 4).value,Golix.cell(2, 4).value)

Gol = [gDash,gLtc,gBcc,gBtc, gBtg]

#Valores
print("Valor de DASH en Bittrex: {}".format(bDash))
print("Valor de LTC en Bittrex: {}".format(bLtc))
print("Valor de BCC en Bittrex: {}".format(bBcc))
print("Valor de BTC en Bittrex: {}".format(bBtc))
print('='*50)
print("Valor de DASH en Golix: {}".format(gDash))
print("Valor de LTC en Golix: {}".format(gLtc))
print("Valor de BCC en Golix: {}".format(gBcc))
print("Valor de BTC en Golix: {}".format(gBtc))
print('='*50)
print(Bit)
print('='*50)
print(Gol)
print('='*50)

biggest_sell = ("Nada", 0)
smallest_buy = ("Nada", 5)


#Calculate Biggest Sell
for i in range(len(Gol)):
    for j in range(len(Bit)):
        if Gol[i][0] == Bit[j][0]:
            for k in range(1,3):
                if Gol[i][k] / Bit[j][1] > biggest_sell[1]:
                    biggest_sell = (Bit[j][0], (Gol[i][k] / Bit[j][1]), Bit[j][1],Gol[i][k])


#Calculate Smallest Buy
for i in range(len(Gol)):
    for j in range(len(Bit)):
        if Gol[i][0] == Bit[j][0]:
            for k in range(1,3):
                if Gol[i][k] / Bit[j][1] < smallest_buy[1]:
                    smallest_buy = (Bit[j][0], Gol[i][k] / Bit[j][1],Gol[i][k], Bit[j][1])

print('%'*50)
print(biggest_sell)
print(smallest_buy)

amount = 100
a = ganancia(amount,biggest_sell,smallest_buy)

print('%'*50)
resultados(amount,a)

wbOut = xlwt.Workbook(encoding="utf-8")
wsOut = wbOut.add_sheet("Sheet 1")

