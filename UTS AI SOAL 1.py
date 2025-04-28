def inferensi(gejala):
    rules = [
        {"gejala": {"daun menguning", "terdapat bercak hitam"}, "hama": "Hama Kutu Daun"},
        {"gejala": {"daun berlubang", "terdapat bercak hitam"}, "hama": "Hama Ulat Daun"},
        {"gejala": {"tanaman layu", "daun menguning"}, "hama": "Hama Nematoda"},
        {"gejala": {"daun berlubang", "tanaman layu"}, "hama": "Hama Penggerek Batang"},
    ]
    
    for rule in rules:
        if rule["gejala"].issubset(gejala):
            return rule["hama"]
    
    return None

def main():
    print("=== Sistem Pakar Diagnosa Hama Tanaman ===")
    print("Masukkan gejala yang dialami tanaman (pisahkan dengan koma):")
    print("Pilihan gejala: daun menguning, terdapat bercak hitam, daun berlubang, tanaman layu")
    
    input_gejala = input("Gejala: ").lower().split(",")
    input_gejala = {gejala.strip() for gejala in input_gejala}
    
    hasil = inferensi(input_gejala)
    
    if hasil:
        print(f"\nJenis hama yang terdeteksi adalah: {hasil}")
    else:
        print("\nTidak dapat menentukan jenis hama berdasarkan gejala tersebut.")

if __name__ == "__main__":
    main()
