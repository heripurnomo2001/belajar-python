# SINGLE INPUT

while True:
    try:
        float_literal = float(input("Masukkan angka, boleh desimal : \n"))
        break
    except ValueError as e:
        print("Data yang anda masukkan tidak valid, ", e)
        
        
