def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i] == target:
            counter += 1
        i += 1

    return counter


def main():
    print("      PROGRAM PENCARIAN PEMBELIAN SKINCARE       ")

    data = []

    while True:
        try:
            jumlah_pelanggan = int(input("Masukkan jumlah pelanggan: "))
            if jumlah_pelanggan > 0:
                break
            else:
                print("Jumlah pelanggan harus lebih dari 0!")
        except ValueError:
            print("Input harus berupa angka!")

    print("\nMasukkan jumlah item skincare yang dibeli pelanggan:\n")

    for i in range(jumlah_pelanggan):
        while True:
            try:
                pembelian = int(input(f"Pelanggan ke-{i+1}: "))
                data.append(pembelian)
                break
            except ValueError:
                print("Input harus berupa angka!")

    n = len(data)

    print(" DATA PEMBELIAN SKINCARE ")
    print(data)

    while True:
        try:
            target = int(input("\nMasukkan jumlah item yang ingin dicari: "))
            break
        except ValueError:
            print("Input harus berupa angka!")

    counter = sequential_search(data, n, target)

    print(" HASIL PENCARIAN ")

    if counter > 0:
        print(f"Pembelian sebanyak {target} item ditemukan {counter} kali.")
        print("Produk skincare dengan jumlah pembelian tersebut cukup populer!")
    else:
        print(f"Pembelian sebanyak {target} item tidak ditemukan.")
        print("Belum ada pelanggan dengan jumlah pembelian tersebut.")

if __name__ == "__main__":
    main()