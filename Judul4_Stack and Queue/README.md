a. Judul Program : Tumpukan Cucian Baju Laundry
b. Deskripsi Singkat : Program tersebut merupakan implementasi struktur data Stack menggunakan Linked List yang diterapkan pada sistem tumpukan laundry atau baju. Program ini bekerja dengan konsep LIFO (Last In First Out), yaitu data yang terakhir dimasukkan akan menjadi data pertama yang diambil kembali. Dalam program, pengguna dapat menambahkan baju ke dalam tumpukan, mengambil baju paling atas, melihat baju yang berada di posisi teratas, serta menampilkan seluruh isi tumpukan. Setiap data baju disimpan dalam node yang saling terhubung menggunakan linked list sehingga ukuran penyimpanan menjadi lebih fleksibel dan dapat bertambah sesuai kebutuhan tanpa harus menentukan kapasitas awal.
c.  Source Code :

<img width="578" height="946" alt="Screenshot 2026-05-19 210606" src="https://github.com/user-attachments/assets/3bc0a28c-63a5-4036-96a0-36401c403896" />

<img width="420" height="702" alt="Screenshot 2026-05-19 210622" src="https://github.com/user-attachments/assets/1b58d2ce-47f1-46b8-ae29-70154176f128" />

Pada baris pertama, program membuat class `Node` yang digunakan sebagai elemen dasar linked list. Di dalam class ini terdapat constructor `__init__` 

Pada baris kedua yang menerima parameter `data`. 

Pada Baris ketiga berfungsi menyimpan nilai data ke dalam variabel `self.data` 

Pada baris keempat mengatur `self.next = None`, yang berarti node belum terhubung dengan node lain.

Pada baris ketujuh dibuat class `LaundryStack` yang berfungsi sebagai stack atau tumpukan baju. 

Constructor pada baris kedelapan digunakan untuk menginisialisasi stack.

Baris kesembilan membuat variabel `top_ptr` bernilai `None` yang menandakan bahwa stack masih kosong dan belum memiliki node paling atas.

Pada baris sebelas dibuat method `is_empty()` untuk memeriksa apakah stack kosong atau tidak. 

Baris kedua belas mengembalikan nilai `True` jika `top_ptr` bernilai `None`, dan `False` jika stack masih memiliki isi.

Baris empat belas sampai delapan belas merupakan method `tambah_baju()` yang berfungsi menambahkan data ke dalam stack (push). 

Pada baris lima belas dibuat node baru menggunakan `Node(baju)`. 

Baris enam belas menghubungkan node baru ke node paling atas sebelumnya menggunakan `new_node.next = self.top_ptr`. 

Pada baris tujuh belas posisi `top_ptr` dipindahkan ke node baru sehingga node tersebut menjadi posisi paling atas stack. 

Baris delapan belas menampilkan pesan bahwa baju berhasil ditambahkan.

Pada baris dua puluh satu dibuat method `ambil_baju()` untuk mengambil data paling atas dari stack (pop). 

Baris dua puluh dua memeriksa apakah stack kosong menggunakan `is_empty()`. 

Jika kosong maka pada baris dua puluh tiga program menampilkan pesan “Tumpukan baju kosong” 

Dan pada baris dua puluh empat function dihentikan menggunakan `return`. 

Jika stack tidak kosong, maka pada baris dua puluh enam data paling atas disimpan sementara ke variabel `temp`. 

Baris dua puluh tujuh menampilkan nama baju yang diambil. 

Pada baris dua puluh delapan `top_ptr` dipindahkan ke node berikutnya sehingga node paling atas sebelumnya terhapus dari stack.

Pada baris tiga puluh satu dibuat method `lihat_atas()` yang berfungsi melihat data paling atas stack tanpa menghapusnya. 

Baris tiga puluh dua kembali memeriksa apakah stack kosong. 

Jika kosong maka pada baris tiga puluh tiga ditampilkan pesan “Tidak ada baju”. 

Lalu function dihentikan pada baris tiga puluh empat. 

Jika stack memiliki isi maka pada baris tiga puluh enam program menampilkan data pada node paling atas menggunakan `self.top_ptr.data`.

Baris tiga puluh delapan sampai empat puluh delapan merupakan method `tampilkan()` yang digunakan untuk menampilkan seluruh isi stack. 

Program terlebih dahulu memeriksa apakah stack kosong pada baris tiga puluh sembilan. 

Jika kosong maka muncul pesan “Tidak ada baju” pada baris empat puluh 

Dan function dihentikan pada baris empat puluh satu. 

Jika stack memiliki isi maka pada baris empat puluh tiga ditampilkan judul “Tumpukan Baju:”. 

Baris empat puluh empat membuat variabel `current` yang menunjuk ke node paling atas. 

Pada baris empat puluh enam digunakan perulangan `while` untuk menelusuri seluruh node selama `current` tidak bernilai `None`. 

Baris empat puluh tujuh mencetak data setiap node

Lalu baris empat puluh delapan memindahkan pointer ke node berikutnya menggunakan `current.next`.

Pada baris lima puluh satu dibuat function `main()` sebagai program utama. 

Baris lima puluh dua membuat object `laundry` dari class `LaundryStack`. 

Selanjutnya pada baris lima puluh empat digunakan perulangan `while True` agar menu terus berjalan sampai pengguna memilih keluar. 

Baris lima puluh lima sampai enam puluh menampilkan menu program, yaitu tambah baju, ambil baju, lihat baju atas, tampilkan tumpukan, dan keluar. 

Pada baris enam puluh dua program meminta input pilihan menu dari pengguna menggunakan `input()`.

Baris enam puluh empat memeriksa apakah pengguna memilih menu “1”. 

Jika benar maka pada baris enam puluh lima pengguna diminta memasukkan nama baju.

Kemudian pada baris enam puluh enam method `tambah_baju()` dipanggil untuk menambahkan baju ke stack. 

Jika pengguna memilih “2”, maka pada baris enam puluh sembilan program menjalankan method `ambil_baju()`. 

Jika memilih “3”, maka pada baris tujuh puluh dua program memanggil method `lihat_atas()`. 

Jika memilih “4”, maka pada baris tujuh puluh lima program menampilkan seluruh isi stack menggunakan method `tampilkan()`. 

Jika pengguna memilih “5”, maka pada baris tujuh puluh delapan program menampilkan pesan “Program selesai”. 

Pada baris tujuh puluh sembilan perulangan dihentikan menggunakan `break`. 

Jika input tidak sesuai pilihan menu, maka pada baris delapan puluh dua ditampilkan pesan “Pilihan tidak valid”.

Terakhir, pada baris delapan puluh lima terdapat kondisi `if __name__ == "__main__":` yang digunakan untuk memastikan bahwa file dijalankan secara langsung, bukan diimpor sebagai module. 

Jika kondisi benar, maka pada baris delapan puluh enam function `main()` dijalankan sehingga seluruh program dapat berjalan. Program ini menerapkan konsep stack dengan metode LIFO (Last In First Out), yaitu data yang terakhir masuk akan menjadi data pertama yang keluar.

d. Output :

<img width="281" height="823" alt="WhatsApp Image 2026-05-19 at 23 14 01" src="https://github.com/user-attachments/assets/c02e58b2-5a38-469f-bed0-066fd20c9488" /><img width="349" height="703" alt="WhatsApp Image 2026-05-19 at 23 14 02" src="https://github.com/user-attachments/assets/09c37011-64a8-4938-bc36-62bbd29a7a29" />

Output program tersebut menunjukkan proses kerja struktur data stack pada sistem laundry yang menggunakan konsep LIFO (Last In First Out), yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Ketika program pertama kali dijalankan, muncul tampilan menu “STACK LAUNDRY” yang berisi pilihan untuk menambah baju, mengambil baju, melihat baju paling atas, menampilkan seluruh tumpukan, dan keluar program. Tampilan menu ini muncul karena adanya perulangan while True pada function main(), sehingga menu akan terus ditampilkan sampai pengguna memilih opsi keluar.

Pada proses pertama, pengguna memilih menu 1 untuk menambahkan baju dan memasukkan nama baju KNITSWEATER. Program kemudian menampilkan pesan “Baju 'KNITSWEATER' ditambahkan”. Hal ini terjadi karena method tambah_baju() dipanggil untuk membuat node baru yang berisi data KNITSWEATER. Karena stack masih kosong, maka node tersebut langsung menjadi node paling atas (top_ptr). Setelah itu menu kembali muncul karena program masih berada di dalam perulangan utama.

Selanjutnya pengguna memilih menu 2 untuk mengambil baju. Program menampilkan output “Mengambil baju: KNITSWEATER”. Output ini berasal dari method ambil_baju() yang mengambil node paling atas stack. Pada saat itu KNITSWEATER merupakan satu-satunya data di dalam stack, sehingga setelah diambil posisi top_ptr berubah menjadi None dan stack kembali kosong.

Kemudian pengguna memilih menu 3 untuk melihat baju paling atas. Namun program menampilkan pesan “Tidak ada baju”. Hal ini terjadi karena sebelumnya KNITSWEATER sudah diambil sehingga stack kosong. Pada method lihat_atas(), program terlebih dahulu memeriksa kondisi stack menggunakan is_empty(). Karena hasilnya True, maka program menampilkan pesan bahwa tidak ada baju di dalam tumpukan.

Setelah itu pengguna kembali memilih menu 1 dan menambahkan baju KEMEJA. Program membuat node baru berisi KEMEJA dan menjadikannya sebagai node paling atas. Selanjutnya pengguna menambahkan lagi baju KAOS. Saat data KAOS dimasukkan, program membuat node baru lalu menghubungkannya ke node KEMEJA menggunakan pointer next. Setelah itu KAOS menjadi posisi paling atas stack. Kondisi stack saat itu adalah KAOS berada di atas KEMEJA.

Pengguna kemudian menambahkan lagi data SWEATER. Sama seperti sebelumnya, program membuat node baru berisi SWEATER, lalu node tersebut diarahkan ke KAOS. Setelah pointer top_ptr dipindahkan, posisi stack menjadi SWEATER di paling atas, diikuti KAOS, lalu KEMEJA di bagian bawah. Urutan ini menunjukkan bahwa stack menyimpan data berdasarkan urutan masuk terakhir.

Ketika pengguna memilih menu 3, program menampilkan output “Baju paling atas: SWEATER”. Hal ini karena method lihat_atas() mengambil data dari self.top_ptr.data. Karena top_ptr menunjuk ke node SWEATER, maka data itulah yang tampil sebagai baju paling atas. Pada proses ini data tidak dihapus, hanya dilihat saja.

Selanjutnya pengguna memilih menu 4 untuk menampilkan seluruh isi stack. Program menampilkan:

Tumpukan Baju:
SWEATER
KAOS
KEMEJA

Output tersebut dihasilkan dari method tampilkan() yang melakukan traversal linked list menggunakan variabel current. Awalnya current menunjuk ke top_ptr, yaitu SWEATER. Program kemudian melakukan perulangan while untuk mencetak setiap data node satu per satu mulai dari atas ke bawah. Setelah mencetak SWEATER, pointer berpindah ke KAOS, kemudian ke KEMEJA, lalu berhenti ketika mencapai None. Urutan output menunjukkan konsep stack bahwa data terakhir masuk berada di posisi paling atas.

Terakhir pengguna memilih menu 5 sehingga program menampilkan pesan “Program selesai”. Output ini muncul karena program menjalankan perintah break yang menghentikan perulangan while True. Dengan demikian program selesai dijalankan. Dari keseluruhan output dapat disimpulkan bahwa program berhasil menerapkan struktur data stack menggunakan linked list, di mana penambahan dan pengambilan data selalu dilakukan dari bagian paling atas tumpukan.

E. Link Youtube : 
https://youtu.be/gM0axHtqs_I
