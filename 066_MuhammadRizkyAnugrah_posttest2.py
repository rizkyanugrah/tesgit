from prettytable  import PrettyTable
import csv
tabel_penyewa = PrettyTable()

#FORMAT RUPIAH
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   formatrupiah(q) + '.' + p
        print ('Rp ') +  formatrupiah(q) + '.' + p 
        
#DATA_USER
users={"username" :  ["rizky", "admin"],
    "password" : ["123", "admin"],
    "ID" : [1,2]
    }

#DATA_PENYEWA_PS
ps = {
    "Nama_Penyewa" : ["Iyok", "Bima", "Alby"],
    "Jenis_PS" :  ["PlayStation 3", "PlayStation 4","PlayStation 5"],
    "Waktu" : ["3 Jam", "1 Jam", "2 Jam"],
    "Harga" : ["RP 24.000",  "Rp 10.000",  "Rp 30.000"] 
    }
    
# MEMASUKAN DATA KE DALAM PRETTYTABLE
# tabel_penyewa.clear_rows()
tabel_penyewa.field_names = ["Nama_Penyewa","Jenis_PS", "Waktu", "Harga"]
for i in range (len(ps.get("Nama_Penyewa"))):
    tabel_penyewa.add_row([ps.get("Nama_Penyewa")[i],ps.get("Jenis_PS")[i],ps.get("Waktu")[i],ps.get("Harga")[i]])
    
    
#MENU PS
def Menu_PS():
    print("\n============== Menu =================")
    print("[1] PlayStation 3 // Rp.8.000 1hours ")
    print("[2] PlayStation 4 // Rp.10.000 1hours ")
    print("[3] PlayStation 5 // Rp.15.000 1hours ")
    print("[4] Tampilkan Daftar Penyewa ")
    print("[5] Cetak Data Ke Excel ")
    print("[6] EXIT ")

    choice = int(input("Masukan Pilihan : "))
    
# TAMBAH DATA
    if choice == 1:
        nama_penyewa = input("\nMasukkan Nama Penyewa : ")
        waktu = input("Masukkan Waktu Sewa : ")
        waktu_jam = waktu + " Jam"
        jenis_ps = "PlayStation 3"
        harga =formatrupiah(8000 * int(waktu))
        print("\n=========== Daftar Tagihan ==============")
        print("Atas Nama   : ", nama_penyewa, "\nWaktu Sewa  : ", waktu, "Jam", "\nTotal Bayar : ", harga)
        pembayaran = input("\nKonfirmasi Pembayaran (Yes/No) ")
        if pembayaran == "Yes" or pembayaran == "yes":
            print("Pembayaran Berhasil!")
            ps.get("Nama_Penyewa").append(nama_penyewa)
            ps.get("Jenis_PS").append(jenis_ps)
            ps.get("Waktu").append(waktu_jam)
            ps.get("Harga").append(harga)
            tabel_penyewa.add_row([nama_penyewa,jenis_ps,waktu_jam,harga])
            Menu_PS()
        else:
            print("Gagal Bayar Silahkan Masukan Ulang Data!")
            Menu_PS()
    elif choice == 2:
        nama_penyewa = input("\nMasukkan Nama Penyewa : ")
        waktu = input("Masukkan Waktu Sewa : ")
        waktu_jam = waktu + " Jam"
        jenis_ps = "PlayStation 4"
        harga =formatrupiah(10000 * int(waktu))
        print("\n=========== Daftar Tagihan ==============")
        print("Atas Nama   : ", nama_penyewa, "\nWaktu Sewa  : ", waktu, "Jam", "\nTotal Bayar : ", harga)
        pembayaran = input("\nKonfirmasi Pembayaran (Yes/No) ")
        if pembayaran == "Yes" or pembayaran == "yes":
            print("Pembayaran Berhasil!")
            ps.get("Nama_Penyewa").append(nama_penyewa)
            ps.get("Jenis_PS").append(jenis_ps)
            ps.get("Waktu").append(waktu_jam)
            ps.get("Harga").append(harga)
            tabel_penyewa.add_row([nama_penyewa,jenis_ps,waktu_jam,harga])
            Menu_PS()
        else:
            print("Gagal Bayar Silahkan Masukan Ulang Data!")
            Menu_PS() 
    elif choice == 3:
        nama_penyewa = input("\nMasukkan Nama Penyewa : ")
        waktu = input("Masukkan Waktu Sewa : ")
        waktu_jam = waktu + " Jam"
        jenis_ps = "PlayStation 3"
        harga =formatrupiah(15000 * int(waktu))
        print("\n=========== Daftar Tagihan ==============")
        print("Atas Nama   : ", nama_penyewa, "\nWaktu Sewa  : ", waktu, "Jam", "\nTotal Bayar : ", harga)
        pembayaran = input("\nKonfirmasi Pembayaran (Yes/No) ")
        if pembayaran == "Yes" or pembayaran == "yes":
            print("Pembayaran Berhasil!")
            ps.get("Nama_Penyewa").append(nama_penyewa)
            ps.get("Jenis_PS").append(jenis_ps)
            ps.get("Waktu").append(waktu_jam)
            ps.get("Harga").append(harga)
            tabel_penyewa.add_row([nama_penyewa,jenis_ps,waktu_jam,harga])
            Menu_PS()
        else:
            print("Gagal Bayar Silahkan Masukan Ulang Data!")
            Menu_PS()
            
#TAMPILKAN, UBAH DAN HAPUS DATA    
    elif choice == 4:
        print(tabel_penyewa)
        print("[1] Hapus Data ")
        print("[2] Ubah Data ")
        print("[3] Kembali Ke Menu ")
        
        
        pilihan = int(input("Masukan Pilihan : "))
        
        if pilihan == 1:
            print("Hapus Data")
            nama_hapus = input("Masukan nama ingin di Hapus?")
            indexNamaPenyewa = ps.get("Nama_Penyewa").index(nama_hapus)
            ps.get("Nama_Penyewa").pop(indexNamaPenyewa)
            ps.get("Jenis_PS").pop(indexNamaPenyewa)
            ps.get("Waktu").pop(indexNamaPenyewa)
            ps.get("Harga").pop(indexNamaPenyewa)
            # del ps['Nama_Penyewa'][indexNamaPenyewa]
            # del ps['Jenis_PS'][indexNamaPenyewa]
            # del ps['Waktu'][indexNamaPenyewa]
            # del ps['Harga'][indexNamaPenyewa]
            # Menu_PS()
        elif pilihan == 2:
            print("Ubah Data")
            nama_ubah = input("Masukan nama ingin di ubah : ")
            indexNamaPenyewa = ps.get("Nama_Penyewa").index(nama_ubah)
            nama_baru = input("Masukan nama baru : ")
            ps.get("Nama_Penyewa")[indexNamaPenyewa]=nama_ubah
            tabel_penyewa.clear_rows()
            tabel_penyewa.field_names = ["Nama_Penyewa","Jenis_PS", "Waktu", "Harga"]
            for i in range (len(ps.get("Nama_Penyewa"))):
                tabel_penyewa.add_row([ps.get("Nama_Penyewa")[i],ps.get("Jenis_PS")[i],ps.get("Waktu")[i],ps.get("Harga")[i]])
            print(tabel_penyewa)
        elif pilihan >= 4 or pilihan <=0:
            print("\nMasukan Pilihan Yang Sesuai!")
            konfirmasi = input("Kembali Ke Menu ? (Y/N)")
            if konfirmasi == "Y" or konfirmasi == "y":
                Menu_PS()
            print("TERIMA KASIH TELAH MENCOBA APLIKASI RENTAL PS")
            exit()
        else:
            Menu_PS()

#PRINT DATA KE EXCEL
    elif choice == "5":
        print("excel")

#EXIT
    elif choice == "6":
        print("TERIMA KASIH TELAH MENCOBA APLIKASI RENTAL PS")
        
#cek login/Register
status = ""
def Menu_Login():
    status =input("Login (Yes/No)? Ketik Register jika ingin mendaftar : ")
    if status == "Yes" or status == "yes":
        Old_User()
    elif status == "Register" or status == "register":
        New_User()
        
#Menambahkan Data User Baru
def New_User():
    Create_Username = input("\nMasukan Username : ")
    if Create_Username in users.get("username"):
        print ("Username Telah Terdaftar, Silahkan Pilih Username Yang Lain")
        New_User()
    else:
        Create_Password = input("Masukan Password : ")
        users.get("username").append(Create_Username)
        users.get("password").append(Create_Password)
        ID = len(users.get("ID"))
        users.get("ID").append(ID+1)
        print("\nData Berhasil Di Tambahkan")
        konfirmasi = input("Ingin Login ? (y/n)")
        if konfirmasi == "y":
            Old_User()
        else :
            exit     
            
#Login
def Old_User():
    login =input("\nMasukan Username: ")
    Password =input("Masukan Password: ")
    try:
        search_user = users.get("username").index(login)
        if login in users.get("username")[search_user] and Password == users.get("password")[search_user]:
            print("Berhasil Login")
            Menu_PS()
        else:
            print("Gagal Login Password Anda Salah!")
            Old_User()
    except ValueError:
        print("\nMaaf Ada Kesalahan Silahkan Login Ulang !")
        Old_User()

Menu_Login()