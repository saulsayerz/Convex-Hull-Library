# NAMA  : SAUL SAYERS
# NIM   : 13520094
# KELAS : K-01 STRATEGI ALGORITMA

# MERUPAKAN FILE MAIN MYCONVEXHULL UNTUK TUCIL 2 STRATEGI ALGORITMA

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import myConvexHull as mch

print("SELAMAT DATANG DI PROGRAM CONVEXHULL SAUL SAYERS :D")
print("--------------------------------------------------------")

kelar = False

while (not kelar) :
    # Proses pemilihan dataset
    print("Silahkan pilih dataset yang ingin digunakan")
    print("Note: pemilihan atribut cukup dengan mengetikkan angkanya")
    print()

    print("Daftar dataset: ")
    print("1. Dataset Iris")
    print("2. Dataset Wine")
    print("3. Dataset Breast Cancer")
    print()

    pilihdataset = int(input("Silahkan pilih dataset: "))
    while (pilihdataset < 1) or (pilihdataset > 3):
        pilihdataset = int(input("input tidak valid, silahkan input ulang dataset: "))

    if pilihdataset == 1 :
        data = datasets.load_iris()
    elif pilihdataset == 2:
        data = datasets.load_wine()
    elif pilihdataset == 3:
        data = datasets.load_breast_cancer()

    # Pembuatan dataframe
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    df.head()

    # Proses pemilihan atribut
    print("Daftar atribut: ")
    for i in range(len(data.feature_names)):
        print(str(i + 1) + ".", data.feature_names[i])
    print()

    atribut1 = int(input("Silahkan pilih atribut yang ingin dipilih sebagai sumbu X: "))
    while (atribut1 < 1) or (atribut1 > len(data.feature_names)):
        atribut1 = int(input("input tidak valid, silahkan input ulang atribut sumbu X: "))
    print()
        
    atribut2 = int(input("Silahkan pilih atribut yang ingin dipilih sebagai sumbu Y: "))
    while (atribut2 < 1) or (atribut2 > len(data.feature_names)) or (atribut1 == atribut2):
        if (atribut1 == atribut2):
            atribut2 = int(input("Atribut sumbu y tidak boleh sama, silahkan input ulang: "))
        else:
            atribut2 = int(input("input tidak valid, silahkan input ulang atribut sumbu Y: "))

    # Visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title(data.feature_names[atribut1 -1] + " vs " + data.feature_names[atribut2 -1])

    plt.xlabel(data.feature_names[atribut1 -1])
    plt.ylabel(data.feature_names[atribut2 -1])

    for i in range(len(data.target_names)) : 
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[atribut1 -1,atribut2 -1]].values
        hull = mch.myConvexHull(bucket) 
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        kumpulansisi = mch.splitXY(hull)
        plt.plot(kumpulansisi[0], kumpulansisi[1], colors[i])
        plt.plot(kumpulansisi[2],kumpulansisi[3], colors[i])
    print()
    print("Berikut adalah grafik Convex Hull nya: ")
    print()
    plt.show()
    
    #Opsi save dataset
    print("Apakah anda ingin save graf ConvexHull tersebut? ")
    inginsave = input("Ketik y untuk iya atau n untuk tidak (defaultnya n): ")
    if inginsave == "y" :
        namafile = input("Silahkan input namafile (tanpa .png): ")
        plt.title(data.feature_names[atribut1 -1] + " vs " + data.feature_names[atribut2 -1])
        plt.xlabel(data.feature_names[atribut1 -1])
        plt.ylabel(data.feature_names[atribut2 -1])
        for i in range(len(data.target_names)) : 
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[atribut1 -1,atribut2 -1]].values
            hull = mch.myConvexHull(bucket) 
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            kumpulansisi = mch.splitXY(hull)
            plt.plot(kumpulansisi[0], kumpulansisi[1], colors[i])
            plt.plot(kumpulansisi[2],kumpulansisi[3], colors[i])
        plt.savefig("./test/"+namafile+".png")
        plt.clf()
    
    # Opsi mengakhiri program atau tidak
    print()
    print("Apakah anda ingin solve Convex Hull dataset lain? ")
    selesai = input("Ketik y untuk iya atau n untuk tidak (defaultnya n): ")
    if (selesai != "y") :
        kelar = True
    
print("Terimakasih telah menggunakan program saya :D")
