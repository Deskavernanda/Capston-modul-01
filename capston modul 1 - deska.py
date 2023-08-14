def main():
    daftarkaryawan = [
    ['WINDAR PRIYANTO','317405200179001','GUNUNG KIDUL','20 JANUARI 1979','KEBAYORAN', 'JAKARTA SELATAN','KARYAWAN TETAP'],
    ['RAHMAT NURYADI','327508120588002','JAKARTA','12 FEBRUARI 1988','PONDOK GEDE', 'BEKASI PUSAT','KARYAWAN TETAP'],
    ['FADHIYAH FITRIANI','327502550796001','JAKARTA','15 JULI 1996','JL BINTARA', 'BEKASI BARAT','KARYAWAN TETAP'],
    ['RUSITO AHMAD','330203270787000','BANYUMAS','27 JULI 1987','KOJA', 'JAKARTA UTARA','KARYAWAN TETAP'],
    ['NURUL FITRIANA','367407210589000','JAKARTA', '4 APRIL 1990', 'BINTARA', 'BEKASI BARAT','KARYAWAN TETAP'],

    ]  

    while True:
        print("Menu:")
        print("1. Daftar Karyawan")
        print("2. Tambah Karyawan")
        print("3. Ubah Data Karyawan")
        print("4. hapus data karyawan")
        print("5. Keluar")
        
        inputuser = input("Masukkan pilihan menu (1/2/3/4/5): ")
        
        if inputuser == '1':
            display_employee_list(daftarkaryawan)
        elif inputuser == '2':
            add_employee(daftarkaryawan)
        elif inputuser == '3':
            modify_employee(daftarkaryawan)
        elif inputuser == '4':
            delete_employee(daftarkaryawan)
        elif inputuser == '5':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")

def display_employee_list(daftarkaryawan):
    print('\nDaftar karyawan\n')
    print('Index\t| Nama karyawan \t| Nomor Induk Penduduk\t| tempat lahir \t| tanggal lahir \t| alamat \t| Kota / Kabupaten \t| status')
    for i in range(len(daftarkaryawan)):
        print(f'{i}\t| {daftarkaryawan[i][0]}  \t| {daftarkaryawan[i][1]}\t| {daftarkaryawan[i][2]} \t| {daftarkaryawan[i][3]}  \t| {daftarkaryawan[i][4]}  \t| {daftarkaryawan[i][5]}  \t| {daftarkaryawan[i][6]}')

def add_employee(daftarkaryawan):
    namakaryawan = input('Masukkan nama karyawan: ')
    nik = input('Masukkan nik: ')
    tempatlahir = input('Masukkan tempat lahir: ')
    tanggallahir = input('Masukkan tanggal lahir: ')
    alamat = input('Masukkan alamat: ')
    kota = input('Masukkan kota: ')
    status = input('Masukkan status: ')
    daftarkaryawan.append([namakaryawan, nik, tempatlahir, tanggallahir, alamat, kota, status])
    print('\nDaftar karyawan\n')
    display_employee_list(daftarkaryawan)

def modify_employee(daftarkaryawan):
    display_employee_list(daftarkaryawan)
    indexKaryawan = int(input('\nMasukkan index karyawan: '))
    print('Data karyawan yang akan diubah:\n')
    print(f'Nama karyawan: {daftarkaryawan[indexKaryawan][0]}')
    print(f'NIK: {daftarkaryawan[indexKaryawan][1]}')

def delete_employee(daftarkaryawan):
    display_employee_list(daftarkaryawan)
    indexKaryawan = int(input('\nMasukkan index karyawan yang akan dihapus: '))
    konfirmasi = input('\nApakah anda yakin ingin menghapus data karyawan ini? (y/n): ')
    if konfirmasi == 'y':
        del daftarkaryawan[indexKaryawan]
        print('data karyawan berhasil di hapus')
    else:
        print('Data karyawan gagal diubah')

if __name__ == "__main__":
    main()
