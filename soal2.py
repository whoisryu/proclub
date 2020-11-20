arrWin = []

def whoWin(a, b):
    global arrWin

    if a < 0 or b < 0:
        arrWin.append("done")
    elif a > b:
        arrWin.append("1")
    elif a < b:
        arrWin.append("2")
    elif a == b:
        arrWin.append("-")




print("Klub A: ", end=" ")
klubA = input()

print("Klub B: ", end=" ")
klubB = input()

a = 0
b = 0

i = 1
while a >= 0 and b >= 0:

    print("Pertandingan ", i,": ", end=" ")
    a, b = input().split()

    a = int(a)
    b = int(b)

    whoWin(a, b)

    i = i + 1 


tanding = 1
for i in arrWin:
    if i == "1":
        print("Hasil " + str(tanding) + ": " + klubA)
    elif i == "2":
        print("Hasil " + str(tanding) + ": " + klubB)
    elif i == "-":
        print("Hasil " + str(tanding) + ": Draw")
    else:
        print("Pertandingan selesai")
    tanding = tanding + 1              