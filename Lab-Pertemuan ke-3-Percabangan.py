#Buatlah pemograman untuk menghitung konversi suhu dari Celcius menjadi Reamur dan Farenheit. 
#Pengguna nantinya akan memilih suhu apa yang ia punya (celcius/reamur/fahrenheit) untuk 
#dimasukkan kedalam input dan output hasil jadinya berupa suhu dalam bentuk Celcius, Reamur, dan Fahrenheit.
    #Input: 
# Pilihan suhu
# Nilai suhu
    # Proses:	
# JIka pengguna memilih celcius, suhu akan diubah dari celcius ke reamur dan fahrenheit
# JIka pengguna memilih reamur, suhu akan diubah dari reamur ke celcius dan fahrenheit
# JIka pengguna memilih fahrenhit, suhu akan diubah dari fahrenheit ke celcius dan fahrenheit
    # Output: 
# suhu celcius
# suhu reamur 
# suhu fahrenheit
#============================================================================================================
print("Mengubah suhu celcius, reamur, dan fahrenheit")
print("Masukkan kode dibawah ini untuk menentukan pilihan suhu yang anda ketahui")
print("a. untuk suhu celcius")
print("b. untuk suhu reamur")
print("c. untuk suhu fahrenheit")
suhu=str(input("Masukkan kode pilihan suhu anda: "))
suhu=suhu.lower()
#======
if suhu=="a":
    suhu_celcius=float(input("Masukkan suhu Celcius yang akan dihitung: "))
    reamur1=(4/5)*suhu_celcius
    fahrenhet1=(9/5*suhu_celcius)+32
    print("Berikut konversi suhunya: ")
    print("Celcius :",suhu_celcius)
    print("Reamur :",reamur1)
    print("Fahrenheit :",fahrenhet1)
elif suhu=="b":
    suhu_reamur=float(input("Masukkan suhu Reamur yang akan dihitung: "))
    celcius2=(5/4)*suhu_reamur
    fahrenhet2=(9/4*suhu_reamur)+32
    print("Berikut konversi suhunya: ")
    print("Celcius :",celcius2)
    print("Reamur :",suhu_reamur)
    print("Fahrenheit :",fahrenhet2)
elif suhu=="c":
    suhu_fahrenheit=float(input("Masukkan suhu Fahreinheit yang akan dihitung: "))
    celcius3=(5/9)*(suhu_fahrenheit-32)
    reamur3=(4/9)*(suhu_fahrenheit-32)
    print("Berikut konversi suhunya: ")
    print("Celcius :",celcius3)
    print("Reamur :",reamur3)
    print("Fahrenheit :",suhu_fahrenheit)
else:
    print("Kode yang anda masukkan salah, silahkan coba lagi.")