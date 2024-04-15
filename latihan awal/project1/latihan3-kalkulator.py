#program kalkukator sederhana
operator = ""
valid_operators = ['+','*','-','/']

while operator not in valid_operators:
    operator = input("Pilih operator '+', '-','*','/' : " )

    if operator in valid_operators:
        print(f'Operator yang anda pilih adalah: {operator}')
    else:    
        print('Yang anda input bukan operator yang valid!')    


angka1 = int(input("angka1 : "))
angka2 = int(input("angka2 : "))

#hitung dengan kondisi
if operator == '+' :
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2 
elif operator == '/':
    hasil = angka1 / angka2

# tampilkan hasil
print(f"Hasil perhitungan {angka1} {operator} {angka2} adalah {hasil}")



