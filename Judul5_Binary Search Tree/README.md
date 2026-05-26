a. Judul Program:
Program Sistem Ranking Game Online Menggunakan Binary Search Tree (BST)

b. Deskripsi Singkat:
Program ini merupakan implementasi struktur data Binary Search Tree (BST) pada sistem ranking game online menggunakan bahasa pemrograman Python. Program digunakan untuk menyimpan dan mengelola data skor pemain secara terstruktur sehingga proses pencarian, pengurutan, dan pengolahan data menjadi lebih cepat dan efisien.

Pada program ini, pengguna dapat menambahkan skor pemain, mencari skor tertentu, menampilkan ranking pemain menggunakan traversal inorder, melihat skor tertinggi dan terendah, menghitung jumlah pemain, serta menghitung total seluruh skor pemain. Dengan menggunakan BST, data skor akan tersusun otomatis berdasarkan nilai sehingga mempermudah pengelolaan ranking dalam game online.

c. Source Code

<img width="763" height="968" alt="Screenshot 2026-05-26 223542" src="https://github.com/user-attachments/assets/e95a7633-41ab-42b5-910e-19fe085c1563" />

<img width="859" height="910" alt="Screenshot 2026-05-26 223601" src="https://github.com/user-attachments/assets/6f296147-b546-4795-9b22-f95ac4f7f566" />

<img width="1240" height="953" alt="Screenshot 2026-05-26 223617" src="https://github.com/user-attachments/assets/05292b47-6acd-44a9-ae6f-8406d9f8a1bb" />

<img width="773" height="924" alt="Screenshot 2026-05-26 223629" src="https://github.com/user-attachments/assets/55f66eed-ac87-44d2-86f7-b0589a272434" />


Baris pertama digunakan untuk membuat class `Node` yang berfungsi sebagai struktur dasar pada Binary Search Tree (BST).

Baris kedua merupakan constructor dari class `Node` yang akan otomatis dijalankan ketika object node dibuat.

Baris ketiga digunakan untuk menyimpan nilai data ke dalam node melalui atribut `key`.

Baris keempat digunakan untuk membuat child kiri dengan nilai awal kosong (`None`).

Baris kelima digunakan untuk membuat child kanan dengan nilai awal kosong (`None`).

Baris keenam merupakan baris kosong yang digunakan agar tampilan kode lebih rapi.

Baris ketujuh juga merupakan baris kosong sebagai pemisah antar class.

Baris kedelapan digunakan untuk membuat class `BSTDasar` yang berfungsi mengelola seluruh operasi Binary Search Tree.

Baris kesembilan merupakan constructor dari class `BSTDasar`.

Baris kesepuluh digunakan untuk membuat root BST dengan nilai awal kosong (`None`).

Baris kesebelas merupakan baris kosong untuk merapikan kode.

Baris kedua belas digunakan untuk membuat function `insert_node()` yang berfungsi memasukkan data ke BST secara rekursif.

Baris ketiga belas digunakan untuk mengecek apakah node saat ini kosong.

Baris keempat belas digunakan untuk membuat node baru jika posisi node masih kosong.

Baris kelima belas merupakan baris kosong.

Baris keenam belas digunakan untuk mengecek apakah nilai yang dimasukkan lebih kecil dari root.

Baris ketujuh belas digunakan untuk memasukkan data ke subtree kiri.

Baris kedelapan belas digunakan untuk mengecek apakah nilai lebih besar dari root.

Baris kesembilan belas digunakan untuk memasukkan data ke subtree kanan.

Baris kedua puluh merupakan baris kosong.

Baris kedua puluh satu digunakan untuk mengembalikan root setelah proses insert selesai.

Baris kedua puluh dua merupakan baris kosong.

Baris kedua puluh tiga digunakan untuk membuat function `insert()` sebagai function utama insert data.

Baris kedua puluh empat digunakan untuk memanggil function `insert_node()` mulai dari root.

Baris kedua puluh lima merupakan baris kosong.

Baris kedua puluh enam digunakan untuk membuat function `search_node()` yang berfungsi mencari data secara rekursif.

Baris kedua puluh tujuh digunakan untuk mengecek apakah node kosong.

Baris kedua puluh delapan digunakan untuk mengembalikan nilai `False` jika data tidak ditemukan.

Baris kedua puluh sembilan merupakan baris kosong.

Baris ketiga puluh digunakan untuk mengecek apakah data pada node sama dengan data yang dicari.

Baris ketiga puluh satu digunakan untuk mengembalikan nilai `True` jika data ditemukan.

Baris ketiga puluh dua merupakan baris kosong.

Baris ketiga puluh tiga digunakan untuk mengecek apakah data yang dicari lebih kecil dari root.

Baris ketiga puluh empat digunakan untuk melanjutkan pencarian ke subtree kiri.

Baris ketiga puluh lima merupakan baris kosong.

Baris ketiga puluh enam digunakan untuk melanjutkan pencarian ke subtree kanan.

Baris ketiga puluh tujuh merupakan baris kosong.

Baris ketiga puluh delapan digunakan untuk membuat function `search()` sebagai function utama pencarian data.

Baris ketiga puluh sembilan digunakan untuk memanggil function `search_node()` mulai dari root.

Baris keempat puluh merupakan baris kosong.

Baris keempat puluh satu digunakan untuk membuat function traversal inorder.

Baris keempat puluh dua digunakan untuk mengecek apakah node kosong.

Baris keempat puluh tiga digunakan untuk menghentikan traversal jika node kosong.

Baris keempat puluh empat merupakan baris kosong.

Baris keempat puluh lima digunakan untuk traversal subtree kiri terlebih dahulu.

Baris keempat puluh enam digunakan untuk menampilkan nilai node.

Baris keempat puluh tujuh digunakan untuk traversal subtree kanan.

Baris keempat puluh delapan merupakan baris kosong.

Baris keempat puluh sembilan digunakan untuk membuat function traversal preorder.

Baris kelima puluh digunakan untuk mengecek apakah node kosong.

Baris kelima puluh satu digunakan untuk menghentikan traversal jika node kosong.

Baris kelima puluh dua merupakan baris kosong.

Baris kelima puluh tiga digunakan untuk menampilkan root terlebih dahulu pada preorder.

Baris kelima puluh empat digunakan untuk traversal subtree kiri.

Baris kelima puluh lima digunakan untuk traversal subtree kanan.

Baris kelima puluh enam merupakan baris kosong.

Baris kelima puluh tujuh digunakan untuk membuat function traversal postorder.

Baris kelima puluh delapan digunakan untuk mengecek apakah node kosong.

Baris kelima puluh sembilan digunakan untuk menghentikan traversal jika node kosong.

Baris keenam puluh merupakan baris kosong.

Baris keenam puluh satu digunakan untuk traversal subtree kiri.

Baris keenam puluh dua digunakan untuk traversal subtree kanan.

Baris keenam puluh tiga digunakan untuk menampilkan root terakhir pada traversal postorder.

Baris keenam puluh empat merupakan baris kosong.

Baris keenam puluh lima digunakan untuk membuat function mencari nilai minimum pada BST.

Baris keenam puluh enam digunakan untuk mengecek apakah BST kosong.

Baris keenam puluh tujuh digunakan untuk mengembalikan nilai `-1` jika tree kosong.

Baris keenam puluh delapan merupakan baris kosong.

Baris keenam puluh sembilan digunakan untuk menyimpan root ke variabel `current`.

Baris ketujuh puluh merupakan baris kosong.

Baris ketujuh puluh satu digunakan untuk melakukan traversal ke kiri selama child kiri masih ada.

Baris ketujuh puluh dua digunakan untuk berpindah ke node kiri.

Baris ketujuh puluh tiga merupakan baris kosong.

Baris ketujuh puluh empat digunakan untuk mengembalikan nilai terkecil pada BST.

Baris ketujuh puluh lima merupakan baris kosong.

Baris ketujuh puluh enam digunakan untuk membuat function mencari nilai maksimum pada BST.

Baris ketujuh puluh tujuh digunakan untuk mengecek apakah tree kosong.

Baris ketujuh puluh delapan digunakan untuk mengembalikan nilai `-1` jika tree kosong.

Baris ketujuh puluh sembilan merupakan baris kosong.

Baris kedelapan puluh digunakan untuk menyimpan root ke variabel `current`.

Baris kedelapan puluh satu merupakan baris kosong.

Baris kedelapan puluh dua digunakan untuk traversal ke kanan selama child kanan masih ada.

Baris kedelapan puluh tiga digunakan untuk berpindah ke node kanan.

Baris kedelapan puluh empat merupakan baris kosong.

Baris kedelapan puluh lima digunakan untuk mengembalikan nilai terbesar pada BST.

Baris kedelapan puluh enam merupakan baris kosong.

Baris kedelapan puluh tujuh digunakan untuk membuat function menghitung jumlah node pada BST.

Baris kedelapan puluh delapan digunakan untuk mengecek apakah node kosong.

Baris kedelapan puluh sembilan digunakan untuk mengembalikan nilai `0` jika node kosong.

Baris kesembilan puluh merupakan baris kosong.

Baris kesembilan puluh satu digunakan untuk menghitung total seluruh node pada BST secara rekursif.

Baris kesembilan puluh dua merupakan baris kosong.

Baris kesembilan puluh tiga digunakan untuk membuat function menghitung total nilai seluruh node.

Baris kesembilan puluh empat digunakan untuk mengecek apakah node kosong.

Baris kesembilan puluh lima digunakan untuk mengembalikan nilai `0` jika node kosong.

Baris kesembilan puluh enam merupakan baris kosong.

Baris kesembilan puluh tujuh digunakan untuk menjumlahkan seluruh nilai node pada BST.

Baris kesembilan puluh delapan merupakan baris kosong.

Baris kesembilan puluh sembilan digunakan untuk membuat function `main()` sebagai program utama.

Baris keseratus digunakan untuk membuat object BST bernama `bst`.

Baris keseratus satu digunakan untuk membuat variabel `pilih` dengan nilai awal `0`.

Baris keseratus dua merupakan baris kosong.

Baris keseratus tiga digunakan untuk melakukan perulangan menu selama user belum memilih keluar.

Baris keseratus empat sampai keseratus empat belas digunakan untuk menampilkan seluruh menu program pada layar.

Baris keseratus lima belas merupakan baris kosong.

Baris keseratus enam belas digunakan untuk menangani error input menggunakan `try`.

Baris keseratus tujuh belas digunakan untuk membaca input pilihan menu dari user.

Baris keseratus delapan belas digunakan untuk menangkap error jika input bukan angka.

Baris keseratus sembilan belas digunakan untuk menampilkan pesan kesalahan input.

Baris keseratus dua puluh digunakan untuk mengulang kembali ke menu awal.

Baris keseratus dua puluh satu merupakan baris kosong.

Baris keseratus dua puluh dua digunakan untuk mengecek apakah user memilih menu insert skor.

Baris keseratus dua puluh tiga digunakan untuk menangani error input skor.

Baris keseratus dua puluh empat digunakan untuk membaca input skor pemain.

Baris keseratus dua puluh lima digunakan untuk memasukkan skor ke BST.

Baris keseratus dua puluh enam digunakan untuk menampilkan pesan bahwa skor berhasil ditambahkan.

Baris keseratus dua puluh tujuh digunakan untuk menangkap error jika input bukan angka.

Baris keseratus dua puluh delapan digunakan untuk menampilkan pesan error input.

Baris keseratus dua puluh sembilan merupakan baris kosong.

Baris keseratus tiga puluh digunakan untuk mengecek apakah user memilih menu pencarian skor.

Baris keseratus tiga puluh satu digunakan untuk menangani error input pencarian.

Baris keseratus tiga puluh dua digunakan untuk membaca skor yang dicari.

Baris keseratus tiga puluh tiga merupakan baris kosong.

Baris keseratus tiga puluh empat digunakan untuk mengecek apakah skor ditemukan di BST.

Baris keseratus tiga puluh lima digunakan untuk menampilkan pesan bahwa skor ditemukan.

Baris keseratus tiga puluh enam digunakan sebagai kondisi jika skor tidak ditemukan.

Baris keseratus tiga puluh tujuh digunakan untuk menampilkan pesan bahwa skor tidak ditemukan.

Baris keseratus tiga puluh delapan merupakan baris kosong.

Baris keseratus tiga puluh sembilan digunakan untuk menangani error input pencarian.

Baris keseratus empat puluh digunakan untuk menampilkan pesan input harus angka.

Baris keseratus empat puluh satu merupakan baris kosong.

Baris keseratus empat puluh dua digunakan untuk mengecek menu traversal inorder.

Baris keseratus empat puluh tiga digunakan untuk menampilkan tulisan ranking pemain.

Baris keseratus empat puluh empat digunakan untuk menjalankan traversal inorder.

Baris keseratus empat puluh lima digunakan untuk membuat baris baru setelah traversal selesai.

Baris keseratus empat puluh enam merupakan baris kosong.

Baris keseratus empat puluh tujuh digunakan untuk mengecek menu preorder.

Baris keseratus empat puluh delapan digunakan untuk menampilkan tulisan preorder.

Baris keseratus empat puluh sembilan digunakan untuk menjalankan traversal preorder.

Baris keseratus lima puluh digunakan untuk membuat baris baru.

Baris keseratus lima puluh satu merupakan baris kosong.

Baris keseratus lima puluh dua digunakan untuk mengecek menu postorder.

Baris keseratus lima puluh tiga digunakan untuk menampilkan tulisan postorder.

Baris keseratus lima puluh empat digunakan untuk menjalankan traversal postorder.

Baris keseratus lima puluh lima digunakan untuk membuat baris baru.

Baris keseratus lima puluh enam merupakan baris kosong.

Baris keseratus lima puluh tujuh digunakan untuk mengecek menu skor minimum.

Baris keseratus lima puluh delapan digunakan untuk menampilkan skor terendah pada BST.

Baris keseratus lima puluh sembilan merupakan baris kosong.

Baris keseratus enam puluh digunakan untuk mengecek menu skor maksimum.

Baris keseratus enam puluh satu digunakan untuk menampilkan skor tertinggi pada BST.

Baris keseratus enam puluh dua merupakan baris kosong.

Baris keseratus enam puluh tiga digunakan untuk mengecek menu jumlah pemain.

Baris keseratus enam puluh empat digunakan untuk menampilkan jumlah seluruh node/pemain.

Baris keseratus enam puluh lima merupakan baris kosong.

Baris keseratus enam puluh enam digunakan untuk mengecek menu total skor.

Baris keseratus enam puluh tujuh digunakan untuk menampilkan jumlah seluruh skor pemain.

Baris keseratus enam puluh delapan merupakan baris kosong.

Baris keseratus enam puluh sembilan digunakan untuk mengecek apakah user memilih keluar program.

Baris keseratus tujuh puluh digunakan untuk menampilkan pesan bahwa program selesai.

Baris keseratus tujuh puluh satu merupakan baris kosong.

Baris keseratus tujuh puluh dua digunakan sebagai kondisi jika pilihan menu tidak tersedia.

Baris keseratus tujuh puluh tiga digunakan untuk menampilkan pesan pilihan tidak valid.

Baris keseratus tujuh puluh empat merupakan baris kosong.

Baris keseratus tujuh puluh lima merupakan baris kosong sebagai pemisah akhir program.

Baris keseratus tujuh puluh enam digunakan untuk mengecek apakah file dijalankan langsung.

Baris keseratus tujuh puluh tujuh digunakan untuk menjalankan function `main()`.

Baris keseratus tujuh puluh delapan merupakan akhir dari program.

D. Output:

<img width="669" height="769" alt="Screenshot 2026-05-26 225221" src="https://github.com/user-attachments/assets/e0a89261-ac2b-48f5-b4eb-a14566b4d1b0" />

<img width="581" height="750" alt="Screenshot 2026-05-26 225253" src="https://github.com/user-attachments/assets/9f7a5709-499c-4962-82c9-5e4c6f92be3b" />

<img width="579" height="745" alt="Screenshot 2026-05-26 225305" src="https://github.com/user-attachments/assets/1757c314-3ab5-4274-bb3a-03ec7b890cb2" />

<img width="561" height="707" alt="Screenshot 2026-05-26 225321" src="https://github.com/user-attachments/assets/eec82270-25fe-469f-b139-52d6e6cacbd4" />

E. Link Youtubw:
https://youtu.be/-P4n5UNvHzs
