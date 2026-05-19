class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LaundryStack:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    def tambah_baju(self, baju):
        new_node = Node(baju)
        new_node.next = self.top_ptr
        self.top_ptr = new_node
        print(f"Baju '{baju}' ditambahkan")

  
    def ambil_baju(self):
        if self.is_empty():
            print("Tumpukan baju kosong")
            return

        temp = self.top_ptr
        print(f"Mengambil baju: {temp.data}")
        self.top_ptr = self.top_ptr.next

   
    def lihat_atas(self):
        if self.is_empty():
            print("Tidak ada baju")
            return

        print(f"Baju paling atas: {self.top_ptr.data}")

    def tampilkan(self):
        if self.is_empty():
            print("Tidak ada baju")
            return

        print("Tumpukan Baju:")
        current = self.top_ptr

        while current is not None:
            print(current.data)
            current = current.next


def main():
    laundry = LaundryStack()

    while True:
        print("\n=== STACK LAUNDRY ===")
        print("1. Tambah Baju")
        print("2. Ambil Baju")
        print("3. Lihat Baju Atas")
        print("4. Tampilkan Tumpukan")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            baju = input("Nama baju: ")
            laundry.tambah_baju(baju)

        elif pilih == "2":
            laundry.ambil_baju()

        elif pilih == "3":
            laundry.lihat_atas()

        elif pilih == "4":
            laundry.tampilkan()

        elif pilih == "5":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()