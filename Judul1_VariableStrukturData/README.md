a. Judul Program : Program To-Do List dengan Deadline dan Fitur Pencarian Berbasis Array (List Python)

b. Deskripsi Singkat : Program ini merupakan aplikasi sederhana untuk mengelola daftar tugas harian (to-do list) dengan memanfaatkan struktur data array yang direpresentasikan menggunakan list dalam Python. Setiap tugas disimpan dalam bentuk elemen list yang berisi nama tugas, deadline, dan status pengerjaan. Program ini menyediakan beberapa fitur utama seperti menambahkan tugas, menghapus tugas, menandai tugas sebagai selesai, menampilkan seluruh daftar tugas, serta mencari tugas berdasarkan kata kunci. Dengan adanya fitur deadline, pengguna dapat mengatur waktu penyelesaian tugas, sedangkan fitur pencarian memudahkan dalam menemukan tugas tertentu secara cepat. Program ini dirancang untuk membantu pengguna dalam mengatur aktivitas sehari-hari secara lebih terstruktur dan efisien.

C. Source Code :

<img width="451" height="961" alt="Screenshot 2026-04-28 172105" src="https://github.com/user-attachments/assets/713f632a-730b-4539-9cf8-1fab454f3a14" />

 
•  Baris 1 mendefinisikan fungsi utama main() sebagai tempat seluruh program dijalankan. 
•  Baris 2 membuat list kosong bernama tugas untuk menyimpan data tugas. 
•  Baris 3 merupakan baris kosong sebagai pemisah agar kode lebih rapi. 
•  Baris 4 membuat perulangan while True agar program terus berjalan sampai dihentikan. 
•  Baris 5 menampilkan judul program “TO DO LIST”. 
•  Baris 6 menampilkan pilihan menu untuk menambahkan tugas. 
•  Baris 7 menampilkan pilihan menu untuk menghapus tugas. 
•  Baris 8 menampilkan pilihan menu untuk menandai tugas selesai. 
•  Baris 9 menampilkan pilihan menu untuk menampilkan semua tugas. 
•  Baris 10 menampilkan pilihan menu untuk mencari tugas. 
•  Baris 11 menampilkan pilihan menu untuk keluar dari program. 
•  Baris 12 adalah baris kosong untuk kerapian. 
•  Baris 13 menerima input dari pengguna untuk memilih menu dan menyimpannya ke variabel pilihan. 
•  Baris 14 baris kosong sebagai pemisah. 
•  Baris 15 memeriksa apakah pengguna memilih menu 1 (menambah tugas). 
•  Baris 16 meminta pengguna memasukkan nama tugas. 
•  Baris 17 meminta pengguna memasukkan deadline tugas. 
•  Baris 18 menambahkan data tugas ke dalam list tugas dengan status awal “Belum selesai”. 
•  Baris 19 menampilkan pesan bahwa tugas berhasil ditambahkan. 
•  Baris 20 baris kosong. 
•  Baris 21 memeriksa apakah pengguna memilih menu 2 (menghapus tugas). 
•  Baris 22 mengecek apakah list tugas kosong. 
•  Baris 23 menampilkan pesan “Tidak ada tugas” jika list kosong. 
•  Baris 24 menggunakan continue untuk kembali ke awal loop. 
•  Baris 25 baris kosong. 
•  Baris 26 melakukan perulangan untuk menampilkan semua tugas beserta indeksnya. 
•  Baris 27 menampilkan detail tugas (nama, deadline, status). 
•  Baris 28 baris kosong. 
•  Baris 29 memulai blok try untuk menangani kemungkinan error. 
•  Baris 30 meminta input indeks tugas yang ingin dihapus. 
•  Baris 31 mengecek apakah indeks valid. 
•  Baris 32 menghapus tugas dari list menggunakan pop(). 
•  Baris 33 menampilkan pesan bahwa tugas berhasil dihapus. 
•  Baris 34 menangani kondisi jika indeks tidak valid. 
•  Baris 35 menampilkan pesan kesalahan indeks. 
•  Baris 36 menangkap error jika input bukan angka. 
•  Baris 37 menampilkan pesan bahwa input harus berupa angka. 
•  Baris 38 memeriksa apakah pengguna memilih menu 3 (tandai selesai). 
•  Baris 39 mengecek apakah list kosong. 
•  Baris 40 menampilkan pesan jika tidak ada tugas. 
•  Baris 41 kembali ke menu awal dengan continue. 
•  Baris 42 baris kosong. 
•  Baris 43 melakukan perulangan untuk menampilkan tugas. 
•  Baris 44 menampilkan detail tugas. 
•  Baris 45 baris kosong. 
•  Baris 46 memulai blok try. 
•  Baris 47 meminta input indeks tugas. 
•  Baris 48 mengecek apakah indeks valid. 
•  Baris 49 mengubah status tugas menjadi “Selesai”. 
•  Baris 50 menampilkan pesan bahwa tugas telah ditandai selesai. 
•  Baris 51 menangani kondisi jika indeks tidak valid. 
•  Baris 52 menampilkan pesan kesalahan. 
•  Baris 53 menangkap error input. 
•  Baris 54 menampilkan pesan bahwa input harus angka. 
•  Baris 55 baris kosong. 
•  Baris 56 memeriksa apakah pengguna memilih menu 4 (tampilkan semua tugas). 
•  Baris 57 mengecek apakah list kosong. 
•  Baris 58 menampilkan pesan jika belum ada tugas. 
•  Baris 59 menangani kondisi jika ada tugas. 
•  Baris 60 menampilkan judul “Daftar Tugas”. 
•  Baris 61 melakukan perulangan pada semua tugas. 
•  Baris 62 menampilkan detail setiap tugas. 
•  Baris 63 baris kosong. 
•  Baris 64 baris kosong tambahan. 
•  Baris 65 memeriksa apakah pengguna memilih menu 5 (mencari tugas). 
•  Baris 66 meminta input kata kunci dan mengubahnya menjadi huruf kecil. 
•  Baris 67 membuat variabel ditemukan dengan nilai awal False. 
•  Baris 68 baris kosong. 
•  Baris 69 melakukan perulangan untuk mencari tugas. 
•  Baris 70 mengecek apakah kata kunci ada dalam nama tugas. 
•  Baris 71 menampilkan tugas yang cocok. 
•  Baris 72 mengubah ditemukan menjadi True jika ada hasil. 
•  Baris 73 baris kosong. 
•  Baris 74 mengecek apakah tidak ada tugas yang ditemukan. 
•  Baris 75 menampilkan pesan “Tugas tidak ditemukan”. 
•  Baris 76 baris kosong. 
•  Baris 77 memeriksa apakah pengguna memilih menu 6 (keluar). 
•  Baris 78 menampilkan pesan bahwa program selesai. 
•  Baris 79 menghentikan perulangan dengan break. 
•  Baris 80 baris kosong. 
•  Baris 81 menangani kondisi jika pilihan tidak valid. 
•  Baris 82 menampilkan pesan “Pilihan tidak valid”. 
•  Baris 83 baris kosong. 
•  Baris 84 baris kosong tambahan. 
•  Baris 85 mengecek apakah file dijalankan langsung. 
•  Baris 86 memanggil fungsi main() untuk menjalankan program.

D. Output Program:

<img width="511" height="911" alt="Screenshot 2026-04-28 165833" src="https://github.com/user-attachments/assets/ffe54e20-f8a4-4794-b179-8b0a3fc67dbf" />

 
Pengguna akan melihat tampilan menu yang berisi beberapa pilihan, yaitu menambah tugas, menghapus tugas, menandai tugas sebagai selesai, menampilkan seluruh daftar tugas, mencari tugas, dan keluar dari program
Ketika pengguna memilih untuk menambah tugas, output yang dihasilkan adalah konfirmasi bahwa tugas telah berhasil ditambahkan ke dalam daftar. Data tugas tersebut akan tersimpan dalam sistem dan dapat dilihat melalui menu tampilkan tugas. 
Jika pengguna memilih menu tampilkan semua tugas, program akan menampilkan seluruh daftar tugas dalam format yang terstruktur, yaitu berupa indeks, nama tugas, deadline, dan status pengerjaan (Belum atau Selesai).
Apabila belum ada tugas yang dimasukkan, program akan menampilkan pesan bahwa daftar tugas masih kosong.
Pada saat pengguna memilih menu hapus tugas, program akan terlebih dahulu menampilkan daftar tugas yang tersedia. Setelah pengguna memasukkan indeks yang valid, program akan menghapus tugas tersebut dan menampilkan pesan konfirmasi bahwa tugas telah dihapus. 
Jika indeks yang dimasukkan tidak valid atau daftar tugas kosong, program akan menampilkan pesan kesalahan yang sesuai. Untuk menu tandai selesai, output yang dihasilkan berupa perubahan status tugas dari “Belum selesai” menjadi “Selesai”, yang kemudian dapat dilihat saat daftar tugas ditampilkan kembali.
Pada menu pencarian, output program akan menampilkan tugas-tugas yang sesuai dengan kata kunci yang dimasukkan oleh pengguna. Jika terdapat kecocokan, tugas tersebut akan ditampilkan lengkap dengan informasi detailnya. 
Namun, jika tidak ditemukan tugas yang sesuai, program akan menampilkan pesan bahwa tugas tidak ditemukan. Terakhir, ketika pengguna memilih menu keluar, program akan menampilkan pesan bahwa program telah selesai dan kemudian berhenti dijalankan.

E. Link Youtube : https://youtu.be/1_v3QUP-sxo
