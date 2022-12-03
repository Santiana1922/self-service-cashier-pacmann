# Import library yang dibutuhkan
from tabulate import tabulate

class Transaction:
    def __init__ (self):
        """
        fungsi menginisialisasi dictionary
        """ 
        self.data_transc = dict()
     
    
    def add_item (self, nama_item, jumlah_item, harga_per_item):
        """
        fungsi menambahkan data transaksi

        parameters
        nama_item       : str   nama produk yang ingin dibeli
        jumlah_item     : int   kuantitas produk
        harga_per_item  : int   harga produk
    
        return 
        Tabel list item yang ingin dibeli
        """
        # Menambah data ke dalam atribut dictrionary
        self.data_transc.update({nama_item : [jumlah_item, harga_per_item, (jumlah_item * harga_per_item)]})

        # Menampilkan list item
        return self.check_order()
     
        
    def update_item_name (self, nama_item, update_nama_item):
        """
        fungsi untuk memperbarui nama produk

        parameters
        nama_item         : str   nama produk yang ingin diperbarui
        update_nama_item  : str   nama baru produk
        
        return 
        Tabel list item yang telah di-update
        """
        try: 
            # Update nama item
            self.data_transc[update_nama_item] = self.data_transc.pop(nama_item)

            # Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def update_item_qty (self, nama_item, update_jumlah_item):
        """
        fungsi untuk memperbarui kuantitas produk

        parameters
        nama_item           : str  nama produk yang dituju
        update_jumlah_item  : int  kuantitas produk yang baru
        
        return
        Tabel list item yang telah di-update
        """
        try: 
            # Update jumlah item
            self.data_transc[nama_item][0] = update_jumlah_item 
            
            # Update data total harga 
            self.data_transc[nama_item][2] = update_jumlah_item * self.data_transc[nama_item][1]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
      
    
    def update_item_price (self, nama_item, update_harga_item):
        """
        fungsi untuk memperbarui harga per produk

        parameters
        nama_item           : str  nama produk yang dituju
        update_harga_item   : int  harga produk yang baru
        
        return
        Tabel list item yang telah di-update
        """
        try:
            # Update harga item
            self.data_transc[nama_item][1] = update_harga_item
            # Update data total harga
            self.data_transc[nama_item][2] = update_harga_item * self.data_transc[nama_item][0]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def delete_item (self, nama_item):
        """
        fungsi untuk menghapus produk yang tidak jadi dibeli

        parameters
        nama_item           : str  nama produk yang ingin dihapus
        
        return
        Tabel list item terbaru
        """
        try:
            # Delete item tertentu
            self.data_transc.pop(nama_item)
            
            # Menampilkan list item terbaru
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def reset_transaction (self):
        """
        fungsi untuk menghapus semua data transaksi
        
        return
        pesan : str semua item berhasil di-delete
        """
        # Delete semua data transaksi
        self.data_transc.clear()
        
        return "Semua item berhasil di-delete!"
    
    
    def check_order(self):
        """
        fungsi untuk menampilkan semua data transaksi yang sudah dibuat
        """
        try: 
            table = []
            
            # Add data dictionary transaksi ke dalam nested list table
            for key, val in self.data_transc.items():
                tmp = []
                tmp.append(key)

                for i in val:
                    tmp.append(i)

                table.append(tmp) 

            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print("Transaksi Anda")
            print("")
            print(tabulate(table, headers, tablefmt='psql')) 
            
        except:
            raise exception("Terjadi kesalahan input! data nama item, jumlah item, dan harga per item tidak boleh kosong! Silahkan input ulang!")
     
    
    def total_price (self):
        """
        fungsi untuk menampilkan total harga transaksi dan memberikan diskon apabila memenuhi syarat
        """
        # Menampilkan list item
        self.check_order()
        print("")
        
        # Menjumlahkan total harga
        total = 0
        for key, val in self.data_transc.items():
            total += self.data_transc[key][2]
            
        # pengecekan diskon
        if total > 500_000:
            total_baru = total * 0.90
            print(f'Total belanja Anda setelah diskon 10% adalah {total_baru}')
        elif total > 300_000:
            total_baru = total * 0.92
            print(f'Total belanja Anda setelah diskon 8% adalah {total_baru}')
        elif total > 200_000:
            total_baru = total * 0.95
            print(f'Total belanja Anda setelah diskon 5% adalah {total_baru}')
        else:
            print(f'Total belanja Anda adalah Rp {total}')