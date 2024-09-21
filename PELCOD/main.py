# [IF,ELIF,ELSE]
nilai=int(input('masukkan nilai'))

if(nilai > 80):
    print('selamat anda lulus')
elif(nilai > 90 and nilai < 100):
    print('selamat anda lulus, dengan nilai memuaskan')
else:
    print('anda masih belum lulus tes,semangat dan coba lagi')

# [LOOP]

# for loop
for i in range(1, 10, 2):
    print(1)

for i in range(1, 10, 1):
    print(i)
    print('hello')

for i in range(10, 1, -2):
    print(i)

# while loop
angka = 10
while(angka > 1):
    print(angka)
    angka -= 1 # angka = angka-1

# [FUNCTION]
# def
def sayHello():
    print('hello zidan')

sayHello()

def sayHello(param_nama):
    print(f'hello{param_nama} ')
    print('selamat pagi')

nilai=int(input('masukkan nilai'))

if(nilai > 80):
    print('selamat anda lulus')
    nama=input('masukkan nama')
    sayHello(nama)
elif(nilai > 90 and nilai < 100):
    print('selamat anda lulus, dengan nilai memuaskan')
else:
    print('anda masih belum lulus tes,semangat dan coba lagi')

# lambda
fungsi_kali2 = lambda param_angka : param_angka * 2

angka=int(input('masukkan angka'))
print(fungsi_kali2(angka))