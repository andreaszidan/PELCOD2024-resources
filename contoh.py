nama1 = "dhani"
nama2 = "kusuma"
alamat1 = "lamongan"
alamat2 = "gresik"
angkatan1 = 24
angkatan2 = 24

print("disuatu jam selesai matkul ada dua orang maba yang bertemu mereka saling berkenalan dan saling menyapa")

input("enter untuk next setiap dialog")

print("kusuma : hai boleh kenalan siapa namamu?")
print("dhani : hallo namaku",nama1)
print("dhani : dan siapa namamu?")
print("kusuma : namaku", nama2)

print("kusuma : eh kamu alamatnya dimana?")
print("dhani : aku berasal dari" , alamat1)

print("dhani : emmm, kamu alamatnya dimana? ")
print("kusuma : aku berasal dari" , alamat2)

print("kusuma : eh dhani, em kamu angkatan berapa ya")
print("dhani : aku angkatan ",angkatan1)

print("dhani : lah kalo kamu kusuma, angkatan berapa? ")
print("kusuma : aku juga angkatan ",angkatan2)
print("dhani : eh kok cuaca nya panas, ayo ke kantin buat beli es? ")

dhani = input("masukkan jawaban? ")
# kusuma = input("kusuma : iyanih,aku juga lapar ayo ke kantin? ")

if dhani =="ayo" :
    print("gaskeun ke kantin") 
else :
    print("masukkan ayo untuk dialog selanjutnya")

input("tekan next")

print("akhirnya mereka ke kantin untuk berteduh dan makan")

print("selesai makan mereka ingin membayar ke ibu kantin dan mereka berencana membayar menjadi satu")
print("mereka pun berdialog")

print("dhani : eh uangmu ada berapa?")
print("kusuma : uangku ada 5000 lah uangmu berapa?")
print("dhani : uangku ada 7500, ini jadi satu totalnya berapa?")

money = input("kusuma : ini uangnya jadikan satu aja?")
duwek = input("dhani : emang berapa totalnya?")

if money == "iya" and duwek == "mari kita itung dulu":
    print("masukkan uang kusuma")
    print("masukkan uang dhani")

bil1uangkusuma = int(input("masukkan uang kusuma :"))
bil2uangdhani = int(input("masukkan uang dhani :") )

hasil = bil1uangkusuma + bil2uangdhani 

print("hasil penjumlahan dari uang kusuma sebesar" , bil1uangkusuma , "ditambah uang dhani sebesar" , bil2uangdhani , "adalah" , hasil)

print("akhirnya mereka berdua mebayar uang sebesar RP12500 ke ibu kantin dan mereka pulang")

print("selesaiiiiii")