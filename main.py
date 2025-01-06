import os


# Fungsi untuk menulis data ke file
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def write_all_to_file(filename,data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

# Fungsi untuk membaca data dari file
def read_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return file.readlines()


# Fungsi untuk menambahkan data ke Tabel.txt
def add_to_table():
    tables = read_file("Tabel.txt")
    if tables:
        last_index = int(tables[-1].split(',')[0])
    else:
        last_index = 9

    # buat index baru
    new_index = last_index + 1

    kode_barang = input("Masukkan Kode Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    harga_satuan = input("Masukkan Harga Satuan: ")
    stock_barang = input("Masukkan Stock Barang: ")

    # Format data dengan index
    data = f"{new_index},{nama_barang},{kode_barang},{harga_satuan},{stock_barang}"
    write_to_file('Tabel.txt',data)

    print(f"Data Berhasil ditambahkan ke Table.txt dengan index {new_index}")


# Fungsi untuk menambahkan data ke Transaksi.txt
def add_to_transaction():
      transactions = read_file("Transaksi.txt")
      if transactions:
          last_index = int(transactions[-1].split(',')[0])
      else:
          last_index = 0 # jika file kosong, mulai dari index 1

      new_index = last_index + 1

      #input data transaksi dari pengguna
      tanggal_transaksi = input("Massukan Tanggal Transaksi (YYYY-MM-DD): ")
      kode_barang = input("Masukan Kode Barang: ")
      jumlah_pesanan = input("Masukkan Jumlah Pesanan: ")
      dibayar = input("Masukkan Total Harga Dibayar: ")

      # Format data dengan index transaksi
      data = f"{new_index},{tanggal_transaksi},{kode_barang},{jumlah_pesanan},{dibayar}"
      write_to_file("Transaksi.txt",data)
      print(f"Data berhasil ditambahkan ke Transaksi.txt dengan index {new_index}")

# Stack (LIFO)
undo_stack = []
redo_stack = []


def undo(file_name):
    global undo_stack, redo_stack
    if not os.path.exists(file_name):
        print(f"File {file_name} tidak ditemukan.")
        return

    # Baca semua data dari file
    data = read_file(file_name)
    if not data:
        print("Tidak ada data yang bisa di-undo.")
        return

    # Hapus data terakhir (LIFO)
    last_data = data.pop()
    undo_stack.append(last_data)  # Simpan di stack undo
    with open(file_name, 'w') as file:
        file.writelines(data)  # Update file tanpa data terakhir

    print(f"Undo berhasil: {last_data}")
def redo(file_name):
    global undo_stack, redo_stack

    if not undo_stack:
        print("Tidak ada data yang bisa di-redo.")
        return

    # Ambil data terakhir dari undo stack
    last_undo = undo_stack.pop()
    redo_stack.append(last_undo)  # Simpan di stack redo

    # Tulis kembali data ke file
    with open(file_name, 'a') as file:
        file.write(last_undo)

    print(f"Redo berhasil: {last_undo.strip()}")

# Queue (FIFO)
queue = []


def add_to_queue(customer):
    queue.append(customer)
    print(f"{customer} ditambahkan ke antrian.")


def process_queue():
    if queue:
        customer = queue.pop(0)
        print(f"{customer} telah diproses.")
    else:
        print("Tidak ada pelanggan dalam antrian.")


# Menu Utama
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data ke Tabel")
        print("2. Tambah Data ke Transaksi")
        print("3. Undo (Stack LIFO)")
        print("4. Redo (Stack LIFO)")
        print("5. Tambah ke Antrian (Queue FIFO)")
        print("6. Proses Antrian (Queue FIFO)")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            add_to_table()
            undo_stack.append("Tambah Data ke Tabel")
        elif choice == '2':
            add_to_transaction()
            undo_stack.append("Tambah Data ke Transaksi")
        elif choice == '3':
            file_name = input("File Target(Tabel.txt/Transaksi.txt): ")
            undo(file_name)
        elif choice == '4':
            file_name = input("File Target(Tabel.txt/Transaksi.txt): ")
            redo(file_name)
        elif choice == '5':
            customer = input("Masukkan nama pelanggan: ")
            add_to_queue(customer)
        elif choice == '6':
            process_queue()
        elif choice == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main_menu()
