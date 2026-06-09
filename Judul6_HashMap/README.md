A. Judul Program: Sistem Data Turnamen Esports

B. Deskripsi Singkat: Program ini merupakan implementasi **Hash Map Open Addressing dengan metode Linear Probing** menggunakan bahasa Python untuk mengelola data tim pada sebuah turnamen esports. Program memungkinkan pengguna untuk menambahkan, mencari, menghapus, dan menampilkan data tim berdasarkan ID Tim sebagai key. Data disimpan dalam hash table sehingga proses penyimpanan dan pencarian dapat dilakukan dengan lebih cepat dan efisien. Jika terjadi collision (dua key menghasilkan indeks yang sama), program akan menggunakan metode Linear Probing untuk mencari slot kosong berikutnya. Tujuan dari program ini adalah untuk memahami penerapan struktur data hash map, cara menangani collision, serta mengelola data tim turnamen esports secara sederhana dan efisien.

C. Source Code:
<img width="728" height="971" alt="Screenshot 2026-06-09 204740" src="https://github.com/user-attachments/assets/6ef31bf3-76a3-4665-845c-917ee795511b" />


<img width="738" height="912" alt="Screenshot 2026-06-09 204811" src="https://github.com/user-attachments/assets/15203f6f-a2c3-4e12-a23d-144c63161e46" />


<img width="768" height="902" alt="Screenshot 2026-06-09 204825" src="https://github.com/user-attachments/assets/5a072de6-c97f-4fa9-8f8d-527640ef990b" />



**Baris 1**: Mendefinisikan class `SlotState` yang digunakan untuk menyimpan status setiap slot pada hash table.

**Baris 2**: Mendefinisikan konstanta `EMPTY` bernilai 0 yang menandakan slot masih kosong.

**Baris 3**: Mendefinisikan konstanta `OCCUPIED` bernilai 1 yang menandakan slot sudah terisi data.

**Baris 4**: Mendefinisikan konstanta `DELETED` bernilai 2 yang menandakan data pada slot telah dihapus.

**Baris 5**: Baris kosong sebagai pemisah kode.

**Baris 6**: Baris kosong.

**Baris 7**: Mendefinisikan class `Entry` yang digunakan untuk menyimpan key, value, dan state.

**Baris 8**: Mendefinisikan constructor `__init__()` pada class `Entry`.

**Baris 9**: Menginisialisasi atribut `key` dengan nilai `None`.

**Baris 10**: Menginisialisasi atribut `value` dengan nilai `None`.

**Baris 11**: Menginisialisasi status slot menjadi `EMPTY`.

**Baris 12**: Baris kosong.

**Baris 13**: Mendefinisikan class `HashMapOpenAddressing`.

**Baris 14**: Mendefinisikan constructor class dengan parameter ukuran tabel default 10.

**Baris 15**: Menyimpan ukuran hash table ke atribut `SIZE`.

**Baris 16**: Membuat list berisi objek `Entry` sebanyak ukuran hash table.

**Baris 17**: Baris kosong.

**Baris 18**: Mendefinisikan fungsi `hash_function()`.

**Baris 19**: Menerima parameter `key` yang akan di-hash.

**Baris 20**: Menghitung dan mengembalikan indeks hash menggunakan operasi modulo.

**Baris 21**: Baris kosong.

**Baris 22**: Mendefinisikan fungsi `insert()` untuk menambahkan data ke hash table.

**Baris 23**: Menghitung indeks awal menggunakan fungsi hash.

**Baris 24**: Membuat variabel `first_deleted` dengan nilai awal -1.

**Baris 25**: Baris kosong.

**Baris 26**: Melakukan perulangan sebanyak ukuran hash table.

**Baris 27**: Menghitung indeks menggunakan metode Linear Probing.

**Baris 28**: Baris kosong.

**Baris 29**: Mengecek apakah slot saat ini berstatus `OCCUPIED`.

**Baris 30**: Mengecek apakah key yang dimasukkan sudah ada.

**Baris 31**: Mengubah value jika key yang sama ditemukan.

**Baris 32**: Mengembalikan nilai `True` karena proses update berhasil.

**Baris 33**: Baris kosong.

**Baris 34**: Mengecek apakah slot berstatus `DELETED`.

**Baris 35**: Mengecek apakah belum ada slot DELETED yang tersimpan.

**Baris 36**: Menyimpan indeks slot DELETED pertama yang ditemukan.

**Baris 37**: Baris kosong.

**Baris 38**: Menangani kondisi ketika slot yang diperiksa berstatus EMPTY.

**Baris 39**: Mengecek apakah sebelumnya ditemukan slot DELETED.

**Baris 40**: Menggunakan indeks slot DELETED tersebut untuk penyimpanan data.

**Baris 41**: Baris kosong.

**Baris 42**: Menyimpan key ke slot hash table.

**Baris 43**: Menyimpan value ke slot hash table.

**Baris 44**: Mengubah status slot menjadi `OCCUPIED`.

**Baris 45**: Mengembalikan nilai `True` karena data berhasil ditambahkan.

**Baris 46**: Baris kosong.

**Baris 47**: Mengecek apakah terdapat slot DELETED yang dapat digunakan.

**Baris 48**: Menyimpan key pada slot DELETED tersebut.

**Baris 49**: Menyimpan value pada slot DELETED tersebut.

**Baris 50**: Mengubah status slot menjadi `OCCUPIED`.

**Baris 51**: Mengembalikan nilai `True` karena data berhasil disimpan.

**Baris 52**: Baris kosong sebagai pemisah kode.

**Baris 53**: Mengembalikan nilai `False` jika tidak ada slot yang dapat digunakan untuk menyimpan data.

Jika baris 53 = return False, maka lanjutan penjelasannya adalah:

Baris 53: Mengembalikan nilai False jika proses penyisipan data gagal karena tidak ada slot yang tersedia.

Baris 54: Baris kosong sebagai pemisah antar fungsi.

Baris 55: Mendefinisikan fungsi search() yang digunakan untuk mencari data berdasarkan key.

Baris 56: Menerima parameter key yang akan dicari pada hash table.

Baris 57: Menghitung indeks awal menggunakan fungsi hash.

Baris 58: Baris kosong.

Baris 59: Melakukan perulangan sebanyak ukuran hash table untuk proses pencarian.

Baris 60: Menghitung indeks menggunakan metode Linear Probing.

Baris 61: Baris kosong.

Baris 62: Mengecek apakah slot yang sedang diperiksa berstatus EMPTY.

Baris 63: Mengembalikan nilai None karena data tidak ditemukan.

Baris 64: Baris kosong.

Baris 65: Mengecek apakah slot berstatus OCCUPIED dan key pada slot sama dengan key yang dicari.

Baris 66: Mengembalikan objek data yang ditemukan.

Baris 67: Baris kosong.

Baris 68: Mengembalikan nilai None jika seluruh pencarian selesai tetapi data tidak ditemukan.

Baris 69: Baris kosong.

Baris 70: Mendefinisikan fungsi remove_key() yang digunakan untuk menghapus data berdasarkan key.

Baris 71: Memanggil fungsi search() untuk mencari data yang akan dihapus.

Baris 72: Baris kosong.

Baris 73: Mengecek apakah data yang dicari tidak ditemukan.

Baris 74: Mengembalikan nilai False jika data tidak ada.

Baris 75: Baris kosong.

Baris 76: Mengubah status data menjadi DELETED.

Baris 77: Mengembalikan nilai True karena data berhasil dihapus.

Baris 78: Baris kosong.

Baris 79: Mendefinisikan fungsi display() untuk menampilkan seluruh isi hash table.

Baris 80: Menampilkan judul "DATA TIM TURNAMEN ESPORTS".

Baris 81: Baris kosong.

Baris 82: Melakukan perulangan untuk seluruh indeks hash table.

Baris 83: Menampilkan nomor indeks yang sedang diperiksa.

Baris 84: Baris kosong.

Baris 85: Mengecek apakah slot berstatus EMPTY.

Baris 86: Menampilkan tulisan "EMPTY".

Baris 87: Mengecek apakah slot berstatus DELETED.

Baris 88: Menampilkan tulisan "DELETED".

Baris 89: Menangani kondisi jika slot berisi data.

Baris 90: Menampilkan ID Tim dan Nama Tim yang tersimpan pada slot tersebut.

Baris 91: Baris kosong.

Baris 92: Mendefinisikan fungsi main() sebagai fungsi utama program.

Baris 93: Membuat objek turnamen dari class HashMapOpenAddressing.

Baris 94: Baris kosong.

Baris 95: Membuat perulangan tak hingga menggunakan while True.

Baris 96: Menampilkan judul menu program.

Baris 97: Menampilkan pilihan menu nomor 1 untuk menambah data tim.

Baris 98: Menampilkan pilihan menu nomor 2 untuk mencari data tim.

Baris 99: Menampilkan pilihan menu nomor 3 untuk menghapus data tim.

Baris 100: Menampilkan pilihan menu nomor 4 untuk menampilkan seluruh data tim.

Baris 101: Menampilkan pilihan menu nomor 5 untuk keluar dari program.

Baris 102: Baris kosong.

Baris 103: Meminta pengguna memasukkan pilihan menu.

Baris 104: Baris kosong.

Baris 105: Mengecek apakah pengguna memilih menu nomor 1.

Baris 106: Meminta pengguna memasukkan ID Tim.

Baris 107: Meminta pengguna memasukkan Nama Tim.

Baris 108: Baris kosong.

Baris 109: Menjalankan fungsi insert() untuk menambahkan data tim.

Baris 110: Menampilkan pesan bahwa data tim berhasil ditambahkan jika proses insert berhasil.

Baris 111: Menangani kondisi jika proses insert gagal.

Baris 112: Menampilkan pesan bahwa hash table penuh.

Baris 113: Baris kosong.

Baris 114: Mengecek apakah pengguna memilih menu nomor 2.

Baris 115: Meminta pengguna memasukkan ID Tim yang ingin dicari.

Baris 116: Baris kosong.

Baris 117: Menjalankan fungsi search().

Baris 118: Baris kosong.

Baris 119: Mengecek apakah data ditemukan.

Baris 120: Menampilkan judul informasi data tim yang ditemukan.

Baris 121: Menampilkan ID Tim yang ditemukan.

Baris 122: Menampilkan Nama Tim yang ditemukan.

Baris 123: Menangani kondisi jika data tidak ditemukan.

Baris 124: Menampilkan pesan bahwa data tim tidak ditemukan.

Baris 125: Baris kosong.

Baris 126: Mengecek apakah pengguna memilih menu nomor 3.

Baris 127: Meminta pengguna memasukkan ID Tim yang akan dihapus.

Baris 128: Baris kosong.

Baris 129: Menjalankan fungsi remove_key().

Baris 130: Mengecek apakah proses penghapusan berhasil.

Baris 131: Menampilkan pesan bahwa data tim berhasil dihapus.

Baris 132: Menangani kondisi jika data tidak ditemukan.

Baris 133: Menampilkan pesan bahwa data tim tidak ditemukan.

Baris 134: Baris kosong.

Baris 135: Mengecek apakah pengguna memilih menu nomor 4.

Baris 136: Menjalankan fungsi display() untuk menampilkan seluruh data tim.

Baris 137: Baris kosong.

Baris 138: Mengecek apakah pengguna memilih menu nomor 5.

Baris 139: Menampilkan pesan terima kasih kepada pengguna.

Baris 140: Menghentikan perulangan menggunakan break.

Baris 141: Baris kosong.

Baris 142: Menangani kondisi jika pilihan menu tidak valid.

Baris 143: Menampilkan pesan "Pilihan tidak valid."

Baris 144: Baris kosong.

Baris 145: Mengecek apakah file dijalankan secara langsung menggunakan if __name__ == "__main__":.

Baris 146: Memanggil fungsi main() untuk menjalankan program.

D. Output

<img width="497" height="895" alt="Screenshot 2026-06-09 230646" src="https://github.com/user-attachments/assets/cf0b7189-f4e1-4d6e-a9fc-00cbf8f0cd72" />

<img width="658" height="807" alt="Screenshot 2026-06-09 230651" src="https://github.com/user-attachments/assets/b29888ef-9146-4386-9acd-f24e7054b8e2" />


E. Link Youtube: https://youtu.be/mu99W-xRRzc
