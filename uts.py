Nana_Colection =["Atasan","Bawahan","Hijab"]

Nana_Colection = "y" 
#While digunakan untuk melakukan perulangan
while Nana_Colection== "y":

    print("======================")
    print("    Nana Colection    ")
    print("======================")
    print("        Atasan        ")
    print("        Bwahan        ")
    print("         Hiab         ")
    print("======================")

    Nana_Colection = input("Pilih Barang: ")
    if Nana_Colection == "Atasan":
        Atasan = ["cardigan","Hoodie","Kemeja"]
        print( 1. | Atasan | [0])
        print( 2. | Atasan | [1])
        print( 3. | Atasan | [2])
    elif Nana_Colection ==  "Bawahan":
        Bawahan = ["Jeans","Rok","Legging"]
        print( 1. | Bawahan | [0])
        print( 2. | Bawahan | [1])
        print( 3. | Bawahan | [2])
    elif Nana_Colection ==  "Hijab":
        Hijab = ["Rawis","Pasmina","Bellasquare"]
        print( 1. | Hijab | [0])
        print( 2. | Hijab | [1])
        print( 3. | Hijab | [2])
    else:
        print("Maaf menu yang anda pilih tidak tersedia, silahkan ketikkan sesuai list menu kami")
       
        print ("Pesanan telah selesai ")

    pesan = input("pesanan: ")
    print()
    restoran = input("order lagi : (Y/N) ")