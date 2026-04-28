def main():
    tugas = []

    while True:
        print("\nTO DO LIST")
        print("1. Menambahkan tugas ke daftar")
        print("2. Menghapus tugas dari daftar")
        print("3. Tandai sudah selesai")
        print("4. Menampilkan semua tugas")
        print("5. Mencari tugas")
        print("6. Keluar")

        pilihan = input("Pilihan: ")

        if pilihan == "1":
            nama = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline (Contoh: 30-04-2026): ")
            tugas.append([nama, deadline, "Belum selesai"])
            print("Tugas ditambahkan")

        elif pilihan == "2":
            if not tugas:
                print("Tidak ada tugas")
                continue

            for i, t in enumerate(tugas):
                print(f"{i}. {t[0]} | Deadline: {t[1]} | Status: {t[2]}")

            try:
                idx = int(input("Pilih indeks yang ingin dihapus: "))
                if 0 <= idx < len(tugas):
                    tugas.pop(idx)
                    print("Tugas dihapus")
                else:
                    print("Indeks tidak valid")
            except ValueError:
                print("Harus angka!")

        elif pilihan == "3":
            if not tugas:
                print("Tidak ada tugas")
                continue

            for i, t in enumerate(tugas):
                print(f"{i}. {t[0]} | Deadline: {t[1]} | Status: {t[2]}")

            try:
                idx = int(input("Pilih indeks tugas: "))
                if 0 <= idx < len(tugas):
                    tugas[idx][2] = "Selesai"
                    print("Tugas ditandai selesai")
                else:
                    print("Indeks tidak valid")
            except ValueError:
                print("Harus angka!")

        elif pilihan == "4":
            if not tugas:
                print("Belum ada tugas")
            else:
                print("\nDaftar Tugas:")
                for i, t in enumerate(tugas):
                    print(f"{i}. {t[0]} | Deadline: {t[1]} | Status: {t[2]}")

        elif pilihan == "5":
            keyword = input("Masukkan kata kunci: ").lower()
            ditemukan = False

            for i, t in enumerate(tugas):
                if keyword in t[0].lower():
                    print(f"{i}. {t[0]} | Deadline: {t[1]} | Status: {t[2]}")
                    ditemukan = True

            if not ditemukan:
                print("Tugas tidak ditemukan")

        elif pilihan == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
