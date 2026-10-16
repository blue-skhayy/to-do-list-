import os

FILE_NAME = "tugas.txt"

def muat_tugas():
    tugas = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for baris in file:
                tugas.append(baris.strip())
    return tugas

def simpan_tugas(tugas):
    with open(FILE_NAME, "w") as file:
        for t in tugas:
            file.write(t + "\n")

tugas = muat_tugas()

while True:
    print("##### APLIKASI TO-DO-LIST #####")
    print("1. lihat tugas\n2. tambah tugas\n3. hapus tugas\n4.keluar")
    pilihan = input("pilih: ")

    if pilihan == "1":
        if not tugas:
            print("tidak ada tugas")
        else:
            print("=== daftar tugas ===\n")
            for i, t in enumerate(tugas):
                print(f"{i+1},{t}")
                print("----------------\n")

    elif pilihan == "2":
        tugas_baru = input("masukkan tugas barus: ")
        tugas.append(tugas_baru)

        simpan_tugas(tugas)
        print("---> tugas berhasil di simpan")

    elif pilihan == "3":
        if not tugas:
            print("tidak ada tugas")
        else: 
            print("\n=== daftar tugas ===\n")
            for i, t in enumerate(tugas):
                print(f"{i+1}.{t}")

            try:
                hapus = int(input("masukkan tugas yg sudah selesai"))
                if 0 < hapus <= len(tugas):
                    tugas_selesai = tugas.pop(hapus - 1)

                    simpan_tugas(tugas)
                    print(f"--- tugas {tugas_selesai} sudah selesai")
                else:
                    print("-- nomor tugas tidak ditemukan")
            except ValueError:
                print("---- tolong masukkan angka")

    elif pilihan == "4":
        print("--- keluar dari program")
        break
    else:
        print("!pilihan tidak valid")