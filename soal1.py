arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    arrBerat.sort()

    bMin = arrBerat[0]
    bMax = arrBerat[len(arrBerat) - 1]
    return bMin,bMax


def rerata(arrBerat):
    total = 0

    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in arrBerat:
        total += i

    rerata = total / len(arrBerat)
    # Return Hasil Rerata
    return total/len(arrBerat)

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    data = input()
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(int(data))

# Panggil procedur hitungMinMax(arrBerat)
bMin, bMax = hitungMinMax(arrBerat)
rerata = rerata(arrBerat)
# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat balita minimum: ",bMin,'Kg')
print("Berat balita maximum: ",bMax, 'Kg')
print("Rta-rata berat balita: ",rerata, 'Kg')