# NAMA  : SAUL SAYERS
# NIM   : 13520094
# KELAS : K-01 STRATEGI ALGORITMA

# MERUPAKAN FILE LIBRARY MYCONVEXHULL UNTUK TUCIL 2 STRATEGI ALGORITMA

import numpy as np
from numpy.linalg import norm

# Fungsi berikut untuk menentukan lokasi dari sebuah titik p3 dengan cara menghitung determinan dari matriks yang tersusun.
# Apabila positif maka di sebelah kanan garis, negatif di sebelah kiri garis, dan 0 tepat pada garis sehingga diabaikan
def periksaLokasi(p1,p2,p3):
    x1 = p1[0]
    x2 = p2[0]
    x3 = p3[0]
    y1 = p1[1]
    y2 = p2[1]
    y3 = p3[1]
    hasil = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3 # Untuk menghitung determinannya secara manual
    return hasil

# Fungsi berikut untuk menghitung jarak sebuah titik p3 terhadap garis yang terbentuk dari p1 dan p2
def hitungJarak(p1, p2, p3):
    a = np.array(p1)
    b = np.array(p2) # Konversi dalam bentuk numpy
    c = np.array(p3)
    jarak = np.abs(np.cross(b-a, a-c)) / norm(b-a)
    
    return jarak

# Fungsi berikut untuk menghitung sudut yang diapit, yakni sudut P3-P1-P2
def hitungSudut(p1,p2,p3):
    if ((p1[0] == p3[0] and p1[1] == p3[1]) or (p2[0] == p3[0] and p2[1] == p3[1]) ) : # KASUS TITIK YANG DIPERIKSA ADALAH TITIK ITU SENDIRI
        return 0
    else:
        a = np.array(p2)
        b = np.array(p3) # Konversi dalam bentuk numpy
        c = np.array(p1)
        
        ca = a - c # Mendapatkan vektornya
        cb = b - c
        
        hasilkalidot = np.dot(ca,cb) # Melakukan perkalian dot
        panjangCA = norm(ca) 
        panjangCB = norm(cb) # Mendapatkan panjang vectornya
        
        sudutDalamCos = hasilkalidot/(panjangCA*panjangCB) # Perkalian dot untuk mendapatkan sudutnya
        sudutDalamRadian = np.arccos(sudutDalamCos) # Mengkonversi dari cos menjadi radian
        return sudutDalamRadian

# Fungsi berikut untuk menentukan sebuah titik terjauh dari dalam variabel bucket terhadap titik p1 dan p2
# Titik terjauh dihitung menggunakan fungsi hitungSudut.
def cariTitikTerjauh(bucket,p1,p2) :
    if len(bucket) == 1 :
        return bucket[0] # Apabila bucket hanya berisi satu titik, maka itu adalah titik terjauh
    else:
        sudutterjauh = hitungSudut(p1,p2,bucket[0])
        pterjauh = bucket[0]
        for i in range (1,len(bucket)): # Pencarian sudut terbesar secara traversal dari awal hingga akhir
            temp = hitungSudut(p1,p2,bucket[i])
            if (temp > sudutterjauh) :
                sudutterjauh = temp
                pterjauh = bucket[i]
        return pterjauh


# Fungsi berikut untuk melakukan sorting dari koordinat x secara menaik, jika sama maka dari koordinat y
def sortKoordinat(arr):
    for i in range (len(arr)-1) :
        for j in range (len(arr)-i-1):
            if (arr[j][0] > arr[j+1][0] or (arr[j][0] == arr[j+1][0] and arr[j][1] > arr[j+1][1])):
                tempx = arr[j][0]
                arr[j][0] = arr[j+1][0]
                arr[j+1][0] = tempx
                
                tempy = arr[j][1]
                arr[j][1] = arr[j+1][1]
                arr[j+1][1] = tempy

# Fungsi berikut untuk menambahkan sebuah koordinat ke dalam array hasilakhir HullVertices
# Perlu diperhatikan bahwa hullVertices memiliki elemen unik sehingga dihandle agar menambahkan apabila belum ada saja        
def tambahSolusi(bucket,p):
    sudahada = False
    for i in range (len(bucket)):
        if (bucket[i][0] == p[0] and bucket[i][1] == p[1]): # Mengecek apakah koordinat tersebut sudah ada apa belum
            sudahada = True 
    if (not sudahada) :
        bucket.append(p) # Jika belum, langsung tambahkan saja
                
# KEDUA FUNGSI DI BAWAH UNTUK MELAKUKAN PARTISI SEBELAH KIRI GARIS DAN SEBELAH KANAN GARIS               
def partisiKiri(bucket,pawal,pakhir):
    arrHasil = []
    for i in range (len(bucket)):
        determinan = periksaLokasi(pawal,pakhir,bucket[i])
        if (determinan) > 10**-6 : # Untuk ngehandle rounding error yang kurang akurat
            tambahSolusi(arrHasil, bucket[i])
    return arrHasil

def partisiKanan(bucket,pawal,pakhir):
    arrHasil = []
    for i in range (len(bucket)):
        determinan = periksaLokasi(pawal,pakhir,bucket[i])
        if (determinan) < -1*(10**-6): # Untuk ngehandle rounding error yang kurang akurat
            tambahSolusi(arrHasil, bucket[i])
    return arrHasil

# Fungsi ini untuk menerapkan tahap rekursif dari algoritma convexHull. Fungsi akan melakukan divide and conquer pada tahap ini
# Basis dari fungsi ini adalah:
# 1. Titik pada sebuah ruangan Kosong, maka do nothing
# 2. Hanya ada satu titik pada ruangan sehingga titik tersebut juga termasuk convexHull sehingga tambahkan pada arrayhasil
# Tahap rekursi dari fungsi ini adalah :
# Tiap ruangan akan dicari terlebih dahulu titik terjauh yang merupakan titik convexhull juga sehingga masukkan ke array
# kemudian mempartisi nya menjadi dua ruangan dan conquer masing masing hingga mencapai basis
def convexHullRecursive(bucket,pawal,pakhir,arrHasil):
    # if len = 0 then do nothing, basis pertama
    if len(bucket) == 1:
        tambahSolusi(arrHasil, bucket[0]) # Panjang array = 1, basis kedua
    elif len(bucket) > 1 :
        terjauh = cariTitikTerjauh(bucket,pawal,pakhir) # Untuk mencari titik terjauh
        tambahSolusi(arrHasil, terjauh) # Untuk menambahkan titik terjauh tadi ke array hasil akhir
        arrKiri = partisiKiri(bucket,pawal,terjauh) 
        arrKanan = partisiKiri(bucket,terjauh,pakhir) # Untuk mempartisikan array kiri dan kanan
        convexHullRecursive(arrKiri,pawal,terjauh,arrHasil) 
        convexHullRecursive(arrKanan,terjauh,pakhir,arrHasil) # Untuk melanjutkan array kiri dan kanan ke tahap rekursi

# Fungsi berikut merupakan tahap pertama dari algoritma convexHull
# Fungsi ini akan melakukan sorting terlebih dahulu terhadap absis, kemudian terhadap ordinat
# Tarik garis dari koordinat paling kiri dan paling kanan untuk membagi menjadi 2 ruangan. Kedua titik tersebut termasuk Hull vertices
def myConvexHull(bucket) :
    sortKoordinat(bucket) # Untuk melakukan sorting
    pawal = bucket[0]
    pakhir = bucket[len(bucket)-1] # Mencatat koordnat paling kiri dan kanan
    arrKiri = partisiKiri(bucket,pawal,pakhir)
    arrKanan = partisiKanan(bucket,pawal,pakhir) # Melakukan partisi ruangan kiri dan kanan
    hullVertices = [pawal,pakhir] # Memasukkan koordinat terkiri dan terkanan tadi termasuk Hull Vertices
    convexHullRecursive(arrKiri,pawal,pakhir,hullVertices)
    convexHullRecursive(arrKanan,pakhir,pawal,hullVertices) # Untuk memasukkan tiap ruangan ke tahap rekursif untuk diconquer
    sortKoordinat(hullVertices) # Untuk melakukan sorting agar hasil akhir tetap terurut agar mempermudah plotting
    return hullVertices

# Fungsi tersebut untuk mensplit koordinat dari Hull Vertices menjadi array absis dan array ordinat
# Fungsi ini ditujukan untuk mempermudah plotting dari hull vertices
def splitXY(bucket):
    arrKiri = partisiKiri(bucket,bucket[0],bucket[-1])
    arrKanan = partisiKanan(bucket,bucket[0],bucket[-1]) # Untuk melakukan partisi tiap array
    sumbuxkiri = [bucket[0][0]]
    sumbuykiri = [bucket[0][1]] # Untuk mengisi elemen pertama dari hull vertices
    sumbuxkanan = [bucket[0][0]]
    sumbuykanan = [bucket[0][1]]
    for koordinat in arrKiri :
        sumbuxkiri.append(koordinat[0])
        sumbuykiri.append(koordinat[1]) # Untuk menambahkan tiap absis/ordinat ke array
    for koordinat in arrKanan :
        sumbuxkanan.append(koordinat[0])
        sumbuykanan.append(koordinat[1])
    sumbuxkiri.append(bucket[-1][0])
    sumbuxkanan.append(bucket[-1][0]) # Untuk mengisi elemen terakhir dari hull vertices
    sumbuykiri.append(bucket[-1][1])
    sumbuykanan.append(bucket[-1][1])
    hasilakhir = [sumbuxkiri,sumbuykiri,sumbuxkanan,sumbuykanan] # Untuk membungkus semua array menjadi satu array
    return hasilakhir



    


