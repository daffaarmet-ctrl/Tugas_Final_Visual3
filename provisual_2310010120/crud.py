# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'dbvisual3_2310010120')


    # ==KARYAWAN==
    def tambahKaryawan(self, id, nm, almt, umur, telp):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into data_karyawan (id_karyawan, nama_karyawan, alamat, umur, no_telp) value (%s, %s, %s, %s, %s)",
        (id, nm, almt, umur, telp))
        self.koneksi.commit()
        aksi.close()

    def ubahKaryawan(self, id, nm, almt, umur, telp):
        aksi = self.koneksi.cursor()
        aksi.execute("update data_karyawan set nama_karyawan = %s, alamat = %s, umur = %s, no_telp = %s where id_karyawan = %s",
        (nm, almt, umur, telp, id))
        self.koneksi.commit()
        aksi.close()

    def hapusKaryawan(self, id):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from data_karyawan where id_karyawan = %s",
        (id, ))
        self.koneksi.commit()
        aksi.close()

    def dataKaryawan(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from data_karyawan order by id_karyawan asc")
        return aksi.fetchall()

    def filterKaryawan(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from data_karyawan where id_karyawan like %s or nama_karyawan like %s or alamat like %s or umur like %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()

    # ==INVENTory==
    def tambahInventory(self, id, nm, kategori, satuan, jml):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into data_inventory (id_barang, nama_barang, kategori, satuan, jumlah) value (%s, %s, %s, %s, %s)",
        (id, nm, kategori, satuan, jml))
        self.koneksi.commit()
        aksi.close()

    def ubahInventory(self, id, nm, kategori, satuan, jml):
        aksi = self.koneksi.cursor()
        aksi.execute("update data_inventory set nama_barang = %s, kategori = %s, satuan = %s, jumlah = %s where id_barang = %s",
        (nm, kategori, satuan, jml, id))
        self.koneksi.commit()
        aksi.close()

    def hapusInventory(self, id):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from data_inventory where id_barang = %s",
        (id, ))
        self.koneksi.commit()
        aksi.close()


    def dataInventory(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from data_inventory order by id_barang asc")
        return aksi.fetchall()


    def filterInventory(self, cari):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from data_inventory where id_barang like %s or nama_barang like %s or kategori like %s or satuan like %s or jumlah like %s",
        ([f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"]))
        return aksi.fetchall()


    # ==Panen==
    def tambahPanen(self, idpn, idkr, tgl, haasil, total):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into data_panen (id_panen, id_karyawan, tanggal_panen, hasil_panen, total_panen) value (%s, %s, %s, %s, %s)",
        (idpn, idkr, tgl, haasil, total))
        self.koneksi.commit()
        aksi.close()

    def ubahPanen(self, idpn, idkr, tgl, haasil, total):
        aksi = self.koneksi.cursor()
        aksi.execute("update data_panen set id_karyawan = %s, tanggal_panen = %s, hasil_panen = %s, total_panen = %s where id_panen = %s",
        (idkr, tgl, haasil, total, idpn))
        self.koneksi.commit()
        aksi.close()

    def hapusPanen(self, idpn):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from data_panen where id_panen = %s",
        (idpn, ))
        self.koneksi.commit()
        aksi.close()


    def dataPanen(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute(
            """select p.id_panen, kr.nama_karyawan, p.tanggal_panen, p.hasil_panen, p.total_panen
            from data_panen p
            join data_karyawan kr on p.id_karyawan = kr.id_karyawan""")
        return aksi.fetchall()

    def filterPanen(self, kata):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT p.id_panen, k.nama_karyawan, p.tanggal_panen,
                   p.hasil_panen, p.total_panen
            FROM data_panen p
            JOIN data_karyawan k ON p.id_karyawan = k.id_karyawan
            WHERE p.id_panen LIKE %s
               OR k.nama_karyawan LIKE %s
               OR p.tanggal_panen LIKE %s
        """, (f"%{kata}%", f"%{kata}%", f"%{kata}%"))

        hasil = aksi.fetchall()
        aksi.close()
        return hasil


    # ==Gaji==
    def tambahGaji(self, idg, idkr, tgl, kategori, gaji):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into data_gaji (id_gaji, id_karyawan, tanggal_gaji, kategori, jumlah_gaji) value (%s, %s, %s, %s, %s)",
        (idg, idkr, tgl, kategori, gaji))
        self.koneksi.commit()
        aksi.close()

    def ubahGaji(self, idg, idkr, tgl, kategori, gaji):
        aksi = self.koneksi.cursor()
        aksi.execute("update data_gaji set id_karyawan = %s, tanggal_gaji = %s, kategori = %s, jumlah_gaji = %s where id_gaji = %s",
        (idkr, tgl, kategori, gaji, idg))
        self.koneksi.commit()
        aksi.close()

    def hapusGaji(self, idg):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from data_gaji where id_gaji = %s",
        (idg, ))
        self.koneksi.commit()
        aksi.close()

    def dataGaji(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute(
            """select g.id_gaji, kr.nama_karyawan, g.tanggal_gaji, g.kategori, g.jumlah_gaji
            from data_gaji g
            join data_karyawan kr on g.id_karyawan = kr.id_karyawan""")
        return aksi.fetchall()

    def filterGaji(self, kata):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT g.id_gaji, k.nama_karyawan, g.tanggal_gaji,
                   g.kategori, g.jumlah_gaji
            FROM data_gaji g
            JOIN data_karyawan k ON g.id_karyawan = k.id_karyawan
            WHERE g.id_gaji LIKE %s
               OR k.nama_karyawan LIKE %s
               OR g.tanggal_gaji LIKE %s
               OR g.kategori LIKE %s
        """, (f"%{kata}%", f"%{kata}%", f"%{kata}%", f"%{kata}%"))

        hasil = aksi.fetchall()
        aksi.close()
        return hasil


    def totalPanenMingguan(self, id_karyawan, tanggal):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT SUM(total_panen)
            FROM data_panen
            WHERE id_karyawan = %s
            AND tanggal_panen BETWEEN DATE_SUB(%s, INTERVAL 7 DAY) AND %s
        """, (id_karyawan, tanggal, tanggal))

        hasil = aksi.fetchone()
        aksi.close()
        return hasil[0] if hasil[0] else 0

    def totalPanenBulanan(self, id_karyawan, tanggal):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT SUM(total_panen)
            FROM data_panen
            WHERE id_karyawan = %s
            AND MONTH(tanggal_panen) = MONTH(%s)
            AND YEAR(tanggal_panen) = YEAR(%s)
        """, (id_karyawan, tanggal, tanggal))

        hasil = aksi.fetchone()
        aksi.close()
        return hasil[0] if hasil[0] else 0

