from transaction import Transaction

def menu(obj):
    """Fungsi untuk menampilkan daftar menu.
    
    parameter
    obj : object hasil instance class
    """
    print("-"*60)
    print("SELAMAT DATANG DI SUPERMARKET PACMANN")
    print("-"*60)
    print("1. Menambahkan item baru")
    print("2. Mengubah nama item")
    print("3. Mengubah jumlah item")
    print("4. Mengubah harga item")
    print("5. Menghapus item")
    print("6. Reset transaksi")
    print("7. Check order")
    print("8. Lihat total harga")
    print("9. Exit\n")
    
    # Input opsi menu
    choice = int(input('Masukan pilihan Anda : '))
    
    try:
        if choice == 1:
            # Input nama item
            nama_item = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input jumlah item
                    jumlah_item = int(input('Masukan jumlah item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input harga item
                    harga_item = int(input('Masukan harga item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break           
            
            # memanggil method yang ada di class Transaction
            obj.add_item(nama_item, jumlah_item, harga_item)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 2:
            
            # Input nama item
            nama_item = input('Masukan nama item : ')
            
            # Input harga item yang baru
            nama_item_baru =input('Masukan nama item yang baru : ') 
            
            # memanggil method yang ada di class Transaction
            obj.update_item_name(nama_item, nama_item_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 3:
            # Input nama item
            nama_item = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input jumlah item yang baru
                    jumlah_item_baru = int(input('Masukan jumlah item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break
            
            # memanggil method yang ada di class Transaction
            obj.update_item_qty(nama_item, jumlah_item_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 4:
            # Input nama item
            nama_item = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input harga item yang baru
                    harga_item_baru = int(input('Masukan harga item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break 
            
            # memanggil method yang ada di class Transaction
            obj.update_item_price(nama_item, harga_item_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 5:
            # Input nama item
            nama_item = input('Masukan nama item : ')
            
            # memanggil method yang ada di class Transaction
            obj.delete_item(nama_item)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 6:
            
            # memanggil method yang ada di class Transaction
            obj.reset_transaction()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 7:
            # memanggil method yang ada di class Transaction
            obj.check_order()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 8:
            # memanggil method yang ada di class Transaction
            obj.total_price()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 9:
            print("-"*60)
            print("Terima kasih telah mengunjungi Supermarket Pacmann.")
            print("-"*60)
            pass
        
        else:
            print("Anda salah input.\n")
            # kembali ke menu
            menu(obj)
            
    except:
        print("Input Anda salah.\n")
        # kembali ke menu
        menu(obj)

# Instance class Transaction    
transc1 = Transaction()

# Memanggil function menu
menu(transc1)