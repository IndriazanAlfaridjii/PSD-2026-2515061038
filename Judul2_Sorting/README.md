a.	Judul Program : 
Mengurutkan Buku Berdasarkan Tahun  Menggunakan Insertion Sort

b.	Deskripsi Singkat : 
Program tersebut merupakan implementasi algoritma Insertion Sort dalam Python untuk mengurutkan data buku berdasarkan tahun terbit. Pengguna diminta memasukkan jumlah buku, kemudian menginput judul dan tahun terbit setiap buku. Data disimpan dalam bentuk list berisi dictionary.
Selanjutnya, program mengurutkan data secara ascending (dari tahun terlama ke terbaru) dengan cara membandingkan dan menyisipkan setiap elemen ke posisi yang tepat. Setelah proses selesai, program menampilkan data sebelum dan sesudah diurutkan.

c.	Source Code :

<img width="882" height="934" alt="Screenshot 2026-05-05 171546" src="https://github.com/user-attachments/assets/9b3dc784-93c5-4fe8-ae5a-8de18c35dc53" />


Baris 1: def insertion_sort(arr, n):
Mendefinisikan fungsi insertion sort dengan parameter array arr dan jumlah elemen n.

Baris 2: for i in range(1, n):
Perulangan dimulai dari indeks ke-1 karena elemen pertama dianggap sudah terurut.

Baris 3: temp = arr[i]
Menyimpan elemen yang sedang diproses ke variabel sementara temp.

Baris 4: j = i - 1
Menentukan indeks sebelumnya untuk dibandingkan.

Baris 5: (baris kosong)
Digunakan untuk kerapihan kode.

Baris 6: # bandingkan berdasarkan tahun
Komentar untuk menjelaskan bahwa pengurutan berdasarkan atribut tahun.
Baris 7: while j >= 0 and arr[j]['tahun'] > temp['tahun']:
Perulangan selama indeks valid dan tahun lebih besar dari temp (ascending).
Baris 8: arr[j + 1] = arr[j]
Menggeser elemen ke kanan.

Baris 9: j -= 1
Mengurangi indeks untuk lanjut membandingkan.

Baris 10: (indentasi lanjutan while)
Bagian dari blok while.

Baris 11: arr[j + 1] = temp
Menyisipkan elemen temp ke posisi yang benar.

Baris 12: (baris kosong)
Pemisah antar fungsi.

Baris 13: def main():
Mendefinisikan fungsi utama.

Baris 14: try:
Memulai blok penanganan error.

Baris 15: n = int(input("Masukkan jumlah buku: "))
Input jumlah buku dari user.

Baris 16: except ValueError:
Menangkap error jika input bukan angka.

Baris 17: print("Input tidak valid!")
Menampilkan pesan kesalahan.

Baris 18: return
Menghentikan program jika terjadi error.

Baris 19: (baris kosong)
Pemisah kode.

Baris 20: arr = []
Membuat list kosong untuk menyimpan data buku.

Baris 21: print("Masukkan data buku (judul dan tahun):")
Menampilkan instruksi input.

Baris 22: (baris kosong)

Baris 23: for i in range(n):
Perulangan untuk input data sebanyak n.

Baris 24: judul = input(f"Judul buku ke-{i+1}: ")
Input judul buku.

Baris 25: (baris kosong)

Baris 26: while True:
Loop sampai input valid.

Baris 27: try:
Mencoba input tahun.

Baris 28: tahun = int(input(f"Tahun terbit buku ke-{i+1}: "))
Input tahun dan konversi ke integer.

Baris 29: break
Keluar dari loop jika input valid.

Baris 30: except ValueError:
Menangkap error input.

Baris 31: print("Input tahun tidak valid, masukkan angka!")
Menampilkan pesan error.

Baris 32: (baris kosong)

Baris 33: arr.append({"judul": judul, "tahun": tahun})
Menyimpan data buku ke dalam list dalam bentuk dictionary.

Baris 34: (baris kosong)

Baris 35: print("\nData sebelum diurutkan:")
Menampilkan teks sebelum sorting.

Baris 36: for buku in arr:
Loop untuk menampilkan data.

Baris 37: print(buku["judul"], "-", buku["tahun"])
Menampilkan isi data buku.

Baris 38: (baris kosong)

Baris 39: insertion_sort(arr, n)
Memanggil fungsi sorting.

Baris 40: (baris kosong)

Baris 41: print("\nData setelah diurutkan (tahun terlama -> terbaru):")
Menampilkan teks setelah sorting.

Baris 42: for buku in arr:
Loop untuk menampilkan hasil.

Baris 43: print(buku["judul"], "-", buku["tahun"])
Menampilkan data yang sudah terurut.

Baris 44: (baris kosong)

Baris 45: (baris kosong tambahan sebelum eksekusi)

Baris 46: if __name__ == "__main__":
Mengecek apakah program dijalankan langsung.

Baris 47: main()
Menjalankan fungsi utama.

Baris 48: (akhir program)

D. Output Program :

<img width="486" height="444" alt="Screenshot 2026-05-05 173802" src="https://github.com/user-attachments/assets/f4c1246a-f2d3-4178-af7b-e9716ec5fc3a" />


Berdasarkan hasil eksekusi program, pengguna memasukkan lima data buku yang masing-masing terdiri dari judul dan tahun terbit. Data yang dimasukkan yaitu buku A dengan tahun 2010, buku B tahun 2012, buku C tahun 2015, buku D tahun 2006, dan buku E tahun 2005. Setelah seluruh data berhasil diinput, program menampilkan data awal (sebelum pengurutan) sesuai dengan urutan input pengguna. Hal ini menunjukkan bahwa data masih dalam kondisi belum terurut dan mencerminkan urutan asli saat dimasukkan.

Selanjutnya, program menjalankan algoritma Insertion Sort untuk melakukan proses pengurutan. Algoritma ini bekerja dengan cara mengambil satu elemen pada setiap iterasi, kemudian membandingkannya dengan elemen-elemen sebelumnya yang sudah dianggap terurut. Jika ditemukan elemen sebelumnya yang memiliki nilai lebih besar, maka elemen tersebut akan digeser ke kanan untuk memberikan ruang. Proses ini terus dilakukan hingga ditemukan posisi yang tepat untuk menyisipkan elemen tersebut. Dengan mekanisme ini, secara bertahap terbentuk bagian array yang terurut hingga seluruh data tersusun dengan benar.

Pada percobaan ini, kriteria pengurutan yang digunakan adalah berdasarkan tahun terbit secara ascending, yaitu dari tahun paling lama ke tahun paling baru. Selama proses berlangsung, data dengan nilai tahun yang lebih kecil akan dipindahkan ke posisi yang lebih depan. Misalnya, buku D (2006) dan buku E (2005) yang awalnya berada di bagian akhir array, secara bertahap dipindahkan ke posisi awal karena memiliki nilai tahun yang lebih kecil dibandingkan data lainnya. Proses ini menunjukkan bagaimana algoritma Insertion Sort bekerja secara iteratif dan sistematis dalam menyusun data.

Hasil akhir dari program menunjukkan bahwa data telah berhasil diurutkan dengan benar, yaitu dimulai dari buku dengan tahun terbit paling lama hingga yang paling baru, yaitu E (2005), D (2006), A (2010), B (2012), dan C (2015). Urutan ini sesuai dengan kriteria yang telah ditentukan sebelumnya, sehingga dapat disimpulkan bahwa algoritma berjalan dengan baik tanpa kesalahan.

Dari segi analisis, algoritma Insertion Sort memiliki kompleksitas waktu rata-rata dan terburuk sebesar O(n²), terutama ketika data dalam kondisi acak atau terbalik. Namun, pada kondisi terbaik (best case), yaitu ketika data sudah hampir terurut, kompleksitas waktunya dapat menjadi O(n). Hal ini menunjukkan bahwa Insertion Sort cukup efisien untuk digunakan pada data dengan jumlah kecil atau data yang sudah hampir terurut. Selain itu, algoritma ini memiliki keunggulan dalam hal kesederhanaan implementasi serta penggunaan memori yang minimal karena tidak memerlukan struktur data tambahan (in-place).

Kesimpulan:

Berdasarkan percobaan yang telah dilakukan, dapat disimpulkan bahwa algoritma Insertion Sort mampu mengurutkan data buku berdasarkan tahun terbit secara ascending dengan baik dan sesuai harapan. Proses pengurutan dilakukan melalui mekanisme perbandingan, pergeseran, dan penyisipan elemen ke posisi yang tepat. Meskipun memiliki keterbatasan pada kompleksitas waktu untuk data berukuran besar, algoritma ini tetap efektif dan efisien untuk digunakan pada data skala kecil hingga menengah serta mudah dipahami dan diimplementasikan dalam berbagai kasus sederhana.

E. Link Youtube : 
https://youtu.be/hAnzqJJ32ik

