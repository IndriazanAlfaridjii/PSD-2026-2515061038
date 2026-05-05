def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        # bandingkan berdasarkan tahun
        while j >= 0 and arr[j]['tahun'] > temp['tahun']:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data buku (judul dan tahun):")

    for i in range(n):
        judul = input(f"Judul buku ke-{i+1}: ")
        
        while True:
            try:
                tahun = int(input(f"Tahun terbit buku ke-{i+1}: "))
                break
            except ValueError:
                print("Input tahun tidak valid, masukkan angka!")

        arr.append({"judul": judul, "tahun": tahun})

    print("\nData sebelum diurutkan:")
    for buku in arr:
        print(buku["judul"], "-", buku["tahun"])

    insertion_sort(arr, n)

    print("\nData setelah diurutkan (tahun terlama → terbaru):")
    for buku in arr:
        print(buku["judul"], "-", buku["tahun"])


if __name__ == "__main__":
    main()