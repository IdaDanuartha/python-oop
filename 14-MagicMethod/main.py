class Buah:
    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # dipakai saat debugging
    def __repr__(self):
        return "Nama buah: {}".format(self.nama)

    # dipakai saat production
    def __str__(self):
        return "Nama buah: {}".format(self.nama)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

mangga = Buah("mangga", 5)
apel = Buah("apel", 10)
print(mangga)
print(apel)
print(mangga + apel)