class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        new_node.next = self.head
        last.next = new_node
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def tambah_di_tengah(self, data, pos):
        if pos <= 0:
            print("Posisi harus lebih dari 0")
            return
        new_node = Node(data)
        if not self.head and pos > 1:
            print("Posisi melebihi panjang linked list")
            return
        if pos == 1:
            self.tambah_di_awal(data)
            return
        curr = self.head
        prev = None
        count = 1
        while curr and count < pos:
            prev = curr
            curr = curr.next
            count += 1
        if not curr:
            print("Posisi melebihi panjang linked list")
            return
        prev.next = new_node
        new_node.next = curr

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list sudah kosong")
            return
        if self.head.next == self.head:
            self.head = None
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = self.head.next
        self.head = self.head.next

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list sudah kosong")
            return
        if self.head.next == self.head:
            self.head = None
            return
        prev = None
        curr = self.head
        while curr.next != self.head:
            prev = curr
            curr = curr.next
        prev.next = self.head

    def hapus_di_tengah(self, pos):
        if pos <= 0:
            print("Posisi harus lebih dari 0")
            return
        if not self.head:
            print("Linked list sudah kosong")
            return
        if pos == 1:
            self.hapus_di_awal()
            return
        curr = self.head
        prev = None
        count = 1
        while curr and count < pos:
            prev = curr
            curr = curr.next
            count += 1
        if not curr:
            print("Posisi melebihi panjang linked list")
            return
        prev.next = curr.next

    def display(self):
        if not self.head:
            print("Linked list kosong")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()


    def merge_sort(arr, key):
     if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], key) < getattr(right_half[j], key):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def sort_kendaraan(parkiran, key):
    if not parkiran.head:
        print("Linked list kosong")
        return
    temp = parkiran.head
    arr = []
    while True:
        arr.append(temp.data)
        temp = temp.next
        if temp == parkiran.head:
            break

    merge_sort(arr, key)

    parkiran.head = None
    for data in arr:
        if not parkiran.head:
            parkiran.head = data
            parkiran.head.next = parkiran.head
        else:
            last = parkiran.head
            while last.next != parkiran.head:
                last = last.next
            last.next = data
            data.next = parkiran.head

    print("Data berhasil diurutkan berdasarkan", key)


class Kendaraan:
    def __init__(self, nama, jenis, plat, jam_masuk, jam_keluar):
        self.nama = nama
        self.jenis = jenis
        self.plat = plat
        self.jam_masuk = jam_masuk
        self.jam_keluar = jam_keluar

    def display_info(self):
        print(f"Nama kendaraan: {self.nama}")
        print(f"Jenis kendaraan: {self.jenis}")
        print(f"Plat: {self.plat}")
        print(f"Jam masuk: {self.jam_masuk}")
        print(f"Jam keluar: {self.jam_keluar}")
        print()


parkiran = LinkedList()

while True:
    print("Menu:")
    print("1. Tambah Kendaraan di Awal")
    print("2. Tambah Kendaraan di Akhir")
    print("3. Tambah Kendaraan di Tengah")
    print("4. Hapus Kendaraan di Awal")
    print("5. Hapus Kendaraan di Akhir")
    print("6. Hapus Kendaraan di Tengah")
    print("7. Tampilkan Katalog Kendaraan")
    print("8. Keluar")
    print("9. menu sorting")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama Kendaraan: ")
        jenis = input("Jenis Kendaraan: ")
        plat = input("Plat Kendaraan: ")
        jam_masuk = input("Jam Masuk: ")
        jam_keluar = input("Jam Keluar: ")
        kendaraan_baru = Kendaraan(nama, jenis, plat, jam_masuk, jam_keluar)
        parkiran.tambah_di_awal(kendaraan_baru)

    elif pilihan == "2":
        nama = input("Nama Kendaraan: ")
        jenis = input("Jenis Kendaraan: ")
        plat = input("Plat Kendaraan: ")
        jam_masuk = input("Jam Masuk: ")
        jam_keluar = input("Jam Keluar: ")
        kendaraan_baru = Kendaraan(nama, jenis, plat, jam_masuk, jam_keluar)
        parkiran.tambah_di_akhir(kendaraan_baru)

    elif pilihan == "3":
        nama = input("Nama Kendaraan: ")
        jenis = input("Jenis Kendaraan: ")
        plat = input("Plat Kendaraan: ")
        jam_masuk = input("Jam Masuk: ")
        jam_keluar = input("Jam Keluar: ")
        pos = int(input("Posisi: "))
        kendaraan_baru = Kendaraan(nama, jenis, plat, jam_masuk, jam_keluar)
        parkiran.tambah_di_tengah(kendaraan_baru, pos)

    elif pilihan == "4":
        parkiran.hapus_di_awal()

    elif pilihan == "5":
        parkiran.hapus_di_akhir()

    elif pilihan == "6":
        pos = int(input("Posisi: "))
        parkiran.hapus_di_tengah(pos)

    elif pilihan == "7":
        parkiran.display()

    elif pilihan == "8":
        print("Program berakhir.")
        break

    elif pilihan == "9":
     print("1. Sorting berdasarkan Nama (Ascending)")
     print("2. Sorting berdasarkan Nama (Descending)")
     print("3. Sorting berdasarkan Jam Masuk (Ascending)")
     print("4. Sorting berdasarkan Jam Masuk (Descending)")
     pilihan_sorting = input("Pilih jenis sorting: ")

    if pilihan_sorting == "1":
        sort_kendaraan(parkiran, 'nama')
    elif pilihan_sorting == "2":
        sort_kendaraan(parkiran, 'nama')
        parkiran.display()
    elif pilihan_sorting == "3":
        sort_kendaraan(parkiran, 'jam_masuk')
    elif pilihan_sorting == "4":
        sort_kendaraan(parkiran, 'jam_masuk')
        parkiran.display()
    else:
        print("Pilihan tidak valid.")

    