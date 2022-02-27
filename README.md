# Tugas Kecil 2 IF2211 Strategi Algoritma
> Implementasi Convex Hull untuk Visualisasi Tes Linear Separability Dataset 

## Penjelasan Program
Himpunan titik pada sebuah bidang dua dimensi disebut _Convex_ apabila untuk setiap dua titik bebas pada bidang tersebut apabila ditarik garis maka letak garis tersebut akan berada dalam bidang itu pula. _Convex Hull_ dari sebuah himpunan titik adalah himpunan terkecil yang memuat semua titik pada himpunan tersebut, namun tetap bersifat _Convex_.

Program ini merupakan sebuah library sederhana untuk menentukan _Convex Hull_ dari sebuah dataset yang tersedia dari scikit-learn (sklearn) yakni **Iris, Wine, dan Breast Cancer**. Program ini menggunakan algoritma secara *Divide and Conquer*. Progam ini bekerja dengan membagi himpunan menjadi dua ruangan dengan cara menarik garis dari koordinat terkiri pada dataset tersebut ke koordinat terkanan dari dataset tersebut. Kemudian, program akan melakukan *divide* (membagi menjadi dua ruangan) lagi dengan cara mencari titik terjauh dari garis tersebut untuk tiap ruangan berulang kali hingga tiap ruangan ter*conquer* atau dengan kata lain tidak bisa dibagi lagi. Proses Divide and Conquer ini menggunakan pendekatan secara rekursif.

Hasil akhir dari program ini adalah gambar plot koordinat untuk dataset tersebut, dimana untuk tiap koordinat yang termasuk titik *Convex Hull* akan ditunjukkan dengan cara ditarik garis sesuai dengan warna tiap target. Gambar plot tersebut akan ditunjukkan saat program berjalan. Program juga menyediakan fitur untuk menyimpan graf tersebut kedalam folder test jika diinginkan. Setelah program selesai menampilkan dan save gambarnya, program akan meminta input apakah anda ingin mencari *Convex Hull* untuk dataset / atribut lain. Apabila anda memilih selesai, maka program akan berhenti.

Program dibungkus dalam 2 file utama, yakni main.py dan myConvexHull.py
1. main.py : Merupakan file yang dijalankan untuk mendapatkan plot *Convex Hull*
2. myConvexHull.py : Merupakan file library untuk algoritma *Convex Hull* yang telah saya buat

## Requirements and Setup
- Python 3 diperlukan dalam program ini. Anda bisa mendownloadnya pada link <a href="http://www.python.org/downloads/">berikut</a>, atau agar mempermudah anda dapat menonton proses instalasinya dari link <a href="https://www.youtube.com/watch?v=Kn1HF3oD19c">berikut</a>.

- pip harus terinstall. Anda bisa melakukan instalasi pada link <a href="https://pip.pypa.io/en/stable/installation/">berikut</a>. Pastikan juga pip harus ada pada PATH dengan cara <a href="https://www.youtube.com/watch?v=UTUlp6L2zkw">berikut</a>.

- Terdapat beberapa library yang harus terinstall untuk menjalankan program ini, yakni pandas, numpy, matplotlib, dan sklearn. Anda bisa menggunakan pip yang sudah diinstall sebelumnya. Buka powershell atau terminal pada komputer anda, kemudian masukkan sintaks berikut: 
```
pip install pandas
pip install numpy
pip install matplotlib
pip install sklearn
```

- Clone repository ini ke dalam komputer anda dengan cara memasukkan sintaks berikut pada powershell atau terminal:
```
git clone https://github.com/saulsayerz/Tucil2_13520094
```

## Cara Menggunakan Program
1. Buka root direktori dari repository yang telah anda clone

2. Jalankan file main.py yang ada dalam folder src. Terdapat dua cara untuk menjalankan file tersebut. Yang pertama dengan secara manual membuka file main.py menggunakan code editor seperti VScode lalu run programnya. Yang kedua dengan cara membuka terminal pada root directory kemudian mengetikkan sintaks berikut :
```
python src/main.py
```
3. Program akan berjalan dan anda diminta untuk memilih dataset yang tersedia. Anda cukup memilih dengan mengetikkan angkanya. Apabila pilihan angka tidak tepat, maka akan diulang. Contoh dari output program:
```
SELAMAT DATANG DI PROGRAM CONVEXHULL SAUL SAYERS :D
--------------------------------------------------------
Silahkan pilih dataset yang ingin digunakan
Note: pemilihan atribut cukup dengan mengetikkan angkanya

Daftar dataset:
1. Dataset Iris
2. Dataset Wine
3. Dataset Breast Cancer

Silahkan pilih dataset: 1
```

4. Program akan mencetak list atribut dari dataset yang telah anda pilih. Anda diminta untuk memilih atribut pertama sebagai data sumbu X, kemudian memilih atribut kedua sebagai sumbu y. Note bahwa kita tidak bisa memilih atribut yang sama sebagai sumbu X dan sumbu Y. Contoh dari output program:
```
Silahkan pilih dataset: 1
Daftar atribut:
1. sepal length (cm)
2. sepal width (cm)
3. petal length (cm)
4. petal width (cm)

Silahkan pilih atribut yang ingin dipilih sebagai sumbu X: 1

Silahkan pilih atribut yang ingin dipilih sebagai sumbu Y: 1
Atribut sumbu y tidak boleh sama, silahkan input ulang: 2
```
5. Program kemudian akan menampilkan plot *Convex Hull* dari dataset dan atribut yang anda pilih. Silahkan close pop up plot apabila ingin melanjutkan program
6. Program akan meminta input apakah anda ingin menyimpan plot tersebut dalam bentuk gambar png. Jika iya, maka program juga akan meminta input filename (tanpa perlu mengetik .png). Contoh output program:
```
Apakah anda ingin save graf ConvexHull tersebut? 
Ketik y untuk iya atau n untuk tidak (defaultnya n): y
Silahkan input namafile (tanpa .png): iris1
```
7. Program kemudian akan meminta input apakah anda ingin memeriksa *Convex Hull* untuk dataset atau atribut lain atau tidak. Apabila tidak, maka anda dapat memasukkan input n kemudian program akan selesai. Apabila ingin lanjut memeriksa, anda dapat memasukkan input y kemudian program akan kembali ke langkah 3.

## Contributors :
> Saul Sayers (13520094), K01 - Informatika ITB 2020. 

More detailed contact: 
- Line : saulsayerz
- Instagram : <a href="https://www.instagram.com/saulsayers/?hl=en">saulsayers</a> 
- Linkedin : <a href="https://www.linkedin.com/in/saulsayers/?originalSubdomain=id">saulsayers</a>
- github : <a href="https://github.com/saulsayerz">saulsayerz</a>
- email : saulsayers@gmail.com
