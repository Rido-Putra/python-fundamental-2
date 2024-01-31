"""
1. user input ==> memasukan data pemilih ==> NIK,
2. memilih paslon capres 1, 2 dan 3
3. anda memilih paslon x 
selesai
4. cari cara agar tidak dapat input data nik yanng sama
5. jsonn update data lanjut, data sebelumnya dapat ditampilkann di output yang baru"""

# identitas_pemilih = {"nik": 123456789,
#                      "nama": "Rido",
#                      "ttl": "Padang, 12 Desember 2000",
#                      "alamat": "Padang, Sumatera Barat"
#                      }

budi = {"nik": 2132, "vote": 1}
budi2 = {"nik": 2132, "vote": 2}
budi3 = {"nik": 2132, "vote": 3}

import json

data = []
while True:
    identitas_pemilih = {"nik": None, "vote": None}
    # identitas_pemilih= {"nik" : 123454567}
    input_nik = int(input("Silahkan masukan identitas anda!"))
    identitas_pemilih["nik"] = input_nik
    calon_capres = int(
        input("Silahkn masukan nomor calon presiden pilihan anda@]! 1, 2, 3")
    )
    calon_capres_key = [1, 2, 3]
    identitas_pemilih["vote"] = calon_capres
    if calon_capres in calon_capres_key:
        print(f"Anda memilih paslon {calon_capres}")
    else:
        print("Tolong periksa kembali pilihan Paslon Presiden Anda")
    data.append(identitas_pemilih)
    print(data)
    lanjutkan = input("apakah anda ingin lanjut? ya/tidak")
    if lanjutkan == "tidak":
        break


output = {"output": data}
with open("output.json", "w") as file:
    json.dump(output, file)
