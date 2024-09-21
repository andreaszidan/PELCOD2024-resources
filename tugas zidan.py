umurzidan 20
umurrusdi = 24

print("Selamat datang di percakapan antara zidan dan rusdi!")

 # Input nama pengguna
nama1 = input("hai dengan siapa ini?")
print("hai" , nama1 , "salam kenal")

print("mari kita baca obrolan zidan dan rusdi")

input("masukkan angka 1 untuk next chapter ")
# Percakapan dimulai
print("zidan: eh haloo rusdi kita ketemu lagi nihh! oh iya kamu umur berapa sih?")
print("rusdi: haloo jugaa zidana! Umurku" , umurrusdi , "umurmu berapa rev?")
print("zidan: Aku sii" , umurzidan , "tahun.")

#  Operasi aritmatika
selisihumur = umurrusdi - umurzidan
print("zidan: loh ga jauh beda dong, berarti selisih umur kita" , selisihumur , "tahun ya.")

# Input dari pengguna
tebakanumur = int(input(" coba tebak berapa jumlah umur zidan dan rusdi: "))

# Operasi aritmatika dan logika
umurkeduanya = umurrusdi + umurzidan

# Output hasil tebakan
if tebakanumur == 44 :
    print("zidan: Wah benar bangett!")
else :
    print("rusdi: Maaf yaa, tebakanmu salah. Jumlah umur kami sebenarnya" , umurkeduanya , "tahun.")

input("tekkan angka 1 untuk melanjutkan dialog")

# # Pertanyaan tambahan dengan operasi logika
print("zidan: Hei rusdi, aku punya pertanyaan matematika nihh buat kamu.")
zidan_number = 15
rusdi_number = 7
    
print("zidan: Jika aku punya" , {zidan_number} , "apel dan kamu punya" , {rusdi_number} , "apel, berapa total apel kita?")
    
user_answer = int(input("coba bantu rusdi menjawab: "))

hasil = zidan_number + rusdi_number

if user_answer == hasil :
        print("rusdi: Terimakasih yaa! Jawabannya benar.")
else :
        print("rusdi: Hmm, sepertinya itu kurang tepat. Jumlah yang benar adalah" , hasil ,"apel")

# Akhir percakapan
print("zidan: Terima kasih yaa rusdi sudah mengobrol")
print("rusdi: Sama-sama, zidan. Dan terima kasih juga untuk" , nama1 ," yang sudah berpartisipasi!")