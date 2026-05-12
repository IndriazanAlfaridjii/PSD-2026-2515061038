
A. Judul Program: 
Pencarian Jumlah Pembelian Skincare

B. Deskripsi Singkat: 
Program tersebut merupakan program pencarian data pembelian skincare menggunakan metode Sequential Search (pencarian berurutan). Program meminta pengguna memasukkan jumlah pelanggan serta jumlah item skincare yang dibeli setiap pelanggan, kemudian menyimpan data tersebut ke dalam list. Setelah itu, pengguna dapat mencari jumlah pembelian tertentu, dan program akan menghitung berapa kali jumlah pembelian tersebut muncul dalam data. Hasil pencarian kemudian ditampilkan beserta informasi apakah data ditemukan atau tidak.

C. Source Code:
<img width="534" height="837" alt="Screenshot 2026-05-12 211548" src="https://github.com/user-attachments/assets/b2805ef9-332e-443e-b626-0969bce93b4b" />

Penjelasan:

Baris 1 → Mendefinisikan fungsi `sequential_search()` yang digunakan untuk mencari data secara berurutan pada list.

Baris 2 → Membuat variabel `i` dengan nilai awal 0 sebagai indeks perulangan.

Baris 3 → Membuat variabel `counter` untuk menghitung jumlah data yang ditemukan.

Baris 4 → Membuat perulangan selama indeks `i` masih kurang dari jumlah data `n`.

Baris 5 → Mengecek apakah data pada indeks ke-`i` sama dengan nilai yang dicari (`target`).

Baris 6 → Jika data ditemukan, maka `counter` ditambah 1.

Baris 7 → Menambah nilai `i` agar perulangan berpindah ke data berikutnya.

Baris 8 → Mengembalikan jumlah data yang ditemukan.

Baris 10 → Mendefinisikan fungsi utama program yaitu `main()`.

Baris 11 → Menampilkan judul program pencarian pembelian skincare.

Baris 13 → Membuat list kosong bernama `data` untuk menyimpan data pembelian pelanggan.

Baris 15 → Membuat perulangan tak terbatas untuk validasi input jumlah pelanggan.

Baris 16 → Memulai blok `try` untuk menangani kemungkinan error input.

Baris 17 → Meminta pengguna memasukkan jumlah pelanggan dan mengubah input menjadi integer.

Baris 18 → Mengecek apakah jumlah pelanggan lebih dari 0.

Baris 19 → Menghentikan perulangan jika input valid.

Baris 20 → Kondisi jika jumlah pelanggan tidak valid.

Baris 21 → Menampilkan pesan bahwa jumlah pelanggan harus lebih dari 0.

Baris 22 → Menangani error jika input bukan angka.

Baris 23 → Menampilkan pesan kesalahan bahwa input harus berupa angka.

Baris 25 → Menampilkan instruksi untuk memasukkan jumlah item skincare yang dibeli pelanggan.

Baris 27 → Melakukan perulangan sebanyak jumlah pelanggan.

Baris 28 → Membuat perulangan validasi input pembelian.

Baris 29 → Memulai blok `try`.

Baris 30 → Meminta input jumlah pembelian pelanggan ke-`i+1`.

Baris 31 → Menambahkan data pembelian ke dalam list `data`.

Baris 32 → Menghentikan perulangan jika input valid.

Baris 33 → Menangani error jika input bukan angka.

Baris 34 → Menampilkan pesan bahwa input harus berupa angka.

Baris 36 → Menghitung jumlah data dalam list `data`.

Baris 38 → Menampilkan judul data pembelian skincare.

Baris 39 → Menampilkan seluruh isi data pembelian.

Baris 41 → Membuat perulangan validasi input pencarian.

Baris 42 → Memulai blok `try`.

Baris 43 → Meminta pengguna memasukkan jumlah item yang ingin dicari.

Baris 44 → Menghentikan perulangan jika input valid.

Baris 45 → Menangani error jika input bukan angka.

Baris 46 → Menampilkan pesan kesalahan input.

Baris 48 → Memanggil fungsi `sequential_search()` untuk mencari data dan menyimpan hasilnya ke variabel `counter`.

Baris 50 → Menampilkan judul hasil pencarian.

Baris 52 → Mengecek apakah data ditemukan.

Baris 53 → Menampilkan jumlah data yang ditemukan.

Baris 54 → Menampilkan informasi bahwa produk cukup populer.

Baris 55 → Kondisi jika data tidak ditemukan.

Baris 56 → Menampilkan pesan bahwa data tidak ditemukan.

Baris 57 → Menampilkan informasi tambahan bahwa belum ada pelanggan dengan jumlah pembelian tersebut.

Baris 59 → Mengecek apakah file dijalankan langsung.

Baris 60 → Memanggil fungsi `main()` untuk menjalankan program.

D.  Output Program:
<img width="586" height="397" alt="Screenshot 2026-05-12 214657" src="https://github.com/user-attachments/assets/b58ffcfa-0391-4034-b4b7-59ff5395329d" />

Penjelasan:
Program dimulai dengan meminta pengguna memasukkan jumlah pelanggan sebanyak 8 orang. Input tersebut menunjukkan bahwa program akan menerima data pembelian skincare dari 8 pelanggan yang berbeda. Setelah jumlah pelanggan dimasukkan, program meminta pengguna menginput jumlah item skincare yang dibeli oleh setiap pelanggan secara berurutan. Data yang dimasukkan yaitu pelanggan pertama membeli 7 item, pelanggan kedua membeli 3 item, pelanggan ketiga membeli 4 item, pelanggan keempat membeli 4 item, pelanggan kelima membeli 3 item, pelanggan keenam membeli 2 item, pelanggan ketujuh membeli 6 item, dan pelanggan kedelapan membeli 5 item. Seluruh data tersebut kemudian disimpan ke dalam sebuah list sehingga menghasilkan data [7, 3, 4, 4, 3, 2, 6, 5].

Setelah semua data pembelian berhasil disimpan, program menampilkan kembali daftar data pembelian skincare agar pengguna dapat melihat seluruh data yang telah diinput. Selanjutnya, program meminta pengguna memasukkan jumlah item yang ingin dicari. Pada contoh output tersebut, pengguna memasukkan angka 3. Program kemudian menjalankan metode Sequential Search atau pencarian berurutan, yaitu dengan memeriksa setiap elemen dalam list mulai dari data pertama hingga data terakhir untuk mencari nilai yang sama dengan angka 3.

Pada proses pencarian, program menemukan bahwa angka 3 muncul sebanyak 2 kali di dalam list, yaitu pada data pelanggan ke-2 dan pelanggan ke-5. Karena jumlah item yang dicari berhasil ditemukan lebih dari satu kali, program menampilkan hasil bahwa pembelian sebanyak 3 item ditemukan 2 kali. Selain itu, program juga memberikan informasi tambahan bahwa produk skincare dengan jumlah pembelian tersebut cukup populer, karena terdapat beberapa pelanggan yang membeli dengan jumlah yang sama.

Kesimpulan:
Program ini digunakan untuk menyimpan data pembelian skincare pelanggan dan mencari jumlah pembelian tertentu menggunakan metode Sequential Search. Program mampu menghitung berapa kali suatu jumlah pembelian muncul dalam data pelanggan dan menampilkan hasil pencarian dengan jelas. Dari hasil output tersebut dapat disimpulkan bahwa jumlah pembelian sebanyak 3 item termasuk cukup sering terjadi karena ditemukan pada dua pelanggan yang berbeda.

E. Link Youtube:
https://youtu.be/-7XwT-lyvVU?si=X544BwfAlYImUe6I


TUGAS POS ITERASI
<img width="894" height="1280" alt="WhatsApp Image 2026-05-12 at 22 21 34" src="https://github.com/user-attachments/assets/d48a7321-895a-4e16-9774-e816273bd536" />
